# -*- coding: utf-8 -*-
"""Gtk.TreeView(), Gtk.TreeStore()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, Gio, Pango, GObject


class MainWindow(Gtk.ApplicationWindow):
    brazilian_cities = {
        'SP': ['Botucatu', 'São Manuel'],
        'SC': ['Florianópolis', 'Joinville']
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.TreeView, Gtk.TreeStore')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        # Janela com rolagem onde será adicionado o Gtk.TreeView().
        scrolledwindow = Gtk.ScrolledWindow.new()
        vbox.pack_end(child=scrolledwindow, expand=True, fill=True, padding=0)

        # Criando o TreeStore (model).
        tree_store = Gtk.TreeStore.new(types=[GObject.TYPE_STRING])
        for state, cities_list in self.brazilian_cities.items():
            iter = tree_store.append(parent=None, row=[state])
            for city in cities_list:
                tree_store.append(parent=iter, row=[city])

        # Criando um `Gtk.TreeView()`.
        treeview = Gtk.TreeView.new_with_model(model=tree_store)
        treeview.connect('row-activated', self.on_row_double_click)
        scrolledwindow.add(widget=treeview)

        # Nome das colunas (title).
        cols = ('Estado',)
        for i, col in enumerate(cols):
            # Criando um rederizador com para o tipo de dado que será exibido.
            cellrender = Gtk.CellRendererText.new()

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

            # Definindo que a coluna pode ordenar o conteúdo.
            treeviewcolumn.set_sort_column_id(sort_column_id=i)

            # Adicionando a coluna no `Gtk.TreeView()`.
            treeview.append_column(column=treeviewcolumn)

            self.show_all()

    def on_row_double_click(self, widget, tree_path, tree_view_column):
        model = widget.get_model()
        tree_iter = model.get_iter(tree_path)

        column = tree_view_column.get_sort_column_id()
        column_title = tree_view_column.get_title()
        print(f'Coluna: {column} - Título: {column_title}')

        value = model.get_value(iter=tree_iter, column=column)
        print(f'Texto da linha {value}')


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
