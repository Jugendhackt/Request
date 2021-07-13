#!/bin/python3

import gi

import components.backend
import components.posts
from components.ui.headerbar import HeaderBar
from components.ui.page import Page
from components.ui.post import Post

import requests
import json
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class RequestApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")

        # load user APIs
        self.file_name = "userAPIs.json"
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                file.write("[]")

        with open(self.file_name, 'r') as file:
            self.apis = json.load(file)
            print(self.apis)

        # Headerbar
        self.headerbar = HeaderBar(self, title="Response", subtitle="Reddit")
        self.set_titlebar(self.headerbar)

        self.headerbar.on_dialog_exit(self.add_api)

        # Sidebar
        grid = Gtk.Grid()
        self.add(grid)

        self.stack = Gtk.Stack()
        self.stack.set_hexpand(True)
        self.stack.set_vexpand(True)
        self.stack.connect("notify::visible-child",
                      lambda stacknow, param: self.page_changed(self.stack.get_visible_child_name()))
        grid.attach(self.stack, 1, 0, 1, 1)

        stacksidebar = Gtk.StackSidebar()
        stacksidebar.set_stack(self.stack)
        grid.attach(stacksidebar, 0, 0, 1, 1)

        # Pages and posts
        for api in self.apis:
            self.create_page(self.stack, api)
    
    # add new api to list an user API file
    def add_api(self, api):
        self.apis.append(api)

        self.create_page(self.stack, api)

        with open(self.file_name, "w") as file:
            json.dump(self.apis, file)

        self.stack.show_all()

    # create stack for each api
    def create_page(self, stack, api):

        page = Page(stack, api["name"])
        page.connect("edge-reached", lambda scrolled_win, pos: pos == 3 and self.edge_reached(api["name"]))
        api["page"] = page

    # listen for UI input changes
    def edge_reached(self, name):
        print("You reached the end of %s" % name)

    def page_changed(self, name):
        print("You changed to %s" % name)

        api = [*filter(lambda elem: elem["name"] == name, self.apis)][0]

        print(api)

        posts = components.backend.Backend.fetch({
            "url": api["url"],
            "query": api["query"]
        })

        for post in posts:
            api["page"].add_to_flowbox(Post(post.title, post.image, post.description, post.author))

        api["page"].show_all()

# Run application
win = RequestApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
