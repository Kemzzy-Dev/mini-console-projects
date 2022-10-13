#importing required modules for my project
import os
import math


#Functions to attend to different needs.
def get_name_and_size(path):

    #validating if the path provided by the user is correct
    if os.path.isdir(path) == True:

        #Variables used in the project
        fileSize=[]# a list to store the size of each file
        max_file = 0#initializing a list to store the largest file
        total_file = 0#Store the number of files in the directory

        #To get the file name and file size 
        for dirpath, dirname, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(str(dirpath), str(filename))
                file_size = os.stat(file_path).st_size
                total_file += 1
                #Get max file size
                if file_size > max_file:
                    max_file = file_size
                #Get max file name
                if file_size == max_file:
                    file_name = file_path

        largestFile = round(max_file/1048576, 1)#calculate the size of the file in Mb instead of bytes and round it to 1 decimal place
        #Print out the final file size
        print('')
        print(f'You have {total_file} files in this folder. ')
        print(f'Your largest file is located in {file_name} and it is {largestFile} Mb')
        print('')
        
    else:
        print('Sorry Hermano, the path you provided is incorrect. Please check and try again')


def delete_duplicate_files(path):
        unique = []

        for filename in os.listdir(path):
            if os.path.isfile(filename):
                filehash = md5.md5(file(filename).read()).hexdigest()
                if filehash not in unique: 
                    unique.append(filehash)
                else: 
                    os.remove(filename)

                            

#End of the funtion to calculate the largest file name and file size


#Request the path of the folder to be scannned. 
# user_path = input('Enter the file path: ')

# get_name_and_size(user_path)

delete_duplicate_files('C:/Users/HP/Documents/duplicate files/Blue exorcist')