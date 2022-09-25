# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Dialog() personalizado."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


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

    def dialog_response(self, dialog, response):
        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.OK:
            print('Botão OK pressionado')
            text = self.get_entry_text()
            if text.split():
                self.parent.label.set_markup(
                    str=f'Valor digitado no dialogo: <b>{text}</b>',
                )
            else:
                self.parent.label.set_text(
                    str=f'Digite algo no campo de texto da janela de diálogo',
                )
        elif response == Gtk.ResponseType.CANCEL:
            print('Botão CANCELAR pressionado')
            self.parent.label.set_text(str=f'Botão CANCELAR pressionado')

        dialog.close()

    def get_entry_text(self):
        return self.entry.get_text()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Dialog() personalizado')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=headerbar)

        menu_button_model = Gio.Menu()
        menu_button_model.append('Preferências', 'app.preferences')

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        headerbar.pack_end(child=menu_button)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        self.label = Gtk.Label.new(str='Este texto será alterado...')
        self.label.set_valign(Gtk.Align.CENTER)
        self.label.set_vexpand(expand=True)
        vbox.append(child=self.label)

        button_open_dialog = Gtk.Button.new_with_label(
            label='Abrir janela de dialogo'
        )
        button_open_dialog.connect('clicked', self.open_dialog)
        vbox.append(child=button_open_dialog)

    def open_dialog(self, button):
        CustomDialog(parent=self)


class ExampleApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='br.com.justcode.Example',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.exit_app, ['<primary>q'])
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ExampleWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def on_preferences_action(self, action, param):
        print('Ação app.preferences foi ativa.')

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)


if __name__ == '__main__':
    import sys

    app = ExampleApplication()
    app.run(sys.argv)
