from binaryTree import Tree

tree_instance = Tree()

tree_instance.insert('a', None)
tree_instance.insert('b', 'a')
tree_instance.insert('c', 'a')
tree_instance.insert('a', 'a')
tree_instance.show_list()