from nltk import *
from nltk.sem import logic

def is_and(formula):
    return isinstance(formula,logic.AndExpression)

def is_n_and(formula):
    n_formula = formula.negate()
    return is_and(n_formula)

def is_or(formula):
    return isinstance(formula,logic.OrExpression)

def is_n_or(formula):
    n_formula = formula.negate()
    return is_or(n_formula)

def is_imp(formula):
    return isinstance(formula,logic.ImpExpression)

def is_n_imp(formula):
    n_formula = formula.negate()
    return is_imp(n_formula)

def is_not(formula):
    return isinstance(formula,logic.NegatedExpression)

def is_not_not(formula):
    n_formula = formula.negate()
    return is_not(n_formula)

def is_atom(formula):
    return isinstance(formula, logic.ApplicationExpression)

def is_n_atom(formula):
    n_formula = formula.negate()
    return is_atom(n_formula)

def is_all(formula):
    return isinstance(formula,logic.AllExpression)

def is_n_all(formula):
    n_formula = formula.negate()
    return is_all(n_formula)

def is_exists(formula):
    return isinstance(formula,logic.ExistsExpression)

def is_n_exists(formula):
    n_formula = formula.negate()
    return is_exists(n_formula)


def is_quantifier(formula):
    return is_all(formula) or is_n_all(formula) or is_exists(formula) or is_n_exists(formula)

def is_universal_quantifier(formula):
    return is_all(formula) or is_n_exists(formula)

def is_existence_quantifier(formula):
    return is_n_all(formula) or is_exists(formula)

def is_indiv_var(var):
    expr_var = Expression().make_VariableExpression(var)
    return isinstance(expr_var, logic.IndividualVariableExpression)

def extract_variables(formula):
    return [v for v in formula.variables() if is_indiv_var(v)]
