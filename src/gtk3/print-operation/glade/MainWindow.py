# -*- coding: utf-8 -*-
"""Gtk.PrintOperation()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='PangoCairo', version='1.0')

from gi.repository import Gtk, Pango, PangoCairo

text = """<span size="xx-large">Lorem</span>
Lorem <b>ipsum</b> <span foreground="red">dolor</span> <big>sit</big> amet,
<i>consectetur</i> adipiscing <s>elit</s>, sed <sub>do</sub> 
<span background="green">eiusmod</span> <sup>tempor</sup> incididunt 
<small>ut</small> <tt>labore</tt> et <u>dolore</u> magna aliqua.\n
"""


class Handler:

    def __init__(self):

        # Variável auxilizar com as configurações do papel.
        self.page_setup = self._page_setup()
        # self.page_setup = self._custom_page_setup()

        # Variável para o dialogo de configuração do papel:
        self.print_settings = Gtk.PrintSettings.new()

        # Acessar os widgets da interface com builder.get_object(name) aqui:
        self.text_buffer = builder.get_object(name='text_buffer')

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



    def _print_operation(self):
        """Operação de impressão."""
        print_operation = Gtk.PrintOperation.new()
        print_operation.set_n_pages(1)
        # configurçaão inicial.
        print_operation.set_default_page_setup(default_page_setup=self.page_setup)
        # O que cada signal (sinal) deve realizar.
        print_operation.connect('begin-print', self.begin_print)
        print_operation.connect('draw_page', self.draw_page)
        return print_operation

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

    def begin_print(self, print_operation, context):
        """Quando a operação de impressão é iniciada."""
        # Posição inicial e final do texto no Gtk.TextView.
        start, stop = self.text_buffer.get_bounds()
        # Texto que está no Gtk.TextView.
        text = self.text_buffer.get_text(
            start=start,
            end=stop,
            include_hidden_chars=True,
        )
        # Contexto onde os dados serão inseridos.
        self.pango_layout = context.create_pango_layout()
        self.pango_layout.set_markup(text=text, length=-1)
        # Definindo uma configuração de fonte para a impressão.
        self.pango_layout.set_font_description(Pango.FontDescription('Arial 12'))

    def draw_page(self, print_operation, context, page_nr):
        """Desenhando a página."""
        # Criando o contexto.
        cairo_context = context.get_cairo_context()
        # Cor da fonte.
        cairo_context.set_source_rgb(0, 0, 0)
        # Adicionando o contexto na página.
        PangoCairo.show_layout(cr=cairo_context, layout=self.pango_layout)

    def open_print_dialog(self, widget):
        """Dialogo de impressão do sistema."""
        # Operação de impressão.
        print_operation = self._print_operation()

        # Resposta da operação de impressão.
        response = print_operation.run(
            action=Gtk.PrintOperationAction.PRINT_DIALOG,
            parent=win,
        )
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
        print_operation = self._print_operation()
        print_operation.run(action=Gtk.PrintOperationAction.PREVIEW, parent=win)

    def open_page_setup_dialog(self, widget):
        """Diálogo para configuração da página."""

        # Verificando o tamanho da página ANTES do diálogo.
        print(self.page_setup.get_page_width(unit=Gtk.Unit.MM))

        self.page_setup = Gtk.print_run_page_setup_dialog(
            parent=win,
            page_setup=self.page_setup,
            settings=self.print_settings,
        )

        # Verificando o tamanho da página DEPOIS do diálogo.
        print(self.page_setup.get_page_width(unit=Gtk.Unit.MM))

    def export_to_pdf(self, widget):
        """Exportando para arquivo."""
        print_operation = self._print_operation()
        print_operation.set_export_filename('nome-do-arquivo.pdf')
        response = print_operation.run(
            action=Gtk.PrintOperationAction.EXPORT,
            parent=win,
        )
        if response == Gtk.PrintOperationResult.APPLY:
            print('Arquivo exportado com sucesso')


if __name__ == '__main__':
    # Criando uma instancia do Builder.
    builder = Gtk.Builder.new()
    # Acessando/lendo arquivo de interface.
    builder.add_from_file(filename='./MainWindow.glade')
    # Registrando widget, métodos, etc.
    builder.connect_signals(obj_or_map=Handler())

    # Listando todos os widgets disponíveis no arquivo de interface.
    # print(builder.get_objects())

    # Acessando a janela que foi criada no arquivo de interface.
    win = builder.get_object(name='MainWindow')

    # Conectando o evento de fechar ao botão fechar da janela.
    win.connect('destroy', Gtk.main_quit)

    # Exibindo a janela.
    win.show_all()

    # Loop da interface.
    Gtk.main()
