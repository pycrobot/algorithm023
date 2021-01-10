class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """递归中序遍历"""
        result_list = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result_list.append(root.val)
            inorder(root.right)
        inorder(root)
        return result_list
