#!/bin/python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from components.headerbar import HeaderBar

class ListItem(Gtk.Button):
    def __init__(self, name, logo=""):
        super().__init__(label=name)
        self.name = name
        self.logo = logo

        self.connect("clicked", lambda x: self.clicked())

    def clicked(self):
        print(f"You clicked {self.name}!")


class RequestApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")

        # Headerbar
        self.headerbar = HeaderBar(self, title="Response", subtitle="Reddit")
        self.set_titlebar(self.headerbar)

        # Pane
        self.pane = Gtk.Paned()
        self.add(self.pane)

        # Sidemenu
        self.sidemenu = Gtk.ListBox()
        self.pane.add1(self.sidemenu)

        self.apiList = []
        self.apiList.append(ListItem("Reddit"))
        self.apiList.append(ListItem("YouTube"))
        self.apiList.append(ListItem("RSS"))

        for item in self.apiList:
            self.sidemenu.prepend(item)


        # Content
        self.btn = Gtk.Button(label="Hello, World!")
        self.btn.connect('clicked', lambda x: self.close())
        self.pane.add2(self.btn)


win = RequestApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

