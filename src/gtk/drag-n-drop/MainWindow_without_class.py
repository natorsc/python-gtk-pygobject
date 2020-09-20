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

        drop_area = Gtk.Label.new(str='Arraste e solte o arquivo aqui')
        drop_area.drag_dest_set(
            flags=Gtk.DestDefaults.ALL,
            targets=[],
            actions=Gdk.DragAction.COPY,
        )
        drop_area.drag_dest_add_image_targets()
        drop_area.drag_dest_add_text_targets()
        drop_area.drag_dest_add_uri_targets()
        drop_area.connect('drag-data-received', self.on_drag_data_received)
        vbox.pack_start(child=drop_area, expand=True, fill=True, padding=0)

        self.show_all()

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
