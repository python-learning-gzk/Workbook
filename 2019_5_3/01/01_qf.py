from string import *
from random import randint
code_chars=''.join([digits,lowercase,ascii_uppercase])
print code_chars
code_list=[]
for i in range(200):
    index_str = [randint(0, len(code_chars) - 1) for i in range(20)]
    code_list.append(''.join([code_chars[ind] for ind in index_str]))
print code_list