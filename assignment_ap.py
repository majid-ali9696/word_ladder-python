import json

print("the dictionary is loading")

def hammingdistance(word1,word2):#gets the hamming distance
    if(word1.__len__()==word2.__len__()):
        difference = 0
        for i  in range(0,word1.__len__()):
            if word1[i] != word2[i]:
                difference += 1
    else:
        print("the length of string is not same")
        return

    return difference

dictionary_data=open('C:\Users\Majid ali\Desktop\dictionary.json.txt')
words=json.load(dictionary_data)
wordladder={}
chains={}



for k,v in words.items():
   
    for k2,v in words.items():
        count = 0
        if k.__len__()==k2.__len__():
            for i in range(0, k.__len__()):
                if k[i] != k2[i]:
                    count = count + 1
                    if count==1:
                        if k in chains:
                             # append the new number to the existing array at this slot
                            chains[k].append(k2)
                        else:
                            chains[k] = [k2]

                        print chains

print("the dictionary is loaded ")
print("enter the source word")
source=raw_input()

print("enter the destination word")
dest=raw_input()

diff=hammingdistance(source,dest)
print diff






            
