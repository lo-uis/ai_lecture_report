#https://github.com/codingjester/code-samples/blob/master/algos/python/dfs.py
#https://www.it-swarm-ja.tech/ja/python/python%E3%81%AE%E6%B7%B1%E3%81%95%E5%84%AA%E5%85%88%E6%A4%9C%E7%B4%A2%EF%BC%88dfs%EF%BC%89%E3%82%B3%E3%83%BC%E3%83%89/830632137/
node = {"S":["A","B"],
            "A":["S","C","D"],
            "B":["S","C"],
            "C":["A","B","D"],
            "D":["A","C"]}
openlist = ["S"] #初期状態をオープンリストに挿入
closedlist = [] #クローズドリストを初期化
print("オープンリスト",openlist,"クローズドリスト",closedlist) 
def redfs(openlist,closedlist):
    while openlist:
        s = openlist.pop(0) #オープンリストから先頭の要素を取り出し
        closedlist.append(s)    #クローズドリストに追加
        visited = openlist+closedlist   
        for i in reversed(node[s]):
            if not i in visited:
                openlist.insert(0,i)    #オープンリストの先頭に追加
        print("オープンリスト",openlist,"クローズドリスト",closedlist)        
        redfs(openlist,closedlist)  #再帰

def main():
    redfs(openlist,closedlist)

if __name__ == '__main__':
    main()