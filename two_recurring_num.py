

def find_recurring_char(my_list):
    dic = {}
    # print(dic)
    for i in range(len(my_list)):
        dic[my_list[i]] = my_list[i]
        if dic[my_list[i]] == my_list[i]:
            return my_list[i]
        else:
            return i
        # if my_list.count(i) > 1:
        #     return my_list[i]


# i for i in my_list if my_list.count(i) > 1
print(find_recurring_char([2, 1, 2, 4, 8, 8, 3, 9, 5, 5]))
