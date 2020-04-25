# -*- coding: utf-8 -*-
"""Aplicando estilo via propriedade `name` (Gnome Builder).

Propriedade `name` é adicionada via arquivo de interface
e arquivo css é carregado via linguagem de programação.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, Gdk


@Gtk.Template(filename='./mainwindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    entry = Gtk.Template.Child(name='entry')
    label = Gtk.Template.Child(name='label')

    def __init__(self):
        super().__init__()
        self._set_custom_css(file='../css/custom.css')

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

    @Gtk.Template.Callback()
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
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
