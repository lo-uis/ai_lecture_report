node = {"S":["A","B"],
            "A":["S","C","D"],
            "B":["S","C"],
            "C":["A","B","D"],
            "D":["A","C"]}
openlist = ["S"] #初期状態をオープンリストに挿入
closedlist = [] #クローズドリストを初期化
print("オープンリスト",openlist,"クローズドリスト",closedlist) 
def rebfs(openlist,closedlist):
    while openlist:
        s = openlist.pop(0) #オープンリストから先頭の要素を取り出し
        closedlist.append(s)    #クローズドリストに追加
        visited = openlist+closedlist   
        for i in node[s]:
            if not i in visited:
                openlist.append(i)    #オープンリストの末尾に追加
        print("オープンリスト",openlist,"クローズドリスト",closedlist)        
        rebfs(openlist,closedlist)  #再帰

def main():
    rebfs(openlist,closedlist)

if __name__ == '__main__':
    main()