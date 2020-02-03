


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

def findClosestValueInBst(tree,target):
    closest = float("inf")
    currentNode = tree
    
    while currentNode:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

b=BST(100)
b.insert(5)
b.insert(15)
b.insert(5)
b.insert(2)
b.insert(1)
b.insert(22)
b.insert(1)
b.insert(1)
b.insert(3)
b.insert(1)
b.insert(1)
b.insert(502)
b.insert(55000)
b.insert(204)
b.insert(205)
b.insert(207)
b.insert(206)
b.insert(208)
b.insert(203)
b.insert(-51)
b.insert(-403)
b.insert(1001)
b.insert(57)
b.insert(60)
b.insert(4500)


val = findClosestValueInBst(b, -5)
print(f'Closest value to -5 is {val}')

