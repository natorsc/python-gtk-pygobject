# -*- coding: utf-8 -*-
"""Gtk.Paned() horizontal."""


import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.Paned horizontal')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        paned = Gtk.Paned.new(orientation=Gtk.Orientation.HORIZONTAL)
        paned.set_wide_handle(wide=True)
        paned.set_border_width(border_width=12)
        self.add(widget=paned)

        vbox1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        paned.pack1(child=vbox1, resize=False, shrink=False)

        vbox2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        paned.pack2(child=vbox2, resize=False, shrink=False)

        # vbox1.
        for n in range(1, 4):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            vbox1.add(widget=button)

        # vbox2
        for n in range(4, 7):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            vbox2.add(widget=button)

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
