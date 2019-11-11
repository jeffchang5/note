#! ~/.virtualenvs/iawriter/bin/python3

# heapq
from utils.filemanager import FileManager
from utils.userinputmanager import UserInputManager

import os

plistFilePath = "./markup-generator.plist"
markdown_dir = "/Users/jeffreychang/Documents/notes/_posts/"


class MarkDownGenerator:

    def __init__(self):
        # not needed at the moment
        # self.plManager = StateSettingsManager(plistFilePath)
        # self.state = self.plManager.getStateOrEmptyState()

        yml_generator = UserInputManager()
        file_manager = FileManager(markdown_dir)

        data = yml_generator.prompt()

        path = file_manager.write(data)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.system(f'osascript {dir_path}/open-in-iawriter.scpt {path}')


if __name__ == '__main__':
    generator = MarkDownGenerator()
