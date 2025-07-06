# AI--CHATBOT--WITH--NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MEGHA

*INTERN ID*: CT04DG457

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

# DESCRIPTION:
This project is an implementation of a simple AI chatbot using Natural Language Processing (NLP) techniques in Python. Created as part of the CodTech internship program, this chatbot demonstrates fundamental concepts of text preprocessing, intent recognition, and human-computer interaction using a rule-based approach. The bot can interact with users through text, respond appropriately to greetings, name-related questions, and farewells, and provide a default response when it doesn't understand the input.

# Objective:
The goal of this task was to build a chatbot that can understand user inputs in natural language, process them intelligently using NLP, and generate relevant responses. This basic conversational agent sets the foundation for more advanced chatbots by introducing essential components like tokenization, lemmatization, keyword detection, and rule-based logic.

# How It Works:
*Input Processing*:
When a user types a message, the chatbot first preprocesses the text. This involves:
Lowercasing the input for uniformity.
Removing punctuation using the string module.
Tokenizing the input (splitting it into words) using NLTK's word_tokenize.
Lemmatizing the words using WordNetLemmatizer to reduce them to their base forms.

*Intent Recognition*:
The chatbot then checks whether the processed input contains specific keywords associated with predefined intents:
Greetings (e.g., "hi", "hello", "hey")
Goodbyes (e.g., "bye", "goodbye", "see ya")
Name-related questions (e.g., "who", "name", "you")
If a keyword is found in the input, the chatbot selects a random response from a list corresponding to that intent. If no keywords match, it returns a default fallback response.

*Response Generation*:
The chatbot uses the Python random module to randomly choose a response from the appropriate category. This makes the interaction feel a bit more natural and less repetitive.

*Chat Loop*:
The main chat function runs in a loop, allowing continuous interaction until the user types "exit", at which point the chatbot ends the conversation with a goodbye message.

# Technologies Used:
Python – Core programming language
NLTK (Natural Language Toolkit) – For tokenization and lemmatization
Random – To randomize responses
String – For text cleaning and punctuation removal

# Learning Outcomes:
By building this chatbot, I learned:
The basics of NLP preprocessing: tokenization, punctuation removal, and lemmatization.
How to create rule-based logic for conversational bots.
How to handle user input and create interactive loops.
The structure and flow of a simple conversational AI system.

# Applications & Scope:
Although this chatbot is simple, it forms the base for more advanced AI chatbots. It can be extended in the future by:
Adding more intents and training data.
Integrating machine learning models for smarter intent classification.
Deploying it on a web platform using Flask or Streamlit.

# OUTPUT:

<img width="1255" height="178" alt="Image" src="https://github.com/user-attachments/assets/36155e9a-33b6-49ea-a84a-433be3d217a6" />
