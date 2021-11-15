# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.MenuButton()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.MenuButton()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_homogeneous(homogeneous=True)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        # Criando headerbar.
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)

        # Criando o menu principal.
        menu = Gio.Menu.new()
        menu.append(label='Item 1', detailed_action='win.item1')
        menu.append(label='Item 2', detailed_action='win.item2')

        # Criando uma sessão
        section = Gio.Menu.new()
        section.append('Item 3', 'win.item3')
        menu.append_section(label='Título da sessão', section=section)

        # Criando um submenu.
        submenu = Gio.Menu.new()
        submenu.append('Item 4', 'win.item4')
        menu.append_submenu(label='Sub Menu', submenu=submenu)

        # Acões que serão realizadas pelos itens do menu.
        action_item1 = Gio.SimpleAction.new(name='item1', parameter_type=None)
        action_item1.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_item1)

        action_item2 = Gio.SimpleAction.new(name='item2', parameter_type=None)
        action_item2.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_item2)

        action_item3 = Gio.SimpleAction.new(name='item3', parameter_type=None)
        action_item3.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_item3)

        action_item4 = Gio.SimpleAction.new(name='item4', parameter_type=None)
        action_item4.connect('activate', self.on_menu_item_clicked)
        self.add_action(action=action_item4)

        # Botão que irá conter o menu.
        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        # Adicionando o menu no botão.
        menu_button.set_menu_model(menu)
        # Adicionando o botão no headerbar.
        headerbar.pack_end(child=menu_button)

    def on_menu_item_clicked(self, widget, parameter):
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
