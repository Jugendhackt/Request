import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class AddAPIDialog(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Add an API", transient_for=parent, flags=Gtk.DialogFlags.MODAL)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.set_default_size(150, 100)

        box = Gtk.ListBox()

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

    def get_input(self):
        return {
            "name": self.nameEntry.get_text(),
            "url": self.urlEntry.get_text(),
            "query": self.queryEntry.get_text()
        }

