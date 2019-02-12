print("Laipni lūdzam fizzbuzz programmā!")

a = input("Izvelies skaitli no 1 līdz 100: ")
a = int(end)

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)