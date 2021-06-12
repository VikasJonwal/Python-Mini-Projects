import json
data = json.load(open("data.json"))
word = input("Enter The Word \n")
word = word.lower()
if word in data:
    print(data[word])
elif word.title() in data:
    print(data[word.title()])
elif word.capitalize() in data:
    print(data[word.capitalize()])
elif word.upper() in data:
    print(data[word.upper()])
else:
    print(f"Sorry '{word}' Word Is Not Present In Our Dict.")
