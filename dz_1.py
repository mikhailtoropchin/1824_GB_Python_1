class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root) -> list:
        ans = []
        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            ans.append(node.val)

        if not root:
            return ans
        helper(root)
        return ans

tree_node_1 = TreeNode(5)
tree_node_2 = TreeNode(3, tree_node_1)
tree_node_3 = TreeNode(3)
tree_node_main = TreeNode(1, tree_node_2, tree_node_3)


sol = Solution()
print(sol.postorderTraversal(tree_node_main))

