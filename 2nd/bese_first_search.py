cost = {"S":4, "A":3, "B":1, "C":1,"D":3, "G":0} 
node = {
            "S":{"A":1, "B":3, "C":5},
                "A":{"S":1, "D":1},
                "B":{"S":3, "D":2, "G":1},
                "C":{"S":5, "G":5},
                "D":{"A":1, "B":2, "G":5},
                "G":{"B":1, "C":5, "D":5}
                }

openlist = {"S":cost["S"]}
closedlist = {} #クローズドリストを空に初期化する
cnt = 0
ans = []

while openlist:
    print("オープンリスト:",openlist,"クローズドリスト:",closedlist)
    cnt +=1

    s = next(iter(openlist)) #オープンリストから先頭要素取り出し
    num = openlist.pop(s) 
    closedlist[s] = num
    ans.append(s)

    if s == "G":
            print("オープンリスト:",openlist,"クローズドリスト:",closedlist)
            break
    else:
        for key in node[s]:
            if not key in closedlist:
                openlist[key] = cost[key]
    memo = {}
    for key, value in sorted(openlist.items(), key=lambda x: x[1]): #予測評価値
        memo[key]=value
    openlist = memo

for i in reversed(range(len(ans))):
        if ans[i] == "S":
            break
        if not ans[i-1] in node[ans[i]]:
            ans.pop(i-1)
for i in range(len(ans)):
    print(ans[i]) if i == len(ans)-1 else print(ans[i],"→ ",end=" ")
        
