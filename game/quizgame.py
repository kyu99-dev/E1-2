import random
import shutil
import os
import json
from game.quiz import Quiz
from game.util import show_logo, show_menu, clear_screen, exit_game, pause, get_valid_input
from datetime import datetime


HISTORY_FILE = "history.json"
STATE_FILE = "state.json"

STATE_BACKUP_FILE = STATE_FILE + ".bak"
HISTORY_BACKUP_FILE = HISTORY_FILE + ".bak"

default_quizzes = [
    Quiz("영화 '기생충'의 감독은?", ["봉준호", "박찬욱", "김지운", "나홍진"], 1,"이 감독은 영화 '살인의 추억', '괴물', '설국열차'도 연출했습니다."),
    Quiz("영화 '타이타닉'의 남자 주인공을 연기한 배우는?", ["브래드 피트", "레오나르도 디카프리오", "톰 크루즈", "조니 뎁"], 2,"영화에서 잭 도슨 역할을 맡았고, 이후 '인셉션'에도 출연했습니다."),
    Quiz("영화 '어벤져스'에서 아이언맨 역을 맡은 배우는?", ["크리스 에반스", "크리스 헴스워스", "로버트 다우니 주니어", "마크 러팔로"], 3,"영화 '셜록 홈즈'에서 셜록 홈즈 역할도 맡았습니다."),
    Quiz("영화 '겨울왕국'에서 눈사람 캐릭터의 이름은?", ["올라프", "스벤", "크리스토프", "한스"], 1,"이름이 '프'로 끝납니다."),
    Quiz("영화 '해리포터' 시리즈의 주인공 이름은?", ["론 위즐리", "해리 포터", "드레이코 말포이", "네빌 롱바텀"], 2,"동그란 안경과 번개 모양 흉터가 상징인 인물입니다."),
    Quiz("박찬욱 감독의 영화 《올드보이》에서 주인공 오대수가 15년 동안 감금되어 매일 먹어야 했던 주된 음식은 무엇인가요?",["샌드위치","컵라면","주먹밥","군만두"],4,"중국집에서 자주 볼 수 있는 튀긴 만두 음식입니다."),
]


