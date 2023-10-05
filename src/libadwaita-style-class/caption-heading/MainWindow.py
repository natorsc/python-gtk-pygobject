# -*- coding: utf-8 -*-
"""Python e GTK: PyGObject libadwaita style class caption-heading."""

from collections.abc import Callable

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()

LOREM = 'Lorem Ipsum is simply dummy...\n{}.'


class ExampleWindow(Adw.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(
            title='Python and GTK: PyGObject style class caption-heading')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        mbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_content(content=mbox)

        header_bar = Gtk.HeaderBar.new()
        mbox.append(child=header_bar)

        menu_button_model = Gio.Menu()
        menu_button_model.append(
            label='Preferences',
            detailed_action='app.preferences',
        )

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        header_bar.pack_end(child=menu_button)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        mbox.append(child=vbox)

        label = Gtk.Label.new(
            str='The caption-heading style class makes the text smaller. It should '
                'be used to differentiate the subtext that accompanies the text in the '
                'regular body style.',
        )
        label.set_vexpand(expand=True)
        label.set_wrap(wrap=True)
        vbox.append(child=label)

        self.label_caption_heading = Gtk.Label.new(
            str=LOREM.format("Classes: ['caption-heading']"))
        self.label_caption_heading.set_vexpand(expand=True)
        self.label_caption_heading.set_wrap(wrap=True)
        self.label_caption_heading.add_css_class(css_class='caption-heading')
        vbox.append(child=self.label_caption_heading)

        button = Gtk.Button.new_with_label(label='Add/remove class')
        button.connect('clicked', self.on_button_clicked)
        vbox.append(child=button)

    def on_button_clicked(self, button):
        if 'caption-heading' in self.label_caption_heading.get_css_classes():
            self.label_caption_heading.remove_css_class(
                css_class='caption-heading')
        else:
            self.label_caption_heading.add_css_class(
                css_class='caption-heading')
        self.label_caption_heading.set_text(
            str=LOREM.format(
                f'Classes: {self.label_caption_heading.get_css_classes()}'),
        )


class ExampleApplication(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.com.justcode.PyGObject',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.exit_app, ['<primary>q'])
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ExampleWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def on_preferences_action(self, action, param):
        print('Action `app.preferences` was active.')

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name: str, callback: Callable[[str, str], None],
                      shortcuts: str | None = None):
        action = Gio.SimpleAction.new(name=name, parameter_type=None)
        action.connect('activate', callback)
        self.add_action(action=action)
        if shortcuts:
            self.set_accels_for_action(
                detailed_action_name=f'app.{name}',
                accels=shortcuts,
            )


if __name__ == '__main__':
    import sys

    app = ExampleApplication()
    app.run(sys.argv)
