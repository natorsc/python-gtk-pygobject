from configparser import ConfigParser

import gi

gi.require_version(namespace='Gtk', version='3.0')
from MainWindow import MainWindow

from gi.repository import Gtk, Gio


class Application(Gtk.Application):
    config_file = './config/config.ini'
    config = ConfigParser()
    config.read(config_file)

    dark_mode = config.getboolean('DEFAULT', 'dark_mode')
    home_page = config.get('DEFAULT', 'home_page')

    settings = Gtk.Settings.get_default()

    def __init__(self):
        super().__init__(application_id='br.natorsc.Pasco',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        print(self.dark_mode)

    def do_startup(self):
        Gtk.Application.do_startup(self)
        if self.dark_mode:
            self.settings.set_property(
                property_name='gtk-application-prefer-dark-theme',
                value=self.dark_mode,
            )

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
