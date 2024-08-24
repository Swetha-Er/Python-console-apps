class Question:
    def __init__(self, question, answer, score):
        self.question = question
        self.answer = answer
        self.score = 0
        self.is_correct = False
        self.points = score
    
class YNQuestions(Question):
    def __init__(self, question, answer, score):
        super().__init__(question, answer, score)

    def ask(self):
        try:
            print(self.question)
            print("Enter (T)rue or (F)alse : ", end="")
            response = input()
            if len(response) != 1 or response.lower() not in ("t", "f"):
                raise Exception
        except Exception as e:
            print("Invalid Response! Try Again!")
            self.ask()
        else:
            if str(self.answer)[0].lower() == response.lower():
                self.is_correct = True
                self.score = self.points

class MQuestion(Question):
    def __init__(self, question, answer, score, options):
        super().__init__(question, answer, score)
        self.options = options

    def ask(self):
        try:
            print(self.question)
            print("Choose from the options below: ")
            for idx, text in enumerate(self.options):
                print(f"({idx + 1}) {text}")
            print()
            response = input("Your Response: ")
            if len(response) != 1 or int(response) not in range(1, len(self.options) + 1):
                raise Exception
        except Exception as e:
            print("Invalid Response! Try Again!")
            self.ask()
        else:
            if self.answer.lower() == self.options[int(response) - 1].lower():
                self.is_correct = True
                self.score = self.points