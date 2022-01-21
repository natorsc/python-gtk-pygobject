# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Overlay()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Overlay()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        overlay = Gtk.Overlay.new()
        self.set_child(child=overlay)

        button = Gtk.Button.new_with_label(
            label='Este botão está abaixo dos outros',
        )
        overlay.add_overlay(widget=button)

        button_go_previous = Gtk.Button.new_from_icon_name(
            icon_name='go-previous',
        )
        button_go_previous.set_halign(align=Gtk.Align.START)
        button_go_previous.set_valign(align=Gtk.Align.CENTER)
        overlay.add_overlay(widget=button_go_previous)

        button_go_next = Gtk.Button.new_from_icon_name(
            icon_name='go-next',
        )
        button_go_next.set_halign(align=Gtk.Align.END)
        button_go_next.set_valign(align=Gtk.Align.CENTER)
        overlay.add_overlay(widget=button_go_next)


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
