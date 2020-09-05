# -*- coding: utf-8 -*-
"""Janela de diálogo personalizada."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Janela de diálogo personalizda.')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')
        self.set_border_width(border_width=10)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(widget=vbox)

        button_open_dialog = Gtk.Button.new_with_label(
            label='Abrir janela de dialogo'
        )
        button_open_dialog.connect("clicked", self.open_dialogue)
        vbox.add(widget=button_open_dialog)

        self.label = Gtk.Label.new(str='Valor digitado no dialogo:')
        vbox.pack_end(child=self.label, expand=True, fill=True, padding=0)

    def open_dialogue(self, button):
        dialog = Gtk.Dialog.new()
        dialog.set_title(title='Janela de dialogo personalizada')
        dialog.set_transient_for(parent=self)
        dialog.add_buttons(
            # Gtk.STOCK_YES é uma constante do Gtk.
            # Essa constante retorna um valor numérico.
            Gtk.STOCK_YES, Gtk.ResponseType.YES,
            Gtk.STOCK_NO, Gtk.ResponseType.NO
        )

        # Adicionando um botão por vez.
        # Utilizando um texto e id de resposta personalizada ao invés de
        # constantes do GTK.
        dialog.add_button(button_text='Talvez', response_id=5000)

        # Acessando a área de conteúdo da janela de dialogo para poder
        # adicionar novos widgets dentro dessa área.
        content_area = dialog.get_content_area()
        # configurando.
        content_area.set_border_width(border_width=10)
        content_area.set_spacing(spacing=10)

        label = Gtk.Label.new(str='Um texto qualquer')
        content_area.add(widget=label)
        # Outras formas de posicionar.
        # content_area.pack_start(child=label, expand=True, fill=True, padding=0)
        # content_area.pack_end(child=label, expand=True, fill=True, padding=0)

        entry = Gtk.Entry.new()
        entry.set_placeholder_text(text='Digite um texto qualquer.')
        content_area.add(widget=entry)

        # É obrigatório utilizar ``show_all()`` senão ``get_content_area()``
        # não adiciona os widgets.
        dialog.show_all()

        response = dialog.run()
        print(f'Resposta do diálogo = {response}.')

        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.YES:
            print('Botão SIM pressionado')
            print(f'Valor digitado no dialogo = {entry.get_text()}')
            self.label.set_markup(
                str=f'Valor digitado no dialogo: <b>{entry.get_text()}</b>',
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


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
