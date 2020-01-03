para = input('enter a paragraph ')
def wordcount(para):
    print('WORDS')
    words = para.split(' ')
    usedwords = []
    for i in words:
        if i not in usedwords:
            count = words.count(i)
            print(i,' is repeated ', count, ' times ')
            usedwords.append(i)
def uniquechar(para):
    print('CHARACTERS')
    uniquechars = []
    for i in para:
        if i not in uniquechars:
            count = para.count(i)
            print(i,' is repeated ', count, ' times ')
            uniquechars.append(i)
        
wordcount(para)
uniquechar(para)
