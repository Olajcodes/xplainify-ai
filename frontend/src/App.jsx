import { useState, useEffect } from "react";
import "./App.css";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  // ---- Load saved chats on mount ----
  useEffect(() => {
    const saved = localStorage.getItem("xplainify_messages");
    if (saved) {
      setMessages(JSON.parse(saved));
    }
  }, []);

  // Format timestamps for display
  function formatTime(ts) {
  if (!ts) return "";
  const date = new Date(ts);
  return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}


  // ---- Save chats whenever messages update ----
  useEffect(() => {
    localStorage.setItem("xplainify_messages", JSON.stringify(messages));
  }, [messages]);

  async function sendMessage() {
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input, timestamp: new Date().toISOString()};

    // Show user message immediately
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch("https://xplainify-ai.onrender.com/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage.content }),
      });

      const data = await response.json();

      const assistantMessage = {
        role: "assistant",
        content: data.response,
        timestamp: new Date().toISOString()
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error("Error:", error);
    }

    setLoading(false);
  }

  return (
    <div className="h-screen flex flex-col bg-xlight font-inter">

      {/* Header */}
      <header className="bg-blue-200 text-white px-2 py-4 shadow-lg flex justify-between gap-10">
        <h1 className="text-blue-500 md:text-xl sm:text-sm font-bold tracking-wide">Xplainify AI</h1>
        <div className="text-blue-00 md:text-xl sm:text-sm   font-bold"> ...Your Intelligent Multi-Persona Learning Companion</div>
      </header>

      {/* Chat Area */}
      <main className="flex-col overflow-y-auto p-6 space-y-4 h-3/4 ">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`  md:max-w-[50%] w-fit  break-word px-4 py-4 rounded-xl shadow-md ${
              msg.role === "user"
                ? "bg-blue-300 text-blue ml-auto text-right"
                : "bg-gray-200 border border-blue-200 text-left"
            }`}
          >
            <p className="whitespace-pre-wrap">{msg.content}</p>
           {/* Timestamp */}
            <p className="text-[10px] text-gray-700 mt-1">
              {formatTime(msg.timestamp)}
            </p> 
          </div>
        ))}

        {loading && (
          <p className="text-gray-500 animate-pulse">Thinking...</p>
        )}
      </main>

      {/* Input Section */}
      <footer className="bg-blue p-3 border-t flex gap-1">
        <input
          type="text"
          className=" w-full mx-auto p-2 border rounded-xl   focus:outline-none focus:ring-2 focus:ring-blue"
          placeholder="Ask Xplainify something..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />

        <button
          onClick={sendMessage}
          className="bg-blue-600 text-white px-6 rounded-xl hover:bg-dark transition"
        >
          Send
        </button>
      </footer>
    </div>
  );
}
