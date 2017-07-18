from nltk import *
from nltk.sem import logic
from new_var import *
from tests import *

# Does not create new branches
def r1_rule_and(expr):
    return [expr.first, expr.second]

def r4_rule_not_not(expr):
    n_expr = expr.negate()
    return [n_expr.negate()]

def r6_rule_n_or(expr):
    n_expr = expr.negate()
    return [n_expr.first.negate(),n_expr.second.negate()]

def r7_rule_n_imp(expr):
    n_expr = expr.negate()
    return [n_expr.first, n_expr.second.negate()]

# Create new branches
def r2_rule_or(expr):
    return [expr.first, expr.second]

def r3_rule_imp(expr):
    return [expr.first.negate(), expr.second]

def r5_rule_n_and(expr):
    n_expr = expr.negate()
    return [n_expr.first.negate(), n_expr.second.negate()]

# Quantifiers Rules
def r8_rule_all(formula,variables):
    term = formula.term
    vs = extract_variables(term)
    substituted_exprs = []
    for v in vs:
        for new_v in variables:
            expr_new_v = Expression().make_VariableExpression(new_v)
            substituted_exprs.append(term.replace(v,expr_new_v))
    return substituted_exprs

def r9_rule_n_all(formula,variables): # "there is some for which this is false"
    term = formula.negate().term
    vs = extract_variables(term)
    for v in vs:
        new_v = new_variable(variables)
        expr_new_v = Expression().make_VariableExpression(new_v)
        term = term.replace(v,expr_new_v)
        variables.append(new_v)
    return term.negate()

def r10_rule_exists(formula,variables):
    term = formula.term
    vs = extract_variables(term)
    for v in vs:
        new_v = new_variable(variables)
        expr_new_v = Expression().make_VariableExpression(new_v)
        term = term.replace(v,expr_new_v)
        variables.append(new_v)
    return term

def r11_rule_n_exists(formula,variables): # "does not exist any"
    term = formula.negate().term
    vs = extract_variables(term)
    substituted_exprs = []
    for v in vs:
        for new_v in variables:
            expr_new_v = Expression().make_VariableExpression(new_v)
            substituted_exprs.append(term.replace(v,expr_new_v).negate())
    return substituted_exprs
