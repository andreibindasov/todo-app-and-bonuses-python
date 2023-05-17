import json

with open("questions.json", 'r') as f:
    content = f.read()


data = json.loads(content)
print(data)

score = 0

for q in data:
    print(q["q_text"])
    for i, alt in enumerate(q["alternatives"]):
        print(f"{i + 1} - {alt.title()}")
    q["user_choice"] = input("Your answer:")


for i, q in enumerate(data):
    if int(q["user_choice"]) == int(q["answer"]):
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    msg = f"{i+1} {result} - Your answer: {q['user_choice']}, " \
          f"Correct answer: {q['answer']}"
    print(msg)

print(score, "/", len(data))