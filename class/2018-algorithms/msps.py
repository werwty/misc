def MPSP(X):
    import ipdb; ipdb.set_trace()
    # X is the input string
    # Create an 2d array l of size len(X) by len(X), each l[i][j]
    # will store the longest palindrome in X[i...j]
    l = [[0 for i in range(len(X)+1)] for i in range(len(X)+1)]

    # initialized l[i][i] with 1s, since each letter is a palindrome of length 1
    for i in range(len(X)):
        l[i][i]=1

    for i in range(1, len(X)):
        for s in range(1, len(X)-i):

            j= i+s
            if X[i] == X[j]:
                if i+1 < j-1:
                    l[i][j] = l[i+1][j-1] + 2
                    l[j][i] = l[i+1][j-1] + 2

                else:
                    l[i][j] = 2
                    l[j][i] = 2
            else:
                l[i][j] = max(l[i+1][j], l[i][j-1])
                l[j][i] = max(l[i+1][j], l[i][j-1])

    return l[1][len(X)-1]


MPSP('aba')
