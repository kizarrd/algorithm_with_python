myDict = {1:"egg", "Answer":42, 8:14, "foo":42}
print({key for key, value in myDict.items() if value==42})