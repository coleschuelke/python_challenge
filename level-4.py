# take the content from one url and use it to find and request the next url, following a chain
import requests
import re

p = re.compile(r"next nothing is (.*)") # re statement to isolate only the "nothings"

# initialize the first "nothing"
nextNothing = "44827" 
# establish the base url
baseUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" 


while True: # condition replaced with stopping condition
    # save the current nothing - won't make it here if nothing becomes zero
    # prevent the final returned url from being meaningless due to no match
    nothing = nextNothing
    totalUrl = baseUrl + nothing # combine the two parts of the url
    page = requests.get(totalUrl) # retrieve webpage using current nothing
    text = page.text

    # read the nextNothing off the webpage
    match = p.search(text) # search the webpage using re
    if match:
        nextNothing = match.group()[16:] # extract just the "nothing from the re match"
    else:
        break # no nothings found
    print(nextNothing)

newUrl = baseUrl + nothing # return the last usable url
print("\n" + newUrl)

print("now continuing -- dividing by two\n")

nextNothing = str(int(int(nothing)/2))
text = "and"
# start the divide by two
while True:
    nothing = nextNothing
    totalUrl = baseUrl + nothing # combine the two parts of the url
    page = requests.get(totalUrl) # retrieve webpage using current nothing
    text = page.text

    # read the nextNothing off the webpage
    match = p.search(text)
    if match:
        nextNothing = match.group()[16:]
    else:
        break 
    print(nextNothing)


newUrl = baseUrl + nothing

print(newUrl)