def lisEndingAtIdx(arr, idx):
  
    if idx == 0:
        return 1

    mx = 1
    for prev in range(idx):
        if arr[prev] < arr[idx]:
            mx = max(mx, lisEndingAtIdx(arr, prev) + 1)
    return mx

def lis(arr):
    n = len(arr)
    res = 1
    for idx in range(1, n):
        res = max(res, lisEndingAtIdx(arr, idx))
    return res

if __name__ == "__main__":
    arr = input()
    # arr = [4, 1, 13, 7, 0, 2, 8, 11, 3];
    # arr = [1,2,3]
    # arr = [2,4,1,13,100]
    print(lis(arr))