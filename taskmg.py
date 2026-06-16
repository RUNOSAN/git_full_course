import os
import requests

tasks = []

#ファイルパスのおまじない
tasks_path = os.path.join(os.path.dirname(__file__), "tasks.txt")




while True:

    #ファイルの読み込みをして配列に代入
    with open(tasks_path, "r", encoding="utf-8") as f:
        tasks = f.read().splitlines()



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
        task = input("タスクを入力してください")

        tasks.append(task)

        with open(tasks_path, "w", encoding="utf-8") as f:
            for i in tasks:
                f.write(i + "\n")
                
    
    if a == 2:
        for i in tasks:
            print(i)

    if a == 3:
        for i in tasks:
            print(i)
        
        ctask = input("完了するタスクを入力してください")

        for i in tasks:
            if ctask == i:
                print("[✓]" + i)
                tasks.remove(i)

                with open(tasks_path, "w", encoding="utf-8") as f:
                    for i in tasks:
                        f.write(i + "\n")
    
    if a == 4:
        spot = input("天気を知りたい場所をローマ字で入力してください").title()

        print(requests.get(f"https://wttr.in/{spot}?format=3").text)





   

   
            
    


