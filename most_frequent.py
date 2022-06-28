# count occurrence of a given characters in a String
import operator
string = 'Mississippi'


def most_frequent(str):
    dictionaries = {}
    for char in str:
        if(char in dictionaries.keys()):
            dictionaries[char] += 1
        else:
            dictionaries[char] = 1

    for char in sorted(dictionaries, reverse=True):
        print(char, ' = ', dictionaries[char])


most_frequent(string)
