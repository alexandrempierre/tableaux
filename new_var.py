from nltk import *
import random

def new_variable(variables=[]):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    var_name = random.choice(letters)
    var_num = 1
    var = Variable(var_name + str(var_num))
    while var in variables:
        var_num += 1
        var = Variable(var_name + str(var_num))
    return var
