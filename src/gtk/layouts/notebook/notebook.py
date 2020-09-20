# -*- coding: utf-8 -*-
"""Contêiner do tipo Notebook Layout.

O container Notebook Layout é muito similar ao Stack e StackSwitcher
Layout, contudo ao invés de botões temos abras para gerenciar as paginas.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Notebook Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        notebook = Gtk.Notebook.new()
        self.add(widget=notebook)

        page1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page1.set_border_width(border_width=10)

        # Adicionando widgets do tipo Label na pagina 1.
        for n in range(1, 6):
            label = Gtk.Label.new(f'Texto {n}')
            page1.pack_start(child=label, expand=False, fill=True, padding=1)

        tab_label = Gtk.Label.new(str='Página 1')
        notebook.append_page(child=page1, tab_label=tab_label)

        page2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page2.set_border_width(border_width=10)

        for n in range(1, 6):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            page2.pack_start(child=button, expand=False, fill=True, padding=2)

        # Ao invés de um label para a aba será utilizado um ícone.
        tab_icon = Gtk.Image.new_from_icon_name(
            icon_name='folder-documents-symbolic',
            size=Gtk.IconSize.MENU
        )

        notebook.append_page(child=page2, tab_label=tab_icon)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
