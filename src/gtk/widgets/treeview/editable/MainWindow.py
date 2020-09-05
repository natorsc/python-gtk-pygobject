# -*- coding: utf-8 -*-
"""GTK TreeView, realizado a edição do valor na celula."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Pango, GObject


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

    def __init__(self):
        super().__init__()
        self.set_title(title='GTK TreeView, realizado a edição do valor na celula')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../../images/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        # Janela com rolagem onde será adicionado o Gtk.TreeView().
        scrolledwindow = Gtk.ScrolledWindow.new()
        vbox.pack_end(child=scrolledwindow, expand=True, fill=True, padding=0)

        # Criando um modelo com `Gtk.ListStore()`.
        self.liststore = Gtk.ListStore.new([GObject.TYPE_INT, GObject.TYPE_STRING])

        # Adicionando os dados no `Gtk.ListStore()`.
        for state in self.brazilian_states:
            self.liststore.append(row=state)

        # Criando um `Gtk.TreeView()`.
        treeview = Gtk.TreeView.new_with_model(model=self.liststore)
        scrolledwindow.add(widget=treeview)

        # Nome das colunas (title).
        cols = ('ID', 'Estados')
        for i, col in enumerate(cols):
            # Criando um rederizador com para o tipo de dado que será exibido.
            cellrender = Gtk.CellRendererText.new()
            # Definindo que o conteúdo pode ser editado.
            cellrender.props.editable = True
            # Método que é executando após a edição.
            cellrender.connect('edited', self.on_cell_edited, i)

            # Configurando o rederizador da primeira coluna.
            if i == 0:
                cellrender.props.weight_set = True
                cellrender.props.weight = Pango.Weight.BOLD

            # Criando a coluna.
            treeviewcolumn = Gtk.TreeViewColumn(
                # Titulo da coluna.
                title=col,
                # Rederizador que será utilizado na coluna.
                cell_renderer=cellrender,
                # Posição (index) da coluna.
                text=i,
            )
            # Adicionando a coluna no `Gtk.TreeView()`.
            treeview.append_column(column=treeviewcolumn)

    def on_cell_edited(self, widget, row, value, column):
        # Alterando o valor diretamente no ListStore, contudo a alteração poderia
        # ser enviada para algum banco de dados.
        if column == 0:
            if value:
                self.liststore[row][column] = int(value)
        else:
            self.liststore[row][column] = value


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
