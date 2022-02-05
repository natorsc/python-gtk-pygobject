# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Popover()."""
import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


def set_app_theme(settings, theme_name):
    settings.set_property('gtk-theme-name', theme_name)


class HamburgerMenu(Gtk.Popover):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_child(child=vbox)

        # linha 01
        hbox_line_01 = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox_line_01.set_homogeneous(True)
        vbox.append(child=hbox_line_01)

        button_new_window = Gtk.Button.new_from_icon_name('window-new-symbolic')
        button_new_window.set_tooltip_text(text='teste')
        hbox_line_01.append(child=button_new_window)

        button_new_tab = Gtk.Button.new_from_icon_name('tab-new-symbolic')
        hbox_line_01.append(child=button_new_tab)

        button_new_folder = Gtk.Button.new_from_icon_name('folder-new-symbolic')
        hbox_line_01.append(child=button_new_folder)

        vseparator_line_01 = Gtk.Separator.new(orientation=Gtk.Orientation.VERTICAL)
        vbox.append(child=vseparator_line_01)

        # linha 02
        hbox_line_02 = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox_line_02.set_homogeneous(True)
        vbox.append(child=hbox_line_02)

        label_edit = Gtk.Label.new()
        label_edit.set_label(str='Editar')
        hbox_line_02.append(child=label_edit)

        button_cut = Gtk.Button.new_from_icon_name('edit-cut-symbolic')
        hbox_line_02.append(child=button_cut)

        button_copy = Gtk.Button.new_from_icon_name('edit-copy-symbolic')
        hbox_line_02.append(child=button_copy)

        button_paste = Gtk.Button.new_from_icon_name('edit-paste-symbolic')
        hbox_line_02.append(child=button_paste)

        vseparator_line_02 = Gtk.Separator.new(orientation=Gtk.Orientation.VERTICAL)
        vbox.append(child=vseparator_line_02)

        # linha 03
        button_select_all = Gtk.Button.new_with_label(label='Selecionar tudo')
        button_select_all.get_style_context().add_class(class_name='flat')
        vbox.append(child=button_select_all)

        vseparator_line_03 = Gtk.Separator.new(orientation=Gtk.Orientation.VERTICAL)
        vbox.append(child=vseparator_line_03)

        # linha 04
        listbox_line_04 = Gtk.ListBox.new()
        listbox_line_04.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        vbox.append(child=listbox_line_04)

        row_show_hidden_files = Gtk.ListBoxRow.new()
        row_show_hidden_files.set_margin_bottom(margin=6)
        row_show_hidden_files.set_halign(align=Gtk.Align.END)
        listbox_line_04.append(child=row_show_hidden_files)

        hbox_row_show_hidden_files = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row_show_hidden_files.set_child(child=hbox_row_show_hidden_files)

        label_show_hidden_files = Gtk.Label.new()
        label_show_hidden_files.set_label(str='Mostrar arquivos ocultos')
        hbox_row_show_hidden_files.append(child=label_show_hidden_files)

        checkbox_show_hidden_files = Gtk.CheckButton.new()
        checkbox_show_hidden_files.set_margin_start(margin=12)
        hbox_row_show_hidden_files.append(child=checkbox_show_hidden_files)

        # Mostrar barra lateral.
        row_show_sidebar = Gtk.ListBoxRow.new()
        row_show_sidebar.set_halign(align=Gtk.Align.END)
        listbox_line_04.append(child=row_show_sidebar)

        hbox_row_show_sidebar = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row_show_sidebar.set_child(child=hbox_row_show_sidebar)

        label_show_sidebar = Gtk.Label.new()
        label_show_sidebar.set_label(str='Mostrar barra lateral')
        hbox_row_show_sidebar.append(child=label_show_sidebar)

        checkbox_show_sidebar = Gtk.CheckButton.new()
        checkbox_show_sidebar.set_margin_start(margin=12)
        hbox_row_show_sidebar.append(child=checkbox_show_sidebar)

        vseparator_line_04 = Gtk.Separator.new(orientation=Gtk.Orientation.VERTICAL)
        vbox.append(child=vseparator_line_04)

        # linha 05
        button_preferences = Gtk.Button.new_with_label(label='Preferências')
        button_preferences.get_style_context().add_class(class_name='flat')
        vbox.append(child=button_preferences)

        button_keyboard_shortcuts = Gtk.Button.new_with_label(label='Atalhos de teclado')
        button_keyboard_shortcuts.get_style_context().add_class(class_name='flat')
        vbox.append(child=button_keyboard_shortcuts)

        button_help = Gtk.Button.new_with_label(label='Ajuda')
        button_help.get_style_context().add_class(class_name='flat')
        vbox.append(child=button_help)

        button_about = Gtk.Button.new_with_label(label='Sobre')
        button_about.get_style_context().add_class(class_name='flat')
        vbox.append(child=button_about)


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Popover()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        # Atibuindo as configurações do aplicativo em uma variável.
        self.settings = Gtk.Settings.get_default()
        gtk_theme_name = self.settings.get_property('gtk-theme-name')
        set_app_theme(settings=self.settings, theme_name=gtk_theme_name)

        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_popover(popover=HamburgerMenu())
        headerbar.pack_end(child=menu_button)


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
