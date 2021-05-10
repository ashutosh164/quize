from Question import Question
from win32com.client import Dispatch

question_prompt = [
    "what color are apples?\n(a) red\n(b) pink\n(c) blue\n\n",
    "what color are banana?\n(a) green\n(b) yellow\n(c) pink\n\n",
    "what color are strawberries?\n(a) yellow\n(b) blue\n(c) red\n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c")

]


def run_test():
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("you got " + str(score) + "/" + str(len(questions)) + "correct")
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak("you got " + str(score) + "out of " + str(len(questions)) + " correct")


run_test()













