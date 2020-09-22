# -*- coding: utf-8 -*-
"""Drag and Drop."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk, Gdk


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    drop_area = Gtk.Template.Child(name='drop-area')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.drop_area.drag_dest_set(
            flags=Gtk.DestDefaults.ALL,
            targets=[],
            actions=Gdk.DragAction.COPY,
        )
        self.drop_area.drag_dest_add_image_targets()
        self.drop_area.drag_dest_add_text_targets()
        self.drop_area.drag_dest_add_uri_targets()

    @Gtk.Template.Callback()
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
