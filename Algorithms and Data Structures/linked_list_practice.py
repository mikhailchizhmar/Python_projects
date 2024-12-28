from linked_list import Node
from linked_list import LinkedList

N1 = Node(10)
print(N1)

N2 = Node(20)
N1.next_node = N2
print(N1.next_node)

l = LinkedList()
l.head = N1
print(l.size())

m = LinkedList()
m.add(1)
m.add(2)
m.add(3)
print(m.size())
print(m.search(2))
