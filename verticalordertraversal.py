"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

"""
#Time: O(n) n:no.of nodes, space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q= deque()
        colIdx= deque()
        if root:
            q.append(root)
            colIdx.append(0)
        h= {}
        nodeList= []
        result=[]
        mini= 200
        maxi= -200
     
        while q:
            size=len(q)
            for i in range(size):
                newroot= q.popleft()
               
                col= colIdx.popleft()
                mini= min(mini, col)
                maxi= max(maxi,col)
                if col not in h:
                    h[col]= []    
                h[col].append(newroot.val)
                
                if newroot.left:
                    q.append(newroot.left)
                    colIdx.append(col-1)
                if newroot.right:
                    q.append(newroot.right)
                    colIdx.append(col+1)
        for i in range(mini,maxi+1):
            if i in h:
                result.append(h[i])
        return result
                    
                    