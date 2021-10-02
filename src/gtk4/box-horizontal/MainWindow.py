# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Box() horizontal."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Box() horizontal')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        hbox.set_homogeneous(homogeneous=True)
        # No GTK 3: set_border_width().
        hbox.set_margin_top(margin=12)
        hbox.set_margin_end(margin=12)
        hbox.set_margin_bottom(margin=12)
        hbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=hbox)

        # Loop de repetição para criar os widgets.
        for n in range(1, 4):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            button.connect('clicked', self.on_button_clicked)
            # No GTK 3: pack_start().
            hbox.prepend(child=button)

        for n in range(1, 4):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            button.connect('clicked', self.on_button_clicked)
            # No GTK 3: pack_end().
            hbox.append(child=button)

    def on_button_clicked(self, button):
        print('Botão pressionado.')



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
