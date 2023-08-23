import sys
import random


while True:
    random_number = random.randint(1, 100)

    bestcounttxt = open("bestcount.txt", "r", encoding="utf-8")

    bestcount = bestcounttxt.readline()

    if bestcount.isdigit() == True:
        bestcount = int(bestcount)

    bestcounttxt.close()

    if type(bestcount) == int:
        print("현재 최고기록은 {}입니다 기록을 갱신해보세요!".format(bestcount))

    def inputnmber():
        number = input("1~100까지의 숫자를 입력하세요!,종료는x입니다>")
        player_number = None
        while True:
            if number == "x":
                quit()
            if number.isdigit() == True:
                if int(number) < 101 and int(number) > 0:
                    player_number = int(number)
                    break
            number = input("1~100까지의 숫자를 입력하세요!,종료는x입니다>")

        return player_number

    besttry = sys.maxsize

    player_number = inputnmber()
    while True:
        count=1
        if player_number == random_number:
            print("성공! {}번 시도했습니다!".format(count))
            break
        elif player_number > random_number:
            count += 1
            print("UP!")
            player_number = inputnmber()
        else:
            count += 1
            print("DOWN!")
            player_number = inputnmber()

    if count < besttry:
        besttry = count

    if bestcount == "기록이 없습니다":
        bestcounttxt = open("bestcount.txt", "w", encoding="utf-8")
        bestcounttxt.write("{}".format(besttry))
        bestcounttxt.close()
    elif bestcount > besttry:
        bestcounttxt = open("bestcount.txt", "w", encoding="utf-8")
        bestcounttxt.write("{}".format(besttry))
        bestcounttxt.close()

    endquestion = input("재시도하시려면 아무키나 끝내시려면 x를 누르세요>")

    if endquestion == "x":
        break
