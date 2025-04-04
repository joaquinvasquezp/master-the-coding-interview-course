# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

# Input: "fun&!! time"
# Output: time

# Input: "I love dogs"
# Output: love


def LongestWord(sen):
    # First approach
    # words = sen.split(' ')
    # return max(words)

    # Better solution
    import re
    words = re.findall(r'\b[a-zA-Z0-9]+\b', sen)

    return max(words, key=len)

word = "I love dogs"
print(LongestWord(word))