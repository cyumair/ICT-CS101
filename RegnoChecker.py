
def ValidityCheck(reg):
    
    regNoElements = reg.split('-')                         # will seperate elements by -(dash) and store those seperated elements in a list
    isValid = True

    if len(regNoElements[0]) != 4 or len(regNoElements[1]) != 3 or len(regNoElements[2]) != 3: # checking if len of reg number elements is valid
        isValid = False

    else:
        firstcharacter = regNoElements[0][0]
        secondcharacter = regNoElements[0][1]
        firstTwoCharacters = firstcharacter + secondcharacter               # alphabetical part of FA19 i.e: FA
        SecondTwoCharacters = regNoElements[0][2] + regNoElements[0][3]      # digital part of FA19 i.e: 19
        
        # Checking 1st part of Reg Number
        if firstTwoCharacters != 'FA' and firstTwoCharacters != 'SP': 
            isValid = False
        
        elif not SecondTwoCharacters.isdigit():  
            isValid = False
        
        elif int(SecondTwoCharacters) < 1 or int(SecondTwoCharacters) > 19:
            isValid = False
        # Checking 2nd Part of Reg Number
        elif not regNoElements[1].isalpha():  
            isValid = False
        
        # checking 3rd part of reg number
        elif not regNoElements[2].isdigit():
            isValid = False
        
        #checking if reg number has two dashes
        elif len(regNoElements) != 3:                                    # if elements are seperated by - (dash) then lenght of list would be three
            isValid = False
            
    return isValid                                                       # it will either return True or False

reg = input('Enter Registration Number ')
Validity = ValidityCheck(reg)                                            # value returned by function is being stored in a variable

if Validity:
    print('The Registration Number Entered is Valid')

else:
    print('The Registration Number Entered is Invalid')
    
