class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
    
    #퀴즈 출력
    def show(self):
        print(self.question)                   
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")          
    
    #정답 비교
    def check(self, user_choice):
        return user_choice == self.answer

    #퀴즈 저장
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }
    #퀴즈 불러오기
    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])