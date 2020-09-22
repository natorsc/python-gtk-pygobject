# -*- coding: utf-8 -*-
"""Signals e Slots utilizando-se um dicionário.

Neste arquivo o acesso ao método é feito utilizando:

.. code-block:: xml

    <signal name="clicked" handler="_on_button_clicked" swapped="no"/>

No arquivo de interface o valor da variável `handler` do arquivo de interface
deve ser o mesmo da chave do dicionário criado no Python.

Neste caso não é necessário acessar o objeto do botão uma vez que não será
utilizado o `connect()` para vincular o sinal a uma ação (slot).
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


def on_button_clicked(button):
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
    # Dicionário para registrar os métodos.
    # Nome da chave deve ser o mesmo que foi criado no arquivo de interface.
    handlers = {
        'on_button_clicked': on_button_clicked
    }

    builder = Gtk.Builder.new()
    builder.add_from_file(filename='window-with-signal.glade')
    # Conectando os sinais da interface com os métodos criados no Python.
    builder.connect_signals(obj_or_map=handlers)

    # Acessando os widgets do arquivo de inteface.
    label = builder.get_object(name='label')
    entry = builder.get_object(name='entry')

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
