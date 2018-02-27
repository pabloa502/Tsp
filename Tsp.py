import sys

class BaseFile():
    def __init__(self, nameFile):
        self.nameFile = nameFile
    """docstring for BaseFile"""
    def file_get_contents(self):
        with open(self.nameFile, "r") as f:
            content = f.readlines()
        """in list content save data file"""
        content = [x.strip() for x in content]
        print(content)

base = BaseFile("data.txt").file_get_contents()