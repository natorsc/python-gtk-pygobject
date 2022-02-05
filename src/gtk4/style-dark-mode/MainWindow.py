# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Ativando e desativando o dark mode (modo escuro)."""
import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.application = kwargs.get('application')
        self.gtk_settings = self.application.gtk_settings

        self.set_title(title='Python e GTK 4: PyGObject Ativando e desativando o dark mode (modo escuro)')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        grid = Gtk.Grid.new()
        grid.set_margin_top(margin=12)
        grid.set_margin_end(margin=12)
        grid.set_margin_bottom(margin=12)
        grid.set_margin_start(margin=12)
        grid.set_column_spacing(spacing=12)
        self.set_child(child=grid)

        text = 'Clique no switch para ativar ou desativar o modo escuro (dark mode)'
        label = Gtk.Label.new(str=text)
        grid.attach(child=label, column=0, row=0, width=1, height=1)

        self.switch = Gtk.Switch.new()
        self.switch.connect('notify::active', self.on_switch_active)
        grid.attach(child=self.switch, column=1, row=0, width=1, height=1)

    def on_switch_active(self, widget, state):
        if widget.get_active():
            # self.settings.set_property('gtk-application-prefer-dark-theme', True)
            self.gtk_settings.set_property('gtk-theme-name', 'Adwaita-dark')
        else:
            # self.settings.set_property('gtk-application-prefer-dark-theme', False)
            self.gtk_settings.set_property('gtk-theme-name', 'Adwaita')


class Application(Gtk.Application):
    gtk_settings = None

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.gtk_settings = Gtk.Settings.get_default()
        self.gtk_theme_name = self.gtk_settings.get_property('gtk-theme-name')

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

        if self.gtk_theme_name == 'Adwaita-dark':
            win.switch.set_state(state=True)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
