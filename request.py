#!/bin/python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from components.headerbar import HeaderBar

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)

    headerbar = HeaderBar(win, title="Response", subtitle="Reddit")
    headerbar.set_custom_title
    win.set_titlebar(headerbar)

    pane = Gtk.Paned()
    win.add(pane)
    
    tree = Gtk.StackSidebar()
    pane.add1(tree)

    btn2 = Gtk.Button(label="Hello, World!")
    btn2.connect('clicked', lambda x: win.close())
    pane.add2(btn2)

    win.show_all()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
