from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        tracker=dict()

        def treeIter(node,level):

            if node==None:
                return

            if level in tracker:
                tracker[level]+=node.val
            else:
                tracker[level] = node.val
            treeIter(node.right,level+1)
            treeIter(node.left,level+1)

        treeIter(root,0)
        result = sorted(tracker.values(),reverse=True)
        print(result)
        if k>len(tracker):
            return -1
        else:
            return result[k-1]

