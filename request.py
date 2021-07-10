#!/bin/python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from components.headerbar import HeaderBar

from gi.repository.GdkPixbuf import Pixbuf
from gi.repository import Gio
import urllib3

class ListItem(Gtk.Button):
    def __init__(self, name, logo=""):
        super().__init__(label=name)
        self.name = name
        self.logo = logo

        self.connect("clicked", lambda x: self.clicked())

    def clicked(self):
        print(f"You clicked {self.name}!")

class Post(Gtk.Button):
    def __init__(self, title="", image="", description="", author_name="", author_image=""):
        super().__init__(label=title)
        self.title = title
        self.image = image
        self.description = description
        self.author_name = author_name
        self.author_image= author_image

        self.connect("clicked", lambda x: self.clicked())

    def clicked(self):
        print(f"You clicked {self.title}!")

class RequestApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")

        self.apis = [
            {
                "name": "Reddit",
                "posts": [
                    {
                        "title": "abc",
                        "image": "https://picsum.photos/200/300",
                        "description": "abc",
                        "author_name": "Gero",
                        "author_image": "https://picsum.photos/200/300"
                    }, 
                    {
                        "title": "abc",
                        "image": "https://picsum.photos/200/300",
                        "description": "def",
                        "author_name": "Gero",
                        "author_image": "https://picsum.photos/200/300"
                    }, 
                    {
                        "title": "abc",
                        "image": "https://picsum.photos/200/300",
                        "description": "ghi",
                        "author_name": "Gero",
                        "author_image": "https://picsum.photos/200/300"
                    }
                ]
            },
            {
                "name": "YouTube",
                "posts": [
                    {
                        "title": "abc",
                        "image": "https://picsum.photos/200/300",
                        "description": "jkl",
                        "author_name": "Gero",
                        "author_image": "https://picsum.photos/200/300"
                    }, 
                    {
                        "title": "abc",
                        "image": "https://picsum.photos/200/300",
                        "description": "mno",
                        "author_name": "Gero",
                        "author_image": "https://picsum.photos/200/300"
                    }, 
                    {
                        "title": "abc",
                        "image": "https://picsum.photos/200/300",
                        "description": "pqr",
                        "author_name": "Gero",
                        "author_image": "https://picsum.photos/200/300"
                    }
                ]
            }
        ]
        # Headerbar
        self.headerbar = HeaderBar(self, title="Response", subtitle="Reddit")
        self.set_titlebar(self.headerbar)

        grid = Gtk.Grid()
        self.add(grid)

        stack = Gtk.Stack()
        stack.set_hexpand(True)
        stack.set_vexpand(True)
        grid.attach(stack, 1, 0, 1, 1)

        stacksidebar = Gtk.StackSidebar()
        stacksidebar.set_stack(stack)
        grid.attach(stacksidebar, 0, 0, 1, 1)

        for api in self.apis:
            page = Gtk.FlowBox()
            page.set_valign(Gtk.Align.START)
            page.set_max_children_per_line(3)
            page.set_selection_mode(Gtk.SelectionMode.NONE)
            for post in api["posts"]:
                myPost = Gtk.Button()
                box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
                myPost.add(box)

                title = Gtk.Label(post["title"])
                description = Gtk.Label(post["description"])
                author = Gtk.Label(post["author_name"])
                image = Gtk.Image()

                http = urllib3.PoolManager()

                url = post["image"]
                response = http.request('GET', url)

                input_stream = Gio.MemoryInputStream.new_from_data(response.data, None)
                pixbuf = Pixbuf.new_from_stream(input_stream, None)
                image = Gtk.Image()
                image.set_from_pixbuf(pixbuf)

                box.pack_start(title, True, True, 0)
                box.pack_start(image, True, True, 0)
                box.pack_start(description, True, True, 0)
                box.pack_start(author, True, True, 0)

                page.add(myPost)



            name = "label%s" % api["name"]
            title = "Page %s" % api["name"]
            stack.add_titled(page, name, title)


win = RequestApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

