####################################
# AVL Tree: Very similar to Binary Search Tree
# Nodes < root will go to the left and > root will go to the right
# Guarantees O(logN) complexity for all scenarios as it checks at each step,if the tree
#is unbalanced.If it is, than makes certain rotations in the tree to first make it balanced.

# Whether a tree is balanced or not is calc using the height parameter of a specific node
# Height of a node = max(height of left child, height of right child) + 1

# Tree is balanced as long as height of left subtree - height of right subtree <= 1, otherwise its unbalanced
# and we need to make certain rotations for it to adhere the above condition.

#Changes that happen on specific rotations:
#Right rotation-> Current root's left child becomes new root. New root's right child becomes current root's left child.
#Left rotation-> Current root's right child becomes new root. New root's left child becomes current root's right child.
#####################################
