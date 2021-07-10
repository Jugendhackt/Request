import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from gi.repository.GdkPixbuf import Pixbuf
from gi.repository import Gio
import urllib3


class Post(Gtk.Button):
    def __init__(self, title="", image="", description="", author_name=""):
        super().__init__()
        self.title = title
        self.image = image
        self.description = description
        self.author_name = author_name

        # Define widgets
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.titleLabel = Gtk.Label(label=self.title)
        self.descriptionLabel = Gtk.Label(label=self.description)
        self.authorLabel = Gtk.Label(label=self.author_name)
        self.imageLabel = Gtk.Image()

        self.box.pack_start(self.titleLabel, True, True, 0)
        self.box.pack_start(self.imageLabel, True, True, 0)
        self.box.pack_start(self.descriptionLabel, True, True, 0)
        self.box.pack_start(self.authorLabel, True, True, 0)

        # Load image from url
        http = urllib3.PoolManager()

        response = http.request('GET', self.image)

        input_stream = Gio.MemoryInputStream.new_from_data(response.data, None)
        pixbuf = Pixbuf.new_from_stream(input_stream, None)
        self.imageLabel.set_from_pixbuf(pixbuf)
