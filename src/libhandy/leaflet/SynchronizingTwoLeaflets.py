# -*- coding: utf-8 -*-
"""Handy.Leaflet()."""

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio, GObject
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.Leaflet')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Para armazenar as barras de título.
        hdy_leaflet_title = Handy.Leaflet.new()
        hdy_leaflet_title.set_transition_type(
            transition=Handy.LeafletChildTransitionType.SLIDE,
        )

        hdy_title_bar = Handy.TitleBar.new()
        hdy_title_bar.add(widget=hdy_leaflet_title)
        self.set_titlebar(titlebar=hdy_title_bar)

        # Para armazenar as páginas.
        self.hdy_leaflet_content = Handy.Leaflet.new()
        self.hdy_leaflet_content.set_transition_type(
            transition=Handy.LeafletChildTransitionType.SLIDE,
        )
        self.add(widget=self.hdy_leaflet_content)

        # Página 1
        # Barra de título.
        header_bar_page_1 = Gtk.HeaderBar.new()
        header_bar_page_1.set_title(title='Handy.Leaflet')
        header_bar_page_1.set_subtitle(subtitle='Página 1')
        header_bar_page_1.set_show_close_button(setting=True)
        hdy_leaflet_title.add(widget=header_bar_page_1)
        hdy_leaflet_title.child_set(child=header_bar_page_1, name='page_1')

        # Widgets
        page_1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        page_1.set_border_width(border_width=12)

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

        # SizeGroup é utilizadopara definir o conteúdo de cada página
        group_page_1 = Gtk.SizeGroup.new(mode=Gtk.SizeGroupMode.HORIZONTAL)
        group_page_1.add_widget(widget=header_bar_page_1)
        group_page_1.add_widget(widget=page_1)

        self.hdy_leaflet_content.add(widget=page_1)
        self.hdy_leaflet_content.child_set(child=page_1, name='page_1')

        # Página 2
        header_bar_page_2 = Gtk.HeaderBar.new()
        header_bar_page_2.set_title(title='Handy.Leaflet')
        header_bar_page_2.set_subtitle(subtitle='Página 2')
        header_bar_page_2.set_show_close_button(setting=True)
        hdy_leaflet_title.add(widget=header_bar_page_2)
        hdy_leaflet_title.child_set(child=header_bar_page_2, name='page_2')

        page_2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        page_2.set_border_width(border_width=12)

        text_page_2 = (
            '<span size="xx-large" weight="bold">Página 2</span>\n\n'
            '<span size="large">Para voltar clique no botão localizado '
            'na barra de título</span>'
        )
        lbl_page_2 = Gtk.Label.new()
        lbl_page_2.set_line_wrap(wrap=True)
        lbl_page_2.set_markup(str=text_page_2)
        page_2.pack_start(child=lbl_page_2, expand=True, fill=True, padding=6)

        btn_back = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic',
            size=Gtk.IconSize.BUTTON,
        )
        header_bar_page_2.add(widget=btn_back)

        group_page_2 = Gtk.SizeGroup.new(mode=Gtk.SizeGroupMode.HORIZONTAL)
        group_page_2.add_widget(widget=header_bar_page_2)
        group_page_2.add_widget(widget=page_2)

        self.hdy_leaflet_content.add(widget=page_2)
        self.hdy_leaflet_content.child_set(child=page_2, name='page_2')

        # Ação dos botões.
        btn_back.connect('clicked', self._show_page, page_1)
        btn_more.connect('clicked', self._show_page, page_2)

        # Binding e Signals!
        hdy_leaflet_title.bind_property(
            'folded',
            btn_back,
            'visible',
            GObject.BindingFlags.SYNC_CREATE
        )

        self.hdy_leaflet_content.bind_property(
            'visible-child-name',
            hdy_leaflet_title,
            'visible-child-name',
            GObject.BindingFlags.SYNC_CREATE
        )

        self.hdy_leaflet_content.bind_property(
            'folded',
            btn_more,
            'visible',
            GObject.BindingFlags.SYNC_CREATE
        )

        self.show_all()

    def _show_page(self, button, page):
        self.hdy_leaflet_content.set_visible_child(page)


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
