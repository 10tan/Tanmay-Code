import matplotlib.pyplot as plt
import matplotlib.patches as patches

black, white = 1, 0
# representation of 1 and 0

message = input("Enter the message here : ")
# taking the message to change to image


fig, ax = plt.subplots()

def messageImage(message):
    binaryArray = [format(ord(char), '08b') for char in message]
    # convert message to a binary array 

    # print(binaryArray)

    # first loop, to navigate through elements of binary array, second loop to navigate through elements of binary array,  
    # if the element being checked is 1 then paint the corresponding pixel black, and if element being check is 0 then paint the corresponding pixel white.
    # the color of pixels is started to be filled from the top, 
    # the characters of the message are representated vertically and their binaries horizontally, so x axis is always 8 pixels because it is character.
    # the vertical lenght is the length of messages. if hello is message the the image formed if of n(8*5)pixels as n(x*y)pixels, n can be factor to enlarge the image.


    for i in range(0, len(binaryArray)):
        for j in range(0, len(binaryArray[0])):

            l = binaryArray[i]
            if (l[j] == '0'):

                whiteBox = patches.Rectangle((j, (len(message)-i-1)), width=1, height=1, color='white')
                ax.add_patch(whiteBox)

            elif(l[j] == '1'):

                blackBox = patches.Rectangle((j, len(message)-i-1), width=1, height=1, color="black")
                ax.add_patch(blackBox)

    plt.axis('off')
    # to not show the coordinates

    # a preset black box to find out the numbers of letters in the message
    blackBox = patches.Rectangle((0,len(message)), width=1,height=1, color="BLACK")
    ax.add_patch(blackBox)


    '''
    for i in range(2, 7):
        lengthBinary = bin(len(message))[2:]
        for j in range(0,len(lengthBinary)-1):
            if(lengthBinary[j:j+1] == '1'):
                blackBox = patches.Rectangle(, width=1, height=1, color = 'black')
                ax.add_patch(blackBox)
            elif(lengthBinary[j:j+1] == '0'):
                whiteBox = patches.Rectangle(, width=1, height=1, color='white')
                ax.add_patch(whiteBox)
    '''
    # to set boundaries of the plot
    ax.set_xlim(0, len(binaryArray[0]))
    ax.set_ylim(0, len(message)+1)

    # plt.savefig(f'{message}.jpg', bbox_inches='tight', pad_inches=0) # save the image
    plt.savefig(f'{message}.jpg', bbox_inches='tight', pad_inches=0)
    plt.savefig('image.jpg', bbox_inches='tight', pad_inches=0)
    # plt.show() #show the image or plot

# for scanner , i am thinking of adding a extra line at the end of the image which show the length of message, and by this information, we can proceed further

messageImage(message)

print("Image saved ")
