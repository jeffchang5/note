from datetime import datetime

from models.yaml import YAML
from utils.datemanager import get_current_date
from typing import Optional


def escapeInput(text: str):
    return text == "!n" or text == ":n"


class UserInputManager:

    def prompt(self) -> YAML:
        title = self.__promptTitle()
        categories = self.__promptCategories()
        tags = self.__promptTags()
        last_modified_date = self.__getLastModifiedDate()
        excerpt = self.__promptExcerpt()

        return YAML(
            title,
            categories,
            tags,
            last_modified_date,
            excerpt
        )

    @staticmethod
    def __promptTitle() -> str:
        return input("What is title of your document?\n")

    @staticmethod
    def __getLastModifiedDate() -> str:
        return get_current_date()

    def __promptTags(self) -> list:
        print("What are the tags of your document? Enter !n or :n to leave.")
        return self.__getManyInputs("tag")

    def __promptCategories(self) -> list:
        print("What are the categories of your document? Enter !n or :n to leave.")
        return self.__getManyInputs("category")

    @staticmethod
    def __promptExcerpt() -> Optional[str]:
        text = input("Is there a byline you want to leave?  Enter !n or :n to leave.\n")
        if escapeInput(text) or len(text) == 0:
            return None
        return text

    @staticmethod
    def __getManyInputs(readable_data_name: str):
        replies = []
        while True:
            reply = input(f'Enter a {readable_data_name}.\n')
            if len(reply) > 0:
                stripped = reply.strip().lower()
                if escapeInput(stripped):
                    break
                replies.append(reply)
        return replies
