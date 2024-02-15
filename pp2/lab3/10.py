def uniq(arr):
    list = []
    for i in arr:
        if i not in list:
            list.append(i)
    return list

num = list(map(int, input().split()))

print(uniq(num))