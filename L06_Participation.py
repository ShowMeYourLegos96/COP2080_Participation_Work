# strip off dashes
def strip_string(b_function):
    def wrapper():
        func = b_function()
        strip_string = func.strip('-')
        return strip_string
    return wrapper

#create upper case version of clli code
def uppercase_decorator(some_function):
  def a_wrapper():
    func = some_function()
    make_uppercase = func.upper()
    return make_uppercase

  return a_wrapper
 
#def clli_code():
  #print('The Florida router clli code is', end = '')
  #return '---tpaflxacg19----'
@strip_string
def clli_code():
   print('The Florida router clli code is', end = '')
   return '---tpaflxacg19----'

clli_code()

@uppercase_decorator
def clli_code():
   print('The Florida router clli code is', end = '')
   return '---tpaflxacg19----'
clli_code()
#print(clli_code())
# Double click to copy code
