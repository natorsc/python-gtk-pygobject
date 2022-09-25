# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.PrintOperation()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk, Pango, PangoCairo
import subprocess
import sys
from pathlib import Path

Adw.init()

BASE_DIR = Path(__file__).resolve().parent
PDF_FILE = str(BASE_DIR.joinpath('nome-do-arquivo.pdf'))

text = """<span size="xx-large">Lorem</span>
Lorem <b>ipsum</b> <span foreground="red">dolor</span> <big>sit</big> amet,
<i>consectetur</i> adipiscing <s>elit</s>, sed <sub>do</sub> 
<span background="green">eiusmod</span> <sup>tempor</sup> incididunt 
<small>ut</small> <tt>labore</tt> et <u>dolore</u> magna aliqua.\n
"""


class PrintOperation(Gtk.PrintOperation):

    def __init__(self, text_buffer):
        super().__init__()

        # Operação de impressão.
        self.set_n_pages(1)
        # self.set_default_page_setup(default_page_setup=page_setup)
        self.connect('begin-print', self.begin_print, text_buffer)
        self.connect('draw_page', self.draw_page)

        self.pango_layout = None

    def begin_print(self, print_operation, context, text_view_buffer):
        """Quando a operação de impressão é iniciada."""
        # Posição inicial e final do texto no Gtk.TextView.
        start, stop = text_view_buffer.get_bounds()
        # Texto que está no Gtk.TextView.
        text = text_view_buffer.get_text(
            start=start,
            end=stop,
            include_hidden_chars=True,
        )
        self.pango_layout = context.create_pango_layout()
        self.pango_layout.set_markup(text=text, length=-1)
        self.pango_layout.set_font_description(
            Pango.FontDescription('Arial 12'),
        )

    def draw_page(self, print_operation, context, page_nr):
        """Desenhando a página."""
        cairo_context = context.get_cairo_context()
        # Cor da fonte.
        cairo_context.set_source_rgb(0, 0, 0)
        # Criando o conteudo na página.
        PangoCairo.show_layout(cr=cairo_context, layout=self.pango_layout)


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.PrintOperation().')
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

        # Variável auxilizar com as configurações do papel.
        self.page_setup = self.page_setup()
        # self.page_setup = self.custom_page_setup()

        # Variável para o dialogo de configuração do papel:
        self.print_settings = Gtk.PrintSettings.new()

        # Buffer de texto.
        self.text_buffer = Gtk.TextBuffer.new()

        # Adicionando texto renderizado ao Gtk.TextView.
        text_buffer_iter = self.text_buffer.get_end_iter()
        self.text_buffer.insert_markup(
            iter=text_buffer_iter,
            markup=text,
            len=-1,
        )

        text_view = Gtk.TextView.new_with_buffer(buffer=self.text_buffer)
        text_view.set_vexpand(expand=True)
        vbox.append(child=text_view)

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        hbox.set_halign(align=Gtk.Align.CENTER)
        vbox.append(child=hbox)

        button_print_dialog = Gtk.Button.new_with_label('Imprimir')
        button_print_dialog.connect('clicked', self.open_print_dialog)
        hbox.append(child=button_print_dialog)

        button_open_preview = Gtk.Button.new_with_label('Visualizar')
        button_open_preview.connect('clicked', self.open_preview)
        hbox.append(child=button_open_preview)

        button_page_setup_dialog = Gtk.Button.new_with_label(
            'Configurar página')
        button_page_setup_dialog.connect(
            'clicked', self.open_page_setup_dialog)
        hbox.append(child=button_page_setup_dialog)

        button_export_pdf = Gtk.Button.new_with_label('Exportar para PDF')
        button_export_pdf.connect('clicked', self.export_to_pdf)
        hbox.append(child=button_export_pdf)

    def page_setup(self):
        """Configuração padrão para o papel."""
        # Tamanho do papel.
        paper_size = Gtk.PaperSize.new(name=Gtk.PAPER_NAME_A4)

        # Configurações da página.
        page_setup = Gtk.PageSetup.new()
        page_setup.set_paper_size_and_default_margins(size=paper_size)
        return page_setup

    def custom_page_setup(self):
        """Configuração personalizada de papel."""
        # Tamanho do papel.
        paper_size = Gtk.PaperSize.new(name=Gtk.PAPER_NAME_A4)

        # Configurações da página.
        custom_page_setup = Gtk.PageSetup.new()
        # Personalizando a marge no topo
        custom_page_setup.set_top_margin(margin=20, unit=Gtk.Unit.MM)
        custom_page_setup.set_left_margin(margin=20, unit=Gtk.Unit.MM)
        # Orientação do papel:
        custom_page_setup.set_orientation(
            orientation=Gtk.PageOrientation.PORTRAIT)
        # Quando a pagina é personalizada utilizar:
        custom_page_setup.set_paper_size(size=paper_size)
        return custom_page_setup

    def open_print_dialog(self, widget):
        """Dialogo de impressão do sistema."""
        # Operação de impressão.
        print_operation = PrintOperation(text_buffer=self.text_buffer)
        print_operation.set_default_page_setup(
            default_page_setup=self.page_setup)

        # Resposta da operação de impressão.
        response = print_operation.run(
            action=Gtk.PrintOperationAction.PRINT_DIALOG, parent=self)
        if response == Gtk.PrintOperationResult.ERROR:
            print('ERROR')
        elif response == Gtk.PrintOperationResult.APPLY:
            print('APPLY')
        elif response == Gtk.PrintOperationResult.CANCEL:
            print('CANCEL')
        elif response == Gtk.PrintOperationResult.IN_PROGRESS:
            print('IN_PROGRESS')

    def open_preview(self, widget):
        """Pré visualizador do sistema."""
        print_operation = PrintOperation(text_buffer=self.text_buffer)
        response = print_operation.run(
            action=Gtk.PrintOperationAction.PREVIEW, parent=self)
        if response == Gtk.PrintOperationResult.ERROR:
            print('ERROR')
        elif response == Gtk.PrintOperationResult.APPLY:
            print('APPLY')
        elif response == Gtk.PrintOperationResult.CANCEL:
            print('CANCEL')
        elif response == Gtk.PrintOperationResult.IN_PROGRESS:
            print('IN_PROGRESS')

    def open_page_setup_dialog(self, widget):
        """Diálogo para configuração da página."""

        # Verificando o tamanho da página ANTES do diálogo.
        print(self.page_setup.get_page_width(unit=Gtk.Unit.MM))
        self.page_setup = Gtk.print_run_page_setup_dialog(
            parent=self,
            page_setup=self.page_setup,
            settings=self.print_settings,
        )
        # Verificando o tamanho da página DEPOIS do diálogo.
        print(self.page_setup.get_page_width(unit=Gtk.Unit.MM))

    def export_to_pdf(self, widget):
        """Exportando para arquivo."""
        print_operation = PrintOperation(text_buffer=self.text_buffer)
        print_operation.set_export_filename(PDF_FILE)
        response = print_operation.run(
            action=Gtk.PrintOperationAction.EXPORT, parent=self)
        if response == Gtk.PrintOperationResult.APPLY:
            print('Arquivo exportado com sucesso')


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
