class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isSymmetric(self, root) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root, root)


    # напечатал значения для визуализации
    # def print_tree(self, root):
    #     def helper(node):
    #         print(node.val)
    #         if node.left:
    #             helper(node.left)
    #         if node.right:
    #             helper(node.right)
    #
    #     if not root:
    #         print("Пустое дерево")
    #
    #     helper(root)


tree_node_1 = TreeNode(5)
tree_node_2 = TreeNode(3, tree_node_1, tree_node_1)

tree_node_main = TreeNode(1, tree_node_2, tree_node_2)


sol = Solution()
print(sol.isSymmetric(tree_node_main))
# sol.print_tree(tree_node_main)

