
import json
from game.quiz import Quiz
from game.util import show_logo, show_menu, clear_screen, exit_game, pause, get_valid_input


default_quizzes = [
    Quiz("영화 '기생충'의 감독은?", ["봉준호", "박찬욱", "김지운", "나홍진"], 1),
    Quiz("영화 '타이타닉'의 남자 주인공을 연기한 배우는?", ["브래드 피트", "레오나르도 디카프리오", "톰 크루즈", "조니 뎁"], 2),
    Quiz("영화 '어벤져스'에서 아이언맨 역을 맡은 배우는?", ["크리스 에반스", "크리스 헴스워스", "로버트 다우니 주니어", "마크 러팔로"], 3),
    Quiz("영화 '겨울왕국'에서 눈사람 캐릭터의 이름은?", ["올라프", "스벤", "크리스토프", "한스"], 1),
    Quiz("영화 '해리포터' 시리즈의 주인공 이름은?", ["론 위즐리", "해리 포터", "드레이코 말포이", "네빌 롱바텀"], 2),
]


class QuizGame:
    def __init__(self):
        self.data = self.load_data()
        self.quizzes = self.load_quizzes()
        if not self.quizzes:                  # 저장된 퀴즈가 없으면
            self.quizzes = default_quizzes    # 기본 퀴즈로 채우기

    # ---------- 파일 저장/불러오기 ----------
    def load_data(self):
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "quizzes": [],
                "best_score": {"correct": 0, "total": 0}
            }

    def save_data(self):                           
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def save_quizzes(self):                        
        self.data["quizzes"] = [q.to_dict() for q in self.quizzes]
        self.save_data()                              
        print("저장 완료!")

    def load_quizzes(self):
        data = self.load_data()
        return [Quiz.from_dict(d) for d in data["quizzes"]]

    # ---------- 퀴즈 만들기 ----------
    def make_quiz(self):
        while True:
            try:
                question = input("문제를 입력하세요: ").strip()
                if not question:
                    print("문제를 입력해 주세요.")
                    continue
                break
            except (KeyboardInterrupt, EOFError):
                exit_game()
        choices = []
        while len(choices) < 4:
            try:
                num = len(choices) + 1
                choice = input(f"{num}번 선택지: ").strip()
                if not choice:
                    print("선택지를 입력해 주세요.")
                    continue
                choices.append(choice)
            except (KeyboardInterrupt, EOFError):
                exit_game()
        answer = get_valid_input("정답 번호(1~4): ", 1, 4)
        return Quiz(question, choices, answer)

    # ---------- 퀴즈 풀기 ----------
    def play_quiz(self):                            
        if not self.quizzes:                         
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            pause()
            return

        total = len(self.quizzes)                 
        score = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)\n")
        print("--------------------------------------")
        for q in self.quizzes:                    
            q.show()
            answer = get_valid_input("정답 번호 : ", 1, 4)
            if q.check(answer):
                print("\n정답입니다!\n")
                score += 1
            else:
                print("\n틀렸어요ㅠㅠ\n")

        print(f"최종 점수: {score} / {total}")
        self.update_best_score(score)            
        pause()

    # ---------- 점수 ----------
    def update_best_score(self, correct):            
        total = len(self.quizzes)                  
        if total == 0:
            print("풀 수 있는 퀴즈가 없어요!")
            return

        current_rate = correct / total
        best = self.data["best_score"] 

        if best["total"] == 0 or current_rate > best["correct"] / best["total"]:
            self.data["best_score"] = {
                "correct": correct,
                "total": total
            }
            self.save_data()
            print("🎉 최고 기록 갱신!")
        else:
            print("최고 기록은 갱신되지 않았어요.")

    def show_best_score(self):                      
        best = self.data["best_score"]   

        if best["total"] == 0:
            print("아직 퀴즈를 풀지 않았어요!")
            return

        correct = best["correct"]
        total = best["total"]
        percent = int(correct / total * 100)
        print(f"🏆 현재 최고 점수: {percent}점 ({total}문제 중 {correct}문제 정답)")

    # ---------- 목록 보기 ----------
    def show_quizzes(self):
        if not self.quizzes:  
            print("저장된 퀴즈가 없어요!")
            return

        for i, q in enumerate(self.quizzes, start=1):
            print(f"[{i}번 문제] {q.question}")