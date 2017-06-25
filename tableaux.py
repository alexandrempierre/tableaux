from nltk import *
from nltk.sem import logic
read_expr = Expression.fromstring
tableaux_prove = TableauProver().prove

from functools import reduce

def tableaux(pergunta=None,bd=None):
    if bd is None:
        bd = []
    bd.append(pergunta.negate())
    
    is_and = lambda expr: isinstance(expr,logic.AndExpression)
    is_neg = lambda expr: isinstance(expr,logic.NegatedExpression)
    is_or = lambda expr: isinstance(expr,logic.OrExpression)
    is_imp = lambda expr: isinstance(expr,logic.ImpExpression)
    
    is_atom = lambda expr: isinstance(expr,logic.ApplicationExpression)
    is_n_atom = lambda expr: is_atom(expr.negate())
    
    breakable = lambda : reduce(lambda x,y: x or y, \
                                [is_and(expr) or (is_neg(expr) and not is_n_atom(expr)) for expr in bd], \
                                False)
    
    while breakable():
        bd_temp = []
        del_list = []
        for i,expr in enumerate(bd):

            expr_from_rule = []
            
            # Rules that does not add branches
            if is_and(expr):
                expr_from_rule = r1_rule_and(expr)
                del_list.append(expr)
            elif is_neg(expr):
                n_expr = expr.negate()
                if is_neg(n_expr):
                    expr_from_rule = r4_rule_not_not(n_expr)
                    del_list.append(expr)
                elif is_or(n_expr):
                    expr_from_rule = r6_rule_n_or(n_expr)
                    del_list.append(expr)
                elif is_imp(n_expr):
                    expr_from_rule = r7_rule_n_imp(n_expr)
                    del_list.append(expr)
            
            bd_temp = bd_temp + expr_from_rule
        
        bd = [expr for expr in bd if expr not in del_list] + bd_temp
    
    for i,expr in enumerate(bd):
        for j,expr2 in enumerate(bd[i+1:]):
            if expr.negate() == expr2:
                return True
    
    return bd

def r1_rule_and(expr):
    return [expr.first, expr.second]

def r2_rule_or(expr):
    pass

def r3_rule_imp(expr):
    pass

def r4_rule_not_not(n_expr):
    return [n_expr.negate()]

def r5_rule_n_and(expr):
    pass

def r6_rule_n_or(n_expr):
    return [-n_expr.first,-n_expr.second]

def r7_rule_n_imp(n_expr):
    return [n_expr.first, -n_expr.second]

# Quantifiers Rules
def r8_rule_all(expr):
    pass

def r9_rule_n_all(expr): # for not all
    pass

def r10_rule_some(expr):
    pass

def r11_rule_n_some(expr): # does not exist
    pass