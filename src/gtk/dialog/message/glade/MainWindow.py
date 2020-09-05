# -*- coding: utf-8 -*-
"""Janela de diálogo personalizado com Gnome Glade."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:

    def open_message_dialog_info(self, widget):
        builder = Gtk.Builder.new()
        builder.add_from_file(filename='./MessageDialogInfo.glade')

        message = builder.get_object(name='MessageDialogInfo')
        message.set_transient_for(parent=win)

        response = message.run()

        # Verificando qual botão foi clicado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão Cancelar pressionado')
        message.destroy()

    def open_message_dialog_warning(self, widget):
        builder = Gtk.Builder.new()
        builder.add_from_file(filename='./MessageDialogWarning.glade')
        message = builder.get_object(name='MessageDialogWarning')
        message.set_transient_for(parent=win)
        response = message.run()
        message.destroy()

    def open_message_dialog_question(self, widget):
        builder = Gtk.Builder.new()
        builder.add_from_file(filename='./MessageDialogQuestion.glade')
        message = builder.get_object(name='MessageDialogQuestion')
        message.set_transient_for(parent=win)
        response = message.run()
        message.destroy()

    def open_message_dialog_error(self, widget):
        builder = Gtk.Builder.new()
        builder.add_from_file(filename='./MessageDialogError.glade')
        message = builder.get_object(name='MessageDialogError')
        message.set_transient_for(parent=win)
        response = message.run()
        message.destroy()

    def open_message_dialog_other(self, widget):
        builder = Gtk.Builder.new()
        builder.add_from_file(filename='./MessageDialogOther.glade')
        message = builder.get_object(name='MessageDialogOther')
        message.set_transient_for(parent=win)
        response = message.run()
        message.destroy()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    # Listando todos os widgets disponíveis no arquivo de interface.
    # print(builder.get_objects())
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
