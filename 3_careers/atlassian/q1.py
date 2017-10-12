# Complete the function below.
def  convert(number):
    # number = str(number)
    table = ['0', 'a', 't', 'l', 's', 'i', 'n']
    result = []

    print(number)

    if (number == 0):
        result.append(0)
    while (number > 0):
        print(number)
        result.append(number % 7)
        number = int(number / 7)

    print("{}".format(result))

    i = 0
    while (i < len(result)):
        result[i] = table[result[i]]
        i += 1

    print("{}".format(result))
    result.reverse()

    print("{}".format(result))

    return ''.join(result)


print(convert(3))
