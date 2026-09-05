storage = 5000
files = 20
file_size = 256
free_space = storage
files_successful_count = 0
files_left = files

for i in range(files):
	if file_size > free_space:
		break
	free_space -= file_size
	files_left -= 1
	files_successful_count += 1
	

print('Files moved:',files_successful_count)
print('Free space left:',free_space,"GB")
if files_left > 0:
	print('Files left:',files_left)
else:
	print('All files moved successfully!')