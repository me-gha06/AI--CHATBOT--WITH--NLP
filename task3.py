import nltk
import random
import string
from nltk.stem import WordNetLemmatizer

# Sample data
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Bye!", "See you later!", "Goodbye!"],
    "name": ["I'm your CodTech Chatbot.", "You can call me CodBot."],
    "default": ["I'm not sure I understand.", "Can you rephrase that?"]
}

lemmatizer = WordNetLemmatizer()

def preprocess(sentence):
    # Lowercase, remove punctuation, tokenize, lemmatize
    sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word) for word in tokens]

def get_response(user_input):
    tokens = preprocess(user_input)

    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"])
    elif any(word in tokens for word in ["bye", "goodbye", "see ya"]):
        return random.choice(responses["goodbye"])
    elif any(word in tokens for word in ["name", "who", "you"]):
        return random.choice(responses["name"])
    else:
        return random.choice(responses["default"])

# Main chat loop
print("CodBot: Hello! I'm your chatbot. Type 'exit' to end.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("CodBot: Goodbye!")
        break
    response = get_response(user_input)
    print(f"CodBot: {response}")
