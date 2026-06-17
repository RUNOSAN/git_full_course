import random


def get_computer_choice():
    ene = random.randint(0,2)
    if ene == 0:
        comhand = "グー"
    elif ene == 1:
        comhand = "パー"
    elif ene == 2:
        comhand = "チョキ"
    return comhand

def judge(comhand,hand):
    if comhand == hand:
        x = 3
        return x
    elif hand == "グー" and comhand == "パー":
        x = 1
        return x
    elif hand == "パー" and comhand == "チョキ":
        x = 1
        return x
    elif hand == "チョキ" and comhand == "グー":
        x = 1
        return x
    elif hand == "グー" and comhand == "チョキ":
        x = 2
        return x
    elif hand == "パー" and comhand == "グー":
        x = 2
        return x
    elif hand == "チョキ" and comhand == "パー":
        x = 2
        return x
    
while True:
    ply = input("グー、チョキ、パー、を入力してください")

    if ply == "グー":
        hand = "グー"
    elif ply == "パー":
        hand = "パー"
    elif ply == "チョキ":
        hand = "チョキ"
    else:
        print("じゃんけんの手を入力してください")

    print("最初はグージャンケンポン")

    comhand = get_computer_choice()

    print(comhand)

    result = judge(comhand,hand)

    if result == 2:
        print("あなたの勝ち")
        break
    elif result == 1:
        print("あなたの負け")
        break
    else:
        print("あいこでしょ")


    