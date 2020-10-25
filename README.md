# Given  a  8  pint  Jug  full  of  water  and  two  Empty  jugs  of  5  and  3  pint  capacity , get  exactly  4  pints  of  water  in  one  of  the  jugs  by  completely  filling  up  and/or  emptying  jugs  into  another.
### Naive Brute force algorithm

Brute Force Algorithms are exactly what they sound like – straightforward methods of solving a problem that rely on sheer computing power and trying every possibility rather than advanced techniques to improve efficiency. This method is easier to implement because of its simplicity.
It is a layman approach of writing the code for any problem. 

In our example, we pour the contents from one jug to another and try to obtain 4 pint water by hit and trial method. Obviously there are many combinations possible so this method is very tedious and not reliable for larger sample size.

Advantages
•	can be applied to a variety of problems.
•	simple to interpret.
•	can be used to judge more efficient approaches to solve a problem.

Disadvantages
•	may not be efficient .
•	slow

### Depth first search algorithm(DFS)

Depth-First processes all children (choices) of a node before considering any siblings (at the same depth). It is similar to Breadth first search(BFS), but instead of a queue we use a stack. Depth-First Search can easily be described recursively, which is why we have used a recursive function to get our desired solution.



Depth first search characteristics

• No need to keep track of a large list of states. 
• May find a solution very fast (and might not).
• “Pruning” is possible – example: branch-and-bound 
• Can easily get caught in loops.

All these information is available on internet :)
