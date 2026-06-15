tasks = []

for i in range(4):
    task = input("タスクを入力してください。最大4つまで")

    tasks.append(task)
    print( task + "を追加しました")

print("完了したタスクを選択してください")

for i in range(len(tasks)):
    print("[]" + tasks[i])

a = ""

while a != "完了":
    a = input("完了したタスクを入力してください")
    print("すべて入力し終わったら完了と入力してください")

    for i in range(len(tasks)):
        if tasks[i] == a:
            print("[✓]" + tasks[i])
            print("完了しました")
            tasks.pop(i)
            break
            
    


