#!/usr/bin/python3
import sys

data = sys.stdin
result = []
fileSize = 0
count = 0


def printResult(code, Size):
    codeDict = dict((i, code.count(i)) for i in code)
    print(f"File size: {Size}")
    for [val, key] in sorted(codeDict.items()):
        if(val.isdigit()):
            print(f"{val} : {key}")


try:
    for line in data:
        data = str(line[-8:]).split(' ')
        count += 1
        try:
            fileSize += int(data[1])
        except:
            pass
        try:
            result.append(data[0].strip())
        except:
            pass
        if (count != 0 and count % 10 == 0):
            printResult(result, fileSize)
    printResult(result, fileSize)
except KeyboardInterrupt:
    printResult(result, fileSize)
    raise
