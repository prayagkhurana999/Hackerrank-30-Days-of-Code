num = int(input())

if num % 2 != 0:
    print("Weird")
else:
    if num <= 5:
        print("Not Weird")
    elif num <= 20:
        print("Weird")
    else:
        print("Not Weird")
