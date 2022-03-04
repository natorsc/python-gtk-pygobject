# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Adw.Carousel()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk
from gi.repository import Adw


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Adw.Carousel()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(12)
        vbox.set_margin_end(12)
        vbox.set_margin_bottom(12)
        vbox.set_margin_start(12)

        # Adicionando o box na janela principal.
        self.set_child(child=vbox)

        label = Gtk.Label.new(str='Arraste com o mouse sobre os elementos abaixo')
        vbox.append(child=label)

        adw_carousel = Adw.Carousel.new()
        adw_carousel.set_vexpand(True)
        adw_carousel.set_spacing(spacing=24)
        adw_carousel.connect('page-changed', self.on_page_changed)
        vbox.append(child=adw_carousel)

        # Loop de repetição para criar os widgets.
        for n in range(1, 11):
            page = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
            adw_carousel.insert(child=page, position=n)

            label = Gtk.Label.new(str=f'Página {n}')
            page.append(child=label)

    def on_page_changed(self, carousel, index):
        print(f'Posição: {carousel.get_position()}')
        print(f'índice: {index}')


class Application(Adw.Application):

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
