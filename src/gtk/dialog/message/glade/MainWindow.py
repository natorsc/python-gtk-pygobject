# -*- coding: utf-8 -*-
"""Janela de diálogo personalizado com Gnome Glade."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


def load_ui_file(filename):
    builder = Gtk.Builder.new()
    builder.add_from_file(filename=filename)
    return builder


class Handler:

    def __init__(self):
        pass

    def open_message_dialog_info(self, widget):
        builder = load_ui_file(filename='./MessageDialogInfo.glade')
        dialog = builder.get_object(name='MessageDialogInfo')
        # Definindo a janela pai.
        dialog.set_transient_for(parent=win)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão Cancelar pressionado')
        dialog.destroy()

    def open_message_dialog_warning(self, widget):
        builder = load_ui_file(filename='./MessageDialogWarning.glade')
        dialog = builder.get_object(name='MessageDialogWarning')
        dialog.set_transient_for(parent=win)
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_question(self, widget):
        builder = load_ui_file(filename='./MessageDialogQuestion.glade')
        dialog = builder.get_object(name='MessageDialogQuestion')
        dialog.set_transient_for(parent=win)
        # Adicionando class action nos botões.
        btn_no = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.NO,
        )
        btn_no.get_style_context().add_class(class_name='destructive-action')
        btn_yes = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.YES,
        )
        btn_yes.get_style_context().add_class(class_name='suggested-action')
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_error(self, widget):
        builder = load_ui_file(filename='./MessageDialogError.glade')
        dialog = builder.get_object(name='MessageDialogError')
        dialog.set_transient_for(parent=win)
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_other(self, widget):
        builder = load_ui_file(filename='./MessageDialogOther.glade')
        dialog = builder.get_object(name='MessageDialogOther')
        dialog.set_transient_for(parent=win)
        # Adicionando class action nos botões.
        btn_no = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.NO,
        )
        btn_no.get_style_context().add_class(class_name='destructive-action')
        btn_yes = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.YES,
        )
        btn_yes.get_style_context().add_class(class_name='suggested-action')
        response = dialog.run()
        dialog.destroy()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
