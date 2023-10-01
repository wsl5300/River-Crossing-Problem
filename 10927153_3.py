# 演算法分析機測
# 學號: 10927153 / 10927248 /10927256
# 姓名: 吳上玲 / 連翊安 / 姜美羚
# 中原大學資訊工程系


def expandsion( path, M, N ) -> list :
    
    path_temp_list = [path]
    m, n = path[0], path[1]
    
    if path[2] == 'W' : # 去東岸
        p = 'E'
        for x in range(2, -1, -1) : # 0 沒上船 1 在船上 2 占滿船
            if x > m :
                continue
        
            for y in range(2, -1, -1) : # 0 沒上船 1 在船上 2 占滿船
                if y > n :
                    continue
                elif x + y <= 0 or x + y > 2 :
                    continue
                path = [ m - x, n - y, p ]
                if is_okay(path) :
                    path_temp_list.append(path)
    else :  # 去西岸
        p = 'W'
        for x in range(3) : # 0 沒上船 1 在船上 2 占滿船
            if x+m > M :
                continue
        
            for y in range(3) : # 0 沒上船 1 在船上 2 占滿船
                if y+n > N :
                    continue
                elif x + y <= 0 or x + y > 2 :
                    continue
                path = [ m + x, n + y, p ]
                if is_okay(path) :
                    path_temp_list.append(path)
        
    return path_temp_list

def is_okay( path ) :
    m, n, p = path
    global M, N
    
    if (M-m <= N-n or N == n) and (m <= n or n == 0) and M >= m and N >= n :  
    # 確認這一步做的所有狀態( W, E, 船 )正確
        return True
    else :
        return False
    
        

def branch( path_list ) -> bool :
    
    M, N, P = path_list[0]
    
    path = path_list[ len(path_list) - 1 ]
    
    path_temp_list = expandsion( path, M, N )  
    # expandsion 擴張
    for path in path_temp_list :
        
        if path in path_list :  # 這狀態已經存在過
            continue
            
        path_list.append(path)
        
        if path == [ 0, 0, 'E' ] : # 結束
            return True
        else :
            if branch( path_list ) :
                return True
            else :
                path_list.pop()
    return False
    

while True :
 
    str = input("continue? (Y/N)\n\n")
    if str == "Y" or str == 'y':
        pass
    elif str == "N" or str == 'n':
        break
    else :
        print("I don't care anymore, bye :) ")
        break
    
    str = input("input (Wolf Sheep): ")
    M, N = 0, 0
    while True:
        if str == "0 0" or str == "\n" :
            break
        num = str.split()
        M = int(num[0]) + M    # 狼數
        N = int(num[1]) + N    # 羊數
        str = input("input (more_Wolf more_Sheep) / (0 0) :")
        
     # 東岸 = 0 西岸 = 1
    path_list = [[M,N,'W']]
    
    if str != "0 0" :
        print( "It's syntax error!" )
    else :
        
        
        if M > N or branch( path_list ) is False :   # branch 分支
            for path in path_list :
                print(path)
            print( "Whooooooo!!!" )
        else :
            for path in path_list :
                print(path)
            print( "Yeahhhhhh!!!" )
    


