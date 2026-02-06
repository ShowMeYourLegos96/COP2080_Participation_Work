# filter_clli.py
# returns only clli codes located in Florida or California
#clli_names = ['flxa99443oc', 'gaxb32443oc', 'caxo99323oc', 'flxa11443ds']
#print(list(filter(lambda x: x[0].upper() in 'FC', clli_names)))

# list_comp1.py
#print([(x, y) for x in ['a', 'b', 'c'] for y in ['first','b', 3] if x!=y])

# conv_neg_pos_nocomp.py
#a_list = [7, 5, -4, 6]
#def check_negative(z):
  #result = []
  #for item in z:
    #if item < 0:
      #result.append(item * -1)
      #return result
#print(check_negative(a_list))
#
#a_list = [7, 5, -4, 6]
#print([(item * -1) for item in a_list if item < 0])
# listcomp_vs_genexp.py
# list comprehension vs generator expression

import sys
a = [x for x in range(1000000)] #list comp
b = (x for x  in range(1000000))
print('list comp byte size is ',sys.getsizeof(a))
print('generator expression byte size is ',sys.getsizeof(b))

