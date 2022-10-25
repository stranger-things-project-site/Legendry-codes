from sys import stdin

def pairSum(arr,si,ei,num):
    c = 0
    j = si
    k = ei
    while j<k:
        if arr[j]+arr[k]<num:
            j+=1
        elif arr[j]+arr[k]>num:
            k-=1
        else:
            if arr[j] == arr[k]:
                t = k - j + 1
                c += ((t) * (t - 1) ) // 2
                return c
            tempj = j
            tempk = k
            while tempj<=tempk and arr[tempj] == arr[j]:
                tempj+=1
            while tempj<=tempk and arr[tempk] == arr[k]:
                tempk-=1
            c += (tempj-j) * (k-tempk)
            j = tempj
            k = tempk
    return c
                

def tripletSum(arr, n, num) :
    arr.sort()
    count = 0
    for i in range(n):
        pairSumFor = num - arr[i]
        tempCount = pairSum(arr,i+1,n-1,pairSumFor)
        count+=tempCount
    return count


def takeInput() :
    n = int(input())
    if n == 0 :
        return list(), 0

    arr = list(map(int, input().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(input())

while t > 0 :
    
    arr, n = takeInput()
    num = int(input())
    print(tripletSum(arr, n, num))

    t -= 1
