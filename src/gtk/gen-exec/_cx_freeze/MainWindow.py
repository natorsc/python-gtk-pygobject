# -*- coding: utf-8 -*-
"""Gerando um executável com Cx_Freeze."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gerando um executável com Cx_Freeze')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='./icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        self.entry = Gtk.Entry.new()
        self.entry.set_placeholder_text(text='Digite algo')
        vbox.pack_start(child=self.entry, expand=False, fill=True, padding=0)

        self.label = Gtk.Label.new(str='Este texto será alterado!')
        vbox.pack_start(child=self.label, expand=True, fill=True, padding=0)

        button = Gtk.Button.new_with_label(label='Clique Aqui')
        button.connect('clicked', self._on_button_clicked)
        vbox.pack_end(child=button, expand=False, fill=True, padding=0)

        self.show_all()

    def _on_button_clicked(self, button):
        """Método é chamado quando o botão da interface é pressionado.

        Caso haja algum texto/caractere no campo de entrada de texto o
        texto será exibido no label da interface, caso não haja
        texto é exibida outra mensagem.

        :param button: Instância do objeto ``Gtk.Button()``. Basicamente
        informaçõe do botão que foi pressionado.
        """
        if self.entry.get_text():
            self.label.set_label(str=self.entry.get_text())
        else:
            self.label.set_label(str='Digite algo no campo acima!')


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
