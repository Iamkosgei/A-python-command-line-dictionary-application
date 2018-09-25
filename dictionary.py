'''
Making a dictionary using json data
'''
import json
import difflib
from difflib import get_close_matches
names = json.load(open("data.json"))

def search(word):
    #convert all characters in the word to be lower case
    y=word.lower()
    if y in names:
        return((names[y]))
    elif len(get_close_matches(word,names,1,0.8)) > 0:
        print("Did you mean %s instead? " % get_close_matches(word,names,1,0.8)[0] + "Enter Y for yes and N for no " )
        if input().lower()=="y":
            return names[get_close_matches(word,names,1,0.8)[0]]
        elif input().lower()=="y":
            return("The word doesnt exist")
        else:
            return("Enter Y for yes and N for no")
    else:
        return("The word doesnt exist")

output= search(input("Enter a word \n"))

if type(output)== list:
    count = 1
    for findings in output:
        print(str(count) + ". "+findings)
        count=count+1
else:
    print(output)
