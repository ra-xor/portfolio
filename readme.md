# Using Python and its data structres in VFX pipeline context

## Basics
**1. Create Node:**
-- Use it for **Singly Linked List**.
-- Create methods to append, reverse and print the list.
```mermaid
graph LR
A(((HEAD))) --Next-->
B((Node B)) --Next-->
C((Node C)) --Next-->
D(((TAIL)))
```
-- Use it for **Doubly Liked List**.
-- Create methods to append, reverse and print the list.
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
**2. Create TreeNode:**
-- Use it for a **Binary Tree**
-- Create methods to append, print and ( **place holder** )
```mermaid
graph TD
A((A)) --left--> B((B));
A((A)) --right--> C((C));
B((B)) --left--> D((D));
B((B)) --right--> E((E));
C((C)) --left--> F((F));
C((C)) --right--> G((G));
```
