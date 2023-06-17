regular_list = [1, 2, [3, 4, [5], 6], 7, 8, 9, 10]
flat_list = [item for sublist in regular_list for item in sublist]
print('Original list', regular_list)
print('Transformed list', flat_list)