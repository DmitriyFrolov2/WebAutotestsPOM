my_list = [1,2,3]
my_iter = iter(my_list)
try:
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))

except StopIteration:
    print("Конец итерации")