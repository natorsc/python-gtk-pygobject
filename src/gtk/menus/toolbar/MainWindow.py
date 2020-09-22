# -*- coding: utf-8 -*-
"""GTK menu toolbar."""

import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='GTK Toolbar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.add(widget=vbox)

        toolbar = Gtk.Toolbar.new()
        vbox.pack_start(child=toolbar, expand=False, fill=False, padding=0)

        item_exit = Gtk.ToolButton.new(icon_widget=None, label='Sair')
        item_exit.set_icon_name(icon_name='application-exit-symbolic')
        item_exit.connect('clicked', self.menu_item_clicked)
        toolbar.insert(item=item_exit, pos=0)

        item_about = Gtk.ToolButton.new(icon_widget=None, label='Sobre')
        item_about.set_icon_name(icon_name='help-about-symbolic')
        item_about.connect('clicked', self.about)
        toolbar.insert(item=item_about, pos=1)

        self.show_all()

    def menu_item_clicked(self, widget):
        print(widget.get_label())

    def about(self, widget):
        about = Gtk.AboutDialog.new()
        about.set_transient_for(parent=self)
        about.set_authors(authors=['Renato Cruz'])
        about.set_comments(
            comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore '
                     'magna aliqua.'
        )
        about.set_website(website='https://github.com/natorsc/gui-python-gtk')
        about.run()
        about.destroy()


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
    app = Application()
    app.run(sys.argv)
