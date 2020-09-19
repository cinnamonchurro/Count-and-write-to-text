def countandwrite(f1, f2):
    with open(f1) as text : 
        aline = text.readlines()
        worddict = dict()
        for data in aline :
            words = data.split()
            for word in words : 
                word = word.lower()
                if word in worddict :
                    worddict[word] += 1
                else : 
                    worddict[word] = 1
        outfile = open(f2, 'w')
        wdlst = list(worddict.items())
        wdlst.sort()
        #print(worddict.items()
        #print(wdlst)
        for kv in wdlst : 
            for dt in kv : 
                outfile.write(str(dt)+' ')
            outfile.write('\n')
        outfile.close()

    return(worddict)
                #print(word)
            #print(data)
            #print(words)
countandwrite('alice.txt','out.txt')
#print(countandwrite('alice.txt','out.txt'))