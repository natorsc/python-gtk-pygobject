# -*- coding: utf-8 -*-
"""Gtk.TreeView() filter."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class Handler:
    software_list = [
        ('Firefox', 2002, 'C++'), ('Eclipse', 2004, 'Java'), ('Pitivi', 2004, 'Python'),
        ('Netbeans', 1996, 'Java'), ('Chrome', 2008, 'C++'), ('Filezilla', 2001, 'C++'),
        ('Bazaar', 2005, 'Python'), ('Git', 2005, 'C'), ('Linux Kernel', 1991, 'C'),
        ('GCC', 1987, 'C'), ('Frostwire', 2004, 'Java'),
    ]

    # Valor inicial do filtro.
    current_filter_language = None

    def __init__(self):
        # Acessando o `Gtk.ListStore()`.
        self.liststore = builder.get_object(name='liststore')
        for state in self.software_list:
            self.liststore.append(row=state)

        # Acessando o filtro que é um modelo de `Gtk.ListStore()`.
        self.language_filter = builder.get_object(name='language-filter')
        # Função que é executada pelo filtro.
        self.language_filter.set_visible_func(self.language_filter_func)

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
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
