def array_left_rotation(a, n, k):
    list = [0]*n
    for i in range (n):
        indice = i - k%n
        if (indice < 0):
            indice = indice + n
        list[indice] = a[i]
    return list   
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
