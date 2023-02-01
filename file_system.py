class FileSystem:
    """
    This implementation uses a dictionary to represent the directories and their contents. The current directory is stored as a 
    string and updated when the cd function is called. The ls function returns the contents of the current directory, the mkdir function 
    creates a new directory if it does not already exist, and the touch function adds a file to the current directory.
    """
    def __init__(self):
        self.current_directory = "/"
        self.directories = {"/": []}

    def ls(self):
        return self.directories[self.current_directory]

    def mkdir(self, directory):
        if directory in self.directories:
            print(f"Directory {directory} already exists")
        else:
            self.directories[directory] = []
            self.directories[self.current_directory].append(directory)

    def cd(self, directory):
        if directory not in self.directories:
            print(f"Directory {directory} does not exist")
        else:
            self.current_directory = directory

    def touch(self, file):
        self.directories[self.current_directory].append(file)

file_system = FileSystem()
file_system.mkdir("docs")
file_system.cd("docs")
file_system.touch("file.txt")
print(file_system.ls())

