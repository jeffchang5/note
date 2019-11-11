from dataclasses import dataclass


@dataclass
class State:
    tags: list = [],
    categories: list = [],

    @staticmethod
    def fromDict(data: dict):
        return State(
            tags=data["tags"],
            categories=["categories"]
        )
