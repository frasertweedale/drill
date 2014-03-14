import trie


def add_spaces(s, all_words):
    all_words_trie = trie.RWayTrie()
    for word in all_words:
        all_words_trie.put(word, 1)
    branches = [['']]
    for c in s:
        branches_to_delete = []
        for i in xrange(len(branches)):
            branch = branches[i]
            branch[-1] += c
            if branch[-1] in all_words_trie:
                if all_words_trie.prefix(branch[-1]):
                    branches.append(list(branch))
                branch.append('')
            elif not all_words_trie.prefix(branch[-1]):
                branches_to_delete.append(i)
        while branches_to_delete:
            branches.pop(branches_to_delete.pop())
    return ' '.join(branches[0][:-1]) if branches else None
