from fputils import *


def fp_growth(items, min_sup, min_conf):
    freq = [1] * len(items)
    min_sup_count = len(items) * min_sup
    fp_tree, table = create_tree(items, freq, min_sup_count)
    freq_pat = []
    mine_rules(table, min_sup_count, set(), freq_pat)
    return freq_pat, get_rules(freq_pat, item_list, min_conf)


if __name__ == "__main__":
    item_list = [['Bread', 'Milk'],
                 ['Bread', 'Diaper', 'Beer', 'Eggs'],
                 ['Milk', 'Diaper', 'Beer', 'Coke'],
                 ['Bread', 'Milk', 'Diaper', 'Beer'],
                 ['Bread', 'Milk', 'Diaper', 'Coke']]
    freq_items, rules = fp_growth(item_list, min_sup=0.4, min_conf=0.6)
    print(freq_items)
    print(rules)
