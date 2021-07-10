import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Request")

        # box
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        # Checlbox
        self.checkbox = Gtk.CheckButton(label='Sure to exit?')
        self.box.pack_start(self.checkbox, True, True, 0)

        # Button
        self.btn = Gtk.Button(label='Close')
        self.btn.connect('clicked', self.close_btn)
        self.box.pack_end(self.btn, True, True, 0)

    # Btn method
    def close_btn(self, widget):
        if self.checkbox.get_active():
            window.close()
        else:
            print('Check the checkbox to Close')


window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
