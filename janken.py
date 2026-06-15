import random

ene = random.randint(0,2)

ply = input("グー、チョキ、パー、を入力してください")

if ply == "グー":
    hand = 0
elif ply == "パー":
    hand = 1
elif ply == "チョキ":
    hand = 2
else:
    print("じゃんけんの手を入力してください")

print("最初はグージャンケンポン")

if ene == 0:
    print("グー")
elif ene == 1:
    print("パー")
elif ene == 0:
    print("チョキ")

if ene == hand:
    print("あいこ")
elif hand == 0 and ene == 1:
    print("あなたの負け")
elif hand == 1 and ene == 2:
    print("あなたの負け")
elif hand == 2 and ene == 0:
    print("あなたの負け")
elif hand == 0 and ene == 2:
    print("あなたの勝ち")
elif hand == 1 and ene == 0:
    print("あなたの勝ち")
elif hand == 2 and ene == 1:
    print("あなたの勝ち")