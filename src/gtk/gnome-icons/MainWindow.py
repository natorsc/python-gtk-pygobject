# -*- coding: utf-8 -*-
"""Ícones standard e symbolic."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):
    # Nome dos ícones.
    standard = ['mail-send-receive', 'user-trash', 'face-smile']
    symbolic = ['mail-send-receive-symbolic', 'user-trash-symbolic',
                'face-smile-symbolic']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Ícones standard e symbolic.')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        paned = Gtk.Paned.new(orientation=Gtk.Orientation.HORIZONTAL)
        paned.set_border_width(border_width=12)
        self.add(widget=paned)

        # Criando um Box Layout para comportar os widgets
        # que serão inseridos no painel 1.
        vbox_standard = Gtk.Box.new(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=0
        )
        # Adicionando vbox_standard no painel 1.
        paned.pack1(child=vbox_standard, resize=False, shrink=False)

        # Criando outro Box Layout para comportar os widgets que serão
        # inseridos no painel 2.
        vbox_symbolic = Gtk.Box.new(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=0
        )
        # Adicionando vbox_symbolic2 no painel 2.
        paned.pack2(child=vbox_symbolic, resize=False, shrink=False)

        # Criando labels.
        label_standard = Gtk.Label.new(str='Ícones Standard')
        vbox_standard.pack_start(
            child=label_standard,
            expand=True,
            fill=True,
            padding=0
        )

        label_symbolic = Gtk.Label.new(str='Ícones Symbolic')
        vbox_symbolic.pack_start(
            child=label_symbolic,
            expand=True,
            fill=True,
            padding=0
        )

        # Adicionando os ícones.
        for icone in self.standard:
            imagem = Gtk.Image.new_from_icon_name(
                icon_name=icone,
                size=Gtk.IconSize.DIALOG
            )
            vbox_standard.pack_start(
                child=imagem,
                expand=True,
                fill=True,
                padding=0
            )

        for icone in self.symbolic:
            imagem = Gtk.Image.new_from_icon_name(
                icon_name=icone,
                size=Gtk.IconSize.DIALOG
            )
            vbox_symbolic.pack_start(
                child=imagem,
                expand=True,
                fill=True,
                padding=0
            )

        self.show_all()


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
