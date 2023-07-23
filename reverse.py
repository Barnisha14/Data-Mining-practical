def reverseWord(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end = end - 1

s = "I am Barnisha"

# convert string to a list of characters
s = list(s)
# to keep track of where each word starts
start = 0

while True:

    try:
        # find space
        end = s.index(' ', start)
        # Call reverseWord for each word
        reverseWord(s, start, end - 1)
        #update start variable
        start = end + 1

    # for the last word in string ValueError is returned
    except ValueError:
        # reverse the last word
        reverseWord(s, start, len(s) - 1)
        break

# reverse the entire list
s.reverse()

# convert the character list back to string
s = "".join(s)

print(s)
