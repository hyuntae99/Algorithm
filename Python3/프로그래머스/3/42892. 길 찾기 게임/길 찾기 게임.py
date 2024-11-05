import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, x, num):
        self.x = x
        self.num = num
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x, num):
        if not self.root:
            self.root = TreeNode(x, num)
        else:
            self._insert(self.root, x, num)

    def _insert(self, node, x, num):
        if x < node.x:
            if node.left:
                self._insert(node.left, x, num)
            else:
                node.left = TreeNode(x, num)
        else:
            if node.right:
                self._insert(node.right, x, num)
            else:
                node.right = TreeNode(x, num)

    def preorder(self, node, traversal):
        if node:
            traversal.append(node.num)
            self.preorder(node.left, traversal)
            self.preorder(node.right, traversal)

    def postorder(self, node, traversal):
        if node:
            self.postorder(node.left, traversal)
            self.postorder(node.right, traversal)
            traversal.append(node.num)

def solution(nodeinfo):
    # 노드에 번호 추가하고, y 좌표 기준으로 내림차순, x 좌표 기준으로 오름차순 정렬
    nodes = sorted([(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)], key=lambda x: (-x[1], x[0]))

    # 이진 트리 생성 및 삽입
    tree = BinaryTree()
    for x, y, num in nodes:
        tree.insert(x, num)

    # 전위 순회 및 후위 순회 결과 얻기
    preorder_result = []
    postorder_result = []
    tree.preorder(tree.root, preorder_result)
    tree.postorder(tree.root, postorder_result)

    return [preorder_result, postorder_result]
