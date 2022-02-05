# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Window()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class NewWindow(Gtk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_modal(modal=True)
        self.set_title(title='Python e GTK 4: PyGObject Gtk.Window()')
        self.set_default_size(width=int(1366 / 3), height=int(768 / 3))
        self.set_size_request(width=int(1366 / 3), height=int(768 / 3))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        vbox.set_valign(Gtk.Align.CENTER)
        self.set_child(child=vbox)

        # Widgets.
        button = Gtk.Button.new_with_label('Fechar janela')
        button.connect('clicked', self.on_window_button_close_clicked)
        vbox.append(child=button)

        self.show()

    def on_window_button_close_clicked(self, widget):
        self.destroy()


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.ApplicationWindow()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        vbox.set_valign(Gtk.Align.CENTER)
        self.set_child(child=vbox)

        # Widgets.
        button = Gtk.Button.new_with_label('Abrir janela')
        button.connect('clicked', self.on_button_clicked)
        vbox.append(child=button)

    def on_button_clicked(self, widget):
        # window = Gtk.Window.new()
        # window.set_transient_for(parent=self)
        # window.set_modal(modal=True)
        # window.set_title(title='Python e GTK 4: PyGObject Gtk.Window()')
        # window.set_default_size(width=int(1366 / 3), height=int(768 / 3))
        # window.set_size_request(width=int(1366 / 3), height=int(768 / 3))
        # window.show()

        # Usando uma classe (recomendado).
        NewWindow(transient_for=self)


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
