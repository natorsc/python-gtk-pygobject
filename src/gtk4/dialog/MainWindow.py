# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Box() vertical."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class CustomDialog(Gtk.Dialog):
    """Exemplo de uma janela de dialogo personalizada."""

    def __init__(self, parent):
        super().__init__(transient_for=parent, use_header_bar=True)
        self.parent = parent

        self.set_title(title='Janela de dialogo personalizada')
        self.use_header_bar = True
        self.set_modal(modal=True)
        self.connect('response', self.dialog_response)

        # Criando os botões.
        self.add_buttons(
            '_Cancelar', Gtk.ResponseType.CANCEL,
            '_OK', Gtk.ResponseType.OK,
        )

        # Adicionando class action nos botões.
        btn_ok = self.get_widget_for_response(
            response_id=Gtk.ResponseType.OK,
        )
        btn_ok.get_style_context().add_class(class_name='suggested-action')
        btn_cancel = self.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL,
        )
        btn_cancel.get_style_context().add_class(class_name='destructive-action')

        # Acessando o box do dialogo.
        content_area = self.get_content_area()
        content_area.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        content_area.set_spacing(spacing=12)
        content_area.set_margin_top(margin=12)
        content_area.set_margin_end(margin=12)
        content_area.set_margin_bottom(margin=12)
        content_area.set_margin_start(margin=12)

        label = Gtk.Label.new(str='Digite um texto qualquer:')
        content_area.append(child=label)

        self.entry = Gtk.Entry.new()
        self.entry.set_placeholder_text(text='Digite um texto qualquer.')
        content_area.append(child=self.entry)

        self.show()

    def dialog_response(self, widget, response):
        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
            self.parent.label.set_markup(
                str=f'Valor digitado no dialogo: <b>{self.get_entry_text()}</b>',
            )
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão CANCELAR pressionado')
            self.parent.label.set_text(str=f'Botão CANCELAR pressionado')
        widget.close()

    def get_entry_text(self):
        return self.entry.get_text()


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Box() vertical')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        # vbox.set_homogeneous(homogeneous=True)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        button_open_dialog = Gtk.Button.new_with_label(
            label='Abrir janela de dialogo'
        )
        button_open_dialog.connect('clicked', self.open_dialog)
        vbox.append(child=button_open_dialog)

        self.label = Gtk.Label.new(str='Valor digitado no dialogo:')
        vbox.append(child=self.label)

    def open_dialog(self, button):
        CustomDialog(parent=self)


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
