from binaryTree import binary_search_tree

inst_binary_tree = binary_search_tree()

inst_binary_tree.insert(12)
inst_binary_tree.insert(-10)
inst_binary_tree.insert(-13)
inst_binary_tree.insert(20)

inst_binary_tree.breadth_first_search()
inst_binary_tree.preorder()
inst_binary_tree.postorder()
inst_binary_tree.inorder()

#inst_binary_tree.find(12)
#inst_binary_tree.find(45)