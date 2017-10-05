def binary(N):
    return bin(N)[2:]

def solution(N):
    # write your code in Python 2.7
    
    binaryN = bin(N)[2:]
    lst = [int(i) for i in binaryN]
    
    max_zero = 0
    cnt_zero = 0
    
    # it starts by leading '1', thus starting counting from the second character
    for i in range(1,len(lst)):
        
        if lst[i] == 0:
            
            # reset the zero counter
            if lst[i-1] == 1:
                cnt_zero = 0
            
            cnt_zero += 1
            
            if i == len(lst)-1:
                pass
            elif lst[i+1] == 1:
                if cnt_zero > max_zero:
                    max_zero = cnt_zero
            
    return max_zero
    

N=529
print(binary(N))
print(solution(N))