class QuizGame:
    def __init__(self):
        self.data = self.load_data()
        self.quizzes = [Quiz.from_dict(d) for d in self.data.get("quizzes", [])]
        self.score_history = self.load_history()
        if not self.quizzes:                  # 저장된 퀴즈가 없으면
            self.quizzes = default_quizzes    # 기본 퀴즈로 채우기
            print("기본퀴즈로 시작합니다.")
    # ---------- 파일 저장/불러오기 ----------
    def is_valid_json_file(self, file_path):
        #파일이 정상적인 JSON 형식인지 확인
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json.load(f)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False


    def backup_file(self, file_path, backup_path):
        """저장 전 기존 파일이 정상 JSON이면 백업 생성"""
        if os.path.exists(file_path) and self.is_valid_json_file(file_path):
            shutil.copy2(file_path, backup_path)


    def restore_from_backup(self, backup_path, target_path):
        """백업 파일에서 데이터를 복구"""
        try:
            with open(backup_path, "r", encoding="utf-8") as f:
                restored_data = json.load(f)

            with open(target_path, "w", encoding="utf-8") as f:
                json.dump(restored_data, f, ensure_ascii=False, indent=2)

            return restored_data

        except FileNotFoundError:
            print("백업 파일이 없어 복구할 수 없습니다.")
        except json.JSONDecodeError:
            print("백업 파일도 손상되어 복구할 수 없습니다.")
        except OSError as e:
            print(f"백업 복구 중 오류가 발생했어요: {e}")

        return None
        
    def load_history(self):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("히스토리 파일이 손상되어 백업에서 복구를 시도합니다.")

            restored_data = self.restore_from_backup(
                HISTORY_BACKUP_FILE,
                HISTORY_FILE
            )

            if isinstance(restored_data, list):
                print("히스토리 백업 복구에 성공했습니다.")
                return restored_data

            print("히스토리를 새로 시작합니다.")
            return []
        
    def save_history(self):
        try:
            self.backup_file(HISTORY_FILE, HISTORY_BACKUP_FILE)

            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.score_history, f, ensure_ascii=False, indent=4)

            return True

        except OSError as e:
            print(f"history 저장 중 오류가 발생했어요: {e}")
            return False

    def load_data(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

                if not isinstance(data, dict):
                    data = {}

                if "quizzes" not in data:
                    data["quizzes"] = []

                if "best_score" not in data or not isinstance(data["best_score"], dict):
                    data["best_score"] = {"correct": 0, "total": 0}

                if "correct" not in data["best_score"]:
                    data["best_score"]["correct"] = 0

                if "total" not in data["best_score"]:
                    data["best_score"]["total"] = 0

                return data

        except FileNotFoundError:
            print("저장된 데이터가 없어 새로 시작합니다.")
        except json.JSONDecodeError:
            print("데이터가 손상되어 백업에서 복구를 시도합니다.")
            restored_data = self.restore_from_backup(
                STATE_BACKUP_FILE,
                STATE_FILE
            )
            if isinstance(restored_data, dict):
                if "quizzes" not in restored_data:
                    restored_data["quizzes"] = []

                if "best_score" not in restored_data or not isinstance(restored_data["best_score"], dict):
                    restored_data["best_score"] = {"correct": 0, "total": 0}

                if "correct" not in restored_data["best_score"]:
                    restored_data["best_score"]["correct"] = 0

                if "total" not in restored_data["best_score"]:
                    restored_data["best_score"]["total"] = 0

                print("백업 파일을 사용해 데이터를 복구했습니다.")
                return restored_data

            print("백업 복구에 실패하여 새로 시작합니다.")

        return {
            "quizzes": [],
            "best_score": {"correct": 0, "total": 0}
        }

# ... rest of code ...

    def save_data(self):
        try:
            # 저장 전 기존 정상 데이터를 백업
            self.backup_file(STATE_FILE, STATE_BACKUP_FILE)

            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)

        except OSError as e:
            print(f"저장 중 오류가 발생했어요: {e}")
            return False

        return True                       # 성공 알림

    def save_quizzes(self):
        self.data["quizzes"] = [q.to_dict() for q in self.quizzes]
        return self.save_data()

    def add_score_history(self, correct_count, total_count):
        record = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "question_count": total_count,
            "score": correct_count
        }

        self.score_history.append(record)
        self.save_history()

    # ---------- 퀴즈 만들기 ----------
    def make_quiz(self):
        try:
            while True:
                        question = input("문제를 입력하세요: ").strip()
                        if not question:
                            print("문제를 입력해 주세요.")
                            continue
                        break
            choices = []
            while len(choices) < 4:
                        num = len(choices) + 1
                        choice = input(f"{num}번 선택지: ").strip()
                        if not choice:
                            print("선택지를 입력해 주세요.")
                            continue
                        choices.append(choice)
            answer = get_valid_input("정답 번호(1~4): ", 1, 4)
            while True:
                hint = input("힌트를 입력하세요: ").strip()
                if not hint:
                    print("힌트를 입력해 주세요.")
                    continue
                break
            return Quiz(question, choices, answer,hint)
        except (KeyboardInterrupt, EOFError):
                return None

    # ---------- 퀴즈 풀기 ----------
    def play_quiz(self):                            
        if not self.quizzes:                         
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            pause()
            return

        total = len(self.quizzes)   # 전체 문제 수
        count = get_valid_input(f"몇 문제를 풀까요? (1~{total}) : ", 1, total)
        quizzes = random.sample(self.quizzes, count)

        score = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {count}문제)\n")
        print("--------------------------------------")
        for q in quizzes:                    
            q.show()
            used_hint = False                               # 문제마다 초기화

            while True:
                answer = get_valid_input("정답 번호(5: hint) : ", 1, 5)
                if answer == 5:                             # 힌트 요청
                    print("힌트:", q.hint)
                    used_hint = True
                    continue                                # 다시 위로 → 답 또 받기
                break    
                                                   # 1~4 → 확정, 탈출
            if q.check(answer):
                print("\n정답입니다!\n")
                if used_hint:
                    print("힌트 사용으로 0.5 추가됩니다.")
                    score += 0.5        # 힌트 썼으면 절반
                else:
                    score += 1          # 힌트 안 썼으면 만점
            else:
                print("\n틀렸어요ㅠㅠ\n")

        print(f"최종 점수: {score} / {count}")
        self.add_score_history(score, count)
        self.update_best_score(score, count)  
                  
        pause()

    # ---------- 점수 ----------
    def update_best_score(self, correct, count):                              
        if count == 0:
            print("풀 수 있는 퀴즈가 없어요!")
            return

        current_rate = correct / count
        best = self.data["best_score"] 
        best_rate = best["correct"] / best["total"] if best["total"] > 0 else -1
        
        if (best["total"] == 0 or current_rate > best_rate or (current_rate == best_rate and count > best["total"])):
            self.data["best_score"] = {
                "correct": correct,
                "total": count
            }
            if self.save_data():
                print("🎉 최고 기록 갱신!")
            else:
                print("기록 저장에 실패했어요.")
        else:
            print("최고 기록은 갱신되지 않았어요.")

    def show_score_history(self):
        if not self.score_history:
            print("저장된 점수 기록이 없습니다.")
            return

        print("\n=== 점수 기록 히스토리 ===")

        for i, record in enumerate(self.score_history, start=1):
            datetime_value = record.get("datetime", "날짜 없음")
            question_count = record.get("question_count", 0)
            score = record.get("score", 0)

            print(
                f"{i}. 날짜/시간: {datetime_value} | "
                f"푼 문제 수: {question_count} | "
                f"점수: {score}/{question_count}"
            )

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

    # ---------- 퀴즈 삭제 ----------
    def delete_quiz(self):
        if not self.quizzes:
            print("삭제할 퀴즈가 없습니다.")
            return

        if len(self.quizzes) == 1:
            print("최소 1개의 퀴즈는 남겨두어야 합니다.")
            return

        print("\n=== 퀴즈 삭제 ===")

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")

        choice = get_valid_input(
            "삭제할 퀴즈 번호를 입력하세요 (0: 취소): ",
            0,
            len(self.quizzes)
        )

        if choice == 0:
            print("삭제를 취소했습니다.")
            return

        deleted_quiz = self.quizzes[choice - 1]

        confirm = input(f"'{deleted_quiz.question}' 퀴즈를 삭제할까요? (y/n): ").strip().lower()

        if confirm != "y":
            print("삭제를 취소했습니다.")
            return

        self.quizzes.pop(choice - 1)

        if self.save_quizzes():
            print("퀴즈가 삭제되었습니다.")
        else:
            print("저장에 실패했어요. 삭제 결과가 파일에 반영되지 않았을 수 있습니다.")