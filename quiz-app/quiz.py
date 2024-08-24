from quizParser import QuizParser
from question import MQuestion, YNQuestions

class Quiz:

    def __init__(self):
        self.username = ""
        self.name = ''
        self.desc = ''
        self.questions = []
        self.totalScore = 0
        self.totalPoints = 0
        self.parser = QuizParser()

    def welcome(self):
        print(f"Welcome To Pyquiz!!")
        print("*" * 50)
        print()
        self.username = input("Enter your Name: ")
    
    def list_quiz(self):
        quizzes = {
            1 : "Python Quiz"
        }

        for k, v in quizzes.items():
            print(f"({k}) {v}")


    def menu(self):
        print(f"Choose an option from the List {self.username}")
        options = ("Repeat the Menu", "List the quizzes", "Take a Quiz", "Exit")
        for no, opt in enumerate(options):
            print(f"({no + 1}) : {opt}")

        selection = ''
        try:
            selection = int(input("Selection ? "))
            if selection not in range(1, len(options) + 1):
                raise Exception
        except Exception:
            print("Please Try Again!!!")
            self.menu()
        else:
            if selection == 4:
                print("Thanks for visiting.")
            elif selection == 1:
                self.menu()
            elif selection == 2:
                print("Available Quizzes")
                print('-' * 50)
                print()
                self.list_quiz()
                print()
                self.menu()
            elif selection == 3:
                try:
                    quiznum = int(input("Enter the quiz id: "))
                    quiz = self.parser.load_questions(quiznum)
                except Exception as e:
                    print("Please Enter a Valid Quiz Id")
                    self.menu()
                else:
                    self.name = quiz['name']
                    self.desc = quiz['description']
                    self.totalPoints = quiz['totalScore']
                    self.totalScore = 0
                    for question in quiz['questions']:
                        if question['type'] == 'mcq':
                            self.questions.append(MQuestion(question['question'], question['answer'], question['score'], question['options']))
                        else:
                            self.questions.append(YNQuestions(question['question'], question['answer'], question['score']))
                    for question in self.questions:
                        question.ask()
                        self.totalScore += question.score

    def print_results(self):
        print("*" * 50)
        print(f"Username : {self.username}")
        print(f"Quiz Name : {self.name}")
        print(f"Quiz Description : {self.desc}")
        print(f"Username : {self.username}")
        print(f"Score Gained : {self.totalScore} / {self.totalPoints}")
        print("*" * 50)

                    

        

    def run(self):
        self.welcome()
        self.menu()
        self.print_results()

if __name__ == "__main__":
    q = Quiz()
    q.run()
