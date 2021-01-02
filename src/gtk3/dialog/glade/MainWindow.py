# -*- coding: utf-8 -*-
"""Gtk.Dialog() custom."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class Handler:

    def __init__(self):
        # Acessando widgets do arquivo de interface.
        self.label = builder.get_object(name='label')

    def open_dialog(self, widget):
        builder = Gtk.Builder.new()
        builder.add_from_file(filename='./CustomDialog.glade')

        entry = builder.get_object(name='entry')

        dialog = builder.get_object(name='CustomDialog')
        dialog.set_transient_for(parent=win)

        response = dialog.run()
        print(f'Resposta do diálogo = {response}.')

        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.YES:
            print('Botão SIM pressionado')
            print(f'Valor digitado no dialogo = {entry.get_text()}')
            self.label.set_markup(
                str=f'Valor digitado no dialogo: <b>{entry.get_text()}</b>',
            )
        elif response == Gtk.ResponseType.NO:
            print('Botão NÃO pressionado')
            self.label.set_text(str=f'Botão NÃO pressionado')
        elif response == Gtk.ResponseType.DELETE_EVENT:
            print('Botão de fechar a janela pressionado')
            self.label.set_text(str=f'Botão de fechar a janela pressionado')
        else:
            print('Botão TALVEZ pressionado')
            self.label.set_text(str=f'Botão TALVEZ pressionado')

        dialog.destroy()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
