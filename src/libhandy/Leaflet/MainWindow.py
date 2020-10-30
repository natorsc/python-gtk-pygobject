# -*- coding: utf-8 -*-
"""Handy.Leaflet. Não sei implementar"""

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '0.0')

from gi.repository import Gtk, Gio, GObject
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.Leaflet')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        hdy_title_bar = Handy.TitleBar.new()

        header_bar = Gtk.HeaderBar.new()
        header_bar.set_title(title='Handy.Leaflet')
        header_bar.set_subtitle(subtitle='Handy.Leaflet')
        header_bar.set_show_close_button(setting=True)
        hdy_title_bar.add(widget=header_bar)

        self.set_titlebar(titlebar=hdy_title_bar)

        self.hdy_leaflet = Handy.Leaflet.new()
        self.hdy_leaflet.set_transition_type(
            transition=Handy.LeafletChildTransitionType.SLIDE,
        )
        self.add(widget=self.hdy_leaflet)

        # Página 1
        page_1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        page_1.set_border_width(border_width=12)
        self.hdy_leaflet.add(widget=page_1)

        text_page_1 = (
            '<span size="xx-large" weight="bold">Leaflet (Folheto)</span>\n\n'
            '<span size="large">Clique no botão para ir para a página 2.</span>'
        )
        lbl_page_1 = Gtk.Label.new()
        lbl_page_1.set_line_wrap(wrap=True)
        lbl_page_1.set_markup(str=text_page_1)
        page_1.pack_start(child=lbl_page_1, expand=True, fill=True, padding=0)

        btn_more = Gtk.Button.new_with_label(label='Leia mais…')
        btn_more.set_halign(align=Gtk.Align.CENTER)
        page_1.pack_start(child=btn_more, expand=False, fill=True, padding=0)

        # Página 2
        page_2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        page_2.set_border_width(border_width=12)
        self.hdy_leaflet.add(widget=page_2)

        text_page_2 = (
            '<span size="xx-large" weight="bold">Página 2</span>\n\n'
            '<span size="large">Para voltar clique no botão localizado '
            'na barra de título</span>'
        )
        lbl_page_2 = Gtk.Label.new()
        lbl_page_2.set_line_wrap(wrap=True)
        lbl_page_2.set_markup(str=text_page_2)
        page_2.pack_start(child=lbl_page_2, expand=True, fill=True, padding=6)

        btn_back = Gtk.Button.new_with_label(label='Voltar')
        btn_back.set_halign(align=Gtk.Align.CENTER)
        page_2.pack_start(child=btn_back, expand=False, fill=True, padding=0)

        # Binding e Signals!
        btn_more.connect('clicked', self.show_page, page_2)
        self.hdy_leaflet.bind_property(
            'folded',
            btn_more,
            'visible',
            GObject.BindingFlags.SYNC_CREATE,
        )

        btn_back.connect('clicked', self.show_page, page_1)
        self.hdy_leaflet.bind_property(
            'folded',
            btn_back,
            'visible',
            GObject.BindingFlags.SYNC_CREATE,
        )

        self.show_all()

    def show_page(self, button, page):
        self.hdy_leaflet.set_visible_child(visible_child=page)


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
