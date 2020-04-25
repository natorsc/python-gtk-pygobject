# -*- coding: utf-8 -*-
"""Carregando um arquivo CSS personalizado."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


class Handler:
    def __init__(self):
        self._set_custom_css(file='../css/custom.css')

        self.label = builder.get_object(name='label')
        self.entry = builder.get_object(name='entry')

    @staticmethod
    def _set_custom_css(file):
        css_provider = Gtk.CssProvider.new()
        css_provider.load_from_path(path=file)

        screen = Gdk.Screen()

        style_context = Gtk.StyleContext.new()
        style_context.add_provider_for_screen(
            screen=screen.get_default(),
            provider=css_provider,
            priority=Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

    def _on_button_clicked(self, button):
        """Método é chamado quando o botão da interface é pressionado.

        Caso haja algum texto/caractere no campo de entrada de texto o
        texto será exibido no label da interface, caso não haja
        é exibida outra mensagem.

        :param button: Instância do objeto ``Gtk.Button()``. Basicamente
        informações do botão que foi pressionado.
        """
        if self.entry.get_text():
            self.label.set_label(str=self.entry.get_text())
        else:
            self.label.set_label(str='Digite algo no campo acima!')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())
    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
