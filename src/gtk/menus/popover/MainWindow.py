# -*- coding: utf-8 -*-
"""Menu popover."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Menu popover')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')

        # Criando headerbar.
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title(title='Menu popover')
        headerbar.set_subtitle(subtitle='Menu popover')
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
        menu_button.connect('clicked', self._show_menu)
        # Adicionando o botão no headerbar.
        headerbar.pack_end(child=menu_button)

        # Box que irá conter os widgets do menu popover.
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=24)

        # Criando o menu do tipo popover.
        self.menu = Gtk.Popover.new(relative_to=menu_button)
        self.menu.add(vbox)
        menu_button.set_popover(popover=self.menu)

        # Utilizando `Gtk.EventBox.new()`.
        item1_eventbox = Gtk.EventBox.new()
        item1_eventbox.connect('button-press-event', self._event_box_callback)
        item1 = Gtk.Label.new(str='Item 1')
        item1_eventbox.add(item1)
        vbox.pack_start(child=item1_eventbox, expand=True, fill=True, padding=0)

        # Utilizando `set_events()`
        item2 = Gtk.Label.new(str='Item 2')
        item2.set_has_window(True)
        item2.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        item2.connect('button-press-event', self._event_button_press)
        vbox.pack_start(child=item2, expand=True, fill=True, padding=0)

        # Separador.
        separator = Gtk.Separator.new(orientation=Gtk.Orientation.HORIZONTAL)
        vbox.pack_start(child=separator, expand=True, fill=True, padding=0)

        # Utilizando `ModelButton()`.
        item3 = Gtk.ModelButton.new()
        item3.set_label(label='Sobre')
        item3.connect('clicked', self._about)
        vbox.pack_start(child=item3, expand=True, fill=True, padding=0)

    def _show_menu(self, widget):
        self.menu.show_all()

    def _event_box_callback(self, GtkEventBox, GdkEventButton):
        widget = GtkEventBox.get_child()
        print(widget.get_label())
        self.menu.popdown()

    def _event_button_press(self, widget, GdkEventButton):
        print(widget.get_label())
        self.menu.popdown()

    def _about(self, widget):
        self.menu.popdown()
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
