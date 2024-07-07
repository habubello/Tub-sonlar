def gen_get_numbers(z,n):
    for i in range(z,n):
        if i%2 == 0:
            print("toq emas",i)
        elif i % 3 == i%i:
            print("toq emas",i)
        elif i % 5 == i%i:
            print("toq emas",i)
        elif i % 7 == i%i:
            print("toq emas", i)
        # if i%i==0  and i%3==1 and i%5==1 and i%7==1 and i%4==1:
        else:
            print("toq son",i)

if __name__ == '__main__':
    gen_get_numbers(100,200)