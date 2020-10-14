# -*- coding: utf-8 -*-
"""Handy.ActionRow()."""
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '0.0')

from gi.repository import Gtk, Gio
from gi.repository import Handy


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    # Nome dos ícones.
    icons_standard = ['mail-send-receive', 'user-trash', 'face-smile',
                      'call-start', 'call-stop']

    # Acessar os widgets da interface com Gtk.Template.Child(name) aqui:
    list_box = Gtk.Template.Child(name='list_box')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Loop para criar as linhas.
        for n in range(len(self.icons_standard)):
            # Criando e configurando ActionRow que será adicionada no listbox.
            hdy_action_row = Handy.ActionRow.new()
            hdy_action_row.set_icon_name(icon_name=self.icons_standard[n - 1])
            hdy_action_row.set_title(title=f'Título {n}')
            hdy_action_row.set_subtitle(subtitle=f'subtítulo {n}')
            # Adicionando a ActionRow no listbox.
            self.list_box.add(widget=hdy_action_row)

        self.show_all()

    @Gtk.Template.Callback()
    def on_row_clicked(self, listbox, row):
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
