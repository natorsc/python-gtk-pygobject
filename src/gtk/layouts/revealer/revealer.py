# -*- coding: utf-8 -*-
"""Container do tipo Revealer Layout.

Revealer Layout tem a função de exibir ou ocultar widgets que estejam
contidos dentro de si.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Revealer Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        grid = Gtk.Grid.new()
        grid.set_border_width(border_width=12)
        self.add(widget=grid)

        self.revealer = Gtk.Revealer.new()
        # Definindo que ele não deve exibir o seu conteúdo.
        self.revealer.set_reveal_child(reveal_child=False)
        # Definindo o tempo da transição.
        self.revealer.set_transition_duration(duration=1000)
        # Definindo o tipo da tansição.
        self.revealer.set_transition_type(
            transition=Gtk.RevealerTransitionType.CROSSFADE
        )
        # Posição do Revealer Layout no Grid Layout.
        grid.attach(child=self.revealer, left=1, top=1, width=1, height=1)

        button_1 = Gtk.Button.new_with_label(label='Exibir/Ocultar')
        button_1.connect('clicked', self._show_hide_widget)
        grid.attach(child=button_1, left=0, top=0, width=1, height=1)

        button_2 = Gtk.Button.new_with_label(label='Botão 2')
        self.revealer.add(widget=button_2)

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
