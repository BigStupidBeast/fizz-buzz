print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,101)),sep='\n')
print('\n'.join('FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else str(i) for i in range(1, 101))) # 2.53 msec
[print('FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i) for i in range(1, 101)] # 8.11 msec
[print('FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8] or i) for i in range(1, 101)] # 8.43 msec
[print('FizzBuzz'[i*i%3*4:8--i**4%5] or i) for i in range(1, 101)] # 8.31 msec
[print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i) for i in range(1, 101)] # 8.38 msec
[print((i%3<1)*'Fizz'+(i%5<1)*'Buzz' or i) for i in range(1, 101)] # 8.4 msec
[print(i%3//2*'Fizz'+i%5//4*'Buzz' or i+1) for i in range(100)] # 8.49 msec