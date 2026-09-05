def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"

    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot created in Python!"

    elif "what can you do" in user_input or "help" in user_input:
        return "I can chat with you about simple things. Try saying hello, asking how I am, or saying bye."

    elif "thank" in user_input:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Could you rephrase?"


def chat():
    print("Chatbot: Hello! I'm your assistant. Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    chat()
