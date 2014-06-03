wordlist=open("wordlist.txt","r")
anagram = raw_input("Enter anagram: ")
anagram=anagram.replace("\n", "")

anlen = len(anagram)
nochar = 0
found = False
i=0
solution=[]


for line in wordlist:
    curtry= line
    curtry = curtry.replace("\n", "")
    #print curtry
    for i in range(anlen):
        if anagram.count(anagram[i]) == curtry.count(anagram[i]):
            #print anagram[i]
            nochar+=1

    if nochar==anlen:
        if len(curtry)==anlen:
             #print curtry
             #print len(curtry)
             solution.append(curtry)

             
       
    nochar=0

print solution