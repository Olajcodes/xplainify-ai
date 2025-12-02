import re

def route_user_intent(message: str) -> str:
    msg = message.lower()

    # Explanation → Teacher
    if any(word in msg for word in ["explain", "what is", "meaning of", "break down", "teach"]):
        return "teacher"

    # Guidance → Socratic Coach
    if any(word in msg for word in ["help me think", "guide me", "how should i approach", "understand"]):
        return "socratic"

    # Quiz → Quiz Master
    if any(word in msg for word in ["quiz", "test me", "generate questions", "mcq", "practice questions"]):
        return "quiz"

    # Evaluation → Evaluator
    if any(word in msg for word in ["evaluate", "score", "grade", "is my answer correct"]):
        return "evaluator"

    # Default → Teacher asks for clarification
    return "teacher"
