import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import json

class AddAPIDialog(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Add an API", transient_for=parent, flags=Gtk.DialogFlags.MODAL)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.set_default_size(150, 100)

        box = Gtk.ListBox()

        importBtn = Gtk.Button(label="Import from file")
        importBtn.connect("clicked", lambda *x:self.import_from_file())
        box.add(importBtn)

        nameLabel = Gtk.Label(label="API Name")
        self.nameEntry = Gtk.Entry()
        box.add(nameLabel)
        box.add(self.nameEntry)

        urlLabel = Gtk.Label(label="URL")
        self.urlEntry = Gtk.Entry()
        box.add(urlLabel)
        box.add(self.urlEntry)

        queryLabel = Gtk.Label(label="JSON Query")
        self.queryEntry = Gtk.Entry()
        box.add(queryLabel)
        box.add(self.queryEntry)

        area = self.get_content_area()
        area.add(box)
        self.show_all()

    def import_from_file(self):
        fileDialog = Gtk.FileChooserDialog(
            title="Import api.json",
            parent=None,
            action=Gtk.FileChooserAction.OPEN
        )

        fileDialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        response = fileDialog.run()

        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            filePath = fileDialog.get_filename()
            print("File selected: " + filePath)
            with open(filePath, "r") as file:
                api = json.load(file)

                self.nameEntry.set_text(api["name"])
                self.urlEntry.set_text(api["url"])
                self.queryEntry.set_text(api["query"])

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        fileDialog.destroy()

    def get_input(self):
        return {
            "name": self.nameEntry.get_text(),
            "url": self.urlEntry.get_text(),
            "query": self.queryEntry.get_text()
        }

