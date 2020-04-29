# -*- coding: utf-8 -*-
"""Gtk MenuBar com Gio menu e action."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gio


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Gtk MenuBar com Gio menu e action')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        # Criando ações.
        action_new = Gio.SimpleAction.new(name='new', parameter_type=None)
        action_new.connect('activate', self.menu_item_clicked)
        self.add_action(action_new)

        action_undo = Gio.SimpleAction.new(name='undo', parameter_type=None)
        action_undo.connect('activate', self.menu_item_clicked)
        self.add_action(action_undo)

        action_about = Gio.SimpleAction.new(name='about', parameter_type=None)
        action_about.connect('activate', self.about)
        self.add_action(action_about)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.add(widget=vbox)

        # Menu principal
        menu = Gio.Menu.new()

        # Criando menu que será um submenu do menu principal.
        menu_file = Gio.Menu.new()
        menu.append_submenu(label='Arquivo', submenu=menu_file)

        menu_edit = Gio.Menu.new()
        menu.append_submenu(label='Editar', submenu=menu_edit)

        menu_help = Gio.Menu.new()
        menu.append_submenu(label='Ajuda', submenu=menu_help)

        # Criando um novo item.
        # detailed_action: Nome da ação que foi criada com `Gio.SimpleAction`.
        # > **OBS**: win: Porque registramos a ação em `ApplicationWindow`.
        item_new = Gio.MenuItem.new(label='Novo', detailed_action='win.new')
        menu_file.append_item(item_new)

        item_undo = Gio.MenuItem.new(label='Desfazer', detailed_action='win.undo')
        menu_edit.append_item(item_undo)

        item_about = Gio.MenuItem.new(label='Sobre', detailed_action='win.about')
        menu_help.append_item(item_about)

        # Criando a barra de menu.
        menubar = Gtk.MenuBar.new_from_model(model=menu)
        # Adicionando a barra de menu no box vertical que está na janela principal.
        vbox.pack_start(child=menubar, expand=False, fill=False, padding=0)

    def menu_item_clicked(self, action, value):
        print(f'Action: {action}\nValue: {value}')

    def about(self, action, value):
        about = Gtk.AboutDialog.new()
        about.set_authors(authors=['Renato Cruz'])
        about.set_comments(
            comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore '
                     'magna aliqua.'
        )
        about.set_website(website='https://github.com/natorsc/gui-python-gtk')
        about.run()
        about.destroy()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
