# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.HeaderBar()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.HeaderBar()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)

        button_mail = Gtk.Button.new_from_icon_name(
            icon_name='mail-send-receive-symbolic',
        )
        button_mail.connect('clicked', self._send_mail)
        headerbar.pack_end(child=button_mail)

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        headerbar.pack_start(child=hbox)

        button_left_arrow = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic',
        )
        button_left_arrow.connect('clicked', self._left_arrow)
        hbox.append(child=button_left_arrow)

        button_right_arrow = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic-rtl',
        )
        button_right_arrow.connect('clicked', self._right_arrow)
        hbox.append(child=button_right_arrow)

        text_view = Gtk.TextView.new()
        text_view.set_margin_top(margin=12)
        text_view.set_margin_end(margin=12)
        text_view.set_margin_bottom(margin=12)
        text_view.set_margin_start(margin=12)
        self.set_child(child=text_view)

    @staticmethod
    def _send_mail(widget):
        print('Você clicou no botão que tem o icone de enviar/receber email')

    @staticmethod
    def _left_arrow(widget):
        print('Você clicou no botão que tem uma seta para a esquerda')

    @staticmethod
    def _right_arrow(widget):
        print('Você clicou no botão que tem uma seta para a direita')


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
