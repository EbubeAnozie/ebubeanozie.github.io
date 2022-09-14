"""
SPECIFICATION

What This Program Will Do:
This program attempts to answer the following problem:
How can one easily tell that every pair of local government areas (LGAs)
in Nigeria can be travelled by road? In formal terms, write an algorithm
to identify a conected map?

What This Program Will NOT Do:
This program will not apply an algorithm based on the brute force
method because of time complexity. This is to avoid resource waste
that would result if one tries all permutations for LGAs of, say, the world.

How It Will Achieve This:
The algorithm will be designed on the principles of graph theory.
The LGAs and the roads connecting them  will be represented with
the vertices and edges of a graph respectively.
Then it will employ the principle that if one could pick up the entire graph by grabbing
just one vertex of his choice, then the graph is connected and every
pair of the LGAs can be travelled by road.

"""
