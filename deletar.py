from gi.repository import Gio, Gtk
import sys
import os
import distro
import socket


class MyWindow(Gtk.ApplicationWindow):
    # constructor for a Gtk.ApplicationWindow

    def __init__(self, app):

        Gtk.Window.__init__(self, title="GTK Example", application=app)
        self.set_default_size(600, 300)
        self.set_default_icon_from_file(filename='logos/gtk.svg')

        # Creating headerbar.
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title(title='GTK Example')
        headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=headerbar)

        # Icon that will be displayed on the menu button.
        menu_button_image = Gtk.Image.new_from_icon_name(
            icon_name='open-menu-symbolic',
            size=Gtk.IconSize.MENU,
        )

        # Button that will contain the popover.
        menu_button = Gtk.MenuButton.new()
        menu_button.add(widget=menu_button_image)
        menu_button.connect('clicked', self.show_menu)

        # Adding the button to the headerbar.
        headerbar.pack_end(child=menu_button)

        # Box that will contain the popover menu widgets.
        menu_box = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        menu_box.set_border_width(border_width=24)

        # Creating the popover menu.
        self.menu = Gtk.Popover.new(relative_to=menu_button)
        self.menu.add(menu_box)
        menu_button.set_popover(popover=self.menu)

        # Using `ModelButton ()`.
        button_about = Gtk.ModelButton.new()
        button_about.set_label(label='About')
        button_about.connect('clicked', self.about)
        menu_box.pack_start(child=button_about, expand=True, fill=True, padding=0)

        # Detecting the current operating system.
        system_name = ""
        logo = ""

        if sys.platform == "linux" or sys.platform == "linux2":

            system_name = distro.name()

            if system_name == "Ubuntu":
                logo = "logos/ubuntu.svg"
            elif system_name == "Debian":
                logo = "logos/debian.svg"
            elif system_name == "RedHat Enterprise Linux":
                logo = "logos/redhat.svg"
            elif system_name == "CentOS":
                logo = "logos/centos.svg"
            elif system_name == "Fedora":
                logo = "logos/fedora.svg"
            elif system_name == "openSUSE":
                logo = "logos/opensuse.svg"
            elif system_name == "Arch Linux":
                logo = "logos/arch.svg"
            elif system_name == "GenToo Linux":
                logo = "logos/gentoo.svg"
            elif system_name == "Manjaro Linux":
                logo = "logos/manjaro.svg"
            elif system_name == "Linux Mint":
                logo = "logos/mint.svg"
            elif system_name == "Mageia":
                logo = "logos/mageia.svg"
            elif system_name == "Raspbian":
                logo = "raspbian.svg"
            else:
                logo = "logos/linux.svg"

        elif sys.platform == "darwin":
            system_name = "MAC OS"
        elif sys.platform == "win32" or sys.platform == "win64":
            system_name = "Windows"
            logo = "logos/windows.svg"

        # Detecting the computer name.
        host = socket.gethostname()

        # Adding the main box
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        # Create an image
        image = Gtk.Image()
        # Set the content of the image as the file filename.png
        image.set_from_file(logo)
        # Add the image to the window
        vbox.pack_start(child=image, expand=True, fill=True, padding=0)

        # Create a label
        label = Gtk.Label()
        # Set the text of the label
        label.set_text("Im running {} on {} ".format(system_name, host))
        # Add the label to the window
        vbox.pack_start(child=label, expand=True, fill=True, padding=0)

        # Create a listbox
        listbox = Gtk.ListBox.new()
        listbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        vbox.pack_start(child=listbox, expand=True, fill=True, padding=0)

        # Creating a container with a switch and a label
        row1 = Gtk.ListBoxRow.new()
        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        hbox.set_border_width(border_width=6)
        row1.add(widget=hbox)

        # Switch
        label = Gtk.Label.new("Switch")
        label.set_xalign(xalign=0)
        hbox.pack_start(child=label, expand=True, fill=True, padding=0)

        # Switch
        switch = Gtk.Switch.new()
        switch.connect("notify::active", self.on_switch_activated)
        switch.set_active(True)
        hbox.pack_start(child=switch, expand=False, fill=True, padding=0)

        listbox.add(widget=row1)

        # Creating a container with a combobox and a label
        examples = ["Option 1", "Option 2", "Option 3"]

        row2 = Gtk.ListBoxRow.new()
        hbox2 = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        hbox2.set_border_width(border_width=6)

        row2.add(widget=hbox2)

        label2 = Gtk.Label.new("Combo box")
        label2.set_xalign(xalign=0)
        hbox2.pack_start(child=label2, expand=True, fill=True, padding=0)

        options_combo = Gtk.ComboBoxText()
        options_combo.connect("changed", self.on_currency_combo_changed)
        for example in examples:
            options_combo.append_text(example)

        options_combo.set_active(0)
        hbox2.pack_start(child=options_combo, expand=False, fill=True, padding=0)

        listbox.add(widget=row2)

        # Creating an entry
        entry = Gtk.Entry()
        entry.set_text("Type here!")

        listbox.add(widget=entry)

    def about(self, widget):
        self.menu.popdown()
        about = Gtk.AboutDialog.new()
        about.set_transient_for(parent=self)
        about.set_program_name("GTK Example")
        about.set_version("1.0")
        about.set_authors(authors=['Vitor Ferreira'])
        about.set_comments(
            comments='Example of a program created with GTK, a free and open-source cross-platform widget toolkit for creating graphical user interfaces.'
        )
        about.set_website(website='https://github.com/Vitor238/GTK-Example')
        about.run()
        about.destroy()

    def show_menu(self, widget):
        self.menu.show_all()

    def on_switch_activated(self, switch, gparam):
        if switch.get_active():
            state = "on"
        else:
            state = "off"
        print("Switch was turned", state)

    def on_currency_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            print("Selected: currency=%s" % text)


class MyApplication(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)