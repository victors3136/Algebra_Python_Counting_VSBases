# Linear Algebra - Counting Vector Space Bases with Python 
Small python script that generates and counts the number of bases for vector spaces of (Z_2)^n for different 'n's. Made as an extra project for my Linear Algebra Course during my first semester of univeristy
# Problem Statement
For a given n, if n <= 4, write all the possible basses of the (Z_2)^n vector space over Z_2. If n > 4, write the number of bases.
# Approach
This approach uses backtracking and the fact that any number <= 2^n can be written as a series of bits, which in turn can be interpreted as vectors belonging to (Z_2)^n.  
We use a simple backtracking algorithm to generate lists of n numbers smaller or equal to 2^n and while checking their linear independence using the bitwise xor operator, which describes Z_2 addition better than + does.  
The formula for the actual number of bases when the numbers get higher than 4 is  
N = ∏(of k=1,n) ​(2^n−2^(k−1)) = ∏(of k=0,n-1) ​(2^n−2^k)  
The actual proof by induction is included in a handwritten pdf file in this project.
# Output
![image](https://github.com/victors3136/Algebra_Python_Counting_VSBases/assets/115093754/9266a4f0-65dd-4550-a9ec-1eadbe4e0755)
![image](https://github.com/victors3136/Algebra_Python_Counting_VSBases/assets/115093754/055ba46c-5228-48f4-8e7f-28d9eba2dc8c)

# Acknowledgements
This project was accomplished with the knowledge I gained during the Linear Algebra course taught by Professor Septimiu Crivei, Fundamentals of Programming course taught by Professor Arthur Molnar, Computational Logic course taught by Professor Mihaiela Lupea and Computer Systems Architecture course taught by Porfessor Alexandru Vancea as part of the Bachelors Degree of Computer Science at Babes Bolyai University. It was a great opportunity to use all the different subjects I learned over the previous months in a single project.
