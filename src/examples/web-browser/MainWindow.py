# -*- coding: utf-8 -*-
"""webkit.WebView()."""

import gi

gi.require_version(namespace='Gdk', version='3.0')
gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='WebKit2', version='4.0')

from gi.repository import Gdk, Gtk, Gio, WebKit2


class Settings(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title(title='Configurações')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        scrolled = Gtk.ScrolledWindow.new(hadjustment=None, vadjustment=None)
        self.add(widget=scrolled)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        scrolled.add(widget=vbox)

        label_start_page = Gtk.Label.new(str='Página inicial')
        label_start_page.set_xalign(xalign=0)
        vbox.pack_start(
            child=label_start_page,
            expand=False,
            fill=False,
            padding=0,
        )

        entry_start_page = Gtk.Entry.new()
        vbox.pack_start(
            child=entry_start_page,
            expand=False,
            fill=True,
            padding=0,
        )

        separetor_start_page = Gtk.Separator.new(
            orientation=Gtk.Orientation.HORIZONTAL,
        )
        vbox.pack_start(
            child=separetor_start_page,
            expand=False,
            fill=True,
            padding=6,
        )

        self.show_all()


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='webkit.WebView')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')
        self.connect('scroll-event', self.on_page_scrool)

        self.headerbar = Gtk.HeaderBar.new()
        self.headerbar.set_title(title='webkit.WebView')
        self.headerbar.set_subtitle(subtitle='webkit.WebView')
        self.headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=self.headerbar)

        hbox_headerbar_left = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.headerbar.pack_start(child=hbox_headerbar_left)
        hbox_headerbar_right = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.headerbar.pack_end(child=hbox_headerbar_right)

        btn_back = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        btn_back.connect('clicked', self.on_btn_back_clicked)
        hbox_headerbar_left.pack_start(child=btn_back, expand=False, fill=True, padding=0)

        btn_reload = Gtk.Button.new_from_icon_name(
            icon_name='view-refresh-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        btn_reload.connect('clicked', self.on_btn_reload_clicked)
        hbox_headerbar_left.pack_start(child=btn_reload, expand=False, fill=True, padding=6)

        btn_forward = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic-rtl',
            size=Gtk.IconSize.BUTTON
        )
        btn_forward.connect('clicked', self.on_btn_forward_clicked)
        hbox_headerbar_left.pack_start(child=btn_forward, expand=False, fill=True, padding=0)

        entry_uri = Gtk.Entry.new()
        entry_uri.set_size_request(width=250, height=-1)
        entry_uri.connect('activate', self.on_entry_activate)
        hbox_headerbar_right.pack_start(child=entry_uri, expand=False, fill=True, padding=6)

        img_btn_menu = Gtk.Image.new_from_icon_name(
            icon_name='open-menu-symbolic',
            size=Gtk.IconSize.MENU,
        )
        btn_open_menu_popover = Gtk.MenuButton.new()
        btn_open_menu_popover.add(widget=img_btn_menu)
        hbox_headerbar_right.pack_end(child=btn_open_menu_popover, expand=False, fill=True, padding=0)

        vbox_popover = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox_popover.set_border_width(border_width=6)
        popover_menu = Gtk.Popover.new(relative_to=btn_open_menu_popover)
        popover_menu.add(widget=vbox_popover)
        btn_open_menu_popover.set_popover(popover=popover_menu)

        btn_open_cnf = Gtk.ModelButton.new()
        btn_open_cnf.set_label(label='Configurações')
        btn_open_cnf.connect('clicked', self.on_btn_open_cnf_clicked)
        vbox_popover.pack_start(child=btn_open_cnf, expand=False, fill=True, padding=0)

        self.web_view = WebKit2.WebView.new()
        self.web_view.load_uri(uri='http://127.0.0.1:8000')
        self.web_view.connect('notify::title', self.notify_title)
        self.add(widget=self.web_view)

        popover_menu.show_all()
        self.show_all()

    def on_btn_open_cnf_clicked(self, widget):
        settings = Settings()
        settings.set_transient_for(parent=self)

    def on_page_scrool(self, widget, event_scroll):
        if event_scroll.direction == Gdk.ScrollDirection.DOWN:
            self.headerbar.hide()
        elif event_scroll.direction == Gdk.ScrollDirection.UP:
            self.headerbar.show()

    def notify_title(self, widget, g_param_string):
        self.headerbar.set_subtitle(subtitle=widget.get_title())

    def on_btn_back_clicked(self, widget):
        if self.web_view.can_go_back():
            self.web_view.go_back()

    def on_btn_reload_clicked(self, widget):
        self.web_view.reload()

    def on_btn_forward_clicked(self, widget):
        if self.web_view.can_go_forward():
            self.web_view.go_forward()

    def on_entry_activate(self, widget):
        uri = widget.get_text()
        if uri.startswith('http://') or uri.startswith('https://'):
            self.web_view.load_uri(uri=uri)
        else:
            uri = f'https://{uri}'
            self.web_view.load_uri(uri=uri)


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
