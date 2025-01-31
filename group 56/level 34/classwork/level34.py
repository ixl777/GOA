def remove_elements(main_list, indexes_list):
    for index in sorted(indexes_list, reverse=True):
        if index < len(main_list):
            main_list.pop(index)
    return main_list

main_list = [10, 20, 30, 40, 50]
indexes_list = [0, 2, 4]
print(remove_elements(main_list, indexes_list))  

def remove_one_element(my_list, index):
    if index < len(my_list):
        my_list.pop(index)
    print(my_list)


my_list = [10, 20, 30, 40, 50]
index = 2
remove_one_element(my_list, index)  