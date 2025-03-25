bills = [5, 5, 5, 20]

cashmoney = {
    5: 0,
    10: 0,
    20: 0
}

def lemonade(list):
    for i in list:
        cashmoney[i] += 1
        if (i == 10 and cashmoney[5] == 0) or i == 20 and (cashmoney[5] < 3 or (cashmoney[10] == 0 and cashmoney[5] == 0)):
            return(False)

    return(True)


print(lemonade(bills))