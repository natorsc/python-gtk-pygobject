# -*- coding: utf-8 -*-
"""Janela de diálogo personalizada."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk

from CustomDialog import CustomDialog


# Parâmetros aceitos: @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='./MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    label = Gtk.Template.Child(name='label')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def open_dialog(self, button):
        dialog = CustomDialog()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        print(f'Resposta do diálogo = {response}.')

        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.YES:
            print('Botão SIM pressionado')
            print(f'Valor digitado no dialogo = {dialog.get_entry_text()}')
            self.label.set_markup(
                str=f'Valor digitado no dialogo: <b>{dialog.get_entry_text()}</b>',
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
    app = Application()
    app.run(sys.argv)
