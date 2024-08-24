import json

with open("data/python-quiz.json", "r") as q:
    questions = json.load(q)

questions = questions["questions"]
for i in questions:
    print(i["answer"])
