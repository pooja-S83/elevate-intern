import datetime
import random

def chatbot():
    print("            🤖 Chatbot: Hello! I am your chatbot."       )
    print("Type 'exit', 'bye', anytime to end the conversation.\n")

    user_name = None
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it caught a virus!",
        "Why do Java developers wear glasses? Because they don’t see sharp!"
    ]

    while True:
        user_input = input("💕You: ").lower().strip()

        # Exit condition
        if user_input in ["exit", "quit", "bye"]:
            print("🤖 Chatbot: Goodbye! Take care 😊")
            break

        # Greeting
        elif any(greet in user_input for greet in ["hello", "hi", "hey"]):
            if user_name:
                print(f"🤖 Chatbot: Hello {user_name}, nice to see you again!")
            else:
                print("🤖 Chatbot: Hi there! What's your name?")

       
        elif "my name is" in user_input:
            user_name = user_input.replace("my name is", "").strip().capitalize()
            print(f"🤖 Chatbot: Nice to meet you, {user_name}!")

        elif user_name is None and "name" in user_input:
            print("🤖 Chatbot: I don’t know your name yet. You can tell me by saying 'My name is <your name>'.")


        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a bot, but I'm doing great! How about you?")

        elif "i am fine" in user_input or "good" in user_input:
            print("🤖 Chatbot: That’s great to hear! Keep smiling 😄")


        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M %p")
            print(f"🤖 Chatbot: The current time is {now}")

        elif "date" in user_input or "day" in user_input:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            print(f"🤖 Chatbot: Today is {today}")

        # Joke
        elif "joke" in user_input:
            print(f"😂 {random.choice(jokes)}")

        # Hobbies / interests
        elif "hobby" in user_input or "hobbies" in user_input:
            print("🤖 Chatbot: I love chatting with humans and making them smile!")

        elif "what can you do" in user_input or "help" in user_input:
            print("🤖 Chatbot: I can tell jokes, share the date & time, greet you, and chat casually!")

        # Default response
        else:
            print("🤖 Chatbot: Hmm... I’m not sure about that. Try asking me for a joke, time, or just say hello!")

if __name__ == "__main__":
    chatbot()
