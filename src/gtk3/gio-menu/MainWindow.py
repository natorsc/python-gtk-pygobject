# -*- coding: utf-8 -*-
"""Gio.Menu()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gio.Menu')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # Criando o menu.
        menu = Gio.Menu.new()

        # Adicionando itens ao menu.
        menu.append(label='Item 1', detailed_action='app.item1')
        menu.append(label='Item 2', detailed_action='app.item2')
        menu.append(label='About', detailed_action='app.about')
        # Adicionando o menu.
        self.set_app_menu(app_menu=menu)

        # Criando ações.
        # Nome da ação deve ser a mesma do detailed_action.
        action_item1 = Gio.SimpleAction.new(name='item1', parameter_type=None)
        action_item1.connect('activate', self.menu_action_selected)
        self.add_action(action_item1)

        action_item2 = Gio.SimpleAction.new(name='item2', parameter_type=None)
        action_item2.connect('activate', self.menu_action_selected)
        self.add_action(action_item2)

        action_about = Gio.SimpleAction.new(name='about', parameter_type=None)
        action_about.connect('activate', self.about)
        self.add_action(action_about)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def menu_action_selected(self, widget, parameter):
        print(f'Nome do menu selecionado: {widget.get_name()}')

    def about(self, widget, parameter):
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
    import sys

    app = Application()
    app.run(sys.argv)
