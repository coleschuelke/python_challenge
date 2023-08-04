# serializing and deserializing data using pickle
import pickle


msg = open("banner", "rb") # opens file in read binary mode (rb)
print(type(msg))
# comes in as an object which is a list of lists of tuples of one string and one int
# instructions on "writing" a word to the console - number of spaces and hashes, each list is a newline
msg_dp = pickle.load(msg)
print(type(msg_dp))
# print(msg_dp)

# for loop to parse and print the code
for i in msg_dp: # each list
    for j in i: # each tuple
        for k in range(j[1]):
            print(j[0], end="")
    print("\n")

# I don't know wether I'm stoked I finally figured that out and think I'm a genius or embarrased that it took me 45 mins
# and wish I wasn't dumb. But I did write that parsing loop on the first try, so that was fun
