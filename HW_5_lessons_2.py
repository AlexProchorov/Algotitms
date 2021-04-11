def print_ascii_char(number = 32):
    if number < 32 or number > 127:
        return

    if number != 32 and (number - 32) % 10 == 0:
        print()
    print(f'{number} - {chr(number)}', end = '\t')
    print_ascii_char(number + 1)


print_ascii_char()