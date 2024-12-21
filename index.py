class SimpleChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hi there! How can I assist you today?",
            "hi": "Hello! How can I help you?",
            "how are you": "I'm just a bot, but I'm doing great! How about you?",
            "bye": "Goodbye! Have a great day!",
            "what is your name": "I am a simple chatbot, I don't have a name yet!",
            "default": "Sorry, I didn't understand that. Can you try asking something else?"
        }

    def get_response(self, user_input):
        user_input = user_input.lower()  # Convert input to lowercase for easy matching
        return self.rules.get(user_input, self.rules["default"])

# Main program
def chat():
    bot = SimpleChatbot()
    print("Chatbot: Hello! I am your chatbot. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "bye":
            print(f"Chatbot: {bot.get_response(user_input)}")
            break
        
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
