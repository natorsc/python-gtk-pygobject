# -*- coding: utf-8 -*-
"""Python e GTK 4: Adw.Carousel()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk
from gi.repository import Adw


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: Adw.Carousel()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_bottom(12)
        vbox.set_margin_end(12)
        vbox.set_margin_start(12)
        vbox.set_margin_top(12)
        # Adicionando o box na janela principal.
        self.set_child(child=vbox)

        label = Gtk.Label.new(str='Arraste com o mouse sobre os elementos abaixo')
        vbox.append(child=label)

        hdy_carousel = Adw.Carousel.new()
        hdy_carousel.set_vexpand(True)
        hdy_carousel.set_spacing(spacing=100)
        vbox.append(child=hdy_carousel)

        # Loop de repetição para criar os widgets.
        for n in range(10):
            page = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
            hdy_carousel.insert(child=page, position=n)

            label = Gtk.Label.new(str=f'Página {n}')
            page.append(child=label)


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
