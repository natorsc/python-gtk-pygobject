# -*- coding: utf-8 -*-
"""Gtk.Overlay()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='GdkPixbuf', version='2.0')

from gi.repository import GdkPixbuf, Gio, Gtk


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    file = GdkPixbuf.Pixbuf.new_from_file(filename='../../../assets/laptop.jpg')
    image = Gtk.Template.Child(name='image')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def _image_resize(self, widget):
        width, height = widget.get_size()
        pixbuf = self.file.scale_simple(
            dest_width=width,
            dest_height=height,
            interp_type=GdkPixbuf.InterpType.BILINEAR,
        )
        self.image.set_from_pixbuf(pixbuf=pixbuf)


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
