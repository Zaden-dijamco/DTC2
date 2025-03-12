sharps = {'0':'C','1':'G','2':'D','3':'A','4':'E','5':'B','6':'G#','7':'C#'}
flats = {'0':'C', '1':'F','2':'Eb','3':'Bb','4':'Ab','5':'Db','6':'Gb','7':'Cb'}

#checking if they key has symbols
checkforsymbols = input('Does your key signature have #s, bs or nothing? ')

#checking how many sharps
if checkforsymbols == '#':

    #checking how many sharps
    numberofsharps = input('How many sharps are there? ')
    
    #determining what key it is and printing it
    print(sharps[numberofsharps], 'major')

#checking how many flats
elif checkforsymbols == 'b':

    #checking how many flats
    numberofflats = input('How many flats are there? ')
    
    print(flats[numberofflats], 'major')

#If there is no symbol then the key is in C major
elif checkforsymbols == 'nothing':

    #printing answer
    print('You are in the key of C major')
    quit()

#if answer not recognized, ask again
else:
    print('Sorry, I don\'t know about',checkforsymbols)
    checkforsymbols = input('Does your key signature have #s, bs, or thing? ')

