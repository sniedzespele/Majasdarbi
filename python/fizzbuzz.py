print("Laipni lūdzam fizzbuzz programmā!")

end = input("Izvelies skaitli no 1 līdz 100: ")
end = int(end)

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)