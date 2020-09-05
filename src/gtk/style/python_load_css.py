css_provider = Gtk.CssProvider.new()
css_provider.load_from_path(path='NomeDoArquivoCSS')

screen = Gdk.Screen()

style_context = Gtk.StyleContext.new()
style_context.add_provider_for_screen(
    screen=screen.get_default(),
    provider=css_provider,
    priority=Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
)
