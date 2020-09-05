# -*- coding: utf-8 -*-
"""Drag and Drop."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Drag and Drop')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_default_icon_from_file(filename='../../../images/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        target_entry = Gtk.TargetEntry.new(
            target='text/uri-list',
            flags=Gtk.TargetFlags.OTHER_APP,
            info=8000,
        )

        drop_area = Gtk.Label.new(str='Arraste e solte o arquivo aqui')
        drop_area.drag_dest_set(
            flags=Gtk.DestDefaults.ALL,
            targets=[target_entry],
            actions=Gdk.DragAction.COPY,
        )
        drop_area.connect('drag-data-received', self.on_drag_data_received)
        vbox.pack_start(child=drop_area, expand=True, fill=True, padding=0)

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
