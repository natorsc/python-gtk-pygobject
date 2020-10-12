# -*- coding: utf-8 -*-
"""Operações de impressão com Gtk.PrintOperation()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='PangoCairo', version='1.0')

from gi.repository import Gio, Gtk, Pango, PangoCairo


class PrintOperation(Gtk.PrintOperation):

    def __init__(self, text_view_buffer):
        super().__init__()

        self.page_setup = self._page_setup()

        # Operação de impressão.
        self.set_n_pages(1)
        self.set_default_page_setup(default_page_setup=self.page_setup)
        self.connect('begin-print', self.begin_print, text_view_buffer)
        self.connect('draw_page', self.draw_page)

    def _page_setup(self):
        """Configuração padrão para o papel."""
        # Tamanho do papel.
        paper_size = Gtk.PaperSize.new(name=Gtk.PAPER_NAME_A4)

        # Configurações da página.
        page_setup = Gtk.PageSetup.new()
        page_setup.set_paper_size_and_default_margins(size=paper_size)
        return page_setup

    def _custom_page_setup(self):
        """Configuração personalizada de papel."""
        # Tamanho do papel.
        paper_size = Gtk.PaperSize.new(name=Gtk.PAPER_NAME_A4)

        # Configurações da página.
        custom_page_setup = Gtk.PageSetup.new()
        # Personalizando a marge no topo
        custom_page_setup.set_top_margin(margin=20, unit=Gtk.Unit.MM)
        custom_page_setup.set_left_margin(margin=20, unit=Gtk.Unit.MM)
        # Orientação do papel:
        custom_page_setup.set_orientation(orientation=Gtk.PageOrientation.PORTRAIT)
        # Quando a pagina é personalizada utilizar:
        custom_page_setup.set_paper_size(size=paper_size)
        return custom_page_setup

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
        self.pango_layout.set_font_description(Pango.FontDescription('Arial 12'))

    def draw_page(self, print_operation, context, page_nr):
        """Desenhando a página."""
        cairo_context = context.get_cairo_context()
        # Cor da fonte.
        cairo_context.set_source_rgb(0, 0, 0)
        # Criando o conteudo na página.
        PangoCairo.show_layout(cr=cairo_context, layout=self.pango_layout)


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configurando a janela principal.
        self.set_title(title='Operações de impressão com Gtk.PrintOperation()')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Variável auxilizar com as configurações do papel.
        self.page_setup = self._page_setup()
        # self.page_setup = self._custom_page_setup()

        # Widgets.
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        self.text_view_buffer = Gtk.TextBuffer.new()
        text_view = Gtk.TextView.new_with_buffer(buffer=self.text_view_buffer)
        vbox.pack_start(child=text_view, expand=True, fill=True, padding=0)

        h_btn_box = Gtk.ButtonBox.new(orientation=Gtk.Orientation.HORIZONTAL)
        h_btn_box.set_spacing(spacing=6)
        vbox.pack_start(child=h_btn_box, expand=False, fill=True, padding=0)

        btn_print_dialog = Gtk.Button.new_with_label('Imprimir')
        btn_print_dialog.connect('clicked', self.open_print_dialog)
        h_btn_box.pack_start(child=btn_print_dialog, expand=False, fill=False, padding=0)

        btn_open_preview = Gtk.Button.new_with_label('Visualizar')
        btn_open_preview.connect('clicked', self.open_preview)
        h_btn_box.pack_start(child=btn_open_preview, expand=False, fill=False, padding=0)

        btn_page_setup_dialog = Gtk.Button.new_with_label('Configurar página')
        btn_page_setup_dialog.connect('clicked', self.open_page_setup_dialog)
        h_btn_box.pack_start(child=btn_page_setup_dialog, expand=False, fill=False, padding=0)

        btn_export_pdf = Gtk.Button.new_with_label('Exportar para PDF')
        btn_export_pdf.connect('clicked', self.export_to_pdf)
        h_btn_box.pack_start(child=btn_export_pdf, expand=False, fill=False, padding=0)

        self.show_all()

    def open_print_dialog(self, widget):
        """Dialogo de impressão do sistema."""
        # Operação de impressão.
        print_operation = PrintOperation(text_view_buffer=self.text_view_buffer)
        print_operation.set_print_settings(print_settings=self.print_settings)
        print_operation.set_default_page_setup(default_page_setup=self.page_setup)

        # Resposta da operação de impressão.
        response = print_operation.run(action=Gtk.PrintOperationAction.PRINT_DIALOG, parent=self)
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
        print_operation = PrintOperation(text_view_buffer=self.text_view_buffer)
        response = print_operation.run(action=Gtk.PrintOperationAction.PREVIEW, parent=self)

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
        print_operation = PrintOperation(text_view_buffer=self.text_view_buffer)
        print_operation.set_export_filename('nome-do-arquivo.pdf')
        response = print_operation.run(action=Gtk.PrintOperationAction.EXPORT, parent=self)
        if response == Gtk.PrintOperationResult.APPLY:
            print('Arquivo exportado com sucesso')


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
