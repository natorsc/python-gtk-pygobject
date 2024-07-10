# -*- coding: utf-8 -*-
"""Python - GTK - PyGObject."""

import logging
import pathlib

from gi.repository import Adw, Gtk

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

BASE_DIR = pathlib.Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / 'log.log'


logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s.',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


adw_widgets = [
    Adw.AboutWindow(),
    Adw.ActionRow(),
    # Adw.Application(),
    Adw.Avatar(),
    Adw.Banner(),
    Adw.ButtonContent(),
    Adw.Carousel(),
    Adw.CarouselIndicatorDots(),
    Adw.CarouselIndicatorLines(),
    Adw.Clamp(),
    Adw.ComboRow(),
    Adw.EntryRow(),
    Adw.ExpanderRow(),
    Adw.MessageDialog(),
    Adw.NavigationSplitView(),
    Adw.PasswordEntryRow(),
    Adw.PreferencesPage(),
    Adw.PreferencesWindow(),
    Adw.SplitButton(),
    Adw.StatusPage(),
    # Adw.Toast(),
    Adw.ToolbarView(),
    Adw.ViewStack(),
]

gtk_widgets = [
    Gtk.ActionBar(),
    # Gtk.Application(),
    Gtk.ApplicationWindow(),
    Gtk.Box(),
    Gtk.Button(),
    Gtk.Calendar(),
    Gtk.CheckButton(),
    Gtk.CheckButton(),
    Gtk.ColorDialogButton(),
    Gtk.DropDown(),
    Gtk.Entry(),
    # Gtk.FileDialog(),
    Gtk.Fixed(),
    Gtk.FlowBox(),
    Gtk.Grid(),
    Gtk.HeaderBar(),
    Gtk.Image(),
    Gtk.ListBox(),
    Gtk.ListView(),
    Gtk.MenuButton(),
    Gtk.Overlay(),
    Gtk.Picture(),
    # Gtk.PrintOperation(),
    Gtk.SearchBar(),
    Gtk.ShortcutsWindow(),
    Gtk.StackSidebar(),
    Gtk.StackSwitcher(),
    Gtk.Switch(),
    Gtk.Video(),
    Gtk.Window(),
]

WIDGETS = adw_widgets + gtk_widgets

if __name__ == '__main__':
    print(WIDGETS)
