import os


class fileRoute():
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.title = self.name[:self.name.rfind(r'.')]
        self.extension = path[path.rfind(r'.')+1:]
        self.folder = os.path.dirname(path)
