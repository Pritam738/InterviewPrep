##Trees are linear data structures, trees are hierarchical data structures.

##Tree Vocabulary: 
	The topmost node is called root of the tree.
	Elements that are directly under an element are called its children.
	The element directly above something is called its parent

      tree
      ----
       1    <-- root
     /   \
    2      3  
  /   \      \
 4     5     6    <-- leaves 
 
 ## horizontal tree traversing 
 # Tree Traversals (Inorder, Preorder and Postorder)

	(a) Inorder (Left, Root, Right) : 4 2 5 1 3 6
	(b) Preorder (Root, Left, Right) : 1 2 4 5 3 6
	(c) Postorder (Left, Right, Root) : 4 5 2 6 3 1 

 # Clockwise Spiral Traversal of Binary Tree

 	              tree
		      ----
		       1    <-- root
		     /    \
		    2       3  
		  /   \    /  \
		 4     5  6     7    <-- leaves 
	the circular clockwise spiral order traversal will be 1 7 6 5 4 2 3 

	eg:
	                    10
                     /     \
                   12       13
                          /     \
                       14       15
                      /   \     /  \
                     21   22   23   24
        res: 10 24 23 22 21 12 13 14 15

 ##verticle order taversing 
 #level order traversing 
     	               
     	               10
                     /     \
                   12       13
                          /     \
                       14       15
                      /   \     /  \
                     21   22   23   24

        top to bottom left to right 12 12 13 14 15 21 22 23 24

 #bottom view of the binary tree
    hd horizontal distance; left <- parent hd - 1; right <- parent hd + 1
    use level order traversing for table creation pick up the last values of the hash table 

                       hd = 0
       	               10
                     /     \
             hd=-1  12       13 hd=1
                          /     \
               hd=0    14       15 hd=2
                      /   \     /  \
          	hd=-1   21   22   23   24  hd=3
          			    hd=1  hd=1
    -1 | 12 21
     0 | 10 14
     1 | 13 22 23
     2 | 15
     3 | 24

      21 14 23 15 24     

 # Binary Tree:
 	A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

	First Simple Tree
		# Python program to introduce Binary Tree 
		# A class that represents an individual node in a 
		# Binary Tree 
		class Node: 
		    def __init__(self,key): 
		        self.left = None
		        self.right = None
		        self.val = key 
		  
		  
		# create root 
		root = Node(1) 
		''' 
			following is the tree after above statement 
			        1 
			      /   \ 
			     None  None
		'''
		  
		root.left      = Node(2); 
		root.right     = Node(3); 
		    
		''' 
			2 and 3 become left and right children of 1 
			           1 
			         /   \ 
			        2      3 
			     /    \    /  \ 
			   None None None None'''
			  
			  
			root.left.left  = Node(4); 
		'''
			4 becomes left child of 2 
			           1 
			       /       \ 
			      2          3 
			    /   \       /  \ 
			   4    None  None  None 
			  /  \ 
			None None 
		'''

##Properties of Binary Tree.
	The maximum number of nodes at level ‘l’ of a binary tree is 2l.
	Maximum number of nodes in a binary tree of height ‘h’ is 2h – 1.

##The following are common types of Binary Trees.
	Full Binary Tree A Binary Tree is a full binary tree if every node has 0 or 2 children
        Complete Binary Tree: A Binary Tree is a complete Binary Tree if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible
	Perfect Binary Tree A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level.
	Binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes.
	Degenerate (or pathological) tree A Tree where every internal node has one child. Such trees are performance-wise same as linked list.
