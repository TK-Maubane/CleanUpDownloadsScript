import os
import shutil

#  Filetypes
PICTURE_TYPES = ['jpg', 'jpeg', 'png', 'svg']
DOCUMENTS_TYPES = ['pdf', 'docx', 'doc', 'odt', 'html', 'md']
VIDEO_TYPES = ['avi','mp4']
AUDIO_TYPES = ['mp3']


def main_cleanup():

    # access the downloads directory
    downloads_dir = os.getcwd()
    downloads = os.listdir(downloads_dir)
    base_folders_dir = ('/'.join(downloads_dir.split("/")[:-1]))+'/'

    # File Types and groups architecture
    filetypes = {'Pictures': {'types': PICTURE_TYPES, 'matches': []},
                'Documents': {'types': DOCUMENTS_TYPES, 'matches': []},
                'Videos': {'types': VIDEO_TYPES, 'matches': []},
                'Music': {'types': AUDIO_TYPES, 'matches': []},
                }

    # Directories to store these filetypes that come with the system
    Directories =  [f for f in filetypes.keys()]

    # Sanity check
    matching_files = 0
    moved_files = 0


    for file in downloads:
        # get obj extension
        file_ext = file.split(".")[-1]

        # add files to matching list based on extention
        for d in Directories:
            if file_ext in filetypes[d]['types']:
                filetypes[d]['matches'].append(file)
                matching_files += 1

    # loop through objects in filetypes
    for group, group_items in filetypes.items(): 
        
        # Get each item in the matches list for each group
        for item in group_items['matches']:
            
            # Try moving file to proper home
            try:
                shutil.move(src=f"{downloads_dir}/{item}", 
                            dst=f"{base_folders_dir}{group}")
                moved_files += 1
                
            # File extension likely not accomodated
            except Exception as e:
                print(f"Error moving file: {e}")

    print(f"Matched files: {matching_files}")
    print(f"Moved files: {moved_files}")
    print(f"All matched files moved: {matching_files == moved_files}")


if __name__ == "__main__":
    main_cleanup()
