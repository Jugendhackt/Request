class Post:
    api: str
    title: str
    image: str
    author: str
    description: str

    def __init__(self, post: dict, api: str):
        self.api = api
        self.title = post["title"]
        self.image = post["image"]
        self.description = post["description"] if "description" in post else ""
        self.author = post["author"]

    def __repr__(self):
        return f"""Post {{
    api: {self.api.__repr__()}
    title: {self.title.__repr__()},
    image: {self.image.__repr__()},
    author: {self.author.__repr__()},
    description: {self.description.__repr__()}
}}"""
