def subsets(superset=None,criteria=None):
    if superset is None:
        sub,compl = [],[]
    elif criteria is None:
        sub,compl = superset[:],[]
    else:
        sub = [element for element in superset if criteria(element)]
        compl = [element for element in superset if not criteria(element)]
    
    return sub,compl