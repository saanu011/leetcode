# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        a = TreeNode(root.val)
        def getAllValues(root):
            ls = []
            q = [root]
            while len(q)>0:
                a = q.pop(0)
                ls.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.left is None:
                    continue
                if a.right:
                    q.append(a.right)
            return ls

        def helper(node, val):
            if val is None:
                return
            queue = []
            while len(queue)>0:
                a = queue.pop(0)
                if a.left:
                    queue.append(a.left)
                else:
                    a.left = val
                    return
                if a.right:
                    queue.append(a.right)
                else:
                    a.right = val
                    return
        ls = getAllVal(root)
        length = len(ls)
        if length>0:
            a = TreeNode(ls[0])
            i = 1
            q = [a]
            while i < length:
                x = q.pop(0)
                x.left = TreeNode(ls[i])
                i += 1
                q.append(x.left)
                if i<length:
                    x.right = TreeNode(ls[i])
                    q.append(x.right)
                    i += 1
            self.root = a
        else:
            self.root = root

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        ans = [0]
        root = self.root
        def helper(node, val):
            if node is None:
                return
            ls = []
            ls.append(node)
            while len(ls)>0:
                a = ls.pop(0)
                if a.left is not None:
                    ls.append(a.left)
                else:
                    a.left = val
                    ans[0] = a.val
                    return
                if a.right is not None:
                    ls.append(a.right)
                else:
                    a.right = val
                    ans[0] = a.val
                    return
        if self.root is not None:
            helper(self.root, TreeNode(val))
            
        return ans[0]

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()