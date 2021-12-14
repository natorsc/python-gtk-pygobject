# GTK 3

## Arquitetura

### bibliotecas:

- **GLib**: Biblioteca com utilitários de uso geral, não é específica para interfaces gráficas. GLib fornece muitos
  tipos de dados úteis, macros, conversões de tipo, utilitários de string, utilitários de arquivo, uma abstração de loop
  principal e assim por diante.
- **GObject**: Biblioteca que fornece um sistema de tipos.
- **GIO**: Uma API VFS (Virtual file system) moderna e fácil de usar, incluindo abstrações para arquivos, drives,
  volumes, fluxo de IO, bem como programação de rede e comunicação DBus.
- **cairo**: Cairo é uma biblioteca de gráficos 2D com suporte para vários dispositivos de saída.
- **Pango**: Pango é uma biblioteca para manipulação de texto internacionalizada. Ele gira em torno do objeto
  PangoLayout, representando um parágrafo de texto. Pango fornece o motor para GtkTextView, GtkLabel, GtkEntry e outros
  widgets que exibem texto.
- **ATK**: ATK é o Kit de ferramentas de acessibilidade. Ele fornece um conjunto de interfaces genéricas que permitem
  que tecnologias de acessibilidade interajam com uma interface gráfica de usuário. Por exemplo, um leitor de tela usa
  ATK para descobrir o texto em uma interface e lê-lo para usuários cegos. Os widgets GTK possuem suporte integrado para
  acessibilidade usando a estrutura ATK.
- **GdkPixbuf**: Esta é uma pequena biblioteca que permite criar objetos GdkPixbuf (“buffer de pixel”) a partir de dados
  de imagem ou arquivos de imagem. Use um GdkPixbuf em combinação com GtkImage para exibir imagens.
- **graphene**: Esta é uma pequena biblioteca que fornece operações e tipos de dados vetoriais e matriciais. O graphene
  fornece implementações otimizadas usando vários conjuntos de instruções SIMD, como SSE.
- **GDK**: GDK é a camada de abstração que permite ao GTK oferecer suporte a vários sistemas de janelas. O GDK fornece
  recursos de sistema de janelas no Wayland, X11, Windows e OSX.
- **GSK**: GSK é uma biblioteca para criar um gráfico de cena a partir de nós de renderização e renderizá-lo usando
  diferentes APIs de renderização. GSK fornece renderizadores para OpenGL, Vulkan e Cairo.

## Gio

- [Gio.Menu](./gtk3-widgets.md#gio-menu).
- [Gio.SimpleAction](./gtk3-widgets.md#gio-simple-action).

## Widgets

- [Gtk.ActionBar](./gtk3-widgets.md#gtk-actionbar).
- [Gtk.ApplicationWindow](./gtk3-widgets.md#gtk-applicationwindow).
- [Gtk.Box horizontal](./gtk3-widgets.md#gtk-box-horizontal).
- [Gtk.Box vertical](./gtk3-widgets.md#gtk-box-vertical).
- [Gtk.Button](./gtk3-widgets.md#gtk-button).
- [Gtk.ButtonBox](./gtk3-widgets.md#gtk-buttonbox).
- [Gtk.Calendar](./gtk3-widgets.md#gtk-calendar).
- [Gtk.CheckButton](./gtk3-widgets.md#gtk-checkbutton).
- [Gtk.Dialog](./gtk3-widgets.md#gtk-dialog).
- [Gtk.DragAndDrop](./gtk3-widgets.md#gtk-drag-and-drop).
- [Gtk.Entry](./gtk3-widgets.md#gtk-entry).
- [Gtk.EntryCompletion](./gtk3-widgets.md#gtk-entrycompletion).
- [Gtk.EventBox](./gtk3-widgets.md#gtk-eventbox).
- [Gtk.FileChooserDialog folder](./gtk3-widgets.md#gtk-filechooserdialog-folder).
- [Gtk.FileChooserDialog open](./gtk3-widgets.md#gtk-filechooserdialog-open).
- [Gtk.FileChooserDialog save](./gtk3-widgets.md#gtk-filechooserdialog-save).
- [Gtk.Fixed](./gtk3-widgets.md#gtk-filechooserdialog-save).
- [Gtk.FlowBox](./gtk3-widgets.md#gtk-flowbox).
- [Gtk.Grid](./gtk3-widgets.md#gtk-grid).
- [Gtk.HeaderBar](./gtk3-widgets.md#gtk-headerbar).
- [Gtk.Image](./gtk3-widgets.md#gtk-image).
- [Gtk.InfoBar](./gtk3-widgets.md#gtk-infobar).
- [Gtk.Layout](./gtk3-widgets.md#gtk-layout).
- [Gtk.LinkButton](./gtk3-widgets.md#gtk-linkbutton).
- [Gtk.ListBox](./gtk3-widgets.md#gtk-listbox).
- [Gtk.Menu](./gtk3-widgets.md#gtk-menu).
- [Gtk.MenuBar](./gtk3-widgets.md#gtk-menubar).
- [Gtk.MenuButton](./gtk3-widgets.md#gtk-menubutton).
- [Gtk.MessageDialog](./gtk3-widgets.md#gtk-messagedialog).
- [Gtk.Notebook](./gtk3-widgets.md#gtk-notebook).
- [Gtk.Notify](./gtk3-widgets.md#gtk-notify).
- [Gtk.Overlay](./gtk3-widgets.md#gtk-overlay).
- [Gtk.Paned horizontal](./gtk3-widgets.md#gtk-paned-horizontal).
- [Gtk.Paned vertical](./gtk3-widgets.md#gtk-paned-vertical).
- [Gtk.Popover](./gtk3-widgets.md#gtk-popover).
- [Gtk.PrintOperation](./gtk3-widgets.md#gtk-printoperation).
- [Gtk.RadioButton](./gtk3-widgets.md#gtk-radiobutton).
- [Gtk.Revealer](./gtk3-widgets.md#gtk-revealer).
- [Gtk.SearchBar](./gtk3-widgets.md#gtk-searchbar).
- [Gtk.SearchEntry](./gtk3-widgets.md#gtk-searchentry).
- [Gtk.Separator](./gtk3-widgets.md#gtk-separator).
- [Gtk.Spinner](./gtk3-widgets.md#gtk-spinner).
- [Gtk.StackSidebar](./gtk3-widgets.md#gtk-stacksidebar).
- [Gtk.StackSwitcher](./gtk3-widgets.md#gtk-stackswitcher).
- [Gtk.Statusbar](./gtk3-widgets.md#gtk-statusbar).
- [Gtk Style add class](./gtk3-widgets.md#gtk-style-add-class).
- [Gtk Style css provider](./gtk3-widgets.md#gtk-style-css-provider).
- [Gtk Style dark mode](./gtk3-widgets.md#gtk-style-dark-mode).
- [Gtk Style set name](./gtk3-widgets.md#gtk-style-set-name).
- [Gtk.Switch](./gtk3-widgets.md#gtk-switch).
- [Gtk.ToggleButton](./gtk3-widgets.md#gtk-togglebutton).
- [Gtk.Toolbar](./gtk3-widgets.md#gtk-toolbar).
- [Gtk.TreeView editable](./gtk3-widgets.md#gtk-treeview-editable).
- [Gtk.TreeView filter](./gtk3-widgets.md#gtk-treeview-filter).
- [Gtk.TreeView sort](./gtk3-widgets.md#gtk-treeview-sort).
- [Gtk.TreeView TreeStore](./gtk3-widgets.md#gtk-treeview-treestore).
- [Gtk.Window](./gtk3-widgets.md#gtk-window).