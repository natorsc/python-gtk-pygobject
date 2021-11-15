# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.FlowBox()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.FlowBox()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 6, height=768 / 6)

        self.fixed = Gtk.Fixed.new()
        self.fixed.set_margin_top(margin=12)
        self.fixed.set_margin_end(margin=12)
        self.fixed.set_margin_bottom(margin=12)
        self.fixed.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=self.fixed)

        scrolled_window = Gtk.ScrolledWindow.new()
        # Adicionando a barra de rolagem na janela principal.
        self.set_child(child=scrolled_window)

        flowbox = Gtk.FlowBox.new()
        flowbox.set_margin_top(margin=12)
        flowbox.set_margin_end(margin=12)
        flowbox.set_margin_bottom(margin=12)
        flowbox.set_margin_start(margin=12)
        # Definindo o alinhamento dos widgets no container.
        flowbox.set_valign(align=Gtk.Align.START)
        # Definindo quantos widgets por linha.
        flowbox.set_max_children_per_line(n_children=5)
        # Definindo se os widgets podem ser selecionados.
        flowbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        # Adicionando o FloBox na barra de rolagem (ScrolledWindow).
        scrolled_window.set_child(child=flowbox)

        # Utilizando um laço de repetição para criar alguns botões.
        for n in range(100):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            flowbox.insert(widget=button, position=n)


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
