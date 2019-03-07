string = input();
special = 0
for i in range(len(string)):
    if(string[i].isdigit()):
        digits = digits + 1
print(digits)
