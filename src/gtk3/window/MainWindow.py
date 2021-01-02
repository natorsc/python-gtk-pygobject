# -*- coding: utf-8 -*-
"""Gtk.Window()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.ApplicationWindow')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        # Widgets.
        button = Gtk.Button.new_with_label('Abrir janela')
        button.connect('clicked', self.on_button_clicked)
        vbox.pack_start(child=button, expand=False, fill=True, padding=0)
        self.show_all()

    def on_button_clicked(self, widget):
        window = Gtk.Window.new(type=Gtk.WindowType.TOPLEVEL)
        window.set_transient_for(parent=self)
        window.set_modal(modal=True)
        window.set_title(title='Gtk.Window')
        window.set_default_size(width=1366 / 3, height=768 / 3)
        window.set_size_request(width=1366 / 3, height=768 / 3)
        window.set_position(position=Gtk.WindowPosition.CENTER)
        window.set_default_icon_from_file(filename='../../assets/icons/person.png')
        window.show_all()


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
