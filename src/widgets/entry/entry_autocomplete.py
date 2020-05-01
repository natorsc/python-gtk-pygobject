# -*- coding: utf-8 -*-
"""GTK EntryCompletion."""
import sqlite3

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='GTK EntryCompletion')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        con = sqlite3.connect('../data/db.sqlite3')
        cur = con.cursor()
        query = 'SELECT rowid, state FROM brazilian_states;'
        cur.execute(query)
        brazilian_states = cur.fetchall()

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        liststore = Gtk.ListStore(int, str)
        for state in brazilian_states:
            liststore.append(row=state)

        completion = Gtk.EntryCompletion.new()
        completion.set_model(model=liststore)
        completion.set_text_column(column=1)

        entry = Gtk.Entry.new()
        entry.set_completion(completion=completion)
        vbox.add(widget=entry)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
