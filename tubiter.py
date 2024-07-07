my_iter_list = [17,19,44,66,331,6653,234,675,324,12,375,78,643,132,635,87,98]
my_iterator = iter(my_iter_list)
for i in my_iterator:
    if i % 2 == 0:
        print("toq emas", i)
    elif i % 3 == i % i:
        print("toq emas", i)
    elif i % 5 == i % i:
        print("toq emas", i)
    elif i % 7 == i % i:
        print("toq emas", i)

    else:
        print(next(my_iterator),"Toq")