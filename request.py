#!/bin/python3

import gi
import urllib3
import components.posts
import components.backend
from threading import Thread

from components.streams import Stream
from gi.repository import Gio
from components.headerbar import HeaderBar
gi.require_version("GdkPixbuf", "2.0")
from gi.repository.GdkPixbuf import Pixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk



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

        self.titleLabel = Gtk.Label(self.title)
        self.descriptionLabel = Gtk.Label(self.description)
        self.authorLabel = Gtk.Label(self.author_name)
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


class Page(Gtk.FlowBox):
    def __init__(self, stack, name):
        super().__init__()
        self.name = name

        self.set_valign(Gtk.Align.START)
        self.set_max_children_per_line(3)
        self.set_selection_mode(Gtk.SelectionMode.NONE)
        stack.add_titled(self, self.name, self.name)


class RequestApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")

        self.apis = [
            {
                "name": "Reddit",
                "api": "reddit.json",
                "posts": []
            },
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

            posts = components.backend.Backend.fetch({
                "api": api["api"]
            })

            for post in posts:
                page.add(Post(post.title, post.image, post.description, post.author))
                print(post)


def handle_posts(post_streams: dict, pages: dict):
    while True:
        for stream in post_streams:
            for post in post_streams[stream]:
                pages[stream].add(Post(post.title, post.image, post.description, post.author))


win = RequestApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
