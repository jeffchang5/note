from dataclasses import dataclass


@dataclass
class YAML:
    title: str
    categories: list
    tags: list
    lastModifiedDate: str

    @staticmethod
    def __getYMLFormatting():
        return ["---\n"]

    def generateYAML(self) -> list:
        title = f'title: "{self.title}"\n'
        categories = ["categories:\n"] + ["  - " + i + "\n" for i in self.categories]
        tags = ["tags:\n"] + ["  - " + i + "\n" for i in self.tags]
        date = f"last_modified_at: {self.lastModifiedDate}\n"

        return \
            self.__getYMLFormatting() + \
            [title] + \
            tags + \
            categories + \
            [date] + \
            self.__getYMLFormatting()
