import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Page(Gtk.ScrolledWindow):
    def __init__(self, stack, name):
        super().__init__()
        self.name = name

        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.box = Gtk.FlowBox()
        self.box.set_valign(Gtk.Align.START)
        self.box.set_max_children_per_line(3)
        self.box.set_selection_mode(Gtk.SelectionMode.NONE)

        self.add(self.box)

        stack.add_titled(self, self.name, self.name)

    def add_to_flowbox(self, widget):
        self.box.add(widget)
