# -*- coding: utf-8 -*-
"""Signal e Slots."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Signal e Slots.')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

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


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
