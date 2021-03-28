given_string = input("Input your string: ")
result_set = set()

for i in range(len(given_string)):
    last_string = given_string[i:]
    for length in range(1, len(last_string) + 1):
        substring = given_string[i:i + length]
        if substring != given_string:
            hashed_substring = hash(substring)
            result_set.add(hashed_substring)

print(f"Total number of substrings: {len(result_set)}")