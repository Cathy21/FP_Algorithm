# FP_Algorithm

## Frequent patterns found:
- {'Bread'}
- {'Milk'}
- {'Diaper'}
- {'Coke'}
- {'Beer'}
- {'Coke', 'Diaper'}
- {'Milk', 'Coke'}
- {'Milk', 'Beer'}
- {'Beer', 'Bread'}
- {'Beer', 'Diaper'}
- {'Milk', 'Bread'}
- {'Bread', 'Diaper'}
- {'Milk', 'Diaper'}
- {'Milk', 'Bread', 'Diaper'}
- {'Milk', 'Coke', 'Diaper'}
- {'Milk', 'Beer', 'Diaper'}
- {'Beer', 'Bread', 'Diaper'}

## Association Mining Rules found:

- {'Coke'} -> {'Diaper'}:           1.0
- {'Coke'} -> {'Milk'}:             1.0
- {'Coke'} -> {'Milk', 'Diaper'}:   1.0
- {'Milk', 'Coke'} -> {'Diaper'}:   1.0
- {'Milk', 'Diaper'} -> {'Coke'}:   0.67
- {'Coke', 'Diaper'} -> {'Milk'}:   1.0
- {'Beer'} -> {'Bread'}:            0.67
- {'Beer'} -> {'Bread', 'Diaper'}:  0.67
- {'Beer', 'Bread'} -> {'Diaper'}:  1.0
- {'Beer', 'Diaper'} -> {'Bread'}:  0.67
- {'Bread', 'Diaper'} -> {'Beer'}:  0.67
- {'Beer'} -> {'Milk'}:             0.67
- {'Beer'} -> {'Milk', 'Diaper'}:   0.67
- {'Milk', 'Beer'} -> {'Diaper'}:   1.0
- {'Milk', 'Diaper'} -> {'Beer'}:   0.67
- {'Beer', 'Diaper'} -> {'Milk'}:   0.67
- {'Beer'} -> {'Diaper'}:           1.0
- {'Diaper'} -> {'Beer'}:           0.75
- {'Milk'} -> {'Bread'}:            0.75
- {'Bread'} -> {'Milk'}:            0.75
- {'Bread'} -> {'Diaper'}:          0.75
- {'Diaper'} -> {'Bread'}:          0.75
- {'Milk', 'Bread'} -> {'Diaper'}:  0.67
- {'Milk', 'Diaper'} -> {'Bread'}:  0.67
- {'Bread', 'Diaper'} -> {'Milk'}:  0.67
- {'Milk'} -> {'Diaper'}:           0.75
- {'Diaper'} -> {'Milk'}:           0.75