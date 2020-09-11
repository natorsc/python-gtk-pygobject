# -*- coding: utf-8 -*-
"""Drag and Drop."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk, Gdk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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

        self.show_all()

    def on_drag_data_received(self, widget, drag_context, x, y, data, info, timestamp):
        print('Widget que recebeu o arquivo (connect()) :', widget)
        print('Drag context                             :', drag_context)
        print('timestamp                                :', timestamp)
        print('ID que foi passada                       :', info)
        print('Selection data                           :', data)
        print('Caminho até o arquivo (uri)              :', data.get_uris())
        print(f'Arquivo foi solta na janela na posição x={x} e y={y}')


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
