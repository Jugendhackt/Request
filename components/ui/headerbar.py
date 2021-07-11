import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

ICONSIZE = Gtk.IconSize.MENU


class HeaderBar(Gtk.HeaderBar):
    def __init__(self, window, *args, **kwargs):
        Gtk.HeaderBar.__init__(self, *args, **kwargs)

        self.window = window
        
        GetIcon = Gtk.Image.new_from_icon_name

        # Close icon
        self.set_show_close_button(True)

        self.add_btn = Gtk.Button()
        add_icon = GetIcon("add", ICONSIZE)
        add_icon.show()
        self.add_btn.add(add_icon)

        self.pack_end(self.add_btn)