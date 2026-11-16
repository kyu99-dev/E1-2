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
    time.sleep(0.3)

def show_menu():
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 퀴즈삭제")
    print("6. 종료")


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

