from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Alex')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train([
    'how are you',
    'I am not feeling well'
])

# Get a response to an input statement
name = input("please enter your name: ")
print(f"welcome to Alexbot service {name} what can I do for you?")

while True:
    request = input(f"{name}: ")

    if request.lower() == 'bye':
        print ("Bot: Bye")
        break
    else:
        response = chatbot.get_response(request)
        print("Bot:", response)

print(f'response: {response}')
