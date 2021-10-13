# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Entry()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Entry()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        label = Gtk.Label.new(
            str='Digite algo e clique no ícone ou pressione Enter:',
        )
        vbox.append(child=label)

        entry = Gtk.Entry.new()
        entry.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.PRIMARY,
            icon_name='system-search-symbolic',
        )
        entry.connect('activate', self.on_key_enter_pressed)
        entry.connect('icon-press', self.on_icon_pressed)
        vbox.append(child=entry)

    def on_key_enter_pressed(self, Entry):
        print(f'Valor digitado no entry: {Entry.get_text()}')

    def on_icon_pressed(self, Entry, EntryIconPosition):
        print(f'Valor digitado no entry: {Entry.get_text()}')


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
