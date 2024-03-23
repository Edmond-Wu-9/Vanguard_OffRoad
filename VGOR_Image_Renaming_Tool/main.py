import os 
import re

#Move directory to where all the Images are 
image_dir = "C:\\Users\\edmon\\OneDrive\\Desktop\\Images_Filezilla"
os.chdir(image_dir)

#Gets all the file names into a variable called file_list
file_list = os.listdir()
count = 0

#Rename the files from PartNumber.Suffix.jpg/png -> PartNumber_Suffix.jpg/png
for filename in file_list:
    if filename.endswith((".jpg" , ".png")):
        parts = filename.split(".")
        if len(parts) == 3 and len(parts[1]) == 1:
            part_number , suffix = parts[0] , parts[1]
            extension = parts[-1]
            new_filename = f"{part_number}_{suffix}.{extension}"
            old_path = os.path.join(image_dir, filename)
            new_path = os.path.join(image_dir, new_filename)
            if not os.path.exists(new_path):
                #os.rename(old_path, new_path)
                #print(f"Renamed {filename} to {new_filename}")
                continue
            else:
                count = count + 1
                print(f"Skipped renaming {filename} (file {new_filename} already exists)")
#rename_period()
print(f"There are {count} files that have issues if changing the name")