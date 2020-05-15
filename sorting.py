def check_sorted(A, ascending = True):
    ''' check if array is in ascending order or decending(as we wish in parametr)'''
    s = 2 * int(ascending) - 1 ##this modify parametr as 1 or -1
    for i in range(len(A) - 1):
        if s * A[i] > s * A[i+1]:
            return False
    return True

def merge_sort(A: list):
    if (len(A) <= 1):
        return A
    return merge(merge_sort(A[:int(len(A) / 2)]), merge_sort(A[int(len(A) / 2):]))

def merge(Left: list, Right: list):
    res = []
    l_i = r_i = 0
    while l_i < len(Left) and r_i < len(Right):
        if Left[l_i] <= Right[r_i]:
            res.append(Left[l_i])
            l_i += 1
        else:
            res.append(Right[r_i])
            r_i += 1
    res[:] = res[:] + Left[l_i:] + Right[r_i:]
    return res

def hoar_sort(A: list):
    if len(A) <= 1:
        return
    barrier = A[0]
    Left, Mid, Right = [], [], []
    for x in A:
        if x < barrier:
            Left.append(x)
        elif x == barrier:
            Mid.append(x)
        else:
            Right.append(x)
    k = 0
    hoar_sort(Left)
    hoar_sort(Right)
    A[:] = Left + Mid + Right
    ##for x in Left + Mid + Right:
    ##    A[k] = x
    ##    k += 1

if __name__ == "__main__":
    A = [-3, 10, 4, 9, 5, 8, 4, 7, 3, 1, 0, -3]
    B = [2, 3, 8]
    C = [3, 5, 7]
    ##print(merge_sort(A))
    hoar_sort(A)
    A.reverse()
    print(check_sorted(A, False))