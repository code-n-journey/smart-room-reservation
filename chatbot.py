def chat_with_ai(user_input: str) -> str:
    user_input = user_input.lower()
    if "book" in user_input or "reserve" in user_input:
        return "Sure! Which room number would you like to reserve?"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    else:
        return "I'm here to help you with reservations or chatting about books!"