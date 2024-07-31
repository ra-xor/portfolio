# Using Python and its data structres in VFX pipeline context

## Basics
- Create Node:
-- Use it for **Singly Linked List**
```mermaid
graph LR
A(((HEAD))) --Next-->
B((Node B)) --Next-->
C((Node C)) --Next-->
D(((TAIL)))
```
-- Use it for **Doubly Liked List**
```mermaid
graph LR
A((Node A)) --Next-->
B((Node B)) --Next-->
C((Node C)) --Next-->
D((Node D))
B --Prev--> A
C --Prev--> B
D --Prev--> C
```
- Create TreeNode:
-- Use it for a **Binary Tree**
```mermaid
graph TD
A((A)) --left--> B((B));
A((A)) --right--> C((C));
B((B)) --left--> D((D));
B((B)) --right--> E((E));
C((C)) --left--> F((F));
C((C)) --right--> G((G));
```
