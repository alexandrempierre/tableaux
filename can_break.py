from tests import *

def can_break_or_simplify(formula):
    if is_and(formula):
        return True
    elif is_not(formula):
        n_formula = formula.negate()
        if is_not(n_formula):
            return True
        elif is_or(n_formula):
            return True
        elif is_imp(n_formula):
            return True
    return False