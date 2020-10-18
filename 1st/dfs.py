def dfs(maze):
    o_list = ["S"]
    c_list = []
    searched = []

   
    print("オープンリスト",o_list,"&","クローズリスト",c_list)
    
    while o_list:
        s = o_list.pop(0)
        c_list.append(s)
        
        for i in reversed(maze):
            
            if (s == i[0]) and (not i[1] in c_list+o_list):
                o_list.insert(0,i[1])
            
        print("オープンリスト",o_list,"&","クローズリスト",c_list)
        

def main():
    maze = [["S","A"],["S","B"],["A","C"],["A","D"],["B","C"],["C","D"]]
    dfs(maze)


if __name__ == '__main__':
    main()