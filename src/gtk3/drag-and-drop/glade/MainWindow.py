# -*- coding: utf-8 -*-
"""Drag and Drop."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


class Handler:

    def __init__(self):
        drop_area = builder.get_object(name='drop_area')
        drop_area.drag_dest_set(
            flags=Gtk.DestDefaults.ALL,
            targets=[],
            actions=Gdk.DragAction.COPY,
        )
        drop_area.drag_dest_add_image_targets()
        drop_area.drag_dest_add_text_targets()
        drop_area.drag_dest_add_uri_targets()

    def on_drag_data_received(self, widget, context, x, y, data, info, time):
        print('ARGS:')
        print(f'Widget que recebeu o arquivo (connect()): {widget}')
        print(f'Drag context: {context}')
        print(f'Objeto solto posição: x={x} e y={y}')
        print(f'timestamp: {time}')
        print(f'info: {info}')
        print(f'data: {data}')
        print('===')
        print('DATA:')
        print(f'get_data: {data.get_data()}')
        print(f'get_data_type: {data.get_data_type()}')
        print(f'get_display: {data.get_display()}')
        print(f'get_format: {data.get_format()}')
        print(f'get_length: {data.get_length()}')
        print(f'get_pixbuf: {data.get_pixbuf()}')
        print(f'get_selection: {data.get_selection()}')
        print(f'get_target: {data.get_target()}')
        print(f'get_targets: {data.get_targets()}')
        print(f'get_uris: {data.get_uris()}')
        print(f'get_text: {data.get_text()}')
        print('===\n')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
