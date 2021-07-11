import gi
import urllib3
from gi.repository import Gio
from gi.repository.GdkPixbuf import Pixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


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
        self.titleLabel.set_max_width_chars(30)
        self.titleLabel.set_line_wrap(True)
        self.descriptionLabel = Gtk.Label(label=self.description)
        self.authorLabel = Gtk.Label(label=self.author_name)
        self.imageLabel = Gtk.Image()

        self.box.pack_start(self.titleLabel, True, True, 0)
        self.box.pack_start(self.imageLabel, True, True, 0)
        self.box.pack_start(self.descriptionLabel, True, True, 0)
        self.box.pack_start(self.authorLabel, True, True, 0)

        if self.image != "":
            # Load image from url
            http = urllib3.PoolManager()

            response = http.request('GET', self.image)

            input_stream = Gio.MemoryInputStream.new_from_data(response.data, None)
            pixbuf = Pixbuf.new_from_stream_at_scale(input_stream, width=300, height=300, preserve_aspect_ratio=True, cancellable=None)
            self.imageLabel.set_from_pixbuf(pixbuf)
