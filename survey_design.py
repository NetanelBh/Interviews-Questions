from enum import Enum


class QuestionType(Enum):
    MULTIPLE_CHOICE = 0
    SINGLE_ANSWER = 1
    
    
SMALL_A_ASCII = 97


class Survey:
    def __init__(self, title):
        self.title = title
        self.questions = list()
        self.users = list()

    def conduct_survey(self):
        for user in self.users:
            print(f"------------- Welcome to survey -------------")
            for index, q in enumerate(self.questions, 1):
                q.ask_question(index)
                user.answer_question(q)

            print()

    def add_question(self, question):
        self.questions.append(question)

    def add_user(self, user):
        self.users.append(user)

    def show_results(self):
        print("========== Results ==========")
        for user in self.users:
            for key, value in user.responses.items():
                print(key)
                print(value)

            print("-------------------------")


class Question:
    def __init__(self, text, q_type, options=None):
        self.text = text
        self.q_type = q_type
        self.options = options if options else list()

    def add_option(self, option):
        self.options.append(option)

    def ask_question(self, q_number):
        print(f"{q_number}. {self.text}")
        if self.q_type == QuestionType.MULTIPLE_CHOICE:
            for i, option in enumerate(self.options, SMALL_A_ASCII):
                print(f"  {chr(i)}. {option}")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Pairs of question-answer
        self.responses = dict()

    def answer_question(self, question):
        if question.q_type == QuestionType.MULTIPLE_CHOICE:
            answers = input("Choose at least one answer: ").split(' ')
            for i, answer in enumerate(answers, 0):
                # Convert the answer letter(a. b. c.) to numbers
                answers[i] = question.options[ord(answer) - SMALL_A_ASCII]
            response = Response(question.text, answers)
            self.responses[response.q] = response.a
        else:
            response = Response(question.text, input("Enter your answer: "))
            self.responses[response.q] = response.a

        # One line space
        print()


class Response:
    def __init__(self, q, a):
        self.q = q
        self.a = a


if __name__ == "__main__":
    survey = Survey("Personal survey")

    question1 = Question("What is your name?", QuestionType.SINGLE_ANSWER)
    question2 = Question("What do you like to eat?", QuestionType.MULTIPLE_CHOICE, ["Kuskus", "Frikase"])

    survey.add_question(question1)
    survey.add_question(question2)

    user1 = User("Netanel", "12@gmail.com")
    user2 = User("Maor", "mun@nana.com")

    survey.add_user(user1)
    survey.add_user(user2)

    survey.conduct_survey()
    survey.show_results()
