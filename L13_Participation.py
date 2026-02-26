import hashlib
#h = hashlib.new('md5', b'ca').hexdigest()
#print(f'initial hash is {h}')

#original = 'cah'
#for letter in 'abcdefghi':
 #best_guess = 'ca' + letter
 #h = hashlib.new('md5', best_guess.encode('UTF-8')).hexdigest()
 #if h == original:
    #print(f'found it as letter {letter}')

 #print(best_guess, h)
 
letters = 'ca'
for letter1 in letters:
    for letter2 in letters:
        xx = letter1 + letter2
        print(xx)

