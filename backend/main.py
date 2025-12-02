from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os
import google.generativeai as genai

from router import route_user_intent
from personas import (
    TEACHER_PROMPT,
    SOCRATIC_PROMPT,
    QUIZ_MASTER_PROMPT,
    EVALUATOR_PROMPT
)

app = FastAPI(title="Xplainify AI System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")



# ---------- Root Endpoint ----------
@app.get("/")
def root():
    return {
        "status": "running",
        "app": "Xplainify AI System",
        "message": "Welcome to Xplainify — Your Intelligent Multi-Persona Learning Companion"
    }



# ---------- Request Schema ----------
class UserMessage(BaseModel):
    message: str = Field(examples=["What is RNN?"])


# ---------- Persona Selector ----------
def get_persona_prompt(persona_name: str) -> str:
    if persona_name == "teacher":
        return TEACHER_PROMPT
    if persona_name == "socratic":
        return SOCRATIC_PROMPT
    if persona_name == "quiz":
        return QUIZ_MASTER_PROMPT
    if persona_name == "evaluator":
        return EVALUATOR_PROMPT
    return TEACHER_PROMPT


# ---------- Chat Endpoint ----------
@app.post("/chat")
def chat_with_Xplainify(payload: UserMessage):

    user_message = payload.message
    persona = route_user_intent(user_message)
    persona_prompt = get_persona_prompt(persona)

    # Create system + user instructions
    prompt = f"""
You are operating under this persona:
{persona_prompt}

User message:
{user_message}
"""

    # Call Gemini
    response = model.generate_content(prompt)

    ai_reply = response.text

    return {
        "persona_selected": persona,
        "response": ai_reply
    }


# ---------- Terminal Version ----------
def main():
    print("\nXplainify AI Terminal Chat")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        persona = route_user_intent(user_message)
        persona_prompt = get_persona_prompt(persona)

        prompt = f"""
Persona: {persona_prompt}

User: {user_message}
"""

        response = model.generate_content(prompt)
        reply = response.text

        print(f"\n{reply}\n")


if __name__ == "__main__":
    main()
