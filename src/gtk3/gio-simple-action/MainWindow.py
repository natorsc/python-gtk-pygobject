# -*- coding: utf-8 -*-
"""Gtk.MenuButton() com Gio.SimpleAction()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gio.SimpleAction')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Criando headerbar.
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title(title='Gio.SimpleAction')
        headerbar.set_subtitle(subtitle='Gio.SimpleAction')
        headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=headerbar)

        # Criando o menu principal.
        menu = Gio.Menu.new()
        menu.append(label='Item 1', detailed_action="win.item1")
        menu.append(label='Item 2', detailed_action="win.item2")

        # Criando uma sessão
        section = Gio.Menu.new()
        section.append("Item 3", "win.item3")
        menu.append_section(label='Título da sessão', section=section)

        # Criando um submenu.
        submenu = Gio.Menu.new()
        submenu.append("Item 4", "win.item4")
        menu.append_submenu(label="Sub Menu", submenu=submenu)

        # Acões que serão realizadas pelos itens do menu.
        action_item1 = Gio.SimpleAction.new(name='item1', parameter_type=None)
        action_item1.connect("activate", self.item_callback)
        self.add_action(action=action_item1)

        action_item2 = Gio.SimpleAction.new(name='item2', parameter_type=None)
        action_item2.connect('activate', self.item_callback)
        self.add_action(action=action_item2)

        action_item3 = Gio.SimpleAction.new(name='item3', parameter_type=None)
        action_item3.connect('activate', self.item_callback)
        self.add_action(action=action_item3)

        action_item4 = Gio.SimpleAction.new(name='item4', parameter_type=None)
        action_item4.connect('activate', self.item_callback)
        self.add_action(action=action_item4)

        # Ícone que será exibido no botão do menu.
        menu_button_image = Gtk.Image.new_from_icon_name(
            icon_name='open-menu-symbolic',
            size=Gtk.IconSize.MENU,
        )

        # Botão que irá conter o menu.
        menu_button = Gtk.MenuButton.new()
        menu_button.add(widget=menu_button_image)
        # Adicionando o menu no botão.
        menu_button.set_menu_model(menu)
        # Adicionando o botão no headerbar.
        headerbar.pack_end(child=menu_button)

        self.show_all()

    def item_callback(self, widget, data):
        print(widget.get_name())


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
