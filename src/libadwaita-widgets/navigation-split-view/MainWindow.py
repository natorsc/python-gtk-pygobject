# -*- coding: utf-8 -*-
"""Python e GTK: PyGObject libadwaita Adw.NavigationSplitView."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Adw.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(
            title='Python e GTK: PyGObject libadwaita Adw.NavigationSplitView',
        )
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))
        # Como definir? (How to define?).
        self.set_property('width-request', 280)
        self.set_property('height-request', 200)

        adw_breakpoint_condition = Adw.BreakpointCondition.new_length(
            type=Adw.BreakpointConditionLengthType.MAX_WIDTH,
            value=400,
            unit=Adw.LengthUnit.SP,
        )

        adw_breakpoint = Adw.Breakpoint.new(condition=adw_breakpoint_condition)
        self.add_breakpoint(breakpoint=adw_breakpoint)

        adw_toolbar_view = Adw.ToolbarView.new()

        adw_navigation_page = Adw.NavigationPage.new(
            child=adw_toolbar_view,
            title='Python e GTK: PyGObject libadwaita Adw.NavigationSplitView',
        )

        adw_navigation_split_view = Adw.NavigationSplitView.new()
        adw_navigation_split_view.set_sidebar(sidebar=adw_navigation_page)
        self.set_content(content=adw_navigation_split_view)

        adw_header_bar = Adw.HeaderBar.new()
        adw_toolbar_view.add_top_bar(widget=adw_header_bar)

        menu_button_model = Gio.Menu()
        menu_button_model.append(
            label='Preferences',
            detailed_action='app.preferences',
        )

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        adw_header_bar.pack_end(child=menu_button)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        adw_toolbar_view.set_content(content=vbox)

        button = Gtk.Button.new_with_label(label='Content')
        button.set_action_name(action_name='navigation.push')
        # Como definir? (How to define?).
        # button.set_action_target('\'content\'')
        vbox.append(child=button)

        toolbar_view_content = Adw.ToolbarView.new()

        navegation_page_content = Adw.NavigationPage.new(
            child=toolbar_view_content,
            title='Content',
        )
        adw_navigation_split_view.set_content(content=navegation_page_content)

        header_bar_content = Adw.HeaderBar.new()
        toolbar_view_content.add_top_bar(widget=header_bar_content)

        content_page = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content_page.set_margin_top(margin=12)
        content_page.set_margin_end(margin=12)
        content_page.set_margin_bottom(margin=12)
        content_page.set_margin_start(margin=12)
        toolbar_view_content.set_content(content=content_page)

        label = Gtk.Label.new(str='Content')
        content_page.append(child=label)

    def on_button_clicked(self, button):
        if 'background' in self.button.get_css_classes():
            self.button.remove_css_class(css_class='background')
        else:
            self.button.add_css_class(css_class='background')


class ExampleApplication(Adw.Application):

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

    def create_action(self, name, callback, shortcuts=None):
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
