# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Grid()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Grid()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        grid = Gtk.Grid.new()
        # No GTK 3: set_border_width().
        grid.set_margin_top(margin=12)
        grid.set_margin_end(margin=12)
        grid.set_margin_bottom(margin=12)
        grid.set_margin_start(margin=12)

        # Definindo o espaço entre as linhas.
        grid.set_row_spacing(spacing=12)
        # Definindo o espaço entre as colunas
        grid.set_column_spacing(spacing=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=grid)

        button1 = Gtk.Button.new_with_label(label='Botão 1')
        button2 = Gtk.Button.new_with_label(label='Botão 2')
        button3 = Gtk.Button.new_with_label(label='Botão 3')
        button4 = Gtk.Button.new_with_label(label='Botão 4')
        button5 = Gtk.Button.new_with_label(label='Botão 5')
        button6 = Gtk.Button.new_with_label(label='Botão 6')

        # Adicionando de forma sequencial.
        # grid.add(widget=button1)
        # grid.add(widget=button2)
        # grid.add(widget=button3)
        # grid.add(widget=button4)
        # grid.add(widget=button5)
        # grid.add(widget=button6)

        # Posicionamento utilizando attach()
        # Determinando a posição com base em colunas e linhas.
        # grid.attach(child=button1, left=0, top=0, width=1, height=1)
        # grid.attach(child=button2, left=1, top=0, width=1, height=1)
        # grid.attach(child=button3, left=0, top=1, width=1, height=1)
        # grid.attach(child=button4, left=1, top=1, width=1, height=1)
        # grid.attach(child=button5, left=0, top=2, width=1, height=1)
        # grid.attach(child=button6, left=1, top=2, width=1, height=1)

        # Posicionamento utilizando attach_next_to()
        # Neste posicionamento utilizamos outros widget como referencia.
        # Botão 1 está na coluna 0 e linha 0
        grid.attach(child=button1, column=0, row=0, width=1, height=1)
        # Botão 2 está na coluna 1 e linha 0 e mescla 2 colunas e 1 linha.
        grid.attach(child=button2, column=1, row=0, width=2, height=1)
        # Botão 3 tem como referencia o botão 1, ele deve ficar a baixo do
        # botão 1 (BOTTOM), ele mescla 1 coluna e 2 linhas.
        grid.attach_next_to(
            child=button3,
            sibling=button1,
            side=Gtk.PositionType.BOTTOM,
            width=1, height=2
        )
        # Botão 4 tem como referência o botão 3, ele deve ficar a direita do
        # botão 3 (RIGHT), ele mescla 2 colunas e 1 linha.
        grid.attach_next_to(
            child=button4,
            sibling=button3,
            side=Gtk.PositionType.RIGHT,
            width=2,
            height=1
        )
        # Botão 5 está na coluna 1, linha 2 e mescla 1 coluna e 1 linha.
        grid.attach(child=button5, column=1, row=2, width=1, height=1)
        # Botão 6 tem mo referencia o botão 5, ele deve ficar a direita do
        # botão 5 (RIGHT), ele mescla 1 colunas e 1 linha.
        grid.attach_next_to(
            child=button6,
            sibling=button5,
            side=Gtk.PositionType.RIGHT,
            width=1,
            height=1
        )


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
    import sys

    app = Application()
    app.run(sys.argv)
