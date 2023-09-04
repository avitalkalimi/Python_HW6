# *************** HOMEWORK 6 ***************
# GOOD LUCK!

# ********************* Helper functions ***********************
import matplotlib.pyplot as plt


def display(image):
    plt.imshow(image, cmap="gist_gray")
    plt.show()


# ************************ QUESTION 1 **************************
def load_binary_image(img_path):
    f = open(img_path, "r")
    content = f.read()

    l = []
    l2 = []
    for i in content:  # '\n'
        if i == '\n':
            if l != []:
                l2.append(l)
            l = []
        else:
            l.append(int(i))
    if l != []:
        l2.append(l)
    image = l2
    return image


# ************************ QUESTION 2 **************************
def add_padding(image, padding):
    l = []
    col = len(image)
    for i in range(col):
        #if i == len(image): break
        for j in range(padding):
            image[i].insert(0, 0)
            image[i].append(0)
    l = []
    col = len(image[0])
    for i in range(padding):
        for j in range(col):
            l.append(0)
        image.insert(0, l)
        image.append(l)
        l = []

    return image


# ************************ QUESTION 3 **************************
def erosion(img_path, structuring_element):
    image = load_binary_image(img_path) #  load: load the pic
    se = structuring_element

    countSE = 0  # setup
    countIm = 0

    for x in range(len(se)):  # chek bag
        for y in range(len(se[x])):
            countSE += se[x][y]
    if countSE == 0: return image

    image = add_padding(image, 1) #  padding: add padding 1 to image

    col_image = len(image)  # setup
    row_image = len(image[0])

    image_after_erosion_local = []  # setup
    image_after_erosion_big = []

    for w in range(1, col_image - 1): #  erosion
        for z in range(1, row_image - 1):
            if image[w][z] == se[1][1] and se[1][1] !=0 :
                countIm +=1
            if image[w + 1][z] == se[2][1] and se[2][1] !=0:
                countIm += 1
            if image[w - 1][z] == se[0][1] and se[0][1] !=0:
                countIm += 1
            if image[w][z - 1] == se[1][0] and se[1][0] !=0:
                countIm += 1
            if image[w][z + 1] == se[1][2] and se[1][2] !=0:
                countIm += 1
            if image[w + 1][z + 1] == se[2][2] and se[2][2] !=0:
                countIm += 1
            if image[w - 1][z - 1] == se[0][0] and se[0][0] !=0:
                countIm += 1
            if image[w - 1][z + 1] == se[0][2] and se[0][2] !=0:
                countIm += 1
            if image[w + 1][z - 1] == se[2][0] and se[2][0] !=0:
                countIm += 1
            if countIm == countSE:
                image_after_erosion_local.append(1)
            else: image_after_erosion_local.append(0)
            countIm = 0
        image_after_erosion_big.append(image_after_erosion_local)
        image_after_erosion_local = []




    return image_after_erosion_big

# ************************ QUESTION 4 **************************
def dilation(img_path, structuring_element):
    image = load_binary_image(img_path)  # load: load the pic
    se = structuring_element

    countSE = 0  # setup
    countIm = 0

    for x in range(len(se)):  # chek bag
        for y in range(len(se[x])):
            countSE += se[x][y]
    if countSE == 0: return image

    image = add_padding(image, 1)  # padding: add padding 1 to image

    col_image = len(image)  # setup
    row_image = len(image[0])

    image_after_dilation_local = []  # setup
    image_after_dilation_big = []

    for w in range(1, col_image - 1):  # erosion
        for z in range(1, row_image - 1):
            if image[w][z] == se[1][1] and se[1][1] != 0:
                countIm += 1
            if image[w + 1][z] == se[2][1] and se[2][1] != 0:
                countIm += 1
            if image[w - 1][z] == se[0][1] and se[0][1] != 0:
                countIm += 1
            if image[w][z - 1] == se[1][0] and se[1][0] != 0:
                countIm += 1
            if image[w][z + 1] == se[1][2] and se[1][2] != 0:
                countIm += 1
            if image[w + 1][z + 1] == se[2][2] and se[2][2] != 0:
                countIm += 1
            if image[w - 1][z - 1] == se[0][0] and se[0][0] != 0:
                countIm += 1
            if image[w - 1][z + 1] == se[0][2] and se[0][2] != 0:
                countIm += 1
            if image[w + 1][z - 1] == se[2][0] and se[2][0] != 0:
                countIm += 1
            if countIm > 0:
                image_after_dilation_local.append(1)
            else:
                image_after_dilation_local.append(0)
            countIm = 0
        image_after_dilation_big.append(image_after_dilation_local)
        image_after_dilation_local = []

    return image_after_dilation_big

