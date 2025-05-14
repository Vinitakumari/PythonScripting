# Write a script to count the number of files in a directory.
import os
directory ="C:/Users/HP/Documents"
for filename in os.listdir(directory):
    file_count = 0
    if(os.path.isfile(os.path.join(directory,filename))):
        file_count += 1
        print (file_count)

    

