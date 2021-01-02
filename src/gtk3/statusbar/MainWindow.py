# -*- coding: utf-8 -*-
"""Gtk.Statusbar()."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):
    context_id = None
    message_id = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.Statusbar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        btn_show_msg = Gtk.Button.new_with_label(label='Exibir menssagem')
        btn_show_msg.connect('clicked', self.statusbar_show_msg)
        vbox.pack_start(child=btn_show_msg, expand=False, fill=True, padding=0)

        btn_remove_msg = Gtk.Button.new_with_label(label='Remover mensagem')
        btn_remove_msg.connect('clicked', self.statusbar_remove_msg)
        vbox.pack_start(child=btn_remove_msg, expand=False, fill=True, padding=0)

        self.statusbar = Gtk.Statusbar.new()
        self.context_id = self.statusbar.get_context_id(context_description='exemplo')
        vbox.pack_end(child=self.statusbar, expand=False, fill=True, padding=0)

        self.show_all()

    def statusbar_show_msg(self, widget):
        self.message_id = self.statusbar.push(
            context_id=self.context_id,
            text='Texto que será exibido no statusbar.',
        )
        print(self.message_id)

    def statusbar_remove_msg(self, widget):
        # self.statusbar.remove(
        #     context_id=self.context_id,
        #     message_id=self.message_id,
        # )
        self.statusbar.remove_all(context_id=self.context_id)


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
