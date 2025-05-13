class RuleBasedAgent:
    def __init__(self, name):
        self.name = name

    def respond(self, input_text):
        input_text = input_text.lower()

        if "hello" in input_text:
            return "Hi there!"
        elif "how are you" in input_text:
            return "I'm an AI agent, I'm always functioning."
        elif "bye" in input_text:
            return "Goodbye!"
        else:
            return "I'm not sure how to respond to that."

# Example interaction
if __name__ == "__main__":
    agent = RuleBasedAgent("HelperBot")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Agent:", agent.respond(user_input))
