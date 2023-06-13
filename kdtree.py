class KdTreeNode:
    def __init__(self, point, depth):
        self.point = point
        self.left = None
        self.right = None
        self.depth = depth

class KdTree:
    def __init__(self, points):
        self.root = self.construct_kd_tree(points, depth=0)

    def construct_kd_tree(self, points, depth):
        if not points:
            return None

        k = len(points[0])
        axis = depth % k
        sorted_points = sorted(points, key=lambda point: point[axis])
        median_index = len(sorted_points) // 2

        node = KdTreeNode(sorted_points[median_index], depth)
        node.left = self.construct_kd_tree(sorted_points[:median_index], depth + 1)
        node.right = self.construct_kd_tree(sorted_points[median_index + 1:], depth + 1)

        return node

    def insert(self, point):
        node = self.root
        depth = 0

        while node:
            if point == node.point:
                return  # Avoid duplicate points

            axis = depth % len(point)
            if point[axis] < node.point[axis]:
                if node.left:
                    node = node.left
                else:
                    node.left = KdTreeNode(point, depth + 1)
                    return
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = KdTreeNode(point, depth + 1)
                    return
            depth += 1

    def search(self, target, node=None, depth=0):
        if node is None:
            node = self.root

        if node.point == target:
            return node.point

        axis = depth % len(target)
        if target[axis] < node.point[axis]:
            if node.left:
                return self.search(target, node.left, depth + 1)
        else:
            if node.right:
                return self.search(target, node.right, depth + 1)
        
        return None
               
