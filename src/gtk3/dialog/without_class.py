# -*- coding: utf-8 -*-
"""Gtk.Dialog() custom."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Janela de diálogo personalizda.')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        button_open_dialog = Gtk.Button.new_with_label(
            label='Abrir janela de dialogo personalizada'
        )
        button_open_dialog.connect("clicked", self.open_dialogue)
        vbox.add(widget=button_open_dialog)

        self.label = Gtk.Label.new(str='Valor digitado no dialogo:')
        vbox.pack_end(child=self.label, expand=True, fill=True, padding=0)

        self.show_all()

    def open_dialogue(self, button):
        dialog = Gtk.Dialog.new()
        dialog.set_transient_for(parent=self)
        dialog.set_title(title='Janela de dialogo personalizada')

        # Adicionando 1 botão.
        dialog.add_button(button_text='Talvez', response_id=5000)
        # Adicionando mais de 1 botão.
        dialog.add_buttons(
            '_Não', Gtk.ResponseType.NO,
            '_Sim', Gtk.ResponseType.YES,
        )
        # Adicionando class action nos botões.
        btn_no = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.NO,
        )
        btn_no.get_style_context().add_class(class_name='destructive-action')
        btn_yes = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.YES,
        )
        btn_yes.get_style_context().add_class(class_name='suggested-action')

        # Acessando o box.
        content_area = dialog.get_content_area()
        # configurando.
        content_area.set_halign(align=Gtk.Align.CENTER)
        content_area.set_border_width(border_width=12)
        content_area.set_spacing(spacing=6)

        label = Gtk.Label.new(str='Um texto qualquer')
        content_area.add(widget=label)
        # Outras formas de posicionar.
        # content_area.pack_start(child=label, expand=True, fill=True, padding=0)
        # content_area.pack_end(child=label, expand=True, fill=True, padding=0)

        entry = Gtk.Entry.new()
        entry.set_placeholder_text(text='Digite um texto qualquer.')
        content_area.add(widget=entry)

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
