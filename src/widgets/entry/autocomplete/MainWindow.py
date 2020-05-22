# -*- coding: utf-8 -*-
"""GTK EntryCompletion, auto completar ao digitar."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, GObject


class MainWindow(Gtk.ApplicationWindow):
    brazilian_states = [
        (1, 'Acre'), (2, 'Alagoas'), (3, 'Amapá'), (4, 'Amazonas'),
        (5, 'Bahia'), (6, 'Ceará'), (7, 'Distrito Federal'), (8, 'Espírito Santo'),
        (9, 'Goiás'), (10, 'Maranhão'), (11, 'Mato Grosso'), (12, 'Mato Grosso do Sul'),
        (13, 'Minas Gerais'), (14, 'Pará'), (15, 'Paraíba'), (16, 'Paraná'),
        (17, 'Pernambuco'), (18, 'Piauí'), (19, 'Rio de Janeiro'),
        (20, 'Rio Grande do Norte'), (21, 'Rio Grande do Sul'), (22, 'Rondônia'),
        (23, 'Roraima'), (24, 'Santa Catarina'), (25, 'São Paulo'), (26, 'Sergipe'),
        (27, 'Tocantins'),
    ]

    def __init__(self):
        super().__init__()
        self.set_title(title='GTK EntryCompletion, auto completar ao digitar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        liststore = Gtk.ListStore.new([GObject.TYPE_INT, GObject.TYPE_STRING])
        for state in self.brazilian_states:
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
