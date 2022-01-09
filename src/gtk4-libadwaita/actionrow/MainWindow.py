# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Adw.ActionRow()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk
from gi.repository import Adw


class MainWindow(Gtk.ApplicationWindow):
    # Nome dos ícones.
    icons_standard = ['mail-send-receive', 'user-trash', 'face-smile',
                      'call-start', 'call-stop']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Adw.ActionRow()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        # Adicionando o box na janela principal.
        self.set_child(child=vbox)

        # Criando um scroll para que a janela principal possa comportar os widgets
        scrolled = Gtk.ScrolledWindow.new()
        self.set_child(child=scrolled)

        list_box = Gtk.ListBox.new()
        # list_box.set_selection_mode(False)
        list_box.set_margin_top(margin=12)
        list_box.set_margin_end(margin=12)
        list_box.set_margin_bottom(margin=12)
        list_box.set_margin_start(margin=12)
        list_box.connect('row-selected', self.on_row_clicked)
        scrolled.set_child(child=list_box)

        # Loop para criar as linhas.
        for i, icon_name in enumerate(self.icons_standard):
            # Criando e configurando ActionRow que será adicionada no listbox.
            adw_action_row = Adw.ActionRow.new()
            adw_action_row.set_margin_top(margin=6)
            adw_action_row.set_margin_end(margin=6)
            adw_action_row.set_margin_bottom(margin=6)
            adw_action_row.set_margin_start(margin=6)
            adw_action_row.set_icon_name(icon_name=icon_name)
            adw_action_row.set_title(title=f'Título {i}')
            adw_action_row.set_subtitle(subtitle=f'subtítulo {i}')
            # Adicionando a ActionRow no listbox.
            list_box.append(adw_action_row)

    def on_row_clicked(self, listbox, row):
        print(f'Ícone da linha = {row.get_icon_name()}')
        print(f'Titulo da linha = {row.get_title()}')
        print(f'Sub titulo da linha = {row.get_subtitle()}')
        print(f'Posição = {row.get_index()}')
        print('---\n')


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
