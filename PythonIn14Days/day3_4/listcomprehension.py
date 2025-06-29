a = [1, 2, 3, 4, 5, 6, 7]

res = [value ** 2 for value in a]
multiply = [value * 2 for value in a]
filter_even = [value for value in a if value % 2 == 0]
#generating list from range
b = [list_from_range for list_from_range in range(8)]
coordinates = [(x, y) for x in range(3) for y in range(3)]
#filtering list from slice
c = [val for val in a[:6] if val % 2 == 0]
#filtering list from slice using range
d = [vall for vall in range(6)[:6] if vall % 2 == 0]



print(f'filtering list from slice using range {d}')
print(f'filtering list from slice {c}')
print(f'creating coordinates from range {coordinates}')
print(f'generating values from range {b}')
print(f'square of values in a {res}')
print(f'value in a x 2 {multiply}')
print(f'filter even in a {filter_even}')