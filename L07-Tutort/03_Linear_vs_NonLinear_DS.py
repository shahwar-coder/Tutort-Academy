'''
Q1. What is the main difference between Linear and Non-Linear data structures?
Ans:
In a Linear data structure, elements are arranged in a single line or sequence.
In a Non-Linear one, elements form a hierarchy or network, not just a straight line.
'''
# Example
# Linear → [A → B → C]
# Non-Linear → A connected to B, C, and D (like a tree)



'''
Q2. What are some common examples of Linear data structures?
Ans:
Arrays, Linked Lists, Stacks, and Queues.
These follow a one-by-one order for storing and accessing data.
'''
# Example
nums = [10, 20, 30]     # Array → Linear
# Access order: 10 → 20 → 30



'''
Q3. What are common examples of Non-Linear data structures?
Ans:
Trees and Graphs.
They allow branching paths and relationships among nodes.
'''
# Example
# A simple tree:
#        A
#       / \
#      B   C
# Here A links to both B and C → hierarchy



'''
Q4. How does traversal differ between Linear and Non-Linear structures?
Ans:
Linear → Traversed one by one (simple sequence).  
Non-Linear → Traversed through multiple possible paths (like branches or connections).
'''
# Example
# Linear:  A → B → C
# Non-Linear (tree):  Preorder, Inorder, Postorder traversals possible



'''
Q5. What type of relationship exists among elements in Linear vs Non-Linear structures?
Ans:
Linear → 1-to-1 relationship (each element linked to next one).  
Non-Linear → 1-to-many or many-to-many relationships.
'''
# Example
# Linear:  A → B → C
# Non-Linear:  A → {B, C, D}



'''
Q6. When would you prefer a Non-Linear structure over a Linear one?
Ans:
When data has hierarchical or connected relationships — like organization charts, maps, or social networks.
They model real-world relationships more efficiently than simple lists.
'''
# Example
# Family tree or graph of friends → Non-Linear
# List of student names → Linear
