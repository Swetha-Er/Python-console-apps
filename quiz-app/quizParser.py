import json

class QuizParser:
    
    def load_questions(self, id):

        filemap = {
            1 : 'python-quiz.json'
        }

        with open(f"data/{filemap[id]}", "r") as q:
            quiz = json.load(q)

        return quiz
    



        
