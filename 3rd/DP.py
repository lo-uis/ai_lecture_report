import numpy as np




node = [                        #define node
    [None,"り",None],
    ["ん","つ","ば"],
    ["め","い","う"],
    ["い","あ","い"],
    ["か","と","さ"],
    ["ん",None,None]

]
t =[                  #define gain
    
        [[2],[5],[4]],
        [[-5,-99,-99],[3,2,3],[-99,5,-99]],
        [[2,-99,-99],[2,-2,2],[-99,0,-99]],
        [[4,-99,-99],[4,2,7],[-99,0,-99]],
        [[2,-99,-99],[1,-99,-99],[8,-99,-99]]


]
last_score  = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]  #define last score
ac = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]  #define Accumulated Points


for i in range(len(ac)):
    if i==0:
        for j in range(3):
            ac[i][j] = t[i][j][0]
            last_score[i][j] = 1
        
        print('last_score: {}'.format(last_score))
        print('ac: {}'.format(ac))
        print()
    else:
        MAX = [-99,-99,-99]
        for j in range(3):
            gain = [ac[i-1][j]+t[i][j][0],ac[i-1][j]+t[i][j][1],ac[i-1][j]+t[i][j][2]]
            for index,val in enumerate(gain):
                if MAX[index] < val:
                    MAX[index] = val
                    last_score[i][j] = index

        ac[i] = MAX
        print("s_t:",last_score)
        print("F_t:",ac)
        
        

ans = []

##############use numpy##############################
max_route = np.argmax(ac[-1])      

for name,dp in zip(reversed(node),reversed(last_score)):
    ans.insert(0,name[max_route])
    max_route = dp[max_route]

ans.insert(0,node[0][max_route])
print(ans)