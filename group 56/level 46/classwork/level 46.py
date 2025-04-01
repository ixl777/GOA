def manual_list(start, end, step, user_num):
    result = [] 
    for num in range(start, end, step):
        if num > user_num:  
            result.append(num)
    return result
result1 = manual_list(1, 20, 2, 10)
print("პირველი შედეგი:", result1)

result2 = manual_list(5, 50, 5, 25)
print("მეორე შედეგი:", result2)

result3 = manual_list(10, 100, 10, 50)
print("მესამე შედეგი:", result3)


result = [num for num in range(1, 101) if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0)]
print(result)

b12 = [num for num in range(10, 201) if str(num) == str(num)[::-1]]
print(b12)

