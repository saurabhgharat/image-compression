from PIL import Image
def compress_image():
    with Image.open('image_name.jpeg','r') as im: # Open the image in Read Mode
         pix_val = list(im.getdata())  # get pixel value in RGB format

    a= [x for sets in pix_val for x in sets] #Convert list of tuples into one list 

    myRoundedList =  [round(x,-1) for x in a]  #Round integers to nearest 10

    b=[tuple(myRoundedList[i:i+3]) for i in range(0, len(myRoundedList), 3)]  #Group list to a tuple of 3 integers 

    list_of_pixels = list(b)

    im2 = Image.new(im.mode, im.size) #Create a new image 

    im2.putdata(list_of_pixels) #put image data into the new image 

    im2.save('new_image_name.jpeg')  #save the file 


if __name__ == "__main__":
    compress_image()