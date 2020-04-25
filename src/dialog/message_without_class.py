# -*- coding: utf-8 -*-
"""Janela de diálogo do tipo mensagem.

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
        self.set_default_icon_from_file(filename='../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(widget=vbox)

        button_info = Gtk.Button.new_with_label(label='Abrir janela de dialogo')
        button_info.connect("clicked", self._open_dialogue)
        vbox.add(widget=button_info)

    def _open_dialogue(self, button):
        dialog = Gtk.MessageDialog(
            parent=self,
            modal=True,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            title='Título da Janela de dialogo',
        )

        dialog.set_markup(
            str='<span foreground="red">Texto primário</span> da janela de '
            'diálogo <big>formatado</big>'
        )

        dialog.format_secondary_markup(
            message_format='<span foreground="orange">Texto secundário</span> '
                           'da janela de diálogo <b>formatado</b>'
        )

        response = dialog.run()

        # Verificando qual botão foi clicado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão Cancelar pressionado')

        dialog.destroy()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
