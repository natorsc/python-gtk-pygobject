# -*- coding: utf-8 -*-
"""Janela de diálogo do tipo MessageDialog."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk

from MessageDialogError import MessageDialogError
from MessageDialogInfo import MessageDialogInfo
from MessageDialogOther import MessageDialogOther
from MessageDialogQuestion import MessageDialogQuestion
from MessageDialogWarning import MessageDialogWarning


@Gtk.Template(filename='./MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def open_message_dialog_info(self, widget):
        dialog = MessageDialogInfo()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão Cancelar pressionado')
        dialog.destroy()

    @Gtk.Template.Callback()
    def open_message_dialog_warning(self, widget):
        dialog = MessageDialogWarning()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        dialog.destroy()

    @Gtk.Template.Callback()
    def open_message_dialog_question(self, widget):
        dialog = MessageDialogQuestion()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        dialog.destroy()

    @Gtk.Template.Callback()
    def open_message_dialog_error(self, widget):
        dialog = MessageDialogError()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        dialog.destroy()

    @Gtk.Template.Callback()
    def open_message_dialog_other(self, widget):
        dialog = MessageDialogOther()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
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
