from docx import Document
from pprint import pprint
import re

class Question:
    def __init__(self,question,choices,answer,explanation):
        self.question = question.strip()
        self.choices = {}
        for choice in choices:
            self.choices[choice] = choices[choice].strip()
        self.answer = answer.strip()
        self.explanation = explanation.strip()

def parse_test_bank(file):
    question_regex = r"QUESTION NO: \d+"
    in_question = False
    question_text = ""
    answer_regex = r"Answer: (.)"
    in_explanation = False
    explanation_text = ""
    option_regex = r"^([A-Z]).$"
    options = {}
    current_option = ""
    answer = ""
    in_option = False
    questions = []
    
    testdoc = Document(file)
    for para in testdoc.paragraphs:
        text = para.text
        question_match = re.search(question_regex,text)
        option_match = re.search(option_regex,text)
        answer_match = re.search(answer_regex,text)
        if in_explanation and not question_match:
            explanation_text = explanation_text + "\n" + text
        if in_option and not option_match and not answer_match:
            options[current_option] = options[current_option] + "\n" + text
        if in_question and not option_match:
            question_text = question_text + "\n"+ text
        if answer_match:
            in_question = False
            in_explanation = True
            in_option = False
            answer = answer_match.group(1)
        if option_match:
            in_question = False
            in_explanation = False
            in_option = True
            current_option = option_match.group(1)
            options[current_option] = ""
        if question_match:
            in_question = True
            in_explanation = False
            in_option = False
            if answer:
                questions.append(Question(question_text,options,answer,explanation_text))
            answer = None
            options = {}
            question_text = ""
            explanation_text = ""
    return questions
