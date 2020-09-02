import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def Transform(word):
    matches = get_close_matches(word, data.keys())
    word = word.lower()
    if word in data:
        return data[word]
    elif len(matches) > 0:
        choice = input("Did you mean %s ? Y if yes, N for no: " %matches[0])
        if choice =='Y':
            return data[matches[0]]
        else:
            return "Sorry, No word found !"
    return "Word Does not Found! Please Check it. "

word = input("Enter a word: ")
output = Transform(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)