import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import numpy 
from PIL import Image

# imagePath = input("Enter the image name to be decode : ")
imagePath = 'image.jpg' # image path
image = Image.open(imagePath).convert('L')
imageArray = numpy.array(image)

# print(imageArray)

# sum pixels value along rows and colums to detect boundaries
rowSum = numpy.sum(imageArray, axis=1)
columnSum = numpy.sum(imageArray, axis=0)

rows, columns = imageArray.shape

horizontalLength = 0
verticalLength = 0

for i in range(0, int(rows)):
    if (imageArray[i][0] < 5):
        verticalLength = i
    else:
        # i = rows
        pass

for i in range(0, int(columns)):
    if (imageArray[0][i] < 5):
        horizontalLength = i
    else:
        # i = columns
        pass
# print("Vertical Length ",  verticalLength)
# print("Horizontal Length " , horizontalLength)

# print('Columns' , rows)
# print(int(rows/verticalLength)-1)
messageLength = int(rows/verticalLength)-1

messageBinary = numpy.full((8, messageLength), '0')

for i in range(0,messageLength):
    for j in range(0, 8):
        xAxis = int(horizontalLength*1/2) + horizontalLength*j
        yAxis = int(verticalLength*3/2) + verticalLength*i


        if(imageArray[yAxis][xAxis] < 100):
            # print("BLACK X : ", xAxis, " Y : ", yAxis)
            messageBinary[j][i] = '1'
        else:
            # print("WHITE X : ", xAxis, " Y : ", yAxis)
            messageBinary[j][i] = '0'

    # print(" ")
    
transposedMatrix = numpy.transpose(messageBinary)
# print(type(transposedMatrix[0][2]))
mergedBinary = numpy.array([''.join(row) for row in transposedMatrix])
# print(mergedBinary)


letters = ''.join([chr(int(b, 2)) for b in mergedBinary])
print(letters)


# plt.imshow(imageArray, cmap='gray')
# # plt.title("GRID IMAGE")
# # plt.axis('off')
# plt.show()



