# riddle #2
import string

keys = list(range(26))
letters = list(string.ascii_lowercase)


# print(keys)

encode = dict(zip(keys, letters))
decode = dict(zip(letters, keys))

print(map)

message = "map"
newMessage = ""

for letter in message:
    if letter not in letters:
        newMessage += letter
    else:
        num = decode[letter]
        num += 2
        newLetter = encode[(num%26)]
        newMessage += newLetter

print(newMessage)