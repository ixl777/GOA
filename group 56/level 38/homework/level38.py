my_tuple = (10, 20, 30, 40, 50)
second_element = my_tuple[1]
last_element = my_tuple[-1]
middle_slice = my_tuple[1:4]

print(f"Second element: {second_element}")
print(f"Last element: {last_element}")
print(f"Middle slice: {middle_slice}")

immutable_tuple = (1, 2, 3, 4, 5)

try:
    immutable_tuple[2] = 10
except TypeError as e:
    print(f"Error: {e}")

packed_tuple = (1, 'apple', 3.14, True)

a, b, c, d = packed_tuple

print(f"First variable: {a}")
print(f"Second variable: {b}")
print(f"Third variable: {c}")
print(f"Fourth variable: {d}")


repeated_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
count_3 = repeated_tuple.count(3)
index_4 = repeated_tuple.index(4)

print(f"Occurrences of 3: {count_3}")
print(f"First occurrence of 4: {index_4}")


my_set = {10, 20, 30, 40, 50}
my_set.add(60)
my_set.remove(30)
value_present = 20 in my_set

print(f"Updated set: {my_set}")
print(f"Is 20 present in the set? {value_present}")


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")


my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_set = set(my_list)
unique_list = list(unique_set)
print(f"Original list: {my_list}")
print(f"List after removing duplicates: {unique_list}")

