import random
import re
from datetime import datetime

# Memory for user details
memory = {"name": None, "mood": None}

def chatbot():
    print("🤖 PyBot: Hi! I’m PyBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if re.search(r"\b(bye|exit|quit)\b", user_input):
            print("🤖 PyBot: It was nice talking to you, take care ❤️")
            break

        # Greeting
        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            if memory["name"]:
                print(f"🤖 PyBot: Hey {memory['name']}! How are you today?")
            else:
                print("🤖 PyBot: Hello! What’s your name?")

        # Capture Name
        elif re.search(r"my name is (.*)", user_input):
            name = re.findall(r"my name is (.*)", user_input)[0]
            memory["name"] = name.capitalize()
            print(f"🤖 PyBot: Nice to meet you, {memory['name']}! 😊")

        # Asking how user is
        elif re.search(r"\b(how are you)\b", user_input):
            print("🤖 PyBot: I’m doing great! Thanks for asking. How about you?")

        # Capture Mood
        elif re.search(r"\bi am (.*)", user_input):
            mood = re.findall(r"\bi am (.*)", user_input)[0]
            memory["mood"] = mood
            print(f"🤖 PyBot: Oh, you are {mood}? Thanks for sharing! 💡")

        # Recall mood
        elif "how am i" in user_input:
            if memory["mood"]:
                print(f"🤖 PyBot: You told me you were {memory['mood']} earlier 😊")
            else:
                print("🤖 PyBot: Hmm, you didn’t tell me yet. How are you feeling?")

        # Time
        elif "time" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 PyBot: The current time is {now} ⏰")

        # Name recall
        elif "what is my name" in user_input:
            if memory["name"]:
                print(f"🤖 PyBot: Of course, your name is {memory['name']} 😎")
            else:
                print("🤖 PyBot: Hmm, I don’t know yet. What’s your name?")

        # Fallback
        else:
            responses = [
                "That’s interesting, tell me more 🤔",
                "Hmm, I see. Can you explain a little more?",
                "Oh really? That sounds cool 😃",
                "I’d love to hear more about that!"
            ]
            print("🤖 PyBot:", random.choice(responses))

chatbot()
