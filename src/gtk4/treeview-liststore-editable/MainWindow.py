# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.TreeView() editable."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gtk, Gio, Pango, GObject


class MainWindow(Gtk.ApplicationWindow):
    brazilian_states = [
        (1, 'Acre'), (2, 'Alagoas'), (3, 'Amapá'), (4, 'Amazonas'),
        (5, 'Bahia'), (6, 'Ceará'), (7, 'Distrito Federal'), (8, 'Espírito Santo'),
        (9, 'Goiás'), (10, 'Maranhão'), (11, 'Mato Grosso'), (12, 'Mato Grosso do Sul'),
        (13, 'Minas Gerais'), (14, 'Pará'), (15, 'Paraíba'), (16, 'Paraná'),
        (17, 'Pernambuco'), (18, 'Piauí'), (19, 'Rio de Janeiro'),
        (20, 'Rio Grande do Norte'), (21, 'Rio Grande do Sul'), (22, 'Rondônia'),
        (23, 'Roraima'), (24, 'Santa Catarina'), (25, 'São Paulo'), (26, 'Sergipe'),
        (27, 'Tocantins'),
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.TreeView() editable')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_homogeneous(homogeneous=True)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        # Janela com rolagem onde será adicionado o Gtk.TreeView().
        scrolledwindow = Gtk.ScrolledWindow.new()
        vbox.append(child=scrolledwindow)

        # Criando um modelo com `Gtk.ListStore()`.
        self.list_store = Gtk.ListStore.new([GObject.TYPE_INT, GObject.TYPE_STRING])

        # Adicionando os dados no `Gtk.ListStore()`.
        for state in self.brazilian_states:
            # insert_with_values(linha, colunas, dados)
            self.list_store.insert_with_values(state[0], (0, 1), state)

        # Criando um `Gtk.TreeView()`.
        tree_view = Gtk.TreeView.new_with_model(model=self.list_store)
        # Adicionando o TreeView dentro de um scroll.
        scrolledwindow.set_child(child=tree_view)

        # Nome das colunas (title).
        cols = ('ID', 'Estados')
        for column_index, title in enumerate(cols):
            # Criando um rederizador do tipo texto.
            cell_render = Gtk.CellRendererText.new()

            # Definindo que o conteúdo pode ser editado.
            cell_render.set_property('editable', 'True')

            # Método que é executando após a edição.
            # column_index: para verificar qual coluna foi editada.
            cell_render.connect('edited', self.on_cell_edited, column_index)

            # Configurando o rederizador da primeira coluna.
            if column_index == 0:
                cell_render.props.weight_set = True
                cell_render.set_property('weight_set', True)
                cell_render.set_property('weight', Pango.Weight.BOLD)

            # Criando a coluna.
            tree_view_column = Gtk.TreeViewColumn(
                title=title,
                cell_renderer=cell_render,
                # Posição (Coluna 0, coluna 1) em que o CellRendererText
                # e o titulo serão inseridos.
                text=column_index,
            )

            # Adicionando a coluna no `Gtk.TreeView()`.
            tree_view.append_column(column=tree_view_column)

    def on_cell_edited(self, widget, row, value, column_index):
        # Alterando o valor.
        if column_index == 1:
            self.list_store[row][column_index] = value


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
