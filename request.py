#!/bin/python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from components.headerbar import HeaderBar

from gi.repository.GdkPixbuf import Pixbuf
from gi.repository import Gio
import urllib3

class Post(Gtk.Button):
    def __init__(self, title="", image="", description="", author_name=""):
        super().__init__()
        self.title = title
        self.image = image
        self.description = description
        self.author_name = author_name

        # Define widgets
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.titleLabel = Gtk.Label(label=self.title)
        self.descriptionLabel = Gtk.Label(label=self.description)
        self.authorLabel = Gtk.Label(label=self.author_name)
        self.imageLabel = Gtk.Image()

        self.box.pack_start(self.titleLabel, True, True, 0)
        self.box.pack_start(self.imageLabel, True, True, 0)
        self.box.pack_start(self.descriptionLabel, True, True, 0)
        self.box.pack_start(self.authorLabel, True, True, 0)

        # Load image from url
        http = urllib3.PoolManager()

        response = http.request('GET', self.image)

        input_stream = Gio.MemoryInputStream.new_from_data(response.data, None)
        pixbuf = Pixbuf.new_from_stream(input_stream, None)
        self.imageLabel.set_from_pixbuf(pixbuf)


class Page(Gtk.ScrolledWindow):
    def __init__(self, stack, name):
        super().__init__()
        self.name = name

        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.box = Gtk.FlowBox()
        self.box.set_valign(Gtk.Align.START)
        self.box.set_max_children_per_line(3)
        self.box.set_selection_mode(Gtk.SelectionMode.NONE)

        self.add(self.box)
        
        stack.add_titled(self, self.name, self.name)

    def add_to_flowbox(self, widget):
        self.box.add(widget)

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

        # Sidebar
        grid = Gtk.Grid()
        self.add(grid)

        stack = Gtk.Stack()
        stack.set_hexpand(True)
        stack.set_vexpand(True)
        grid.attach(stack, 1, 0, 1, 1)

        stacksidebar = Gtk.StackSidebar()
        stacksidebar.set_stack(stack)
        grid.attach(stacksidebar, 0, 0, 1, 1)

        # Pages and posts
        for api in self.apis:
            page = Page(stack, api["name"])

            for post in api["posts"]:
                page.add_to_flowbox(Post(post["title"], post["image"], post["description"], post["author_name"]))
            

win = RequestApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

