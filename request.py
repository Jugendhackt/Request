#!/bin/python3

import gi

import components.backend
import components.posts
from components.ui.headerbar import HeaderBar
from components.ui.page import Page
from components.ui.post import Post

import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class RequestApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")

        self.apis = [
            {
                "name": "Reddit mildlyinteresting",
                "api": "mildlyinteresting.json"
            },
            {
                "name": "Reddit memes",
                "api": "memes.json"
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
        stack.connect("notify::visible-child", lambda stacknow, param: self.page_changed(stack.get_visible_child_name()))
        grid.attach(stack, 1, 0, 1, 1)

        stacksidebar = Gtk.StackSidebar()
        stacksidebar.set_stack(stack)
        grid.attach(stacksidebar, 0, 0, 1, 1)

        # Pages and posts
        for api in self.apis:
            self.create_page(stack, api)

    def create_page(self, stack, api):
        
        page = Page(stack, api["name"])
        page.connect("edge-reached", lambda scrolled_win, pos: pos == 3 and self.edge_reached(api["name"]))

        posts = components.backend.Backend.fetch({
            "api": api["api"]
        })

        for post in posts:
            page.add_to_flowbox(Post(post.title, post.image, post.description, post.author))

    def edge_reached(self, name):
        print("You reached the end of %s" % name)

    def page_changed(self, name):
        print("You changed to %s" % name)
    


win = RequestApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
