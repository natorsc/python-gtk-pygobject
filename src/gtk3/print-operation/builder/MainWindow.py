# -*- coding: utf-8 -*-
"""Gtk.PrintOperation()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='PangoCairo', version='1.0')

from gi.repository import Gio, Gtk, Pango, PangoCairo

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


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    # Acessar os widgets da interface com Gtk.Template.Child(name) aqui:
    text_buffer = Gtk.Template.Child(name='text_buffer')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Variável auxilizar com as configurações do papel.
        self.page_setup = self._page_setup()
        # self.page_setup = self._custom_page_setup()

        # Variável para o dialogo de configuração do papel:
        self.print_settings = Gtk.PrintSettings.new()

        # Adicionando texto renderizado ao Gtk.TextView.
        text_buffer_iter = self.text_buffer.get_end_iter()
        self.text_buffer.insert_markup(
            iter=text_buffer_iter,
            markup=text,
            len=-1,
        )

        # Adicionando texto SEM renderizar ao Gtk.TextView.
        # Este texto será renderizado quando impresso ou no preview.
        text_buffer_iter = self.text_buffer.get_end_iter()
        self.text_buffer.insert(
            iter=text_buffer_iter,
            text=text,
            length=-1,
        )

        self.show_all()

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

    @Gtk.Template.Callback()
    def open_print_dialog(self, widget):
        """Dialogo de impressão do sistema."""
        # Operação de impressão.
        print_operation = PrintOperation(text_buffer=self.text_buffer)
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

    @Gtk.Template.Callback()
    def open_preview(self, widget):
        """Pré visualizador do sistema."""
        print_operation = PrintOperation(text_buffer=self.text_buffer)
        response = print_operation.run(action=Gtk.PrintOperationAction.PREVIEW, parent=self)

    @Gtk.Template.Callback()
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

    @Gtk.Template.Callback()
    def export_to_pdf(self, widget):
        """Exportando para arquivo."""
        print_operation = PrintOperation(text_buffer=self.text_buffer)
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
