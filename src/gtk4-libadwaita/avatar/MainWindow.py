# -*- coding: utf-8 -*-
"""Python e GTK 4: Adw.Avatar()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk
from gi.repository import Adw


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: Adw.Avatar()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        hbox.set_margin_bottom(12)
        hbox.set_margin_end(12)
        hbox.set_margin_start(12)
        hbox.set_margin_top(12)
        # Adicionando o box na janela principal.
        self.set_child(child=hbox)

        # Exibindo o ícone padrão.
        avatar_01 = Adw.Avatar.new(
            size=100,
            text='Renato Cruz',
            show_initials=False,
        )
        avatar_01.set_hexpand(True)
        avatar_01.set_vexpand(True)
        hbox.append(child=avatar_01)

        # Exibindo as iniciais no lugar do ícone.
        avatar_02 = Adw.Avatar.new(
            size=100,
            text='Renato Cruz',
            show_initials=True,
        )
        avatar_02.set_hexpand(True)
        avatar_02.set_vexpand(True)
        hbox.append(child=avatar_02)

        avatar_03 = Adw.Avatar.new(
            size=100,
            text='Renato Cruz',
            show_initials=False,
        )
        avatar_03.set_hexpand(True)
        avatar_03.set_vexpand(True)
        avatar_03.set_icon_name('contact-new-symbolic')
        hbox.append(child=avatar_03)


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
