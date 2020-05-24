# -*- coding: utf-8 -*-
"""Drag and Drop."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


class Handler:
    def __init__(self):
        target_entry = Gtk.TargetEntry.new(
            target='text/uri-list',
            flags=Gtk.TargetFlags.OTHER_APP,
            info=8000,
        )

        drop_area = builder.get_object(name='drop-area')
        drop_area.drag_dest_set(
            flags=Gtk.DestDefaults.ALL,
            targets=[target_entry],
            actions=Gdk.DragAction.COPY,
        )

    def on_drag_data_received(self, widget, drag_context, x, y, data, info, timestamp):
        print('Widget que recebeu o arquivo (connect()) :', widget)
        print('Drag context                             :', drag_context)
        print('timestamp                                :', timestamp)
        print('ID que foi passada                       :', info)
        print('Selection data                           :', data)
        print('Caminho até o arquivo (uri)              :', data.get_uris())
        print(f'Arquivo foi solta na janela na posição x={x} e y={y}')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
