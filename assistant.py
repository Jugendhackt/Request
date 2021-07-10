#!/bin/python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from gi.repository.GdkPixbuf import Pixbuf
from gi.repository import Gio
import urllib3
import requests

class RequestApp(Gtk.Assistant):
    def __init__(self):
        super().__init__()


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

        for api in self.apis:
            page = Gtk.Box()
            for post in api["posts"]:
                container = Gtk.Box()


                label = Gtk.Label(label=post["description"])
                container.pack_start(label, True, True, 0)

                page.pack_start(container, True, True, 0)
            self.append_page(page)
            self.set_page_title(page, api["name"])
            self.set_page_complete(page, True)


win = RequestApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
