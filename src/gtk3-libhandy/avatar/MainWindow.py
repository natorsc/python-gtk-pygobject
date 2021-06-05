# -*- coding: utf-8 -*-
"""Handy.Avatar()."""
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio, GdkPixbuf
from gi.repository import Handy


def load_image_func(size):
    path = '../../assets/icons/icon.png'
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
        filename=path,
        width=size,
        height=size,
        preserve_aspect_ratio=False,
    )
    return pixbuf


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.Avatar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        hbox.set_border_width(border_width=12)
        self.add(widget=hbox)

        # Exibindo avatar com o ícone padrão.
        avatar_1 = Handy.Avatar.new(
            size=100,
            text='Renato Cruz',
            show_initials=False,
        )
        hbox.add(widget=avatar_1)

        # Exibindo as iniciais no lugar do ícone.
        avatar_2 = Handy.Avatar.new(
            size=100,
            text='Renato Cruz',
            show_initials=True,
        )
        hbox.add(widget=avatar_2)

        # Tamanho do ícone irá se ajustar dinânmicamente.
        avatar_3 = Handy.Avatar.new(
            size=100,
            text='Renato Cruz',
            show_initials=False,
        )
        hbox.pack_start(child=avatar_3, expand=True, fill=True, padding=0)

        avatar_4 = Handy.Avatar.new(
            size=100,
            text='Renato Cruz',
            show_initials=False,
        )
        avatar_4.set_image_load_func(load_image=load_image_func)
        hbox.add(widget=avatar_4)

        self.show_all()


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
