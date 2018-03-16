import cairo
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

class TransparentWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_size_request(300, 220)

        self.connect('destroy', Gtk.main_quit)
        self.connect('draw', self.draw)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)

        hbox = Gtk.Box(spacing=10)
        label1 = Gtk.Label()
        label1.set_text("hello world")
        self.connect("key-press-event", self.on_key_press)
        hbox.pack_start(label1, True, True, 0)
        self.add(hbox)

        self.connect("delete-event", Gtk.main_quit)
        self.set_wmclass("trust", "trust")
        self.set_app_paintable(True)
        self.show_all()

    def on_key_press(self, widget, ev, data=None):

        self.fullscreen()
        print(ev)

    def draw(self, widget, context):
        t = 1
        context.set_source_rgba(t, t, t, t)
        context.set_operator(cairo.OPERATOR_SOURCE)
        context.paint()
        context.set_operator(cairo.OPERATOR_OVER)


TransparentWindow()
Gtk.main()
