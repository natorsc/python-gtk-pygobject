import gi
import sys
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gio
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title(title="Adw.AboutWindow example")
        headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=headerbar)
        self.set_default_size(310,120)
        
        # Gtk.Box() layout
        self.mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.mainBox.set_margin_start(10)
        self.mainBox.set_margin_end(10)
        self.set_child(self.mainBox)
        
        # App menu
        menu_button_model = Gio.Menu()
        menu_button_model.append("About App", 'app.about')
        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        headerbar.pack_end(child=menu_button)
        
        self.label = Gtk.Label()
        self.label.set_label("Click on three dots for the display about window")
        self.mainBox.append(self.label)
        
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
            super().__init__(**kwargs, flags=Gio.ApplicationFlags.FLAGS_NONE)
            self.connect('activate', self.on_activate)
            self.create_action('about', self.on_about_action)
            
    def on_about_action(self, action, param):
        dialog = Adw.AboutWindow(transient_for=app.get_active_window())
        dialog.set_application_name("GUI Python PyObject GTK4")
        dialog.set_version("v1.0")
        dialog.set_developer_name("natorsc")
        dialog.set_license_type(Gtk.License(Gtk.License.BSD))
        dialog.set_comments("Python GTK4 Adw examples")
        dialog.set_website("https://github.com/natorsc/gui-python-pygobject-gtk4")
        dialog.set_issue_url("https://github.com/natorsc/gui-python-pygobject-gtk4/issues")
        dialog.add_credit_section("Contributors", ["Name1"])
        dialog.set_translator_credits("Translator")
        dialog.set_copyright("© 2022 natorsc")
        dialog.set_developers(["natorsc https://github.com/natorsc"])
        dialog.set_application_icon("python-symbolic")
        dialog.show()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)
    
    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()
app = MyApp(application_id="com.github.natorsc.gui-python-pygobject-gtk4")
app.run(sys.argv)
