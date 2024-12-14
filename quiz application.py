def quiz_application():
    questions = [("What is 2 + 2?", "4"), ("What is the capital of France?", "Paris")]
    score = 0
    for question, answer in questions:
        user_answer = input(f"{question}: ")
        if user_answer == answer:
            score += 1
    print(f"You scored {score}/{len(questions)}")
quiz_application()
