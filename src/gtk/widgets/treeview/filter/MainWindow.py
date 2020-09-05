# -*- coding: utf-8 -*-
"""GTK TreeView, utilizando filtro."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Pango, GObject


class MainWindow(Gtk.ApplicationWindow):
    software_list = [
        ('Firefox', 2002, 'C++'), ('Eclipse', 2004, 'Java'), ('Pitivi', 2004, 'Python'),
        ('Netbeans', 1996, 'Java'), ('Chrome', 2008, 'C++'), ('Filezilla', 2001, 'C++'),
        ('Bazaar', 2005, 'Python'), ('Git', 2005, 'C'), ('Linux Kernel', 1991, 'C'),
        ('GCC', 1987, 'C'), ('Frostwire', 2004, 'Java'),
    ]

    # Valor inicial do filtro.
    current_filter_language = None

    def __init__(self):
        super().__init__()
        self.set_title(title='GTK TreeView, utilizando filtro')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../../images/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        # Janela com rolagem onde será adicionado o Gtk.TreeView().
        scrolledwindow = Gtk.ScrolledWindow.new()
        vbox.pack_start(child=scrolledwindow, expand=True, fill=True, padding=0)

        # Criando um modelo com `Gtk.ListStore()`.
        self.liststore = Gtk.ListStore.new(
            [GObject.TYPE_STRING, GObject.TYPE_INT, GObject.TYPE_STRING]
        )

        # Adicionando os dados no `Gtk.ListStore()`.
        for data in self.software_list:
            self.liststore.append(row=data)

        # Criando um filtro a partir do `Gtk.ListStore()`.
        self.language_filter = self.liststore.filter_new()
        # Função que é executada pelo filtro.
        self.language_filter.set_visible_func(self.language_filter_func)

        # Passando o filtro como modelo para o `Gtk.TreeView()`.
        treeview = Gtk.TreeView.new_with_model(model=self.language_filter)
        scrolledwindow.add(widget=treeview)

        # Nome das colunas (title).
        cols = ('Software', 'Lançamento', 'Linguagem')
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

        btn_box = Gtk.ButtonBox.new(orientation=Gtk.Orientation.HORIZONTAL)
        btn_box.set_layout(layout_style=Gtk.ButtonBoxStyle.START)
        vbox.pack_end(child=btn_box, expand=False, fill=True, padding=0)

        btn_label_list = ['Java', 'C', 'C++', 'Python', 'Todos']
        for label in btn_label_list:
            button = Gtk.Button.new_with_label(label=label)
            button.connect('clicked', self.on_button_clicked)
            btn_box.add(widget=button)

    def language_filter_func(self, liststore, iter, data):
        if self.current_filter_language is None or self.current_filter_language == 'Todos':
            return True
        else:
            return liststore[iter][2] == self.current_filter_language

    def on_button_clicked(self, widget):
        """Este método é executado quando o botão é pressionado.

        Ele atualiza o valor da variável que guarda o valor atual do filtro.
        """
        # Passando o valor do label do botão para a variável.
        self.current_filter_language = widget.get_label()
        # `refilter()`: Ele atualiza o filtro, basicamente ele chama o método
        # `language_filter_func()` que foi registrado em `set_visible_func()`.
        self.language_filter.refilter()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
