class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadtreeNode:
    def __init__(self, bounds):
        self.bounds = bounds
        self.points = []
        self.children = [None, None, None, None]  # Four quadrants

class Quadtree:
    def __init__(self, bounds):
        self.root = QuadtreeNode(bounds)

    def insert(self, point, node=None):
        if node is None:
            node = self.root

        if len(node.points) < 4:
            node.points.append(point)
        else:
            if node.children[0] is None:
                self.split_node(node)

            for i in range(4):
                if self.is_point_in_bounds(point, node.children[i].bounds):
                    self.insert(point, node.children[i])
                    break

    def split_node(self, node):
        x = node.bounds.x
        y = node.bounds.y
        half_width = node.bounds.width / 2
        half_height = node.bounds.height / 2

        node.children[0] = QuadtreeNode(Bounds(x - half_width, y - half_height, half_width, half_height))
        node.children[1] = QuadtreeNode(Bounds(x + half_width, y - half_height, half_width, half_height))
        node.children[2] = QuadtreeNode(Bounds(x - half_width, y + half_height, half_width, half_height))
        node.children[3] = QuadtreeNode(Bounds(x + half_width, y + half_height, half_width, half_height))

        for point in node.points:
            for i in range(4):
                if self.is_point_in_bounds(point, node.children[i].bounds):
                    self.insert(point, node.children[i])
                    break

        node.points = []

    def is_point_in_bounds(self, point, bounds):
        return (point.x >= bounds.x - bounds.width and
                point.x <= bounds.x + bounds.width and
                point.y >= bounds.y - bounds.height and
                point.y <= bounds.y + bounds.height)
