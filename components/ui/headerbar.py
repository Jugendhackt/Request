import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk

from components.ui.dialog import AddAPIDialog

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

        self.add_btn.connect("clicked", lambda *x: self.add_api())

        self.response = {}
        self.dialog = {}
        self.callback=lambda *x:()

    def add_api(self):
        self.dialog = AddAPIDialog(None)
        response = self.dialog.run()
        self.dialog.hide()

        if response == Gtk.ResponseType.OK:
            print("The OK button was clicked")
            responseData = self.dialog.get_input()
            self.callback(responseData)
        elif response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")

        print(response)

    def on_dialog_exit(self, callback):
        self.callback = callback
