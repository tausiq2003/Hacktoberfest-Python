#Program to count the number of words in a text file and print the word and count of the word with biggest count
#The filename you enter must be in same directory as of the program
filename = input('Enter filename:')
fh = open(name, 'r')
counts = dict()

for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
