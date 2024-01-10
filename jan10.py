#2385. Amount of Time for Binary Tree to Be Infected

#You are given the root of a binary tree with unique values, and an integer start. 
#At minute 0, an infection starts from the node with value start.
#Each minute, a node becomes infected if:
#The node is currently uninfected.
#The node is adjacent to an infected node.
@Return the number of minutes needed for the entire tree to be infected.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def connectParent(node, parent):
            if node is None:
                return

            node.parent = parent

            connectParent(node.left, node) 
            connectParent(node.right, node)

        connectParent(root, None)

        found = None

        def findNode(node):
            if node is None:
                return
            if node.val == start:
                nonlocal found
                found = node

            findNode(node.left)
            findNode(node.right)

        findNode(root) 
        assert(found is not None)

        def findFarthest (node, previous, depth):
            farthest = 0
            for nextNode in [node. left, node.right, node.parent]:
                if nextNode is not None and nextNode != previous: 
                    farthest = max(farthest, findFarthest (nextNode, node, depth + 1) + 1) 
            return farthest
        return findFarthest (found, None, 0)
