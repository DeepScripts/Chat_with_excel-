import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent

# -----------------------------
# Global Matplotlib Settings to force small charts
# -----------------------------
mpl.rcParams["figure.figsize"] = (5, 3)
mpl.rcParams["figure.dpi"] = 100
mpl.rcParams["savefig.dpi"] = 100
mpl.rcParams["font.size"] = 9
sns.set_context("notebook", font_scale=0.8)

# -----------------------------
# Monkeypatch pandas DataFrame.__repr__ to capture DataFrames
# -----------------------------
LAST_DF = None

_original_repr = pd.DataFrame.__repr__

def _capture_df(self):
    global LAST_DF
    LAST_DF = self
    return _original_repr(self)

pd.DataFrame.__repr__ = _capture_df

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("❌ GROQ_API_KEY not found. Please set it in your .env file.")
    st.stop()

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="📊 Chat with CSV/Excel (Groq)",
    layout="wide"
)
st.title("📊 RAG Chatbot with CSV / Excel (Powered by Groq)")

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:
    # Load Data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")
    st.dataframe(df.head())

    # -----------------------------
    # Groq LLM
    # -----------------------------
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=groq_api_key
    )

    # -----------------------------
    # Pandas DataFrame Agent
    # -----------------------------
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=False,
        allow_dangerous_code=True
    )

    # -----------------------------
    # Chat State
    # -----------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # -----------------------------
    # Chat Input
    # -----------------------------
    user_input = st.chat_input("Ask questions or request charts...")

    if user_input:
        LAST_DF = None
        st.session_state.messages.append(("user", user_input))

        with st.spinner("Groq is thinking..."):
            response = agent.run(user_input)

        has_plot = bool(plt.get_fignums())
        has_table = LAST_DF is not None

        st.session_state.messages.append(
            ("assistant", response, has_plot, has_table, LAST_DF)
        )

    # -----------------------------
    # Display Chat Messages
    # -----------------------------
    for message in st.session_state.messages:
        if message[0] == "user":
            st.chat_message("user").write(message[1])
        else:
            _, content, has_plot, has_table, table_df = message
            with st.chat_message("assistant"):
                if has_table:
                    # Show only the table, hide the text
                    st.dataframe(table_df, use_container_width=True)
                else:
                    # Show text only if no table
                    st.write(content)

                if has_plot:
                    fig = plt.gcf()
                    fig.set_size_inches(5, 3)
                    fig.set_dpi(100)
                    plt.tight_layout()
                    st.pyplot(fig)

else:
    st.info("Upload a CSV or Excel file to start chatting.")
