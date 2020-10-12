# -*- coding: utf-8 -*-
"""Ativando e desativando o dark mode (modo escuro)."""
import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Utilizando modo escuro (dark mode)')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        # Atibuindo as configurações do aplicativo em uma variável.
        self.settings = Gtk.Settings.get_default()

        grid_layout = grid = Gtk.Grid.new()
        grid_layout.set_border_width(border_width=12)
        grid.set_column_spacing(spacing=12)
        self.add(widget=grid_layout)

        text = 'Clique no switch para ativar ou desativar o modo escuro (dark mode)'
        label = Gtk.Label.new(str=text)
        grid_layout.add(widget=label)

        switch = Gtk.Switch.new()
        switch.connect('notify::active', self.on_switch_clicked)
        grid_layout.add(widget=switch)

        self.show_all()

    def on_switch_clicked(self, widget, state):
        if widget.get_active():
            self.settings.set_property(
                'gtk-application-prefer-dark-theme', True)
        else:
            self.settings.set_property(
                'gtk-application-prefer-dark-theme', False)


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
