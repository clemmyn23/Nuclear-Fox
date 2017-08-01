# Problem
# You have a list of words. (dictionary) (already mapped to memory)
# You have one long string input, no spaces.
#
# Extract the list of words in that string that appear in the dictionary.
#

input_str = "ihavecatandcatsanddog"
dictionary = {
    "cat",
    "cats",
    "dog",
    "dogs"
}

for entry in dictionary:
    if entry in input_str:
        print(entry)
