"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy=Node(-1)
        node=head
        copyNode=dummy
        nodeList=[]
        nodeMap={}
        i=0
        while node:
            val=node.val
            random= node.random

            nodeMap[node]=i
            i+=1

            copyNode.next=Node(val)
            copyNode=copyNode.next
            nodeList.append([val, random, copyNode])
            node=node.next

        # print(nodeList)
        # print(nodeMap)

        copyNode=dummy.next
        i=0

        while i<len(nodeList):
            randomIndex=nodeMap[nodeList[i][1]] if nodeList[i][1] else -1
            randomNode=nodeList[randomIndex][2] if randomIndex!=-1 else None
            # print(f"i:{i}, val: {copyNode.val}, randomIndex: {randomIndex}, randomNode: {randomNode}")
            copyNode.random=randomNode
            copyNode=copyNode.next
            i+=1        


        return dummy.next