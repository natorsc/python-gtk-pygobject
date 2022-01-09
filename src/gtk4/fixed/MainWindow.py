# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Fixed()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Fixed()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        self.fixed = Gtk.Fixed.new()
        self.fixed.set_margin_top(margin=12)
        self.fixed.set_margin_end(margin=12)
        self.fixed.set_margin_bottom(margin=12)
        self.fixed.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=self.fixed)

        button = Gtk.Button.new_with_label(label='Clique Aqui')
        # Adicionando uma ação para quando o botão for clicado.

        button.connect('clicked', self.on_button_clicked)
        # Posicionando o botão no Fixed Layout.
        self.fixed.put(widget=button, x=0, y=0)

    def on_button_clicked(self, widget):
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
    import sys

    app = Application()
    app.run(sys.argv)
