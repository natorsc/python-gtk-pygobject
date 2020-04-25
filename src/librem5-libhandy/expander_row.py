# -*- coding: utf-8 -*-
"""Handy.ExpanderRow."""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    # Nome dos ícones.
    icons_standard = ['mail-send-receive', 'user-trash', 'face-smile',
                      'call-start', 'call-stop']

    def __init__(self):
        super().__init__()

        self.set_title(title='Handy.ExpanderRow')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        # Criando um scroll para que a janela principal possa comportar os widgets
        scrolled = Gtk.ScrolledWindow.new(hadjustment=None, vadjustment=None)

        # Não é necessário declarar ``.set_policy()`` a menos que o scroll
        # apresente algum comportamento estranho.
        # scrolled.set_policy(
        #     hscrollbar_policy=Gtk.PolicyType.EXTERNAL,
        #     vscrollbar_policy=Gtk.PolicyType.EXTERNAL
        # )

        # Adicionando a barra de rolagem na janela principal.
        self.add(widget=scrolled)

        # Criando o ListBox.
        list_box = Gtk.ListBox.new()
        # Definindo o modo de seleção.
        list_box.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        # Adicionando o ListBox no container da janela principal.
        list_box.connect('row-activated', self.on_row_clicked)
        # self.add(list_box)
        # vbox.pack_start(child=list_box, expand=True, fill=True, padding=0)
        scrolled.add(widget=list_box)

        # Loop para criar os widgets.
        for n in range(1, len(self.icons_standard) + 1):
            label = Gtk.Label.new(str='Olá Mundo')

            hdy_expander_row = Handy.ExpanderRow.new()
            hdy_expander_row.set_icon_name(icon_name=self.icons_standard[n - 1])
            hdy_expander_row.set_title(title='Clique na seta ao lado para expandir')
            hdy_expander_row.set_subtitle(subtitle='subtítulo')
            hdy_expander_row.add(widget=label)
            list_box.add(widget=hdy_expander_row)

    def on_row_clicked(self, listbox, listbox_row):
        # Exibindo qual dos itens foi clicado.
        print(f'Ícone da linha: {listbox_row.get_icon_name()}')
        print(f'Titulo da linha: {listbox_row.get_title()}')
        print(f'Sub titulo da linha: {listbox_row.get_subtitle()}')
        print(f'Posição = {listbox_row.get_index()}')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
