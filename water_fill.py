'''
This file/module conatains fucntions related solve the 
problem of finding the amount of water retained in a platform of
specific shape and dimension
'''

import numpy as np

def CreateLevelCoords(platform,rows,columns):
	'''
	Creates a dictionary which contains
	Key   - which indicates the different height levels in the platform and
	Value - which is a list of all coordinates at that particular elevation on the platform

	@params
	platform - This is the numpy array that represents the platform
	rows     - This contains the number or rows in the platform matrix
	columns  - This contains the number of columns in the platform matrix

	returns the height:coords dictionary 'level'
	'''

	level = {} # This is the dictionary which will store the details

	# Iterate through the matrix and parse it
	for i in range(0,rows):
		for j in range(0,columns):
			# If a new level is found, then add it dictionary 'level'
			if platform[i,j] not in level: 
				level[platform[i,j]] = []
			# Add the particular coordinate location to the corresponding level entry in 'level'
			level[platform[i,j]] += [(i,j)] 
	return level 

def FloodFill(platform,i,j,rows,columns,cli=[],minLarg=float('inf'),dead=False):
	'''
	Executes the flood fill algorithm at a certain coordinates and corresponding height level

	@params
	platform - This is the numpy array that represents the platform
	i        - This contains the value row of the coordinate
	j        - This contains the value column of the coordinate
	rows     - This contains the number or rows in the platform matrix
	columns  - This contains the number of columns in the platform matrix
	cli      - This is a list of coordinates that belong the current flood fill region
	minLarge - This contains the final height that this corresponding pool should be elevated to
	dead     - This tells whether this current pool will drain out or not

	This function modifies the cli argument which is later used to deduce the coordinates of the current pool

	# returns the status of the pool, whether it will drain or not and 
	# the height to elavate it to
	'''
	cli += [(i,j)] # Adds the current proccessing coordinate to the pool
	if i==0 or i==rows-1 or j==0 or j==columns-1: # checks whether the location is an edge, if yes it will drain
		dead = True

	# This series of checks determine the minimum greatest height that it should raise this pool to
	# It does so by checking each of the surrounding block height for every block in the pool
	# and finds the smallest one that is greater than the current one
	if i<rows-1 and minLarg > platform[i+1,j] > platform[i,j]:
		minLarg = platform[i+1,j]
	if i>0 and minLarg > platform[i-1,j] > platform[i,j]:
		minLarg = platform[i-1,j]
	if j<columns-1 and minLarg > platform[i,j+1] > platform[i,j]:
		minLarg = platform[i,j+1]
	if j>0 and minLarg > platform[i,j-1] > platform[i,j]:
		minLarg = platform[i,j-1]

	# This is the flood fill checks and calls
	# it checks for boundary overflow
	# it checks if it is on same level to be able to flood
	# it checks whether the coordinate has not already been processed
	# if true recursively flood the next block
	if i<rows-1 and (platform[i+1,j] == platform[i,j]) and ((i+1,j) not in cli):
		dead,minLarg = FloodFill(platform,i+1,j,rows,columns,cli,minLarg,dead)
	if j<columns-1 and (platform[i,j+1] == platform[i,j]) and ((i,j+1) not in cli):
		dead,minLarg = FloodFill(platform,i,j+1,rows,columns,cli,minLarg,dead)
	if j>0 and (platform[i,j-1] == platform[i,j]) and ((i,j-1) not in cli):
		dead,minLarg = FloodFill(platform,i,j-1,rows,columns,cli,minLarg,dead)
	if i>0 and (platform[i-1,j] == platform[i,j]) and ((i-1,j) not in cli):
		dead,minLarg = FloodFill(platform,i-1,j,rows,columns,cli,minLarg,dead)

	return (dead,minLarg) 

def WaterStoredInPlatform(platform):
	'''
	This is the main function that should be called
	This function calculates the amount of water retained in a platform structure

	@params
	platform - A NxM numpy array that stores the elevation at each position
	
	returns the amount of water retained
	'''
	rows,columns = platform.shape # Obtaining the dimensions of the platform 
	pltCopy = platform.copy() # Creating a deep copy of the platform as it will be modified later on
	waterStored = 0 # contains the amount of water stored
	result = CreateLevelCoords(pltCopy,rows,columns) # Create the coordinate level mapped dictionary
	ky = sorted(result.keys()) # create a list of the levels and sort to be able to flood fill from ground up
	ky.pop() # remove the hieghest key as no water can be retained there
	for level in ky: # go through each of the heights in the platform
		while result[level]: # for each height flood fill all coordinates at that height
			i,j = result[level][0]	# takes on of the remaining coordinates to flood 
			wellCoords,newLevel,deadWell = [],0,0 # temporary variables to hold return values
			deadWell, newLevel = FloodFill(pltCopy,i,j,rows,columns,wellCoords) # flood fill the coordinate i,j
			# for each coordinate in the obtained pool remove the coordinate for further processing
			# and elevate each of the coordinate to new height after being flooded
			for xi,xj in wellCoords: 
				if (xi,xj) in result[level]:
					result[level].remove((xi,xj))
				pltCopy[xi,xj] = newLevel
			# if the pool is valid and will not drain then calculate and store the amount of water it holds
			waterStored += len(wellCoords)*(newLevel-level)*(not deadWell)
	return waterStored







