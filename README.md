# 🤖 Gemini AI Chatbot

A chatbot powered by **Google Gemini AI** using **Streamlit** for an interactive web interface.

---

## 🚀 Features
- 🌍 Uses **Google Gemini AI (gemini-1.5-flash)** for conversational responses.
- ⚡ **Real-time streaming** response for better user experience.
- 📝 Maintains **chat history** within the session.
- 🔑 Securely fetches API keys using **dotenv**.
- 🎨 Simple **Streamlit-based UI**.

---

## 🛠 Installation

### **1️⃣ Clone the Repository**
```bash

cd gemini-chatbot
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
venv\Scripts\activate  
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the project directory and add your Google API key:
```env
GOOGLE_API_KEY= "api_key"
```

---

## 🚀 Run the Chatbot
```bash
streamlit run app.py
```

Open **`http://localhost:8501`** in your browser to start chatting!

---

## 🏗 Project Structure
```
📂 gemini-chatbot
│── app.py                # Main Streamlit app
│── requirements.txt       # Dependencies
│── .env                   # API key (not to be shared)
│── README.md              # Project documentation
```

---

## 📌 Usage
1️⃣ Open the **chat interface**.
2️⃣ Type your message and hit Enter.
3️⃣ The chatbot **streams responses** from Gemini AI.
4️⃣ Enjoy an interactive chat experience! 🚀

---

## 🔗 Resources
- [Google Gemini API Docs](https://ai.google.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 📜 License
This project is licensed under the **MIT License**.

---

🚀 **Happy Coding!** 💡

