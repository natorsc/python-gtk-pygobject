# -*- coding: utf-8 -*-
"""Contêiner do tipo FlowBox Layout.

Neste gerenciador de layout os widget são posicionados horizontalmente,
da esquerda para a direita.

É possível definir quantos widgets são posicionados na linha.

Ao se ajustar a janela principal os widgets são reorganizados dentro
do gerenciador de layout.

Para evitar problemas de exibição dos widgets é recomendada a utilização
de um ``ScrolledWindow()`` (barra de rolagem).
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='FlowBox Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')


        scrolled = Gtk.ScrolledWindow.new(hadjustment=None, vadjustment=None)

        # Não é necessário declarar ``.set_policy()`` a menos que o scroll
        # apresente algum comportamento estranho.
        # scrolled.set_policy(
        #     hscrollbar_policy=Gtk.PolicyType.EXTERNAL,
        #     vscrollbar_policy=Gtk.PolicyType.EXTERNAL
        # )

        # Adicionando a barra de rolagem na janela principal.
        self.add(widget=scrolled)

        flowbox = Gtk.FlowBox.new()
        flowbox.set_border_width(border_width=12)
        # Definindo o alinhamento dos widgets no container.
        flowbox.set_valign(align=Gtk.Align.START)
        # Definindo quantos widgets por linha.
        flowbox.set_max_children_per_line(n_children=5)
        # Definindo se os widgets podem ser selecionados.
        flowbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        # Adicionando o FloBox na barra de rolagem (ScrolledWindow).
        scrolled.add(widget=flowbox)

        # Utilizando um laço de repetição para criar alguns botões.
        for n in range(100):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            flowbox.add(button)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
