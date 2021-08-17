""" you are given three integers x,y and z  representing the dimensions of a cuboid
along with an integer n.Print a list of all possible coordinates given by (i,j,k) on
a 3D grid where the sum of (i,j,k) is not equal to n."""

# taking 3 integer inputs and a n as the sum
x,y,z,n = (int(input()) for _ in range(4))

### print ordered pairs
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n])


