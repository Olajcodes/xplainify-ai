# 🧠 Xplainify-AI

A simple and powerful AI-assistant built with **FastAPI**, **React**, **TailwindCSS**, and **Gemini API** — designed to help users ask questions, and get explanations.

Xplainify-AI provides:

- A FastAPI backend that connects to the Gemini API
- A React frontend with a clean chat UI
- Timestamps for both user and AI messages
- Mobile-friendly interface
- User messages right-aligned
- AI responses left-aligned

---

## 🚀 Features

### **Backend (FastAPI)**

- `/` root endpoint — health check + welcome message  
- `/chat` — send a message to Gemini and receive a reply   
- Automatic timestamps  
- CORS enabled  
- Error handling  

### **Frontend (React + TailwindCSS)**

- Clean chat interface  
- User messages aligned right  
- AI messages aligned left  
- Auto-scroll to bottom  
- Displays timestamps  

---

## 📁 Project Structure


```
xplainify-ai/
│
├── backend/
│   ├── main.py
│   ├── chats.json
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── ...
│   ├── index.html
│   ├── tailwind.config.js
│   └── package.json
│
└── README.md
```