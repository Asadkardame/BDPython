# def devide_string(input_string):
#     words_list = input_string.split()
#     return words_list
# string = "the quick brown fox jumps over the lazy dog"
# result = devide_string(string)
# print(result)


def remove_duplicates(lst):
    result = []
    seen = {}
    for num in lst:
        if num not in seen:
            result.append(num)
            seen[num] = True
    return result

lst = [1, 1, 2, 5, 5, 3, 6, 2, 1, 1, 3, 7, 5, 5, 3]
result = remove_duplicates(lst)
print(result)
