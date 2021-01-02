# -*- coding: utf-8 -*-
"""Gtk.MessageDialog()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MessageDialogInfo(Gtk.MessageDialog):

    def __init__(self):
        super().__init__()

        self.props.message_type = Gtk.MessageType.INFO
        self.set_title(title='Janela de mensagem do tipo INFO')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>INFO</big>',
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>INFO</b>',
        )
        self.add_button(button_text='_OK', response_id=Gtk.ResponseType.OK)
        self.show_all()


class MessageDialogWarning(Gtk.MessageDialog):

    def __init__(self):
        super().__init__()

        self.props.message_type = Gtk.MessageType.WARNING
        self.set_title(title='Janela de mensagem do tipo WARNING')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>WARNING</big>',
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>WARNING</b>',
        )
        self.add_button(button_text='_OK', response_id=Gtk.ResponseType.OK)
        self.show_all()


class MessageDialogQuestion(Gtk.MessageDialog):

    def __init__(self):
        super().__init__()

        self.props.message_type = Gtk.MessageType.QUESTION
        self.set_title(title='Janela de mensagem do tipo QUESTION')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>QUESTION</big>',
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>QUESTION</b>',
        )
        self.add_buttons(
            '_Não', Gtk.ResponseType.NO,
            '_Sim', Gtk.ResponseType.YES,
        )
        # Adicionando class action nos botões.
        btn_no = self.get_widget_for_response(
            response_id=Gtk.ResponseType.NO,
        )
        btn_no.get_style_context().add_class(class_name='destructive-action')

        btn_yes = self.get_widget_for_response(
            response_id=Gtk.ResponseType.YES,
        )
        btn_yes.get_style_context().add_class(class_name='suggested-action')
        self.show_all()


class MessageDialogError(Gtk.MessageDialog):

    def __init__(self):
        super().__init__()

        self.props.message_type = Gtk.MessageType.ERROR
        self.set_title(title='Janela de mensagem do tipo ERROR')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>ERROR</big>',
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>ERROR</b>',
        )
        self.add_button(button_text='_OK', response_id=Gtk.ResponseType.OK)
        self.show_all()


class MessageDialogOther(Gtk.MessageDialog):

    def __init__(self):
        super().__init__()

        self.props.message_type = Gtk.MessageType.OTHER
        self.set_title(title='Janela de mensagem do tipo OTHER')
        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>OTHER</big>',
        )
        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>OTHER</b>',
        )
        self.add_buttons(
            '_Cancelar', Gtk.ResponseType.CANCEL,
            '_Não', Gtk.ResponseType.NO,
            '_Sim', Gtk.ResponseType.YES,
        )
        # Adicionando class action nos botões.
        btn_no = self.get_widget_for_response(
            response_id=Gtk.ResponseType.NO,
        )
        btn_no.get_style_context().add_class(class_name='destructive-action')

        btn_yes = self.get_widget_for_response(
            response_id=Gtk.ResponseType.YES,
        )
        btn_yes.get_style_context().add_class(class_name='suggested-action')
        self.show_all()


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.MessageDialog')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_border_width(border_width=12)
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

        self.show_all()

    def open_message_dialog_info(self, widget):
        dialog = MessageDialogInfo()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        # Verificando qual botão foi clicado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão Cancelar pressionado')
        dialog.destroy()

    def open_message_dialog_warning(self, widget):
        dialog = MessageDialogWarning()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_question(self, widget):
        dialog = MessageDialogQuestion()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        dialog.destroy()

    def open_message_dialog_error(self, widget):
        dialog = MessageDialogError()
        dialog.set_transient_for(parent=self)
        response = dialog.run()
        dialog.destroy()

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
    import sys

    app = Application()
    app.run(sys.argv)
