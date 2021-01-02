# -*- coding: utf-8 -*-
"""Gtk.MenuButton()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.MenuButton')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Criando headerbar.
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title(title='Gtk.MenuButton')
        headerbar.set_subtitle(subtitle='Gtk.MenuButton')
        headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=headerbar)

        # Ícone que será exibido no botão do menu.
        menu_button_image = Gtk.Image.new_from_icon_name(
            icon_name='open-menu-symbolic',
            size=Gtk.IconSize.MENU,
        )

        # Botão que irá conter o popover.
        menu_button = Gtk.MenuButton.new()
        menu_button.add(widget=menu_button_image)
        # Adicionando o botão no headerbar.
        headerbar.pack_end(child=menu_button)

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
