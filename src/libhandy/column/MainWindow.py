# -*- coding: utf-8 -*-
"""Handy.Column()."""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configurando a janela principal.
        self.set_title(title='Handy.Column')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        hdy_column = Handy.Column.new()
        hdy_column.set_maximum_width(maximum_width=300)
        self.add(widget=hdy_column)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_border_width(border_width=10)
        hdy_column.add(widget=vbox)

        text_view = Gtk.TextView.new()
        vbox.pack_start(child=text_view, expand=True, fill=True, padding=0)

        button_1 = Gtk.Button.new_with_label(label='Botão 1')
        # Adicionando widgets de cima para baixo.
        vbox.add(widget=button_1)

        button_2 = Gtk.Button.new_with_label(label='Botão 2')
        # Adicionando widgets de cima para baixo.
        vbox.add(widget=button_2)

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
