def countandwrite(f1, f2 = None):
    #define output file if not given
    if f2 == None :
        f2 = 'out.txt'

    #open text file f1 for reading
    with open(f1) as text : 
        #read the whole of text file and store in aline
        aline = text.readlines()

        #create dictionary for list of words
        worddict = dict()

        #going through words line by line
        for data in aline :
            #print('aline', aline)
            words = data.split()
            for word in words : 
                #print('words', words)
                rempunc = ''
                for char in word :
                    #print('char', char)

                    #remove punctuations
                    #if char in """!()-[]{};:'"\,<>./?@#$%^&*_~ """ : 
                        #pass
                        #print (char)
                    #else :     
                    if char not in """!()-[]{};:'"\,<>./?@#$%^&*_~ """ :
                        rempunc = rempunc + char
                #print('rempunc', rempunc)
                rempunc = rempunc.lower()
                #create key or add value to key
                if rempunc in worddict :
                    worddict[rempunc] += 1
                else : 
                    worddict[rempunc] = 1
        
        #write into output file
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
#countandwrite('example.txt','out.txt')
countandwrite('alice.txt', 'outfile.txt')
#print(countandwrite('alice.txt','out.txt'))