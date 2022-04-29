from collections import deque
T = int(input())
for i in range(T):
    fl = True
    n = int(input())
    arr = deque(map(int, input().split()))
    if(arr[0] >= arr[-1]):
        mx = arr.popleft()
    else:
        mx = arr.pop()
    while arr:
        if(len(arr) == 1):
            if(arr[0] <= mx):
                break
            else:
                fl = False
                break
        else:
            if((arr[0] <= mx) and (arr[-1] <= mx)):
                if(arr[0] >= arr[-1]):
                    mx = arr.popleft()
                else:
                    mx = arr.pop()
            elif(arr[0] <= mx):
                mx = arr.popleft()
            elif(arr[-1] <= mx):
                mx = arr.pop()
            else:
                fl = False
                break
    if(fl):
        print('Yes')
    else:
        print('No')
                