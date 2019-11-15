from models.yaml import YAML
from utils.datemanager import get_current_date
from typing import Optional


def escape_input(text: str) -> bool:
    return text == "!n" or text == ":n"


class UserInputManager:

    def prompt(self) -> YAML:
        title = self.__prompt_title()
        categories = self.__prompt_categories()
        tags = self.__prompt_tags()
        last_modified_date = self.__prompt_last_modified_date()
        excerpt = self.__prompt_excerpt()

        return YAML(
            title,
            categories,
            tags,
            last_modified_date,
            excerpt
        )

    @staticmethod
    def __prompt_title() -> str:
        return input("What is title of your document?\n")

    @staticmethod
    def __prompt_last_modified_date() -> str:
        return get_current_date()

    def __prompt_tags(self) -> list:
        print("What are the tags of your document? Enter !n or :n to leave.")
        return self.__prompt_many_inputs("tag")

    def __prompt_categories(self) -> list:
        print("What are the categories of your document? Enter !n or :n to leave.")
        return self.__prompt_many_inputs("category")

    @staticmethod
    def __prompt_excerpt() -> Optional[str]:
        text = input("Is there a byline you want to leave?  Enter !n or :n to leave.\n")
        if escape_input(text) or len(text) == 0:
            return None
        return text

    @staticmethod
    def __prompt_many_inputs(readable_data_name: str):
        replies = []
        while True:
            reply = input(f'Enter a {readable_data_name}.\n')
            if len(reply) > 0:
                stripped = reply.strip().lower()
                if escape_input(stripped):
                    break
                replies.append(stripped)
        return replies
