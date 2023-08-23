import random

stactics = {"컴퓨터": 0, "인간!": 0, "무승부": 0}
gamebox = ["lock", "scissor", "paper"]


def winlose(computer, player):
    if computer == 0:
        (a, b) = ([3, 0][player - 1], player)
    elif player == 0:
        (a, b) = (computer, [3, 0][computer - 1])
    else:
        (a, b) = (computer, player)

    if b > a:
        print("인간:{}vs컴퓨터{}".format(gamebox[player], gamebox[computer]), "인간이 이겼다!")
        return "인간!"
    elif a == b:
        print("인간:{}vs컴퓨터{}".format(gamebox[player], gamebox[computer]), "무승부다!")
        return "무승부"
    else:
        print("인간:{}vs컴퓨터{}".format(gamebox[player], gamebox[computer]), "컴퓨터가 이겼다!")
        return "컴퓨터"


while True:
    random_number = random.randint(0, 2)

    while True:
        player_choice = input("lock(숫자0) scissor(숫자1) paper(숫자2) 중 하나를 입력하세요!>")
        try:
            player_choice = int(player_choice)
            excepttest = gamebox[player_choice]
        except ValueError:
            print("숫자가 아닙니다!")
        except IndexError:
            print("0,1,2중 하나의 숫자가 아닙니다!")
        if player_choice < 3 and player_choice > -1:
            break

    stactics[winlose(random_number, player_choice)] += 1

    retry = input("종료하시려면 x를 눌러주세요~!,계속진행하시려면 아무키나 눌러주세요")
    if retry == "x":
        print(stactics)
        break
