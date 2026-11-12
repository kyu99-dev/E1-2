from quiz import Quiz
import json
import os,sys
import time


def show_logo():
    print(r'''
  /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$$
 /$$__  $$| $$  | $$|_  $$_/|_____ $$      
| $$  \ $$| $$  | $$  | $$       /$$/
| $$  | $$| $$  | $$  | $$      /$$/     
| $$  | $$| $$  | $$  | $$     /$$/    
| $$/$$ $$| $$  | $$  | $$    /$$/         
|  $$$$$$/|  $$$$$$/ /$$$$$$ /$$$$$$$$     
 \____ $$$ \______/ |______/|________/     
      \__/                                 
                                           
                                           
  /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$
 /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/
| $$  \__/| $$  \ $$| $$$$  /$$$$| $$      
| $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$   
| $$|_  $$| $$__  $$| $$  $$$| $$| $$__/   
| $$  \ $$| $$  | $$| $$\  $ | $$| $$      
|  $$$$$$/| $$  | $$| $$ \/  | $$| $$$$$$$$
 \______/ |__/  |__/|__/     |__/|________/
                                                                            
''')
    time.sleep(0.5)

def show_menu():
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def exit_game():
    print("\n게임을 종료합니다. 안녕히 가세요!")
    sys.exit(0)

def pause():
    try:
        input("\n계속하려면 Enter를 누르세요...")
    except (KeyboardInterrupt, EOFError):
        exit_game()



def get_valid_input(prompt, min_val, max_val):
    while True:                                    # ① 올바른 입력까지 반복
        try:
            choice = input(prompt).strip()
            if not choice:                         # 빈 입력 체크
                print("입력이 비어 있어요. 숫자를 입력해 주세요.")
                continue
            choice = int(choice)                   # 숫자 변환

            if choice < min_val or choice > max_val:  # ② 범위 체크
                print(f"{min_val}-{max_val} 사이 숫자를 입력하세요.")
                continue

            return choice                          # ③ 통과하면 값 돌려주고 종료

        except ValueError:
            print("숫자만 입력하세요.")
            continue
        except (KeyboardInterrupt, EOFError):
            exit_game()                           # ④ 종료 신호

default_quizzes = [
    Quiz("영화 '기생충'의 감독은?",
         ["봉준호", "박찬욱", "김지운", "나홍진"], 1),

    Quiz("영화 '타이타닉'의 남자 주인공을 연기한 배우는?",
         ["브래드 피트", "레오나르도 디카프리오", "톰 크루즈", "조니 뎁"], 2),

    Quiz("영화 '어벤져스'에서 아이언맨 역을 맡은 배우는?",
         ["크리스 에반스", "크리스 헴스워스", "로버트 다우니 주니어", "마크 러팔로"], 3),

    Quiz("영화 '겨울왕국'에서 눈사람 캐릭터의 이름은?",
         ["올라프", "스벤", "크리스토프", "한스"], 1),

    Quiz("영화 '해리포터' 시리즈의 주인공 이름은?",
         ["론 위즐리", "해리 포터", "드레이코 말포이", "네빌 롱바텀"], 2),
]


def make_quiz():
        # 질문 받기
    while True:                              # 제대로 입력될 때까지
        try:
            question = input("문제를 입력하세요: ").strip()
            if not question:                 # 빈 값 체크
                print("문제를 입력해 주세요.")
                continue
            break                            # 제대로 입력됨 → 탈출!
        except (KeyboardInterrupt, EOFError):
            exit_game()
    choices = []
    while len(choices) < 4:                    # 4개 채워질 때까지
        try:
            num = len(choices) + 1             # 지금 몇 번째인지
            choice = input(f"{num}번 선택지: ").strip()
            if not choice:
                print("선택지를 입력해 주세요.")
                continue                       # 다시 입력받기 (안 버려짐!)
            choices.append(choice)
        except (KeyboardInterrupt, EOFError):
            exit_game()
    answer = get_valid_input("정답 번호(1~4): ", 1, 4)
    
    return Quiz(question, choices, answer)

def play_quiz(quizzes):
    if not quizzes:
        print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
        pause()
        return

    total = len(quizzes)
    score = 0
    print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)\n")
    print("--------------------------------------")
    for q in quizzes:
        q.show()
        answer = get_valid_input("정답 번호 : ", 1, 4)
        if q.check(answer):
            print("\n정답입니다!\n")
            score += 1
        else:
            print("\n틀렸어요ㅠㅠ\n")

    print(f"최종 점수: {score} / {total}")
    pause()


def save_quizzes(quizzes):
    data = [quiz.to_dict() for quiz in quizzes]   # ① 변환
    with open("state.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)  # ② 저장
    print("저장 완료!")




def main():
    quizzes = default_quizzes 
    show_logo()
    while True:
        clear_screen()
        show_menu()
        choice = get_valid_input("메뉴 번호를 선택하세요: ", 1, 5)

        if choice == 1:
            clear_screen()
            play_quiz(quizzes)

        elif choice == 2:
            quiz = make_quiz()    
            print("\n--- 만들어진 퀴즈 ---")
            quiz.show()
            print("정답 : ",quiz.answer)
            while True:
                try:
                    confirm = input("\n이 퀴즈를 추가할까요? (y/n): ").strip().lower()

                    if confirm == "y":
                        quizzes.append(quiz)      # ① 기존 목록에 추가
                        save_quizzes(quizzes)     # ② 전체를 저장
                        print("추가되었어요!")
                        break
                    elif confirm == "n":
                        print("추가를 취소했어요.")
                        break
                    else:
                        print("y 또는 n만 입력해주세요.")
                        continue

                except (KeyboardInterrupt, EOFError):
                    print("\n입력이 중단되었어요. 추가를 취소할게요.")
                    break
            pause()
            
        elif choice == 3:

             # TODO: 퀴즈 목록 안내 문구 출력
            pass
        elif choice == 4:

            # TODO: 점수 확인 안내 문구 출력
            pass
        elif choice == 5:
            exit_game()



if __name__ == '__main__':
    main()