from nltk import *
from nltk.sem import logic
from tests import *
from subsets import *
from new_var import *
from rules import *
from can_break import *

read_expr = Expression.fromstring

def tableaux(goal=None,assumptions=None):
    if assumptions is None:
        assumptions = []
    
    if goal is not None:
        assumptions.append(goal.negate())
    
    rules = {
        'non_branching': {
            is_and: r1_rule_and,
            is_not_not: r4_rule_not_not,
            is_n_or: r6_rule_n_or,
            is_n_imp: r7_rule_n_imp,
        },
        'branching': {
            is_or: r2_rule_or,
            is_imp: r3_rule_imp,
            is_n_and: r5_rule_n_and,
        },
        'existence': {
            is_n_all: r9_rule_n_all,
            is_exists: r10_rule_exists
        },
        'universal': {
            is_all: r8_rule_all,
            is_n_exists: r11_rule_n_exists
        }
    }
    
    # Deal with formulae that does not create new branches
    breakable = list(filter(can_break_or_simplify,assumptions))
    assumptions = [formula for formula in assumptions if not can_break_or_simplify(formula)]
    
    while breakable:
        assumptions_temp = []
        for formula in breakable:
            from_rule = []
            for cond,rule in rules['non_branching'].items():
                if cond(formula):
                    from_rule = rule(formula)
                    break
            assumptions_temp += from_rule
            
        breakable = list(filter(can_break_or_simplify, assumptions_temp))
        assumptions += [formula for formula in assumptions_temp if not can_break_or_simplify(formula)]
    
    all_atoms = True
    for i,formula in enumerate(assumptions):
        all_atoms = all_atoms and (is_atom(formula) or is_n_atom(formula))

        for j,formula2 in enumerate(assumptions[i+1:]):
            if formula.negate() == formula2:
                return True

    # If all formulae are atoms or negated atoms and the tableaux isn't closed, than it can't be closed
    if all_atoms:
        return False

    # Deal with formulae that does create new branches
    for i,formula in enumerate(assumptions):
        for cond,rule in rules['branching'].items():
            if cond(formula):
                from_rule = rule(formula)
                assumptions_b1 = assumptions[:i] + [from_rule[0]] + assumptions[i+1:]
                assumptions_b2 = assumptions[:i] + [from_rule[1]] + assumptions[i+1:]

                del assumptions
                
                return tableaux(assumptions=assumptions_b1) and tableaux(assumptions=assumptions_b2)

    # Deal with formulae with quantifiers    
    quantifiers,assumptions = subsets(assumptions,is_quantifier)
    
    variables = []
    for formula in assumptions:
        variables += extract_variables(formula)
        
    while quantifiers:
        existence_formulae,universal_formulae = subsets(quantifiers,is_existence_quantifier)
        
        while existence_formulae:
            for i,formula in enumerate(existence_formulae):
                for cond,rule in rules['existence'].items():
                    if cond(formula):
                        substituted_formula = rule(formula,variables)
                        if is_universal_quantifier(substituted_formula):
                            universal_formulae.append(substituted_formula)
                        elif is_existence_quantifier(substituted_formula):
                            existence_formulae.append(substituted_formula)
                        else:
                            assumptions.append(substituted_formula)
                        del existence_formulae[i]
                        
        while universal_formulae:
            if len(variables) == 0:
                variables.append(new_variable([]))
            for i,formula in enumerate(universal_formulae):
                for cond,rule in rules['universal'].items():
                    if cond(formula):
                        substituted_formulae = rule(formula,variables)
                        if is_existence_quantifier(substituted_formulae[0]):
                            existence_formulae += substituted_formulae
                        elif is_universal_quantifier(substituted_formulae[0]):
                            universal_formulae += substituted_formulae
                        else:
                            assumptions += substituted_formulae
                        del universal_formulae[i]
                        
        quantifiers = existence_formulae + universal_formulae
    
    return tableaux(assumptions=assumptions)
