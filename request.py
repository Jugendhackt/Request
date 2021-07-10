#!/bin/python3

import gi

import components.backend
import components.posts
from components.ui.headerbar import HeaderBar
from components.ui.page import Page
from components.ui.post import Post

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class RequestApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")

        self.apis = [
            {
                "name": "Reddit",
                "api": "reddit.json"
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
            def edge_reached(_scrolled_window, pos):
                if pos ==3:
                    print("You reached the end")

            page = Page(stack, api["name"])
            page.connect("edge-reached", edge_reached)

            posts = components.backend.Backend.fetch({
                "api": api["api"]
            })

            for post in posts:
                page.add_to_flowbox(Post(post.title, post.image, post.description, post.author))


win = RequestApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
