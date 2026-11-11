from quiz import Quiz

import os
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


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")

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
            input("\n계속하려면 Enter를 누르세요...")
        except (KeyboardInterrupt, EOFError):
            print("\n게임을 종료합니다. 안녕히 가세요!")
            return None                            # ④ 종료 신호


def main():
    show_logo()
    while True:
        clear_screen()
        show_menu()
        choice = get_valid_input("메뉴 번호를 선택하세요: ", 1, 5)

        if choice is None:   # 종료 신호면
            break

        if choice == 1:
            clear_screen()
            print("퀴즈 풀기 기능 (준비 중)")
            q = Quiz("파이썬을 만든 사람은?", ["귀도", "리누스", "제임스", "데니스"], 1)
            q.show()                              # ① 문제 보여주기

            answer = get_valid_input("정답 번호를 입력하세요: ", 1, 5)  # ② 답 입력받기
            if choice is None:   # 종료 신호면
            break

            
        elif choice == 2:

            # TODO: 퀴즈 추가 안내 문구 출력
            pass
        elif choice == 3:

             # TODO: 퀴즈 목록 안내 문구 출력
            pass
        elif choice == 4:

            # TODO: 점수 확인 안내 문구 출력
            pass
        elif choice == 5:
            print("게임을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("1-5 사이 숫자를 입력해 주세요")
            input("\n계속하려면 Enter를 누르세요...")




if __name__ == '__main__':
    main()