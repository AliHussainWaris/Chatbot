import os
from pyaiml21 import Kernel
from nltk import pos_tag, word_tokenize
from bs4 import BeautifulSoup
import requests

aimFiles = []
aimlDirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aimlfile")

my_bot = Kernel()

for file in os.listdir(aimlDirectory):
    if file.endswith(".aiml"):
        aimFiles.append(os.path.join(aimlDirectory, file))

for aimFile in aimFiles:
    my_bot.learn_aiml(aimFile)

def aimlfun(user_input, name):
    tokens = word_tokenize(user_input)
    pos = pos_tag(tokens)

    my_bot.setBotPredicate("username", name)
    x = True

    while x:
        reply = my_bot.respond(user_input, "")
        if reply == "Your name is unknown.":
            username = my_bot.getBotPredicate("username")
            reply = "Your name is " + username+"."
        elif "unknown" in reply:
            tags = [tag for _, tag in pos]

            if 'NN' in tags:
                noun_index = tags.index('NN')
                noun = tokens[noun_index]
                url = f"https://www.google.com/search?q={noun}"
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')

                search_result = soup.find('div', class_='g')
                if search_result:
                    link = search_result.find('a')
                    if link:
                        extracted_data = link.get('href')
                        reply = "The data I found from Google is: " + extracted_data

        print("Bot:", reply)

        if user_input:
            x = False

    return reply