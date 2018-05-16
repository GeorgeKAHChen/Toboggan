############################################################
#
#		Toboggan Image Segmentation Algorithm
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Algorithm.py
#
############################################################

"""
		FUNCTION INSTRUCTION
		
Toboggan(img)
	Main toboggan algorithm

	img = array of image need processing

	return TobImg (the value for every pixel which toboggan block the belong to
		   TobBlock (The infomation for every toboggan block, include
				[LocX (center Location X), 
				 LocT (center Location Y), 
				 Gery (ave grey), 
				 Value of pixel (the total number of pixel)])

"""

def Toboggan(img):
