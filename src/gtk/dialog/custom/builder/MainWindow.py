# -*- coding: utf-8 -*-
"""Janela de diálogo personalizado com Gnome Builder."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk

from CustomDialog import CustomDialog


# Parâmetros aceitos: @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='./MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    label = Gtk.Template.Child(name='label')

    @Gtk.Template.Callback()
    def open_dialog(self, button):
        custom_dialog = CustomDialog(parent=self)
        response = custom_dialog.run()
        print(f'Resposta do diálogo = {response}.')

        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.YES:
            print('Botão SIM pressionado')
            print(f'Valor digitado no dialogo = {custom_dialog.get_entry_text()}')
            self.label.set_markup(
                str=f'Valor digitado no dialogo: <b>{custom_dialog.get_entry_text()}</b>',
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

        custom_dialog.destroy()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
