#Import the needed modules
import os
import shutil

#To collect user input and store them in string format
file_location = input('Enter the path of the folder to search for video files: ')
find = int(input('''What are we looking for? 
	Press a corresponding number:
	1. Video files
	2. Audio files 
	3. Images
Pick a number: '''))
new_location = input('Now for the last part enter the location to move it to: ')

#To normalize the given path above as we cannot enter it with one slash
os.path.normpath(file_location)
os.path.normpath(new_location)

#loop through the given directory and get all the files in it
for dirpath, dirnames, filenames in os.walk(file_location):
	for filename in filenames:
		extension = os.path.splitext(filename)
		file_path = os.path.join(dirpath, filename)
		if find == 1:
			if extension[1] == '.mp4' or extension[1] == '.mkv':
				shutil.move(file_path, new_location)
				print('DONE.........')
			else:
				print('There is no video file here')
		elif find == 2:
			if extension[1] == '.mp3':
				shutil.move(file_path, new_location)
				print('DONE.........')
			else:
				print('There is no music file here')
		elif find == 3:
			if extension[1] == '.mpeg' or extension[1] == '.jpg':
				shutil.move(file_path, new_location)
				print('DONE.........')
			else:
				print('There is no image here')
		else:
			print('Enter either 1, 2, 3 to continue!')

