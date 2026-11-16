from game.quizgame import QuizGame
from game.util import show_logo, show_menu, clear_screen, exit_game, pause, get_valid_input


def main():
    
    show_logo()
    game = QuizGame()          # 객체 생성 (data, quizzes 자동 준비)
    pause()
    
    
    while True:
        clear_screen()
        show_menu()
        choice = get_valid_input("메뉴 번호를 선택하세요: ", 1, 7)
        
        if choice == 1:
            clear_screen()
            game.play_quiz()

        elif choice == 2:
            quiz = game.make_quiz()
            if quiz is None:
                print("\n퀴즈 추가를 취소했어요.")
                pause()
                continue
            print("\n--- 만들어진 퀴즈 ---")
            quiz.show()
            print("정답 : ", quiz.answer)
            print("힌트 : ", quiz.hint)
            while True:
                try:
                    confirm = input("\n이 퀴즈를 추가할까요? (y/n): ").strip().lower()

                    if confirm == "y":
                        game.quizzes.append(quiz)
                        if game.save_quizzes():
                            print("추가되었어요!")
                        break
                    elif confirm == "n":
                        print("퀴즈 추가를 취소했어요.")
                        break
                    else:
                        print("y 또는 n만 입력해주세요.")
                        continue
                except (KeyboardInterrupt, EOFError):
                    print("\n퀴즈 추가를 취소했어요.")
                    break
            pause()

        elif choice == 3:
            game.show_quizzes()
            pause()

        elif choice == 4:
            game.show_best_score()
            pause()

        elif choice == 5:
            game.delete_quiz()
            pause()
        
        elif choice == 6:
            game.show_score_history()
            pause()

        elif choice == 7:
            exit_game()
    

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        exit_game()