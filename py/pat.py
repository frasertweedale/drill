# very naive NFA implementation (``*`` only, no parens or pipe)
#
def match(e, s):
    e = e + '\0'  # None is accept state
    nfa = set([0])
    i = 0
    while nfa:
        newnfa = set()
        for j in nfa:
            if e[j] == '\0':
                return True
            elif e[j] == '*':
                newnfa.add(j - 1)
                newnfa.add(j + 1)
            elif e[j + 1] == '*':
                newnfa.add(j)
                newnfa.add(j + 2)
            else:
                newnfa.add(j)
        nfa = newnfa
        newnfa = set()
        for j in nfa:
            if e[j] == '\0':
                return True
            elif i < len(s) and (e[j] == '.' or e[j] == s[i]):
                newnfa.add(j + 1)
        nfa = newnfa
    return False
