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
    time.sleep(3)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def main():
    show_logo()
    while True:
        clear_screen()
        show_menu()
        try:
            choice = input("메뉴 번호를 선택하세요: ").strip()  # 앞뒤 공백 제거
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C 나 입력 종료 시 안전하게 마무리
            print("\n게임을 종료합니다. 안녕히 가세요!")
            break

        if choice == "":
            print("입력이 비어 있어요. 1-5 사이 숫자를 입력해 주세요")
            continue

        if choice == "1":
            print("퀴즈 풀기 기능 (준비 중)")
        elif choice == "2":

            # TODO: 퀴즈 추가 안내 문구 출력
            pass
        elif choice == "3":

             # TODO: 퀴즈 목록 안내 문구 출력
            pass
        elif choice == "4":

            # TODO: 점수 확인 안내 문구 출력
            pass
        elif choice == "5":
            print("게임을 종료합니다. 안녕히 가세요!")
            break
        else:

            print("\n잘못된 입력이에요. 1부터 5 사이 숫자를 선택해 주세요!")
            input("\n계속하려면 Enter를 누르세요...")




if __name__ == '__main__':
    main()