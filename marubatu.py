cir = "〇"

x = "Ｘ"

none = "・"

gamecount = 0

field = [
    [none,none,none],
    [none,none,none],
    [none,none,none]
]

prefield = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def inputResult(zahyo):
    row = (zahyo - 1) // 3
    col = (zahyo - 1) % 3
    return row, col

def printField(lists):

    print(f"  {lists[0][0]} |  {lists[0][1]} |  {lists[0][2]}")
    print("-----+-----+-----")
    print(f"  {lists[1][0]} |  {lists[1][1]} |  {lists[1][2]}")
    print("-----+-----+-----")
    print(f"  {lists[2][0]} |  {lists[2][1]} |  {lists[2][2]}")


def printplayfield(lists,zahyo,player):
    
    row, col = inputResult(zahyo)

    
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if i == row and j == col:
                lists[i][j] = player
                break
    printField(lists)
    


def play(lists,sign):
    while True:
        try:
            zahyo = int(input(f"{sign}の座標を入力してください"))

            if not (1 <= zahyo <= 9):
                print("座標の中に存在しません")
                continue
            
                
            row, col = inputResult(zahyo)

            if lists[row][col] != none:
                print("すでに入力されています")
                continue

            return zahyo
            break
        except ValueError:
            print("数字で入力してください。")

def judge(lists,player):
    y = 0
    for row in lists:
        if row[0] == row[1] == row[2] == player:
            print(f"{player}の勝ち")
            return True
    for i in range(3):
        if lists[0][i] == lists[1][i] == lists[2][i] == player:
            print(f"{player}の勝ち")
            return True
    if lists[0][0] == lists[1][1] == lists[2][2] == player:
        print(f"{player}の勝ち")
        return True
    elif lists[0][2] == lists[1][1] == lists[2][0] == player:
        print(f"{player}の勝ち")
        return True
    
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if lists[i][j] == none:
                y += 1
    if y == 0:
        print("引き分け")
        return True

printField(prefield)

while True:


    zahyo = play(field,cir)
    printplayfield(field,zahyo,cir)
    if judge(field,cir):
        break

    zahyo = play(field,x)
    printplayfield(field,zahyo,x)
    if judge(field,x):
        break







        