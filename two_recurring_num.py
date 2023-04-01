

def first_recurring_char1(my_list):
    """
    Shorter and more readable code.
    with O(n) runtime
    """
    dic = {}
    for i in my_list:

        if i in dic:
            return i
        else:
            dic[i] = 1
        print(dic)


print(first_recurring_char1([2, 1, 2, 4, 8, 8, 3, 9, 5, 5]))



