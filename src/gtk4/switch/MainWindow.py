# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Switch()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Switch()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        grid = Gtk.Grid.new()
        grid.set_margin_top(margin=12)
        grid.set_margin_end(margin=12)
        grid.set_margin_bottom(margin=12)
        grid.set_margin_start(margin=12)
        self.set_child(child=grid)

        switch = Gtk.Switch.new()
        switch.connect('notify::active', self.on_switch_button_clicked)
        grid.attach(child=switch, column=0, row=0, width=1, height=1)

    def on_switch_button_clicked(self, widget, g_param):
        if widget.get_active():
            print('Botão marcado')
        else:
            print('Botão desmarcado')


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
