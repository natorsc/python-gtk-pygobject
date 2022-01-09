# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.TreeView() filter."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gtk, Gio, Pango, GObject


class MainWindow(Gtk.ApplicationWindow):
    software_list = [
        ('Firefox', 2002, 'C++'), ('Eclipse', 2004, 'Java'), ('Pitivi', 2004, 'Python'),
        ('Netbeans', 1996, 'Java'), ('Chrome', 2008, 'C++'), ('Filezilla', 2001, 'C++'),
        ('Bazaar', 2005, 'Python'), ('Git', 2005, 'C'), ('Linux Kernel', 1991, 'C'),
        ('GCC', 1987, 'C'), ('Frostwire', 2004, 'Java'),
    ]

    # Variável auxiliar que armazena o valor do filtro.
    current_filter_language = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.TreeView() filter')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        # Janela com rolagem onde será adicionado o Gtk.TreeView().
        scrolled_window = Gtk.ScrolledWindow.new()
        vbox.append(child=scrolled_window)

        # Criando um modelo com `Gtk.ListStore()`.
        self.list_store = Gtk.ListStore.new(
            [GObject.TYPE_STRING, GObject.TYPE_INT, GObject.TYPE_STRING],
        )

        # Criando um filtro a partir do `Gtk.ListStore()`.
        self.list_store_lang_filter = self.list_store.filter_new()
        # Função que é executada pelo filtro.
        self.list_store_lang_filter.set_visible_func(
            self.language_filter_func,
            data=None,
        )

        # Adicionando os dados no `Gtk.ListStore()`.
        for row_index, data in enumerate(self.software_list):
            self.list_store.insert_with_values(row_index, (0, 1, 2), data)

        # Criando um `Gtk.TreeView()`.
        tree_view = Gtk.TreeView.new_with_model(model=self.list_store_lang_filter)
        tree_view.set_vexpand(expand=True)
        scrolled_window.set_child(child=tree_view)

        # Nome das colunas (title).
        cols = ('Software', 'Lançamento', 'Linguagem')
        for i, col in enumerate(cols):
            # Criando um rederizador com para o tipo de dado que será exibido.
            cell_render = Gtk.CellRendererText.new()

            # Configurando o rederizador da primeira coluna.
            if i == 0:
                cell_render.set_property('weight_set', True)
                cell_render.set_property('weight', Pango.Weight.BOLD)

            # Criando a coluna.
            treeviewcolumn = Gtk.TreeViewColumn(
                # Titulo da coluna.
                title=col,
                # Rederizador que será utilizado na coluna.
                cell_renderer=cell_render,
                # Posição (index) da coluna.
                text=i,
            )

            # Adicionando a coluna no `Gtk.TreeView()`.
            tree_view.append_column(column=treeviewcolumn)

        hbuton_box = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        vbox.append(child=hbuton_box)

        button_label_list = ['Java', 'C', 'C++', 'Python', 'Todos']
        for label in button_label_list:
            button = Gtk.Button.new_with_label(label=label)
            button.connect('clicked', self.on_button_clicked)
            hbuton_box.append(child=button)

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
        self.list_store_lang_filter.refilter()


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
