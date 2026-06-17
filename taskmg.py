import os
import requests

tasks = []

#ファイルパスのおまじない
tasks_path = os.path.join(os.path.dirname(__file__), "tasks.txt")

def readtasks():
    with open(tasks_path, "r", encoding="utf-8") as f:
        tasklist= f.read().splitlines()
        return tasklist

def showtasks(tasklist):
    for i in tasklist:
            print(i)


def taskaddfile(tasklist):
    with open(tasks_path, "w", encoding="utf-8") as f:
        for i in tasklist:
            f.write(i + "\n")

def addtask(tasklist):
    task = input("タスクを入力してください")

    tasklist.append(task)

    taskaddfile(tasklist)
    

def ctask(tasklist):
    showtasks(tasklist)

    cleartask = input("完了するタスクを入力してください")

    for i in tasklist:
        if cleartask == i:
            print("[✓]" + i)
            tasklist.remove(i)
            taskaddfile(tasklist)

while True:

    #ファイルの読み込みをして配列に代入
    tasks = readtasks()



    print("項目を選んでください。")
    print("1:タスクの追加")
    print("2:一覧表示")
    print("3:タスクの完了")
    print("4:天気の表示")
    print("5:終了")

    a = int(input("数字を入力してください"))

    if a == 5:
        break
    

    if a == 1:
        addtask(tasks)
                
    
    if a == 2:
        showtasks(tasks)

    if a == 3:
        ctask(tasks)
    
    if a == 4:
        spot = input("天気を知りたい場所をローマ字で入力してください").title()

        print(requests.get(f"https://wttr.in/{spot}?format=3").text)





   

   
            
    


