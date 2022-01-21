# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Picture().

É adequando para carregar imagens e permite que o tamanho da imagem
seja manupulada.

Caso queira carregar um ícone utilize Gtk.Imagem.
"""

from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent.parent
PICTURE = str(ROOT_DIR.joinpath('assets', 'images', 'laptop.jpg'))


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Picture()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_child(child=vbox)

        picture = Gtk.Picture.new_for_filename(filename=PICTURE)
        picture.set_keep_aspect_ratio(keep_aspect_ratio=False)
        vbox.append(child=picture)


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
