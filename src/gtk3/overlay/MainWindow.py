# -*- coding: utf-8 -*-
"""Gtk.Overlay()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='GdkPixbuf', version='2.0')

from gi.repository import GdkPixbuf, Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.Overlay')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.connect('check-resize', self._image_resize)

        self.file = GdkPixbuf.Pixbuf.new_from_file(filename='../../assets/laptop.jpg')

        overlay = Gtk.Overlay.new()
        self.add(widget=overlay)

        self.image = Gtk.Image.new()
        overlay.add_overlay(self.image)

        btn_go_previous = Gtk.Button.new_from_icon_name(
            icon_name='go-previous',
            size=Gtk.IconSize.BUTTON,
        )
        btn_go_previous.set_halign(align=Gtk.Align.START)
        btn_go_previous.set_valign(align=Gtk.Align.CENTER)
        overlay.add_overlay(widget=btn_go_previous)

        btn_go_next = Gtk.Button.new_from_icon_name(
            icon_name='go-next',
            size=Gtk.IconSize.BUTTON,
        )
        btn_go_next.set_halign(align=Gtk.Align.END)
        btn_go_next.set_valign(align=Gtk.Align.CENTER)
        overlay.add_overlay(widget=btn_go_next)

        self.show_all()

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
