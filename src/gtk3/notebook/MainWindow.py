# -*- coding: utf-8 -*-
"""Gtk.Notebook()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.Notebook')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        notebook = Gtk.Notebook.new()
        self.add(widget=notebook)

        page1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page1.set_border_width(border_width=12)

        # Adicionando widgets do tipo Label na pagina 1.
        for n in range(1, 6):
            label = Gtk.Label.new(f'Texto {n}')
            page1.pack_start(child=label, expand=False, fill=True, padding=6)

        tab_label = Gtk.Label.new(str='Página 1')
        notebook.append_page(child=page1, tab_label=tab_label)

        page2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page2.set_border_width(border_width=12)

        for n in range(1, 6):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            page2.pack_start(child=button, expand=False, fill=True, padding=6)

        # Ao invés de um label para a aba será utilizado um ícone.
        tab_icon = Gtk.Image.new_from_icon_name(
            icon_name='folder-documents-symbolic',
            size=Gtk.IconSize.MENU
        )

        notebook.append_page(child=page2, tab_label=tab_icon)

        self.show_all()


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
