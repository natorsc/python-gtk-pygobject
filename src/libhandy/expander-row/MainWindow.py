# -*- coding: utf-8 -*-
"""Handy.ExpanderRow()."""

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '0.0')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    # Nome dos ícones.
    icons_standard = ['mail-send-receive', 'user-trash', 'face-smile',
                      'call-start', 'call-stop']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.ExpanderRow')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        # Criando um scroll para que a janela principal possa comportar os widgets
        scrolled = Gtk.ScrolledWindow.new(hadjustment=None, vadjustment=None)
        self.add(widget=scrolled)

        list_box = Gtk.ListBox.new()
        scrolled.add(widget=list_box)

        # Loop para criar as linhas.
        for n in range(len(self.icons_standard)):
            text = Gtk.Label.new(
                f'Texto {n}. Esse texto será exibido quando a linha for expandida.'
            )
            text.set_line_wrap(wrap=True)

            # Criando e configurando ExpanderRow que será adicionada no listbox.
            hdy_action_row = Handy.ExpanderRow.new()
            hdy_action_row.set_icon_name(icon_name=self.icons_standard[n - 1])
            hdy_action_row.set_title(title=f'Título {n}')
            hdy_action_row.set_subtitle(subtitle=f'subtítulo {n}')
            # Adicionando o texto.
            hdy_action_row.add(widget=text)

            # Adicionando a ActionRow no listbox.
            list_box.add(widget=hdy_action_row)

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
