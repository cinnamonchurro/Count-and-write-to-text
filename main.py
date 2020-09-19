def countandwrite(file):
    with open(file) as text : 
        aline = text.readlines()
        worddict = dict()
        for data in aline :
            words = data.split()
            #print(data)
            #print(words)

countandwrite('alice.txt')