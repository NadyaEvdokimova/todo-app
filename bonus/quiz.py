import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer


for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1} - {result} Your answer: {question['user_answer']}, Correct answer: {question["correct_answer"]}"
    print(message)

print(f"Your score is {score}/{len(data)}")

