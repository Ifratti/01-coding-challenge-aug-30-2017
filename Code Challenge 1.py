#this function breaks up a square image into equal parts and stores them in an array
def image_breakup(number_of_rows,block_length,image_file_name):
    from PIL import Image
    #testing for square image
    img = Image.open(img_file)
    width, height = img.size
    if width != height:
        print("Not square image")
        image_array = "Not square image"
    else:
        #if the image is square partition the image into number of rows sqrd regions
        image_array = []
        box = (0,0,block_length_int,block_length_int)
        for j in range(0,number_of_rows):
            for i in range(0,number_of_rows):
                img = Image.open(image_file_name)
                box =(0+i*block_length
                      ,0+j*block_length
                      ,block_length_int+i*block_length
                      ,block_length_int+j*block_length
                      )
                img = img.crop(box)
                image_array.append(img)
    return image_array;
#this function returns TRUE if two images are equal
def equal(image1,image2):
    from PIL import ImageChops
    return ImageChops.difference(image1, image2).getbbox() is None;
from PIL import Image
from PIL import ImageChops

# Open the image with Pillow.
img_file = 'puzzle-scramble.png'
img = Image.open(img_file)

# Assign width and height values.
width, height = img.size

# Expected result: (330, 330)
print(width, height)

#set up of 3X3 Grid
block_length = width / 3
block_length_int = int(block_length)
block_rows = 3

#Breaking images into 9 parts
scrambled_image_array = image_breakup(block_rows,block_length_int,img_file)
img_file = 'puzzle-unscrambled.png'
unscrambled_image_array = image_breakup(block_rows,block_length_int,img_file)
#reordering scrabled_image to equal unscrambled_image
solution=[]
for i in range(0,len(unscrambled_image_array)):
    while not equal(scrambled_image_array[0], unscrambled_image_array[i]):
        scrambled_image_array = scrambled_image_array[1:] + scrambled_image_array[:1]
    solution.append(scrambled_image_array[0]);
#Putting unscrabled image onto scrambled image
solution_img = Image.new("RGB",(330,330))
for j in range(0,block_rows):
    for i in range(0,block_rows):
        box =(0+i*block_length_int
              ,0+j*block_length_int
              ,block_length_int+i*block_length_int
              ,block_length_int+j*block_length_int
              )
        solution_img.paste(solution[i+(j*3)],box)


file_name = "Solution" +".png"
solution_img.save(file_name, 'PNG')

