from pytestprep.testparser import parse_test_bank
from pytestprep.testtypes import *
import sys
from datetime import datetime
from datetime import timedelta

def print_question(q):
    print(q.question)
    for choice in q.choices:
        print("%s %s" % (choice, q.choices[choice]))
    print(q.answer)
    print(q.explanation)

def ask_question(q,num,show_answer):
    print("----------------------------------------")
    print("==Question %s==" % num)
    print(q.question)
    print()
    for choice in q.choices:
        print("%s: %s" % (choice, q.choices[choice]))
    print()
    answer = input("Answer: ")
    answer_correct = (answer.lower() == q.answer.lower())
    if show_answer:
        if answer_correct:
            print("Correct")
        else:
            print("Incorrect, the correct answer is %s" % q.answer)
        if q.explanation:
            print(q.explanation)
    print("----------------------------------------")
    return answer_correct

testfile = sys.argv[1]
print("Parsing %s..." % testfile)
questions = parse_test_bank(testfile)
print("Parsed %s questions from %s" % (len(questions),testfile))

selection = input("Select a test type:\n1) Infinite Random Question\n2) Timed Test (90 questions, 90 minutes)\n")
questionProvider = None
show_answers = False
if selection == "1":
    questionProvider = RandomTest(questions)
    show_answers = True
    time_limit = datetime.now() + timedelta(days=10)
if selection == "2":
    questionProvider = TimedTest(questions,90)
    show_answers = False
    time_limit = datetime.now() + timedelta(minutes=90)

question_num = 0
num_correct = 0
while questionProvider.has_more_questions() and datetime.now() < time_limit:
    question = questionProvider.get_next_question()
    correct = ask_question(question,question_num + 1,show_answers)
    question_num = question_num + 1
    if correct:
        num_correct = num_correct + 1
    if show_answers:
        print("You have answered %s/%s questions correctly, for a score of %s" % (num_correct,question_num,(num_correct / question_num) * 100.0))

print("Test Complete")
print("You have answered %s/%s questions correctly, for a score of %s" % (num_correct,questionProvider.get_num_questions(),(num_correct / questionProvider.get_num_questions()) * 100.0))