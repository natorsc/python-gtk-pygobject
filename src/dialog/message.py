# -*- coding: utf-8 -*-
"""Dialogo do tipo MessageDialog."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Janela de diálogo do tipo mensagem')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(widget=vbox)

        button_info = Gtk.Button.new_with_label(label='Abrir janela de dialogo')
        button_info.connect("clicked", self.open_message_dialog)
        vbox.add(widget=button_info)

    def open_message_dialog(self, button):
        dialog = MyMessageDialog(parent=self)

        response = dialog.run()

        # Verificando qual botão foi clicado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão Cancelar pressionado')

        dialog.destroy()


class MyMessageDialog(Gtk.MessageDialog):
    def __init__(self, parent):
        """Construtor.

        :param parent: Widget ao qual o dialogo pertence.
        """
        super().__init__(parent=parent, message_type=Gtk.MessageType.INFO,
                         buttons=Gtk.ButtonsType.OK_CANCEL)

        self.set_title(title='Título da Janela de dialogo')
        self.set_modal(modal=True)

        self.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
                'diálogo <big>formatado</big>'
        )

        self.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>formatado</b>'
        )

        # É obrigatório utilizar ``show_all()`` senão ``get_content_area()``
        # não adiciona os widgets.
        self.show_all()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
