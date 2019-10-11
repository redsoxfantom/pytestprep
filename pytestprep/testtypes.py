import random

class RandomTest:
    def __init__(self,questions):
        self.questions = questions
        self.num_questions_asked = 0

    def has_more_questions(self):
        return True

    def get_next_question(self):
        self.num_questions_asked = self.num_questions_asked + 1
        return self.questions[random.randrange(len(self.questions))]

    def get_num_questions(self):
        return self.num_questions_asked

class TimedTest:
    def __init__(self,questions,num_questions):
        self.questions = []
        self.curr_question = 0
        self.num_questions = num_questions
        for i in range(0,num_questions):
            question = None
            while question not in self.questions:
                question = random.choice(questions)
            self.questions.append(question)

    def has_more_questions(self):
        if self.curr_question < self.num_questions:
            return True
        return False

    def get_next_question(self):
        question = self.questions[self.curr_question]
        self.curr_question += 1
        return question

    def get_num_questions(self):
        return self.num_questions