import re

from models.yaml import YAML
from utils.datemanager import get_date_from_string


class FileManager:

    def __init__(self, markdown_dir: str):
        self.__markdown_dir = markdown_dir

    def __generateFileName(self, data: YAML):
        date = get_date_from_string(data.lastModifiedDate)
        hyphen_format_title = self.__generate_hyphen_format(data.title).lower()

        return f"{date.year}-{date.month}-{date.day}-{hyphen_format_title}.md"

    def write(self, data: YAML) -> str:
        title = self.__generateFileName(data)
        path = self.__markdown_dir + title
        with open(path, 'w') as fp:
            yaml = data.generateYAML()
            fp.writelines(yaml)
        return path

    @staticmethod
    def __generate_hyphen_format(title: str):
        stripped = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", title)
        return re.sub(r"[^\S\n\t]+", "-", stripped).strip('-')

