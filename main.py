import shutil
import os
import frontmatter

# List of frontmatter properties with folder destinations
frontmatter_to_dir = {
    'project': '1. Projects',
    'area': '2. Areas',
    'resource': '3. Resources',
    'other': '4. Other',
}

# Read all the files inside the "!inbox" directory
def process_directory(directory):
    # Read all the files inside the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            note_path = os.path.join(root, file)
            # Read the file's frontmatter
            note_metadata = frontmatter.load(note_path)
            
            # Check if the file has a property to categorize this note,
            # for example: project, area, resource, or other
            for group, group_destination in frontmatter_to_dir.items():
                if group in note_metadata:
                    # Try moving the file, it can be the case the project is
                    # for example mispelled, in that case it won't do anything with the note
                    destination_path = f"{group_destination}/{note_metadata[group]}"
                    # Create the directory if it doesn't exist
                    os.makedirs(destination_path, exist_ok=True)
                    # Try moving the file
                    try_move_file(note_path, f"{destination_path}/{file}")

# Move a file to a destination
def try_move_file(file, destination):
    print('- Moving file', file, "to", destination)
    try:
        shutil.move(file, destination)
    except Exception as err:
        print('-  - Project not found', err)


# Process files in the "!inbox" directory
process_directory('!inbox')

# Process files in the destination directories
for group_destination in frontmatter_to_dir.values():
    process_directory(group_destination)