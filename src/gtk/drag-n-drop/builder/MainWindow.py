# -*- coding: utf-8 -*-
"""Drag and Drop."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


@Gtk.Template(filename='MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    drop_area = Gtk.Template.Child(name='drop-area')

    def __init__(self):
        super().__init__()
        target_entry = Gtk.TargetEntry.new(
            target='text/uri-list',
            flags=Gtk.TargetFlags.OTHER_APP,
            info=8000,
        )

        self.drop_area.drag_dest_set(
            flags=Gtk.DestDefaults.ALL,
            targets=[target_entry],
            actions=Gdk.DragAction.COPY,
        )

    @Gtk.Template.Callback()
    def on_drag_data_received(self, widget, drag_context, x, y, data, info, timestamp):
        print('Widget que recebeu o arquivo (connect()) :', widget)
        print('Drag context                             :', drag_context)
        print('timestamp                                :', timestamp)
        print('ID que foi passada                       :', info)
        print('Selection data                           :', data)
        print('Caminho até o arquivo (uri)              :', data.get_uris())
        print(f'Arquivo foi solta na janela na posição x={x} e y={y}')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
