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
	import cv2

	SavArr = [[-1 for n in range(len(img[0]))] for n in range(len(img))]
	Gradient = [[0 for n in range(len(img[0]))] for n in range(len(img))]

	#Get Gradient
	img1 = cv2.Sobel(img, cv2.CV_16S, 1, 0)
	img2 = cv2.Sobel(img, cv2.CV_16S, 0, 1)

	for i in range(0, len(img1)):
		for j in range(0, len(img1[i])):
			Gradient[i][j] = math.sqrt(pow(img1[i][j], 2)+pow(img2[i][j], 2))

	Label = -1
	TobBlock = []
	#MainLoop
	for i in range(0, len(SavArr)):
		for j in range(0, len(SavArr[i])):
			print("TobBlock = " + str(Label), end = "\r")
			if SavArr[i][j] != -1:
				continue

			Stack = [[i, j]]
			ImaLabel = 0
			while 1:
				Neigh = []
				for p in range(-1, 2):
					for q in range(-1, 2):
						if p == 0 and q == 0:
							continue
						LocX = i + p
						LocY = j + q
						if LocX < 0 or LocY < 0 or LocX > len(SavArr) - 1 or LocY > len(SavArr[0]) - 1:
							continue
						else:
							Neigh.append([Gradient[LocX][LocY], LocX, LocY])

				Neigh.sort()
				#print(Neigh)
				if SavArr[Neigh[0][1]][Neigh[0][2]] != -1:
					ImaLabel = SavArr[Neigh[0][1]][Neigh[0][2]]
					break

				if Neigh[0][1] != Stack[len(Stack) - 1][0] and Neigh[0][2] != Stack[len(Stack) - 1][1]:
					Stack.append([Neigh[0][1], Neigh[0][2]])
				else:
					TobBlock.append([-1, 0, 0, 0, 0])
					Label += 1
					ImaLabel = Label
					break


			while len(Stack) != 0:
				LocX = Stack[len(Stack) - 1][0]
				LocY = Stack[len(Stack) - 1][1]
				Grey = img[LocX][LocY]
				Stack.pop()
				SavArr[LocX][LocY] = ImaLabel
				TobBlock[ImaLabel][1] += Grey
				TobBlock[ImaLabel][2] += LocX
				TobBlock[ImaLabel][3] += LocY
				TobBlock[ImaLabel][4] += 1
	
	print("TobBlock = " + str(Label), end = "\n")
	
	for i in range(1, len(TobBlock)):
		TobBlock[i][1] /= TobBlock[i][4]
		TobBlock[i][2] /= TobBlock[i][4]
		TobBlock[i][3] /= TobBlock[i][4]


	return [SavArr, TobBlock]
