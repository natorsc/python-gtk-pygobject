# -*- coding: utf-8 -*-
"""GTK Menu."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='GTK Menu')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Criando headerbar.
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title(title='GTK Menu')
        headerbar.set_subtitle(subtitle='GTK Menu')
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

        # Criando o menu.
        menu = Gtk.Menu.new()
        menu.set_border_width(border_width=6)
        menu_button.set_popup(menu=menu)

        # Item que será inserido no menu.
        item1 = Gtk.MenuItem.new_with_label(label='Item 1')
        # Ação que é realizada quando o item é clicado.
        item1.connect('activate', self.menu_item_clicked)
        # Adicionando o item.
        menu.add(widget=item1)

        item2 = Gtk.MenuItem.new_with_label(label='Item 2')
        item2.connect('activate', self.menu_item_clicked)
        menu.add(widget=item2)

        separator = Gtk.SeparatorMenuItem.new()
        menu.add(widget=separator)

        item3 = Gtk.MenuItem.new_with_label(label='Sobre')
        item3.connect('activate', self.about)
        menu.add(widget=item3)

        # Construindo o menu.
        menu.show_all()

    def menu_item_clicked(self, widget):
        print(widget.get_label())

    def about(self, widget):
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
