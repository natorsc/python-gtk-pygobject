# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject drag and drop."""

import gi

gi.require_version(namespace='Gdk', version='4.0')
gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gdk, Gio, GObject, Gtk


class DropArea(Gtk.Label):

    def __init__(self):
        super().__init__()

        self.set_label(str='Arraste e solte o arquivo aqui (class DropArea)')
        drag_source = Gtk.DragSource.new()
        drag_source.set_actions(Gdk.DragAction.COPY)
        drag_source.connect('prepare', self.on_prepare)
        drag_source.connect('drag-begin', self.on_drag_begin)
        drag_source.connect('drag-end', self.on_drag_end)
        drag_source.connect('drag-cancel', self.on_drag_cancel)

        drop_target = Gtk.DropTarget.new(GObject.TYPE_STRING, Gdk.DragAction.COPY)
        drop_target.connect('drop', self.on_drop)

        self.add_controller(drag_source)
        self.add_controller(drop_target)

    def on_prepare(self, DropTarget, x, y):
        print('[!] drag_source (prepare) [!]')
        print(f'Widget = {DropTarget}')
        print(f'Posição no eixo x = {x}')
        print(f'Posição no eixo y = {y}')

    def on_drag_begin(self):
        print('[!] drag_source (drag_begin) [!]')

    def on_drag_end(self):
        print('[!] drag_source (drag_end) [!]')

    def on_drag_cancel(self):
        print('[!] drag_source (drag_cancel) [!]')

    def on_drop(self, DropTarget, data, x, y):
        print('[!] drop_target (drop) [!]')
        print(f'Widget = {DropTarget}')
        print(f'Data = {data}')
        print(f'Posição no eixo x = {x}')
        print(f'Posição no eixo y = {y}')


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject drag and drop')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_homogeneous(homogeneous=True)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        drag_source = Gtk.DragSource.new()
        drag_source.set_actions(Gdk.DragAction.COPY)
        drag_source.connect('prepare', self.on_prepare)
        drag_source.connect('drag-begin', self.on_drag_begin)
        drag_source.connect('drag-end', self.on_drag_end)
        drag_source.connect('drag-cancel', self.on_drag_cancel)

        drop_target = Gtk.DropTarget.new(GObject.TYPE_STRING, Gdk.DragAction.COPY)
        drop_target.connect('drop', self.on_drop)

        label = Gtk.Label.new('Arraste e solte algo aqui.')
        label.add_controller(drag_source)
        label.add_controller(drop_target)
        vbox.append(child=label)

        # class DropArea(Gtk.Label).
        drop_area = DropArea()
        vbox.append(child=drop_area)

    def on_prepare(self, DropTarget, x, y):
        print('[!] drag_source (prepare) [!]')
        print(f'Widget = {DropTarget}')
        print(f'Posição no eixo x = {x}')
        print(f'Posição no eixo y = {y}')

    def on_drag_begin(self):
        print('[!] drag_source (drag_begin) [!]')

    def on_drag_end(self):
        print('[!] drag_source (drag_end) [!]')

    def on_drag_cancel(self):
        print('[!] drag_source (drag_cancel) [!]')

    def on_drop(self, DropTarget, data, x, y):
        print('[!] drop_target (drop) [!]')
        print(f'Widget = {DropTarget}')
        print(f'Data = {data}')
        print(f'Posição no eixo x = {x}')
        print(f'Posição no eixo y = {y}')


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
    import sys

    app = Application()
    app.run(sys.argv)
