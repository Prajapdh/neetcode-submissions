class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.prev = self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}   #key-> key, value-> pointer to the node
        # Creating a doubly linked list
        # Left most is the LRU, Right is most recent
        self.left, self.right = Node(-1,-1), Node(-1,-1)
        self.left.next, self.right.prev = self.right, self.left

    # Insert the given node to the right
    def insert(self, node):
        first, right = self.right.prev, self.right
        first.next = node
        node.prev = first
        right.prev = node
        node.next = right
    
    # remove reference of provided node from the list
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        #remove and insert node to the right
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # remove the node with old value(if present) and insert the new node with updated value
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key, value)
        self.insert(self.cache[key])
        
        # remove the LRU node if full size reached
        if len(self.cache)>self.cap:
            lruNode = self.left.next
            lruKey = lruNode.key
            self.remove(lruNode)
            del self.cache[lruKey]
        
        
