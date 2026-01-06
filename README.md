
# 📊 Chat with Excel / CSV using AI (Groq-Powered)

This project is an **AI-powered data analysis application** built with **Streamlit**, **Pandas**, and **Groq LLM**.
It allows users to upload **Excel or CSV files**, ask **natural language questions**, and receive **answers, tables, and visualizations (graphs)** automatically.

The system behaves like a **chatbot for structured data**, enabling non-technical users to analyze datasets without writing SQL or Python code.

---

## 🚀 Features

* 📁 Upload **CSV or Excel (.xlsx)** files
* 💬 Ask questions in **plain English**
* 📊 Automatically generates:

  * Tabular results
  * Charts and graphs (bar, line, etc.)
* 🤖 Uses **Groq LLM (LLaMA 3.3 – 70B)** for intelligent reasoning
* 🧠 Pandas DataFrame Agent for accurate data operations
* ⚡ Fast response time powered by Groq
* 🖥️ Interactive UI built with Streamlit

---

## 🛠️ Tech Stack

* **Frontend / UI**: Streamlit
* **Data Handling**: Pandas
* **Visualization**: Matplotlib, Seaborn
* **LLM**: Groq (LLaMA 3.3 – 70B)
* **AI Framework**: LangChain
* **Environment Management**: python-dotenv

---

## 📂 Project Structure

```
├── app.py                # Main Streamlit application
├── .env                  # Environment variables (API key)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🔑 Prerequisites

* Python 3.9+
* Groq API Key

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DeepScripts/Chat_with_excel-.git
cd chat-with-excel-groq
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser.

---

## 🧑‍💻 How to Use

1. Upload a **CSV or Excel file**
2. Preview the dataset in the UI
3. Ask questions such as:

   * *“Show total sales by region”*
   * *“Create a bar chart of monthly revenue”*
   * *“Which product has the highest profit?”*
4. Get:

   * 📋 Tables for data queries
   * 📈 Graphs for visualization requests
   * 💬 Text explanations where required

---

## 📈 Example Queries

* “Show top 5 rows”
* “Calculate average salary department-wise”
* “Plot a line chart of sales over time”
* “Which category contributes the most revenue?”

---

## 🧠 How It Works (High Level)

1. User uploads a dataset
2. Dataset is loaded into a Pandas DataFrame
3. A **LangChain Pandas Agent** is created
4. User questions are passed to **Groq LLM**
5. LLM generates:

   * Data operations
   * Visualizations (if needed)
6. Results are rendered in Streamlit

---

## 🔒 Security Notes

* API keys are stored securely using environment variables
* No data is stored or logged externally
* Uploaded files remain in-memory during the session

---

## 🌱 Future Enhancements

* Support for multiple files
* Downloadable charts and reports
* Query history export
* Authentication & role-based access
* Dashboard-style summaries

---

## 📄 License

This project is for **educational and experimental purposes**.
You may modify and extend it as per your requirements.

