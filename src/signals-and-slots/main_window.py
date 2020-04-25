# -*- coding: utf-8 -*-
"""Signals e Slots."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


def _on_button_clicked(button):
    """Método é chamado quando o botão da interface é pressionado.

    Caso haja algum texto/caractere no campo de entrada de texto o
    texto será exibido no label da interface, caso não haja
    texto é exibida outra mensagem.

    :param button: Instância do objeto ``Gtk.Button()``. Basicamente
    informaçõe do botão que foi pressionado.
    """
    if entry.get_text():
        label.set_label(str=entry.get_text())
    else:
        label.set_label(str='Digite algo no campo acima!')


win = Gtk.ApplicationWindow()
win.set_title(title='Python com GTK')
win.set_default_size(width=1366 / 2, height=768 / 2)
win.set_position(position=Gtk.WindowPosition.CENTER)
win.set_default_icon_from_file(filename='../assets/icons/icon.png')
win.connect('destroy', Gtk.main_quit)

vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
vbox.set_border_width(border_width=12)
win.add(widget=vbox)

entry = Gtk.Entry.new()
entry.set_placeholder_text(text='Digite algo')
vbox.pack_start(child=entry, expand=False, fill=True, padding=0)

label = Gtk.Label.new(str='Este texto será alterado!')
vbox.pack_start(child=label, expand=True, fill=True, padding=0)

button = Gtk.Button.new_with_label(label='Clique Aqui')
button.connect('clicked', _on_button_clicked)
vbox.pack_end(child=button, expand=False, fill=True, padding=0)

win.show_all()

Gtk.main()
