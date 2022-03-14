
def lowestCommonAncestor(self, root, p, q):
    if not root:
        return None

    if root.val == p.val or root.val == q.val: # ищем значение, равное p или q
        return root

    left = self.lowestCommonAncestor(root.left, p, q) # рекурсивно заходим в левого ребенка
    right = self.lowestCommonAncestor(root.right, p, q) # рекурсивно заходим в правого ребенка, ищем там

    if left and right: # если и слева и справа есть искомое, значит root - общий минимум
        return root
    elif left: # если только слева есть искомое, значит нужный нам родитель - это верхнее левое значение
        return left
    elif right: # наоборот
        return right
    else: # если нет искомых нигде
        return None

