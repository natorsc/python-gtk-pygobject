# -*- coding: utf-8 -*-
"""Janela de diálogo do tipo MessageDialog.

``Gtk.MessageType``:
- Gtk.MessageType.INFO
- Gtk.MessageType.WARNING
- Gtk.MessageType.QUESTION
- Gtk.MessageType.ERROR
- Gtk.MessageType.OTHER

``Gtk.ButtonsType``:
- Gtk.ButtonsType.NONE
- Gtk.ButtonsType.OK
- Gtk.ButtonsType.CLOSE
- Gtk.ButtonsType.CANCEL
- Gtk.ButtonsType.YES_NO
- Gtk.ButtonsType.OK_CANCEL

``Gtk.ResponseType``:
- Gtk.ResponseType.NONE
- Gtk.ResponseType.APPLY
- Gtk.ResponseType.HELP
- Gtk.ResponseType.REJECT
- Gtk.ResponseType.ACCEPT
- Gtk.ResponseType.DELETE_EVENT
- Gtk.ResponseType.OK
- Gtk.ResponseType.CANCEL
- Gtk.ResponseType.CLOSE
- Gtk.ResponseType.YES
- Gtk.ResponseType.NO
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self):
        super().__init__()

        self.set_title(title='Janela de diálogo do tipo mensagem')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')
        self.set_border_width(border_width=10)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(widget=vbox)

        button_info = Gtk.Button.new_with_label(label='Abrir janela de dialogo INFO')
        button_info.connect("clicked", self.open_message_dialog_infor)
        vbox.add(widget=button_info)

        button_warning = Gtk.Button.new_with_label(label='Abrir janela de mensagem WARNING')
        button_warning.connect('clicked', self.open_message_dialog_warning)
        vbox.add(widget=button_warning)

        button_question = Gtk.Button.new_with_label(label='Abrir janela de mensagem QUESTION')
        button_question.connect('clicked', self.open_message_dialog_question)
        vbox.add(widget=button_question)

        button_error = Gtk.Button.new_with_label(label='Abrir janela de mensagem ERROR')
        button_error.connect('clicked', self.open_message_dialog_error)
        vbox.add(widget=button_error)

        button_other = Gtk.Button.new_with_label(label='Abrir janela de mensagem OTHER')
        button_other.connect('clicked', self.open_message_dialog_other)
        vbox.add(widget=button_other)

    def open_message_dialog_infor(self, widget):
        dialog = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            title='Janela de diálogo do tipo mensagem info.',
        )
        dialog.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>INFO</big>'
        )
        dialog.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>INFO</b>'
        )
        response = dialog.run()
        # Verificando qual botão foi clicado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão Cancelar pressionado')
        dialog.destroy()

    def open_message_dialog_warning(self, widget):
        dialog = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            title='Janela de diálogo do tipo mensagem WARNING.',
        )
        dialog.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>WARNING</big>'
        )
        dialog.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>WARNING</b>'
        )
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_question(self, widget):
        dialog = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            title='Janela de diálogo do tipo mensagem QUESTION.',
        )
        dialog.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>QUESTION</big>'
        )
        dialog.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>QUESTION</b>'
        )
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_error(self, widget):
        dialog = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            title='Janela de diálogo do tipo mensagem ERROR.',
        )
        dialog.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>ERROR</big>'
        )
        dialog.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>ERROR</b>'
        )
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_other(self, widget):
        dialog = Gtk.MessageDialog(
            parent=self,
            message_type=Gtk.MessageType.OTHER,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            title='Janela de diálogo do tipo mensagem OTHER.',
        )
        dialog.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>OTHER</big>'
        )
        dialog.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>OTHER</b>'
        )
        response = dialog.run()
        dialog.destroy()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
