# -*- coding: utf-8 -*-
"""Handy.Dialog.

Janela de dialogo que se adapta a telas pequenas.
"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    """Classe herda de ``Gtk.ApplicationWindow``."""

    def __init__(self):
        """Construtor."""
        super().__init__()

        # Configurando a janela principal.
        self.set_title(title='Handy.Dialog')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        # Box vertical que irá comportar os botões que chamam os diálogos de mensagem.
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        # Adicionando o Box Layout vertical na janela principal
        self.add(widget=vbox)

        # Botão que ira abrir a janela de dialogo
        button_open_dialog = Gtk.Button.new_with_label(
            label='Abrir janela de dialogo'
        )
        button_open_dialog.connect('clicked', self.open_dialog)
        vbox.add(widget=button_open_dialog)

    def open_dialog(self, button):
        hdy_dialog = Handy.Dialog.new(parent=self)
        # dialog.set_modal(modal=False)
        hdy_dialog.set_title(title='Janela de dialogo com libhandy')

        # Adicionando vários botões de uma vez.
        hdy_dialog.add_buttons(
            # Gtk.STOCK_OK é uma constante do Gtk,
            # pode ser utilizada uma string no lugar da constante.
            Gtk.STOCK_YES, Gtk.ResponseType.YES,
            Gtk.STOCK_NO, Gtk.ResponseType.NO
        )

        # Acessando a área de conteúdo da janela de dialogo para poder
        # adicionar novos widgets dentro dessa área.
        content_area = hdy_dialog.get_content_area()
        content_area.set_border_width(border_width=10)
        content_area.set_spacing(spacing=10)

        # Criando widgets que serão adicionados na janela de dialogo.
        label = Gtk.Label.new(str='Valor do entry será exibido no terminal.')
        content_area.add(widget=label)
        # content_area.pack_start(child=label, expand=True, fill=True, padding=0)
        # content_area.pack_end(child=label, expand=True, fill=True, padding=0)

        entry = Gtk.Entry.new()
        entry.set_placeholder_text(text='Digite algo e clique em sim')
        content_area.add(widget=entry)

        # É obrigatório utilizar ``show_all()`` senão ``get_content_area()``
        # não adiciona os widgets.
        hdy_dialog.show_all()

        response = hdy_dialog.run()

        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.YES:
            print('Botão SIM pressionado')
            print(f'Valor do Gtk.Entry = {entry.get_text()}')

        # Fechando a janela de diálogo.
        hdy_dialog.destroy()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
