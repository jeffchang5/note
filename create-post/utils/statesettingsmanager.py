import plistlib

from models.state import State


class StateSettingsManager:

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def getStateOrEmptyState(self) -> State:
        try:
            with open(self.__file_path, 'rb') as fp:
                data = plistlib.load(fp)
                return State.fromDict(data)
        except plistlib.InvalidFileException:
            return State()
        except FileNotFoundError:
            return State()

    def save(self, plist: dict):
        with open(self.__file_path, 'wb') as fp:
            plistlib.dump(plist, fp)
