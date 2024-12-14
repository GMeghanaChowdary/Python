def chatbot():
    print("Hello, I am your chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif "hello" in user_input.lower():
            print("Chatbot: Hello! How can I help you?")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm doing great! How about you?")
        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()
