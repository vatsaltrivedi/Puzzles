
A = [10,8,7,5,11,3]


def Maximum_Profit(A):
    buy = A[0]
    sell = A[1]
    profit = A[1]-A[0]
    last_index = A[1]

    for i in A[2:]:
        new_pro = i-last_index
        if (new_pro > profit):
            buy = last_index
            sell = i
            profit = new_pro
            print buy, " ", sell, " ", profit

        last_index = i

    return profit

print Maximum_Profit(A)
