from collections import defaultdict
from collections import OrderedDict

d = defaultdict(float)  
print(d['algo'])
print(d)
defaultdict(float, {'algo': 0.0})
d = defaultdict(str)  
print(d['algo'])
print(d)


n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print(n)
OrderedDict([('uno', 'one'), ('dos', 'two'), ('tres', 'three')])
n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'
