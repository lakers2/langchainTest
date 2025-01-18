from chat_assistant import ChatAssistant

def main():
    # Create chat assistant with specific model
    assistant = ChatAssistant(model_name="llama3.2:latest")
    
    print("Ollama Chat Assistant (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            break
            
        response = assistant.chat_with_ai(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
