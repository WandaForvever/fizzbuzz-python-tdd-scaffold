def FizzBuzz(i):
    if i % 3 * i % 5:
        return i
    else:
        return "Fizz"[i % 3 * 4:] + "Buzz"[i % 5 * 4:]


if __name__ == '__main__':
    for i in range(1, 101):
        print(FizzBuzz(i))
