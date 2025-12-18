def print_lis(arr):
    n = len(arr)
    if n == 0: return []

    lis_len = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and lis_len[i] < lis_len[j] + 1:
                lis_len[i] = lis_len[j] + 1
                parent[i] = j

    max_len = max(lis_len)
    index = lis_len.index(max_len)

    subsequence = []
    while index != -1:
        subsequence.append(arr[index])
        index = parent[index]

    return subsequence[::-1]

if __name__ == "__main__":
    # Input contoh: 4 1 13 7 0 2 8 11 3
    # 2 4 1 13
    raw_input = input("Masukkan angka dipisah spasi: ")
    arr = [int(x) for x in raw_input.split()]
    
    hasil = print_lis(arr)
    print(hasil)
    print(f"panjang longest subsequence: {len(hasil)}")