num = list(input().split())

for i in range(len(num)):
    if num[i] == '1':
        num.append('00')
    elif num[i] == '2':
        # num.append('\n')
        num.append('00')
    elif num[i] == '3':
        # num.append('\n')
        num.append('00')
    elif num[i] == '4':
        # num.append('\n')
        num.append('01')
    elif num[i] == '5':
        # num.append('\n')
        num.append('01')
    elif num[i] == '6':
        # num.append('\n')
        num.append('01')
    elif num[i] == '7':
        # num.append('\n')
        num.append('10')
    else:
        num.append('11')
print(num)