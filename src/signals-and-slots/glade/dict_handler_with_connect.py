# -*- coding: utf-8 -*-
"""Signals e Slots utilizando-se um dicionário.

O arquivo de interface não tem a tag:

.. code-block:: xml

    <signal name="clicked" handler="_on_button_clicked" swapped="no"/>

Neste caso é necessário utilizar o `connect()` para vincular o sinal a uma ação
(slot).
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


def _on_button_clicked(button):
    """Método é chamado quando o botão da interface é pressionado.

    Caso haja algum texto/caractere no campo de entrada de texto o
    texto será exibido no label da interface, caso não haja
    é exibida outra mensagem.

    :param button: Instância do objeto ``Gtk.Button()``. Basicamente
    informações do botão que foi pressionado.
    """
    if entry.get_text():
        label.set_label(str=entry.get_text())
    else:
        label.set_label(str='Digite algo no campo acima!')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='window-without-signal.glade')

    # Acessando os widgets do arquivo de inteface.
    label = builder.get_object(name='label')
    entry = builder.get_object(name='entry')

    button = builder.get_object(name='button')
    button.connect('clicked', _on_button_clicked)

    window = builder.get_object(name='MainWindow')
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()
