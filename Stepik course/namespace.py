parents = {'None': ['global']}
vars_in_namespaces = {'global': []}


def get_parent(d, value):
    for parent, child in d.items():
        if value in child:
            return parent


def create(namespace, parent):
    if parent not in parents.keys():
        parents[parent] = []
    parents[parent].append(namespace)
    vars_in_namespaces[namespace] = []


def add(namespace, var):
    vars_in_namespaces[namespace].append(var)


def get(namespace, var):
    flag = False
    for lists in parents.values():
        if namespace in lists:
            flag = True
            break

    if flag:
        if var in vars_in_namespaces[namespace]:
            return namespace
        else:
            c = get_parent(parents, namespace)
            if c == 'None':
                return 'None'
            return get(c, var)
    else:
        return 'None'


n = int(input())

for i in range(n):
    s = input().split()
    if s[0] == 'create':
        create(s[1], s[2])
    if s[0] == 'add':
        add(s[1], s[2])
    if s[0] == 'get':
        # get(s[1], s[2])
        print(get(s[1], s[2]))

print(parents.values())
print(parents)
print(vars_in_namespaces)
