import os
import csv
from collections import namedtuple
from bisect import bisect, insort
from operator import attrgetter
from pprint import pprint

pathName = "/home/lana/Projects/Bundeswehrbung/transcript"

blocks = []
block = []
count = []
Result =  namedtuple('Word', ('word', 'amount'))
result = []


print("1")

numFiles = []
fileNames = os.listdir(pathName)
for fileNames in fileNames:
    if fileNames.endswith(".csv"):
        numFiles.append(fileNames)

for i in numFiles:
    file = open(os.path.join(pathName, i), "rU")
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        block.append(row[4])

for e in block:
    words = e.split()
    for word in words:
        word = word.lower()
        word =  word.translate({ ord(c): None for c in "._!,' " })

        if word in count:
            index = count.index(word)
            count[index+1] += 1
        else:
            count.append(word)
            count.append(1)

by_amount = attrgetter('amount')
result.sort(key=by_amount)

for n in count[::2]:
    index = count.index(n)
    amount = count[index+1]
    newWord = Result(n, amount)
    insort(result, newWord, key=by_amount)

with open('wordNumber.txt', 'w') as f:
    print(result, file=f)




