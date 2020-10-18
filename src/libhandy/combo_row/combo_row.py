# -*- coding: utf-8 -*-
"""Handy.ComboRow()."""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    # Nome dos ícones.
    icons_standard = ['mail-send-receive', 'user-trash', 'face-smile',
                      'call-start', 'call-stop']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configurando a janela principal.
        self.set_title(title='Handy.ComboRow')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=12)


        headerbar = Gtk.HeaderBar.new()
        # Definindo o título que será exibido na barra.
        # O titulo definido aqui sobrescreve o titulo da janela principal.
        headerbar.set_title(title='Gtk.ListBox')
        # Definindo um sub titulo para o HeaderBar.
        headerbar.set_subtitle(subtitle='com Handy.ComboRow')
        # Torna visível os botões de minimizar, maximizar e fechar.
        # Por padrão essa opção é False.
        headerbar.set_show_close_button(setting=True)
        # Adicionando o HeaderBar na janela principal.
        self.set_titlebar(titlebar=headerbar)

        button_create = Gtk.Button.new_from_icon_name(
            icon_name='document-new-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        button_create.connect('clicked', self.create)
        headerbar.pack_start(child=button_create)

        # Variável auxilizar com os métodos que serão executados pelos
        # botões contidos no menu popover.
        self.menu_func = {
            'editar': self.update,
            'deletar': self.delete,
        }

        # Criando um scroll para que a janela principal possa comportar os widgets
        scrolled = Gtk.ScrolledWindow.new(hadjustment=None, vadjustment=None)
        self.add(widget=scrolled)

        self.list_box = Gtk.ListBox.new()
        scrolled.add(widget=self.list_box)

        # NotImplementedError: ListModel can not be constructed
        # gio_list_model = Gio.ListModel()
        # Utilizando Gio.ListStore no lugar do Gio.ListModel().
        self.gio_list_store = Gio.ListStore.new(item_type=Gtk.Button)
        # Adicionando e forma dinâmica.
        for label in self.menu_func.keys():
            self.gio_list_store.append(Gtk.Button.new_with_label(label=label))

        self.combo_row_list = []
        # Criando Handy.ComboRow:
        for i, icon in enumerate(self.icons_standard):
            self.hdy_combo_row = Handy.ComboRow.new()
            self.hdy_combo_row.set_icon_name(icon_name=self.icons_standard[i])
            self.hdy_combo_row.set_title(title=f'Título {i}')
            self.hdy_combo_row.set_subtitle(subtitle=f'subtítulo {i}')
            self.hdy_combo_row.bind_model(
                model=self.gio_list_store,
                create_list_widget_func=self._create_list_widget_func,
                create_current_widget_func=self._create_current_widget_func,
            )

            # Adicionando a linha no listbox.
            self.list_box.add(widget=self.hdy_combo_row)
            self.combo_row_list.append(self.hdy_combo_row)

        self.show_all()

    def create(self, widget):
        print('update')
        hdy_combo_row = Handy.ComboRow.new()
        hdy_combo_row.set_icon_name(icon_name='document-new')
        hdy_combo_row.set_title(title=f'Novo item criado')
        hdy_combo_row.set_subtitle(subtitle=f'Novo item criado')
        hdy_combo_row.bind_model(
            model=self.gio_list_store,
            create_list_widget_func=self._create_list_widget_func,
            create_current_widget_func=self._create_current_widget_func,
        )
        # Adicionando a linha no listbox.
        self.list_box.add(widget=hdy_combo_row)
        self.list_box.show_all()

    def update(self, widget):
        print('update')
        selected_row = self.list_box.get_selected_row()
        selected_row.set_title('Novo título')
        selected_row.set_subtitle(subtitle=f'Novo subtitulo')

    def delete(self, widget):
        print('Delete')
        selected_row = self.list_box.get_selected_row()
        self.list_box.remove(selected_row)
        self.list_box.show_all()

    def _create_current_widget_func(self, widget):
        print('_create_current_widget_func')
        print(widget)
        print('---\n')
        return Gtk.Label.new(str='Opções')

    def _create_list_widget_func(self, widget, extra):
        print('_create_list_widget_func')
        print(widget)
        print(extra)
        print('---\n')

        label = widget.get_label()

        btn_menu_popover = Gtk.ModelButton.new()
        btn_menu_popover.set_label(label=label.capitalize())
        btn_menu_popover.connect('clicked', self.menu_func[label])
        return btn_menu_popover


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
