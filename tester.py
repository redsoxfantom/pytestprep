from pytestprep.testparser import parse_test_bank
import sys
from pprint import pprint

def print_question(q):
    print(q.question)
    pprint(q.choices)
    print(q.answer)
    print(q.explanation)


testfile = sys.argv[1]
print("Parsing %s..." % testfile)
questions = parse_test_bank(testfile)
print("Parsed %s questions from %s" % (len(questions),testfile))

for q in questions:
    print_question(q)