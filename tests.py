import heapq
import uuid
import numpy as np

# import matplotlib.pyplot as plt

from linked_list import LinkedList
from dbllkd_list import DoublyLinkedList
from stack import Stack
from queue import Queue
from hashmap import HashMap
from bnsrchtr import BinarySearchTree
from heap import MinHeap
from trie import Trie
from graph import Graph

def lnkdlst_test():
    ls = [10, 5, 18, 22, 29]
    ll = LinkedList()

    for e in ls:
        ll.append(e)

    ll.prepend(100)
    ll.insert(200, 1)

    print(ll)

    ll.delete(18)

    print(ll)

    ll.pop(1)

    print(ll)

    print(ll.get(1))
    print(29 in ll)
    print(800 in ll)
    print(f'Length: {len(ll)}')

def dbllkdlst_test():
    ll = DoublyLinkedList()

    ll.append(10)

    ls = [5, 20, 18, 22, 88, 97]
    for l in ls:
        ll.insert(l, 1)

    ll.prepend(100)
    ll.insert(200, 1)

    ll.delete(18)
    ll.delete(22)
    ll.delete(5)

    ll.pop(1)

    print(ll)

    print(ll.get(1))
    print(29 in ll)
    print(800 in ll)
    print(f'Length: {len(ll)}')

def stack_test():
     stack = Stack()
     slist = [10, 14, 16, 6, 12]

     for s in slist:
         stack.push(s)

     print(stack)
     print(f'Peek-a-boo, I see you: {stack.peek()}')

     print("Popcorn popping on the apricot tree! :D")
     while stack.is_empty() == False:
         print(stack.pop())
         print(stack)

     print(f'Is the stack empty? {stack.is_empty()}')

def queue_test():
    queue = Queue()

    qlist = list(range(10, 61, 10))

    for q in qlist:
        queue.enqueue(q)
    print(f'Queue: {queue} Length: {len(queue)}')
    print("\nDequeue:")
    while queue.is_empty() == False:
        queue.dequeue()
        print(f'Dequeue: {queue} Length: {len(queue)}')

def hashmap_01_test():
    hash_map = HashMap(32)

    hash_map.put('name', 'Mike')
    hash_map.put('age', 30)
    hash_map.put('job', 'Programmer')

    print(hash_map.items())
    print(hash_map.buckets)

    print(hash_map.items())

# def hashmap_02_test():
#     hash_map = HashMap(100)
# 
#     for _ in range(1000):
#         hash_map.put(uuid.uuid4(), 'some_value')
# 
#     X = []
#     y = []
# 
#     for i, bucket in enumerate(hash_map.buckets):
#         X.append(i)
#         y.append(len(bucket))
# 
#     plt.bar(X, y)
#     plt.show()

def bnsrtre_test():
    bst = BinarySearchTree()

    bsl = [10, 5, 22, 2, 9, 12, 30, 11, 15, 30, 23, 35]
    for b in bsl:
        bst.insert(b, 'x')

    for i in bst.traverse('inorder'):
        print(i)
    print('-'*15)
    for i in bst.traverse('preorder'):
        print(i)

def heap_test():
    min_heap = MinHeap()
    min_heap.heapify([[10, '10'], [9, '9'], [8, '8'], [7, '7'], [6, '6'], [5, '5'], [4, '4'], [3, '3'], [2, '2'], [1, '1']])
    print(min_heap)

    mylist = list(range(1, 11)[::-1])
    heapq.heapify(mylist)
    print(mylist)

    print(min_heap.extract_min())
    print(min_heap.extract_min())
    print(min_heap.extract_min())

    print(heapq.heappop(mylist))
    print(heapq.heappop(mylist))
    print(heapq.heappop(mylist))

    min_heap.insert(2, '2')
    print(min_heap)

    heapq.heappush(mylist, 2)
    print(mylist)

    min_heap2 = MinHeap()
    min_heap2.heapify([[5, '5'], [7, '7'], [2, '2']])
    min_heap.meld(min_heap2)
    print(min_heap)

def trie_test():
    trie = Trie()

    words = ['hello', 'henry', 'mike', 'minimal', 'minimum']

    for word in words:
        trie.insert(word)

    print(trie.list_words())
    print(trie.has_prefix('mi'))
    print(trie.starts_with('mi'))
    trie.delete('minimal')
    print(trie.starts_with('mi'))

    print(trie.search('minimum'))
    print(trie.search('minimal'))
    print(trie.search('mini'))

    trie.insert('mini')
    print(trie.starts_with('mi'))

def graph_test():
    g = Graph(directed=True)

    ltrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for l in ltrs:
        g.add_node(l)

    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 10)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 1)
    g.add_edge('D', 'C', 1)
    g.add_edge('A', 'E', 1)
    g.add_edge('E', 'F', 1)
    g.add_edge('G', 'F', 1)
    g.add_edge('F', 'H', 1)
    g.add_edge('H', 'I', 1)
    g.add_edge('I', 'G', 100)

    print(g)

    print(np.array(g.to_adj_matrix()))

    print(f'BFS from A: {g.bfs("A")}')
    print(f'DFS from A: {g.dfs("A")}')
    print(f'Dijkstra from A: {g.dijkstra("A")}')
    print(f'Shortest Path from A --> C: {g.shortest_path("A", "C")}')

# lnkdlst_test()
# dbllkdlst_test()
# stack_test()
# queue_test()
# hashmap_01_test()
# hashmap_02_test()
# bnsrtre_test()
# heap_test()
# trie_test()
graph_test()