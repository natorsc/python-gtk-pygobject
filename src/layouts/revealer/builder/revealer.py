# -*- coding: utf-8 -*-
"""Contêiner do tipo Overlay Layout"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./revealer.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    revealer = Gtk.Template.Child(name='revealer')

    @Gtk.Template.Callback()
    def _show_hide_widget(self, widget):
        # Verificando se o botão está sendo exibido ou não.
        # get_reveal_child() retorna True ou False.
        show = self.revealer.get_reveal_child()

        # Laço de decisão altera o estado de exibição.
        if show:
            self.revealer.set_reveal_child(reveal_child=False)
        else:
            self.revealer.set_reveal_child(reveal_child=True)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
