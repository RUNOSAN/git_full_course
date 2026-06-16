tasks = []

while True:

    print("項目を選んでください。")
    print("1:タスクの追加")
    print("2:一覧表示")
    print("3:タスクの完了")
    print("4:終了")

    a = int(input("数字を入力してください"))

    if a == 4:
        break
    

    if a == 1:
        task = input("タスクを入力してください")

        tasks.append(task)
    
    if a == 2:
        for i in range(len(tasks)):
            print(tasks[i])

    if a == 3:
        for i in range(len(tasks)):
            print(tasks[i])
        
        ctask = input("完了するタスクを入力してください")

        for i in range(len(tasks)):
            if ctask == tasks[i]:
                print("[✓]" + tasks[i])
                tasks.pop(i)



   

   
            
    


