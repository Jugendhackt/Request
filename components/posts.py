import json


class Post:
    title: str
    image: str
    author: str
    description: str

    def __init__(self, title, image, description, author):
        self.title = title
        self.image = image
        self.description = description
        self.author = author

    def __repr__(self):
        return f"""Post {{
    title: {self.title.__repr__()},
    image: {self.image.__repr__()},
    author: {self.author.__repr__()},
    description: {self.description.__repr__()}
}}"""
