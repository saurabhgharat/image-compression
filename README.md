Image compression using Python 

Image compression is done to reduce the cost of storage and transmission
Steps
1. Open the file and read it
2. Get the pixel values in RGB format
3. Convert the tuples into one list
4. Round the pixel values to nearest 10
5. Regroup the pixel values into tuple of 3
6. Create a new image from the tuple list where each pixel value in tuple indicate R,G,B value
   E.g. (42,34,67) indicates R=42,G=34,B=67
7. Save the compressed image