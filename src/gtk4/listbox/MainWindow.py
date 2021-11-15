# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.ListBox()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):
    # Dados que serão inseridos nas linhas do listbox_2
    itens = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.ListBox()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_homogeneous(homogeneous=True)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        listbox_1 = Gtk.ListBox.new()
        # Definindo o modo de seleção.
        listbox_1.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        vbox.append(child=listbox_1)

        # Loop para criar os widgets.
        for n in range(1, 4):
            row = Gtk.ListBoxRow.new()
            row.set_selectable(selectable=False)

            hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            # Adicionando container na linha
            row.set_child(child=hbox)

            label = Gtk.Label.new(str=f'Linha {n}')
            label.set_margin_top(margin=6)
            label.set_margin_end(margin=6)
            label.set_margin_bottom(margin=6)
            label.set_margin_start(margin=6)
            label.set_xalign(xalign=0)
            label.set_hexpand(expand=True)
            hbox.append(child=label)

            switch = Gtk.Switch.new()
            switch.set_margin_top(margin=6)
            switch.set_margin_end(margin=6)
            switch.set_margin_bottom(margin=6)
            switch.set_margin_start(margin=6)
            hbox.append(child=switch)

            listbox_1.append(child=row)

        # Criando um segundo ListBox
        listbox_2 = Gtk.ListBox.new()

        # Definindo um sinal (evento).
        listbox_2.connect('row-activated', self._on_row_clicked)
        vbox.append(child=listbox_2)

        # Loop para criar as linhas.
        for item in self.itens:
            label = Gtk.Label.new(str=item)
            label.set_margin_top(6)
            label.set_margin_bottom(6)
            listbox_2.append(child=label)

    def _on_row_clicked(self, listbox, listboxrow):
        print(f'Clicou no {self.itens[listboxrow.get_index()]}')


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
