# -*- coding: utf-8 -*-
"""Contêiner do tipo Fixed Layout."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Fixed Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        self.fixed = Gtk.Fixed.new()
        self.fixed.set_border_width(border_width=12)
        self.add(widget=self.fixed)

        button = Gtk.Button.new_with_label(label='Clique Aqui')
        # Adicionando uma ação para quando o botão for clicado.
        button.connect('clicked', self._on_button_clicked)
        # Posicionando o botão no Fixed Layout.
        self.fixed.put(widget=button, x=0, y=0)

        self.show_all()

    def _on_button_clicked(self, widget):
        # Quando botão é clicado o mesmo é movido para uma nova posição.
        self.fixed.move(widget=widget, x=100, y=100)
        widget.set_label(label='Movido')


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
    app = Application()
    app.run(sys.argv)
