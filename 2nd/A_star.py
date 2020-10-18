cost = {"S":4, "A":3, "B":1, "C":1,"D":3, "G":0} 
node = {
            "S":{"A":1, "B":3, "C":5},
                "A":{"S":1, "D":1},
                "B":{"S":3, "D":2, "G":1},
                "C":{"S":5, "G":5},
                "D":{"A":1, "B":2, "G":5},
                "G":{"B":1, "C":5, "D":5}
                }

openlist = {"S":0} #初期状態のコスト値を0としてオープンリストに追加
closedlist = {} #クローズドリストを空に初期化する
cnt = 0
ans = []

while openlist:
    print("オープンリスト:",openlist,"クローズドリスト:",closedlist)
    cnt +=1

    s = next(iter(openlist)) #オープンリストから先頭要素取り出し
    num = openlist.pop(s)
    closedlist[s] = num #クローズドリストにsを追加
    ans.append(s)

    if s == "G":
            print("オープンリスト:",openlist,"クローズドリスト:",closedlist)
            break
    else:
        for key,value in node[s].items(): 
            if not key in closedlist:
                if not key in openlist:
                    openlist[key] = value+num+cost[key]  #sから接続していてまだ探査していない状態をオープンリストに追加する
                    continue

                if openlist[key] > num+node[s][key]+cost[key]: 
                    openlist[key] = num+node[s][key]-cost[s]
    memo = {}
    for key, value in sorted(openlist.items(), key=lambda x: x[1]): #コストと予測評価の小さい順に並び替え
        memo[key]=value
    openlist = memo

for i in reversed(range(len(ans))):
        if ans[i] == "S":
            break
        if not ans[i-1] in node[ans[i]]:
            ans.pop(i-1)
for i in range(len(ans)):
    print(ans[i]) if i == len(ans)-1 else print(ans[i],"→ ",end=" ")