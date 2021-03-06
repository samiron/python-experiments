import sys
import fileinput


class Node:
    def __init__(self, number):
        self.value = number
        self.color = None
        self.neighbors = []

    def add_neighbor(self, other_node):
        self.neighbors.append(other_node)


class Edge:
    def __init__(self, left, right):
        assert left is not None
        assert right is not None
        self.left_node = left
        self.right_node = right


class Tree:
    """
    A data structurally simpler approach would be like this
    Tree:
        3
        1 2
        2 3
        1 3 2
        
    Edges:
        all_edges= [
            [1, 2],
            [2, 3]
        ]
    Nodes:
        value => [color, [all_neighbors]]
        all_nodes = {
            1 => [1, [2]],
            2 => [3, [1,3]],
            3 => [2, [2]]
        }
    However, this class based Node and Edge approach seems more cleaner
    """
    def __init__(self, total_count):
        self.max_nodes = total_count
        self.all_edges = []
        self.all_nodes = [None] * total_count
        self.vertex_in_hand = None

    def register_node(self, number):
        if self.all_nodes[number-1] is not None:
            return self.all_nodes[number-1]
        n = self.all_nodes[number-1] = Node(number)
        return n

    def register_edge(self, node_num_1, node_num_2):
        n1 = self.register_node(node_num_1)
        n2 = self.register_node(node_num_2)
        e = Edge(n1, n2)
        self.all_edges.append(e)
        n1.add_neighbor(n2)
        n2.add_neighbor(n1)

    def add_node_color(self, node_num, color):
        self.all_nodes[node_num-1].color = color

    def log(self):
        print "Log by edges:"
        for e in self.all_edges:
            print "%s (color: %s) -> %s (color %s)" % (e.left_node.value, e.left_node.color, e.right_node.value, e.right_node.color)

        print "Log by nodes:"
        for n in self.all_nodes:
            print "Node %s" % n.value
            for nn in n.neighbors:
                print "    Edge with %s:" % nn.value


def build_tree_from_input(vertices):
    global INH
    tree = Tree(vertices)
    for i in range(1, vertices):
        (x, y) = INH.readline().split()
        x = int(x)
        y = int(y)
        tree.register_edge(x, y)

    colors = INH.readline().split()
    for i in range(0, vertices):
        tree.add_node_color(i+1, colors[i])
    tree.all_colors = colors
    return tree


def _if_multicolor_subtree(color, stack, subtree_root):
    multicolor = False
    visited = {}
    while len(stack) > 0:
        n = stack.pop()
        if n.color != color:
            multicolor = True
            break
        visited[n.value] = True
        for ngh in n.neighbors:
            if not visited.get(ngh.value, False) and subtree_root.value != ngh.value:
                stack.append(ngh)

    return multicolor


def _is_valid_root(possible_root):
    valid = True
    for neighbor in possible_root.neighbors:
        stack = [neighbor]
        if _if_multicolor_subtree(neighbor.color, stack, possible_root):
            valid = False
            break
    return valid


def process(n):
    vertices = int(n)
    tree = build_tree_from_input(vertices)

    mono_colored = True
    multi_color_edge = None
    for e in tree.all_edges:
        if e.left_node.color != e.right_node.color:
            mono_colored = False
            multi_color_edge = e
            break

    if mono_colored:
        tree.vertex_in_hand = tree.all_nodes[0]
    else:
        assert multi_color_edge is not None
        for n in [multi_color_edge.left_node, multi_color_edge.right_node]:
            if _is_valid_root(n):
                tree.vertex_in_hand = n
                break

    _print(tree)


def _print(tree):
    if tree.vertex_in_hand is not None:
        print "YES"
        print tree.vertex_in_hand.value
    else:
        print "NO"

##################
#   Main parts   #
##################
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

INH = fileinput.FileInput(files=INPUT)
l1 = INH.readline()
while l1:
    process(l1)
    l1 = INH.readline()

INH.close()
