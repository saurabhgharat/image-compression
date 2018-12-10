from PIL import Image
def compress_image():
    im=Image.open('image_name.jpeg','r') # Open the image in Read Mode
    pix_val = list(im.getdata())  # get pixel value in RGB format

    a= [x for sets in pix_val for x in sets] #Convert list of tuples into one list 

    myRoundedList =  [round(x,-1) for x in a]  #Round integers to nearest 10
    if im.mode in("RGBA","p"):
        b=[tuple(myRoundedList[i:i+4]) for i in range(0, len(myRoundedList), 4)]  #Group list to a tuple of 4 integers
    elif im.mode in("RGB"):
        b=[tuple(myRoundedList[i:i+3]) for i in range(0, len(myRoundedList), 3)]   #Group list to a tuple of 3 integers
   
    list_of_pixels = list(b)

    im2 = Image.new(im.mode, im.size) #Create a new image 

    im2.putdata(list_of_pixels) #put image data into the new image 
    
    if im.mode in("RGBA","p"):           #save the file 
        im2.save(image_path,"PNG")
    elif im.mode in("RGB"):
        im2.save(image_path,"JPEG")
      #save the file 


if __name__ == "__main__":
    compress_image()
