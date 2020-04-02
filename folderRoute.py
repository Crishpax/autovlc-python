import os
from fileRoute import fileRoute
from supportedExtensions import supportedExtensions


def filterExtensions(files, extensions=()):
    assert isinstance(extensions, tuple), "extensions not provided as a tuple"
    filteredFiles = []
    for ext in extensions:
        filteredFileBatch = filter(lambda x: x.upper().endswith(ext), files)
        filteredFiles += filteredFileBatch

    return filteredFiles


class folderRoute():
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        filteredFiles = filterExtensions(os.listdir(path), supportedExtensions)
        self.files = {}
        for file in filteredFiles:
            self.files.setdefault(filteredFiles.index(
                file)+1, fileRoute(os.path.join(self.path, file)))

    def printContents(self, withFolder=False):
        contents = []
        if withFolder:
            contents += [self.name+'\n']
        for key in self.files:
            contents += ['{}. {}'.format(str(key), self.files[key].title)]
        print('\n'.join(contents))
