import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class AddAPIDialog(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Add an API", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.set_default_size(150, 100)

        box = Gtk.ListBox()

        nameLabel = Gtk.Label(label="API Name")
        nameEntry = Gtk.Entry()
        box.add(nameLabel)
        box.add(nameEntry)

        urlLabel = Gtk.Label(label="URL")
        urlEntry = Gtk.Entry()
        box.add(urlLabel)
        box.add(urlEntry)

        queryLabel = Gtk.Label(label="JSON Query")
        queryEntry = Gtk.Entry()
        box.add(queryLabel)
        box.add(queryEntry)

        area = self.get_content_area()
        area.add(box)
        self.show_all()
