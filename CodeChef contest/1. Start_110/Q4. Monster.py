""" 
Ben is fighting a monster with a health of H. He starts with an attack power of 1
Ben has two types of moves:

He can use a regular attack, which damages the monster by his current attack power.
After this, his attack power doubles.
He can use a special move: choose a prime number P such that ≤ P ≤ H (H being the current health of the monster), and deal P damage to the monster.
This move can be done at most once.

Note that this special move doesn't affect his attack power: it doesn't double, and remains the same.
To kill the monster, Ben must deal exactly H damage to it.
Find the minimum number of moves needed for Ben to kill the monster, or print -1 if it's impossible to kill it no matter what.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each of the next T lines contains one integer H — the initial health of monster.

Output Format
For each test case, output on a new line the minimum number of moves Ben will perform to kill the monster (if he's able to do so at all).
If he is unable to kill the monster no matter what, output 
−
1
−1 instead.

Sample 1:
Input
3
10
21
1000000

output
3
-1
15

Explanation:
Test case 1
1: Ben can do the following:

Initially, the monster has H=10 health.
Use a regular attack, with power 1. The monster's health drops to 9, and the regular attack's power increases to 2.Use a special attack with 
�
=
7
P=7. 
�
H becomes 
2
2.
Use a regular attack, with power 
2
2. The monster is defeated.
Test case 
2
2: It can be shown that no matter what sequence of moves is chosen, Ben cannot deal exactly 
21
21 damage. So, the answer is 
−
1
−1.

Test case 
3
3: There exists a sequence of 
15
15 moves that kills the monster, and it can be shown that achieving this in 
14
14 or less moves is impossible.
"""