# File organizer


This project is designed to organize files based on their metadata. The project structure is as follows:

File-organizer
├── !inbox
│   └── note to be moved
├── 1. Projects
│   ├── group
│   │   └── note to be moved if changes made
├── 2. Areas
│   ├── group
│   │   └── note to be moved if changes made
├── 3. Resources
│   ├── group
│   │   └── note to be moved if changes made
├── 4. Other
│   ├── group
│   │   └── note to be moved if changes made
└── main.py


- "!inbox" directory contains notes that need to be moved to the appropriate directories based on their metadata.

- "1. Projects", "2. Areas", "3. Resources", and "4. Other" are the destination directories for the notes that contain subdirectories (groups). Each of these groups can contain notes that might need to be moved if changes are made.



### Creating Notes

To create a note that can be moved by the program, simply create a text file in the !inbox directory. The note should be a plain text file.

The program uses metadata to determine where to move the notes. This metadata should be included at the top of the note, and should be formatted as follows:

---
project: name
---

or

---
area: name
---

or

---
resource: name
---

or

---
other: name
---


The program will read this metadata and move the note to the corresponding directory and group. For example, if a note has the metadata project: myProject, the program will move the note to the 1. Projects/myProject directory. If the specified group does not exist, the program will create it.

