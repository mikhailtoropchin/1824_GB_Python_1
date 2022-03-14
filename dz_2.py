from collections import deque

class Solution:
    def connect(self, root):

        cur = deque([root])
        next_n = deque()

        while any(cur):

            n = cur.popleft() # достаем текущий элемент из очереди
            if cur:
                n.next = cur[0]
            if n.left:
                next_n.append(n.left)
            if n.right:
                next_n.append(n.right)
            if not cur:
                cur, next_n = next_n, deque()

        return root
