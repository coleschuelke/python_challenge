import requests
import re

p = re.compile(r"next nothing is (.*)")

nextNothing = "44827" 
baseUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="             # establish the base url


while True: # condition replaced with stopping condition
    # save the current nothing - won't make it here if nothing becomes zero
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
print("\n" + newUrl)

print("now continuing -- dividing by two\n")

nextNothing = str(int(int(nothing)/2))
text = "and"
# start the divide by two
while True: # if the first word isn't "and" - ^^
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