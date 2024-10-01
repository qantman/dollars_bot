def plural(num: str, ruble: bool):
    if ruble is True:
        words = ["рублей", "рубль", "рубля"]
    else:
        words = ["копеек", "копейка", "копейки"]
    num = int(num)
    if num % 100 in [11, 12, 13, 14]:
        return f"{num} {words[0]}"
    elif num % 10 == 1:
        return f"{num} {words[1]}"
    elif num % 10 in [2, 3, 4]:
        return f"{num} {words[2]}"
    else:
        return f"{num} {words[0]}"
