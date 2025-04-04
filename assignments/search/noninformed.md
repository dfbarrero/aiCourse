# 8-queens with non-informed search

## Preliminary steps

The 4-queens puzzle is the problem of placing four chess queens on an 4×4 chessboard so that no two queens threaten each other. A solution requires that no two queens are placed on the same row, column, or diagonal. The 4-queens puzzle is a sub-problem of the more general n queens problem of placing n non-attacking queens on an n×n chessboard. There are no solutions when n=2 or n=3, so n=4 it is first problem where you can find a solution.

Check the following link to see how to find a solution to the 4-queens problem:

https://acrogenesis.com/or-tools/documentation/user_manual/manual/introduction/4queens.html#see-what-n-queens-problem-really-is

## The 8-queens problem

It is a generalization of the 4-queen problem but in this case we need to place 8-queens instead of 4. It has only 12 solutions (not counting as solutions the symmetry operations of rotation and reflection of the board. If we do, then there are 92 distinct solutions). 

There are at least two different problems when we talk about the n-Queens Problem:
- Finding one solution.
- Counting the number of solutions and finding (explicitly) all the solutions.

The first one is easier than the second one!!

The problem can be solved at least by two search strategy aproaches:
1) Incrementally, that is, we start by an empty tree node and gradually we add nodes to the tree to comply to the imposed constraints.
2) Iterative repairing, that is, we start with all queens on the board and then try to count the number of conflicts (attacks), and try to improve the placement of the queens.

Based on these considerations, implement the 8-queens problem using:

- A programming language such as Python (or any other of your election)  
- A tree-based representation.
- You can provide 1 solution or all of them.
- You can use an incremental approach or a repairing one. 

However, the search has to be uninformed using any of the algorithms explained in the class. Using a tree-based representation you will be able to integrate any kind of search algorithm for solving your problem. You can also increment or decrement the number of queens. Try to parametrize the problem as much as possible.

## The 8-puzzle problem
If the 8-queen problem does not appeal you much, you can insead try to solve the 8-puzzle problem. In this case we have a square board with 9 positions, filled by 8 numbered tiles and one gap. At any point, a tile adjacent to the gap can be moved into the gap, creating a new gap position. In other words the gap can be swapped with an adjacent (horizontally and vertically) tile. The objective in the game is to begin with an arbitrary configuration of tiles, and move them so as to get the numbered tiles arranged in ascending order either running around the perimeter of the board or ordered from left to right, with 1 in the top left-hand position. You can read more in:

http://www.aiai.ed.ac.uk/~gwickler/eightpuzzle-uninf.html

In this case, you only need to provide one solution and it will be incremental. Again, using a tree-based representation will help to use any type of search and practice AI!!
