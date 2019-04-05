n = int(input())
if n % 2 !=0:
    print('Weird')
elif 2<= n <=5 and n % 2==0:
    print('Not Weird')
elif n % 2 ==0 and 6<= n <=20:
    print('Weird')
elif n % 2==0 and n > 20:
    print('Not Weird')

