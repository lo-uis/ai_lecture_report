def BFS(maze):
    o_list = ["S"]
    c_list = []
    searched = []

   
    print("オープンリスト",o_list,"&","クローズリスト",c_list)
    
    while len(o_list) != 0:
        s = o_list.pop(0)
        c_list.append(s)
        
        for i in maze:
            
            if (s == i[0]) and (not i[1] in c_list+o_list):
                o_list.append(i[1])
            
        print("オープンリスト",o_list,"&","クローズリスト",c_list)
        


def main():
    maze = [["S","A"],["S","B"],["A","C"],["A","D"],["B","C"],["C","D"]]
    BFS(maze)


if __name__ == '__main__':
    main()
