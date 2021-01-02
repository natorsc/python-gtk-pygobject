# -*- coding: utf-8 -*-
"""Gtk.Popover()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, GdkPixbuf


class Handler:
    logo = GdkPixbuf.Pixbuf.new_from_file(filename='../../../assets/icons/icon.png')

    def __init__(self):
        pass

    def menu_item_clicked(self, widget):
        print(widget.props.text)

    def about(self, widget):
        about = Gtk.AboutDialog.new()
        about.set_transient_for(parent=win)
        about.set_logo(logo=self.logo)
        about.set_authors(authors=('Renato Cruz',))
        about.set_comments(
            comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore '
                     'magna aliqua.'
        )
        about.set_website(website='https://github.com/natorsc/gui-python-gtk')
        about.run()
        about.destroy()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
