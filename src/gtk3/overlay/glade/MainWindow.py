# -*- coding: utf-8 -*-
"""Gtk.Overlay()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='GdkPixbuf', version='2.0')

from gi.repository import GdkPixbuf, Gtk


class Handler:

    def __init__(self):
        self.file = GdkPixbuf.Pixbuf.new_from_file(filename='../../../assets/laptop.jpg')
        self.image = builder.get_object(name='image')

    def _image_resize(self, widget):
        width, height = widget.get_size()
        pixbuf = self.file.scale_simple(
            dest_width=width,
            dest_height=height,
            interp_type=GdkPixbuf.InterpType.BILINEAR,
        )
        self.image.set_from_pixbuf(pixbuf=pixbuf)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
