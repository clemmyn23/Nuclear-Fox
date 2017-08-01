###
# Problem:
# Write a program to find out duplicate or repeated characters in a string.
# Characters should be returned only once.
# If you have a twice, I only want one.
# Case insensitive.
#
# 'JavaSenpai' => 'a'
# 'Javajava' => 'java'  'ajv'
# 'JjAaboom' => 'jao'


input_str = "JjAaboom"
counters = [0] * 26             # 26 characters in the alphabet

for current_char in input_str:

    # converts chars into int per ascii position
    # subtract by ord('a') to start 'a' at 0 and 'z' at 25
    char_index = ord(current_char.lower()) - ord('a')

    # increment corresponding counter every time the char is referenced
    counters[char_index] += 1

    # print duplicates only once
    if counters[char_index] == 2:
        print(current_char.lower(), end='')
