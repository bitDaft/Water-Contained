# Water-Contained
Calculate the amount of water retained in NxM platform of specific shape.

There is a partially constructed platform made of cubes. The platform can be represented in a 2-D array 
with each element representing the number of cubes in the respective position.

The way the platform is piled up, is given by a NxM matrix, where each element says how many cubes are stavked upwards in that position.

This python scripts calculates the amount water retained in the platform if an infinite amount of water was poured on it.

# Examples
A 3x3 matrix like following:

[2 2 2]

[2 2 2]

[2 2 2]

indicates a cuboid 3x3x2 area unit, and it can retain 0 water units

[2 2 2]

[2 1 2]

[2 2 2]

indicates a cuboid 3x3x2 area unit, and it can retain 1 water units
if the center was 0 instead of 1, it would retain 2 units if water

Consider the following matrix:

[3 5 3 3 3 3]

[3 1 2 3 1 3]

[3 1 2 3 1 3]

[3 3 3 1 3 3]

Notice that the there is a 1 level on the edge but it cannot retain any water as it will drain over the edge.
The areas that can retain water although diagonal to the draining block at bottom row, does not drain it, as water cannot drain diagonally. Although the highest position is the 5, this platform can only retain water till a height of 3 blocks, as ay higher will cause it to flow out the edges.
This platform can retain a total amount of 10 units of water.(4+2+4 for the 3 columns that can retain water)  

[5 5 5 5 5]

[9 1 1 1 5]

[5 1 5 1 5]

[5 1 1 1 5]

[5 5 5 5 5]

The above platform can retain upto 32 block of water.(12+8+12 for the 3 columns that can retain water)
 
