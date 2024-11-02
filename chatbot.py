import json
import random
import os

# Load responses from the JSON file
def load_responses(file_path="data/responses.json"):
    with open(file_path, "r") as file:
        return json.load(file)

# Define response functions
def get_response(user_input, responses):
    user_input = user_input.lower()
    
    # Respond to greetings
    if any(greet in user_input for greet in ["hello", "hi", "hey"]):
        return random.choice(responses["greetings"])
    
    # Respond to farewells
    elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return random.choice(responses["farewells"])
    
    # Respond to "how are you"
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    
    # Respond with a fun fact
    elif "tell me a fun fact" in user_input:
        return random.choice(responses["fun_fact"])
    
    # Default response
    else:
        return "I'm sorry, I don't understand that yet. Can you try asking something else?"

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! I'm here to chat with you. Type 'bye' to end the conversation.")
    responses = load_responses()
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot:", random.choice(responses["farewells"]))
            break
        
        response = get_response(user_input, responses)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
