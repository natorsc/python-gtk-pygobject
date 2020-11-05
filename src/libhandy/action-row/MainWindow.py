# -*- coding: utf-8 -*-
"""Handy.ActionRow()."""
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    # Nome dos ícones.
    icons_standard = ['mail-send-receive', 'user-trash', 'face-smile',
                      'call-start', 'call-stop']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.ActionRow')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Criando um scroll para que a janela principal possa comportar os widgets
        scrolled = Gtk.ScrolledWindow.new(hadjustment=None, vadjustment=None)
        self.add(widget=scrolled)

        list_box = Gtk.ListBox.new()
        self.set_border_width(border_width=12)
        list_box.set_activate_on_single_click(single=True)
        list_box.connect('row_activated', self.on_row_clicked)
        scrolled.add(widget=list_box)

        # Loop para criar as linhas.
        for i, icon_name in enumerate(self.icons_standard):
            # Criando e configurando ActionRow que será adicionada no listbox.
            hdy_action_row = Handy.ActionRow.new()
            hdy_action_row.set_icon_name(icon_name=icon_name)
            hdy_action_row.set_title(title=f'Título {i}')
            hdy_action_row.set_subtitle(subtitle=f'subtítulo {i}')
            # Adicionando a ActionRow no listbox.
            list_box.add(widget=hdy_action_row)

        self.show_all()

    def on_row_clicked(self, listbox, row):
        print('aqui')
        # Exibindo qual dos itens foi clicado.
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
