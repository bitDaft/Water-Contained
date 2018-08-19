import numpy as np

from water_fill import WaterStoredInPlatform

test_case = np.array([
# test case 0 = 10
	[
	(3,5,3,3,3,3),
	(3,1,2,3,1,3),
	(3,1,2,3,1,3),
	(3,3,3,1,3,3)],
# test case 1 = 2
	[
	(2,2,2),
	(2,0,2),
	(2,2,2)],
# test case 2 = 0
	[
	(2,2,2),
	(2,0,2),
	(2,0,2)],
# test case 3 = 0
	[
	(2,2,2),
	(2,2,2),
	(2,2,2)],
# test case 4  = 0
	[
	(0,0,0),
	(0,0,0),
	(0,0,0)],
# test case 5 = 32
	[
	(5,5,5,5,5),
	(9,1,1,1,5),
	(5,1,5,1,5),
	(5,1,1,1,5),
	(5,5,5,5,5)],
# test case 6 = 4
	[
	(3,9,5,5,5),
	(3,1,3,1,5),
	(3,3,5,5,5)],
# test case 7 = 3
	[
	(3,9,5,5,5),
	(3,2,3,1,5),
	(3,3,5,5,5)],
# test case 8 = 6
	[
	(3,3,3,3,3),
	(3,1,1,1,3),
	(3,3,3,3,3)],
# test case 9 = 0
	[
	(1,2,2,2,1),
	(1,2,3,2,1),
	(1,2,2,2,1)],
# test case 10 = 2
	[
	(3,3,5,3,3),
	(3,2,5,2,3),
	(3,3,5,3,3)],
# test case 11 = 3
	[
	(3,3,5,3,5,3,3),
	(3,1,5,2,5,3,3),
	(3,3,5,3,5,3,3)],

	])


for i in range(test_case.shape[0]):
	print(str(i)+": ",WaterStoredInPlatform(np.array(test_case[i])))



