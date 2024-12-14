import re
def resume_screener(resume_text):
    keywords = ["python", "data science", "machine learning"]
    score = 0
    for keyword in keywords:
        if re.search(r'\b' + keyword + r'\b', resume_text, re.IGNORECASE):
            score += 1
    print(f"Resume score: {score}/{len(keywords)}")
resume_text = input("Enter resume text: ")
resume_screener(resume_text)
