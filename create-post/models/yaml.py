from dataclasses import dataclass
from typing import Optional


@dataclass
class YAML:
    title: str
    categories: list
    tags: list
    lastModifiedDate: str
    excerpt: Optional[str]

    @staticmethod
    def __getYMLFormatting():
        return ["---\n"]

    def generateYAML(self) -> list:
        title = f'title: "{self.title}"\n'
        categories = ["categories:\n"] + ["  - " + i + "\n" for i in self.categories]
        tags = ["tags:\n"] + ["  - " + i + "\n" for i in self.tags]
        if self.excerpt:
            excerpt = f'excerpt: "{self.excerpt}"\n'
        else:
            excerpt = None
        date = f"last_modified_at: {self.lastModifiedDate}\n"
        builder = \
            self.__getYMLFormatting() + \
            [title] + \
            tags + \
            categories
        if self.excerpt:
            builder += excerpt
        builder += [date] + self.__getYMLFormatting()
        return builder
