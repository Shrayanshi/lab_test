number = 5
flag = False
if number > 1:
  for i in range(2, num):
        if (number % i) == 0:
            flag = True
            break

if flag:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")
