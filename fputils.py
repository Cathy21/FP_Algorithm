from collections import *
from itertools import *


class Node:
    def __init__(self, item, sup, parent):
        self.item = item
        self.sup = sup
        self.parent = parent
        self.children = {}
        self.next = None


def create_tree(items, sup, min_sup_count):
    fp_tree = Node('', 1, None)
    table = defaultdict(int)

    for i, item in enumerate(items):
        for it in item:
            table[it] += sup[i]

    table = dict((item, sup) for item, sup in table.items() if sup >= min_sup_count)

    if len(table) == 0:
        return None, None

    for item in table:
        table[item] = [table[item], None]

    for i, item in enumerate(items):
        item = [it for it in item if it in table]
        item.sort(key=lambda j: table[j][0], reverse=True)
        currentNode = fp_tree
        for it in item:
            currentNode = update_tree(it, currentNode, table, sup[i])

    return fp_tree, table


def update_tree(child, node, table, sup):
    if child in node.children:
        node.children[child].sup += sup
    else:
        node.children[child] = Node(child, sup, node)
        update_table(child, node.children[child], table)

    return node.children[child]


def update_table(item, new_item, table):
    if table[item][1] is None:
        table[item][1] = new_item
    else:
        current = table[item][1]
        while current.next is not None:
            current = current.next
        current.next = new_item


def ascend(node, path):
    if node.parent is not None:
        path.append(node.item)
        ascend(node.parent, path)


def find_path(pat, table):
    node = table[pat][1]
    patterns = []
    sup = []
    while node is not None:
        path = []
        ascend(node, path)
        if len(path) > 1:
            patterns.append(path[1:])
            sup.append(node.sup)
        node = node.next
    return patterns, sup


def mine_rules(table, min_sup_count, freq_set, freq_items):
    sorted_list = [item[0] for item in sorted(list(table.items()), key=lambda p: p[1][0])]
    for item in sorted_list:
        new_freq = freq_set.copy()
        new_freq.add(item)
        freq_items.append(new_freq)
        cond_pattern_base, frequency = find_path(item, table)
        cond_tree, f_table = create_tree(cond_pattern_base, frequency, min_sup_count)
        if f_table is not None:
            mine_rules(f_table, min_sup_count, new_freq, freq_items)


def get_rules(freq_items, items, min_conf):
    rules = []
    for item in freq_items:
        it = chain.from_iterable(combinations(item, i) for i in range(1, len(item)))
        sup = get_num(item, items)
        for i in it:
            if float(sup / get_num(i, items)) > min_conf:
                rules.append([set(i), set(item.difference(i)), float(sup / get_num(i, items))])
    return rules


def get_num(item, items):
    num = 0
    for it in items:
        if set(item).issubset(it):
            num += 1
    return num
