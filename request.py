#!/bin/python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from components.ui.headerbar import HeaderBar
from components.ui.page import Page
from components.ui.post import Post
import example_api

class RequestApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")

        self.apis = example_api.apis
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

