# -*- coding: utf-8 -*-
"""Janela de diálogo do tipo MessageDialog."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Janela de diálogo do tipo MessageDialog.')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_border_width(border_width=10)
        self.add(widget=vbox)

        button_info = Gtk.Button.new_with_label(label='Abrir janela de mensagem INFO')
        button_info.connect('clicked', self.open_message_dialog_info)
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

    def open_message_dialog_info(self, widget):
        dialog = MessageDialogInfo(parent=self)
        response = dialog.run()
        # Verificando qual botão foi clicado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão Cancelar pressionado')
        dialog.destroy()

    def open_message_dialog_warning(self, widget):
        dialog = MessageDialogWarning(parent=self)
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_question(self, widget):
        dialog = MessageDialogQuestion(parent=self)
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_error(self, widget):
        dialog = MessageDialogError(parent=self)
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_other(self, widget):
        dialog = MessageDialogOther(parent=self)
        response = dialog.run()
        dialog.destroy()


class MessageDialogInfo(Gtk.MessageDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent, message_type=Gtk.MessageType.INFO,
                         buttons=Gtk.ButtonsType.OK_CANCEL)
        self.set_title(title='Janela de mensagem do tipo INFO')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>INFO</big>'
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>INFO</b>'
        )
        self.show_all()


class MessageDialogWarning(Gtk.MessageDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent, message_type=Gtk.MessageType.WARNING,
                         buttons=Gtk.ButtonsType.OK_CANCEL)
        self.set_title(title='Janela de mensagem do tipo WARNING')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>WARNING</big>'
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>WARNING</b>'
        )
        self.show_all()


class MessageDialogQuestion(Gtk.MessageDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent, message_type=Gtk.MessageType.QUESTION,
                         buttons=Gtk.ButtonsType.OK_CANCEL)
        self.set_title(title='Janela de mensagem do tipo QUESTION')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>QUESTION</big>'
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>QUESTION</b>'
        )
        self.show_all()


class MessageDialogError(Gtk.MessageDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent, message_type=Gtk.MessageType.ERROR,
                         buttons=Gtk.ButtonsType.OK_CANCEL)
        self.set_title(title='Janela de mensagem do tipo ERROR')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>ERROR</big>'
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>ERROR</b>'
        )
        self.show_all()


class MessageDialogOther(Gtk.MessageDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent, message_type=Gtk.MessageType.OTHER,
                         buttons=Gtk.ButtonsType.OK_CANCEL)
        self.set_title(title='Janela de mensagem do tipo OTHER')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>OTHER</big>'
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>OTHER</b>'
        )
        self.show_all()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
