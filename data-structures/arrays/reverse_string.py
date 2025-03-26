# In interviews treat strings questions as an array question, strings are simply an array of characters.

# Create a function that reverses a string:
# 'Hi My name is Rick' should be:
# 'kciR si eman yM iH'

def reverse(string):
    if not string or not isinstance(string, str) or len(string) < 2:
        print('Error')
        return

    reversed_string = []

    for idx in range(0, len(string)):
        reversed_string.append(string[len(string) - 1 - idx])

    return ''.join(reversed_string)

string = 'Hi My name is Rick'
print(string)
print(reverse(string))
# reverse(2)