import json


class Post:
    title: str
    image: str
    author: str
    description: str

    def __init__(self, post: dict):
        self.title = post["title"]
        self.image = post["image"]
        self.description = post["description"]
        self.author = post["author"]

    def __repr__(self):
        return f"""Post {{
    title: {self.title.__repr__()},
    image: {self.image.__repr__()},
    author: {self.author.__repr__()},
    description: {self.description.__repr__()}
}}"""
