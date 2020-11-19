 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Please do not theme this app](https://stopthemingmy.app/badge.svg)](https://stopthemingmy.app) 

# Criando interfaces gráficas com Python (PyGObject) e GTK

## GTK

O GTK é um **toolkit multiplataforma** para a criação de interfaces gráficas.

Este toolkit utiliza [licença GNU LGPL](https://pt.wikipedia.org/wiki/GNU_Lesser_General_Public_License), o que permite a sua utilização para construção de softwares que seja livres ou proprietários.

Foi desenvolvido inicialmente para o [GIMP](https://www.gimp.org/) (GNU Image Manipulation Program), por isso foi batizado de **GIMP Toolkit** ou simplesmente **GTK**.

Originalmente criado por, Peter Mattis, Spencer Kimball e Josh MacDonald.

O GTK+ é comumente utilizado na elaboração de aplicativos para o ambiente de desktop [GNOME](https://www.gnome.org/), contudo por ser multiplataforma pode ser executado sem problemas em diversos sistemas operacionais e ambientes gráficos.

O toolkit é escrito em `C` , seu design é orientado a objeto com base no sistema de objetos da biblioteca `GLib` .

Existe o suporte (bindings) a diversas linguagens de programação, contudo as linguagem que são suportadas **oficialmente** (até o momento que escrevo) são:

* C++.
* C\#.
* C.
* JavaScript.
* Python.
* Rust.
* Vala.

## O que estou publicando?

A ideia é apenas **estudar** e documentar a construção de interfaces gráficas com a linguagem de programação Python e o toolkit para construção de interfaces gráficas GTK.

!!! note "Nota"

    Em caso de problemas entre em contato para que o material possa ser melhorado.

## Tutoriais

- [Criando o ambiente de desenvolvimento]([https://www.codigoninja.dev/gtk/criando-ambiente-desenvolvimento-python-pygobject/).

### Windows

- [Criando um executável com o Cx_Freeze e listdlls](https://www.codigoninja.dev/gtk/criando-executavel-cx-freeze-windows-python-pygobject/).
- [Como instalar o PyGObject for Windows (não recomendado)](https://www.codigoninja.dev/gtk/instalar-pygobject-for-windows/).

### Linux

- [Criando um executável com o Cx_Freeze](https://www.codigoninja.dev/gtk/criando-executavel-cx-freeze-linux-python-pygobject/).

### Style

- [Exemplo de alguns seletores css no Gtk](https://www.codigoninja.dev/gtk/principais-seletores-css-python-pygobject/).
- [Alterando o estilo de um componete com a propriedade name](https://www.codigoninja.dev/gtk/adicionar-propriedade-name-widget-python-pygobject/).
- [Alterando o estilo de um componete com a tag class](https://www.codigoninja.dev/gtk/cadicionar-tag-class-widget-python-pygobject/).
- [Ativar e desativar o modo escuro (dark mode)](https://www.codigoninja.dev/gtk/utilizar-modo-escuro-dark-mode-python-pygobject/).

### Ferramentas

- [Ativando o Gkt Inspector](https://www.codigoninja.dev/gtk/ativar-gtk-inspector/).
- [Como instalar o Gnome Builder](https://www.codigoninja.dev/gtk/instalar-gnome-builder/).
- [Como instalar o Gnome Gnome Glade](https://www.codigoninja.dev/gtk/instalar-gnome-glade/).
- [Como instalar o Gtk icon browser](https://www.codigoninja.dev/gtk/instalar-gtk-icon-browser/).

### Libhandy

- [Como instalar a biblioteca libhandy no Linux e Windows](https://www.codigoninja.dev/gtk/instalar-biblioteca-libhandy-python-pygobject/).

## Código GTK

### Janela principal

* [Lendo arquivos de interface do Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/application-window/builder).
* [Lendo arquivos interface do Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/application-window/glade).
* [Criando a janela com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/application-window).

![Python e GTK Janela principal](https://codigoninja.dev/images/gtk/pygobject/widgets/python-gtk-mainwindow.webp)

### Layouts

* [Actionbar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/actionbar/builder).
* [Actionbar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/actionbar/glade).
* [Actionbar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/actionbar).

![Gtk layout do tipo actionbar](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-action-bar.webp)

* [Box horizontal com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box-horizontal/builder).
* [Box horizontal com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box-horizontal/glade).
* [Box horizontal com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box-horizontal).

![Gtk layout do tipo box horizontal](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-box-horizontal.webp)

* [Box vertical com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box-vertical).
* [Box vertical com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box-vertical).
* [Box vertical com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box-vertical).

![Gtk layout do tipo box vertical](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-box-vertical.webp)

* [Button box com Gnome Bulder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/buttonbox/builder).
* [Button box com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/buttonbox/glade).
* [Button box com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/buttonbox).

![Gtk layout do tipo button box](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-button-box.webp)

* [Fixed com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/fixed/builder).
* [Fixed com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/fixed/Glade).
* [Fixed com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/fixed).

![Gtk layout do tipo fixed](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-fixed.webp)

* [Flowbox com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/flowbox/builder).
* [Flowbox com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/flowbox/glade).
* [Flowbox com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/flowbox).

![Gtk layout do tipo flow box](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-flow-box.webp)

* [Grid com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/grid/builder).
* [Grid com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/grid/glade).
* [Grid com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/grid).

![Gtk layout do tipo grid](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-grid.webp)

* [Layout com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/gtk-layout/builder).
* [Layout com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/gtk-layout/glade).
* [Layout com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/gtk_layout).

![Gtk layout do tipo layout](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-gtk.webp)

* [Headerbar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/headerbar/builder).
* [Headerbar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/headerbar/glade).
* [Headerbar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/headerbar).

![Gtk layout do tipo header bar](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-header-bar.webp)

* [Listbox com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/listbox/builder).
* [Listbox com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/listbox/glade).
* [Listbox com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/listbox).

![Gtk layout do tipo list box](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-list-box.webp)

* [Notebook com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/notebook/builder).
* [Notebook com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/notebook/builder).
* [Notebook com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/notebook).

![Gtk layout do tipo notebook](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-notebook.webp)

* [Overlay com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/overlay/builder).
* [Overlay com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/overlay/glade).
* [Overlay com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/overlay).

![Gtk layout do tipo overlay](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-overlay.webp)

* [Paned horizontal com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned-horizontal/builder).
* [Paned horizontal com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned-horizontal/glade).
* [Paned horizontal com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned-horizontal).

![Gtk layout do tipo paned horizontal](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-paned-horizontal.webp)

* [Paned vertical com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned-vertical/builder).
* [Paned vertical com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned-vertical/glade).
* [Paned vertical com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned-vertical).

![Gtk layout do tipo paned vertical](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-paned-vertical.webp)

* [Revealer com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/revealer/builder).
* [Revealer com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/revealer/glade).
* [Revealer com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/revealer).

![Gtk layout do tipo revealer](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-revealer.webp)

* [Stack e stacksidebar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack-stacksidebar/builder).
* [Stack e stacksidebar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack-stacksidebar/glade).
* [Stack e stacksidebar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack-stacksidebar).

![Gtk layout do tipo stack com stacksidebar](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-stack-stacksidebar.webp)

* [Stack e stackswitcher com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack-switcher/builder).
* [Stack e stackswitcher com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack-switcher/glade).
* [Stack e stackswitcher com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack-switcher).

![Gtk layout do tipo stack com stackswitcher](https://codigoninja.dev/images/gtk/pygobject/widgets/layout-stack-stackswitcher.webp)

### Diálogos

* [Personalizado com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/custom/builder).
* [Personalizado com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/custom/glade).
* [Personalizado com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/custom).

![GTK diálogo personalizado](https://codigoninja.dev/images/gtk/pygobject/widgets/dialog-custom.webp)

* [Mensagem com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/message/builder).
* [Mensagem com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/message/glade).
* [Mensagem com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/message).

![GTK diálogo de mensagem](https://codigoninja.dev/images/gtk/pygobject/widgets/dialog-message.webp)

* [Salvar arquivo com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/save_file/builder).
* [Salvar arquivo com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/save_file/glade).
* [Salvar arquivo com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/save_file).

![GTK diálogo para salvar arquivo](https://codigoninja.dev/images/gtk/pygobject/widgets/dialog-save-file.webp)

* [Selecionar arquivo Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_file/builder).
* [Selecionar arquivo Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_file/glade).
* [Selecionar arquivo Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_file).

![GTK diálogo para selecionar arquivo](https://codigoninja.dev/images/gtk/pygobject/widgets/dialog-select-file.webp)

* [Selecionar pasta com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_folder/builder).
* [Selecionar pasta com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_folder/glade).
* [Selecionar pasta com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_folder).

![GTK diálogo para selecionar pasta](https://codigoninja.dev/images/gtk/pygobject/widgets/dialog-select-folder.webp)

### Dialogo de impressão, configuração de página e exportar para PDF

* [Imprimindo e exportando para pdf com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/printer/builder)
* [Imprimindo e exportando para pdf com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/printer/glade)
* [Imprimindo e exportando para pdf com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/printer)

![GTK imprindo e exportand para pdf](https://codigoninja.dev/images/gtk/pygobject/widgets/dialog-printer.webp)

### Drag and drop (Arrastar e soltar)

* [Com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/drag-and-drop/builder).
* [Com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/ddrag-and-drop/glade).
* [Com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/drag-and-drop).

![GTK drag and drop (arrastar e soltar)](https://codigoninja.dev/images/gtk/pygobject/widgets/drag-and-drop.webp)

### Signals e slots

* [Com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/signals-and-slots/builder).
* [Com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/signals-and-slots/glade).
* [Com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/signals-and-slots).

![GTK signals e slots](https://codigoninja.dev/images/gtk/pygobject/widgets/signal-and-slots.webp)

### Menus

* [GTK Menu com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menu/builder).
* [GTK Menu com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menu/glade).
* [GTK Menu com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menu).

![GTK menu](https://codigoninja.dev/images/gtk/pygobject/widgets/menu.webp)

* [GTK menu Popover com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/popover/builder).
* [GTK menu Popover com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/popover/glade).
* [GTK menu Popover com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/menus/gtk/popover). 

![GTK menu popover](https://codigoninja.dev/images/gtk/pygobject/widgets/menu-popover.webp)   

* [GTK MenuBar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menubar/builder).
* [GTK MenuBar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menubar/glade).
* [GTK MenuBar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/menus/gtk/menubar).

![GTK menubar](https://codigoninja.dev/images/gtk/pygobject/widgets/menubar.webp)

* [GTK menu ToolBar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/toolbar/builder).
* [GTK menu ToolBar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/toolbar/glade).
* [GTK menu ToolBar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/toolbar/builder).

![GTK menu toolbar](https://codigoninja.dev/images/gtk/pygobject/widgets/menu-toolbar.webp)

### Style

> **OBS**: Ao utilizar `background-color` deve-se utilizar `background-image: none;` .

> **OBS**: Ao utilizar somente `background` não é necessário utilizar `background-image: none;` .

> **OBS**: Alguns widgets utilizam uma imagem de fundo em alguns casos pode ser interessante remover essa imagem com `background-image: none;` .

* [Adicionar classe a um widget com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/class/builder)
* [Adicionar classe a um widget com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/class/glade)
* [Adicionar classe a um widget com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/class)

![GTK Adicionar classe a um widget](https://codigoninja.dev/images/gtk/pygobject/widgets/style-class.webp)

* [Adicionar um nome a um widget com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/name/builder)
* [Adicionar um nome a um widget com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/name/glade)
* [Adicionar um nome a um widget com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/name)

![GTK Adicionar nome a um widget](https://codigoninja.dev/images/gtk/pygobject/widgets/style-name.webp)

* [CSS selectors com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/selectors/builder)
* [CSS selectors com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/selectors/glade)
* [CSS selectors com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/selectors/name)

![GTK CSS selectors](https://codigoninja.dev/images/gtk/pygobject/widgets/style-selectors.webp)

* [Dark Mode (modo escuro) com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/darkmode/builder)
* [Dark Mode (modo escuro) com  com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/darkmode/glade)
* [Dark Mode (modo escuro) com  com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/darkmode)

![GTK Dark Mode (modo escuro)](https://codigoninja.dev/images/gtk/pygobject/widgets/style-dark-mode.webp)

### Ícones standard e symbolic

* [Utilizando ícones standard e symbolic com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/gnome-icons/builder).
* [Utilizando ícones standard e symbolic com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/gnome-icons/glade).
* [Utilizando ícones standard e symbolic com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/gnome-icons).

![GTK utilizando ícones standard e symbolic](https://codigoninja.dev/images/gtk/pygobject/widgets/icons-standard-symbolic.webp)

### Window

* [GTK Window Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/window/builder).
* [GTK Window com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/window/glade).
* [GTK Window com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/window).

![GTK utilizando ícones standard e symbolic](https://codigoninja.dev/images/gtk/pygobject/widgets/icons-standard-symbolic.webp)

### Widgets

#### Calendar

* [GTK Calendar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/calendar/builder).
* [GTK Calendar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/calendar/glade).
* [GTK Calendar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/calendar).

![GTK Calendar](https://codigoninja.dev/images/gtk/pygobject/widgets/calendar.webp)

#### Entry

* [GTK Entry com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/entry/builder).
* [GTK Entry com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/entry/glade).
* [GTK Entry com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/entry).

![GTK Entry](https://codigoninja.dev/images/gtk/pygobject/widgets/entry.webp)

#### EntryCompletion

* [GTK EntryCompletion com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/entry-completion/builder).
* [GTK EntryCompletion com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/entry-completion/glade).
* [GTK EntryCompletion com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/entry-completion).

![GTK EntryCompletion](https://codigoninja.dev/images/gtk/pygobject/widgets/entry-completion.webp)

#### RadioButton

* [GTK RadioButton com  Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/radio-button/builder).
* [GTK RadioButton com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/radio-button/glade).
* [GTK RadioButton com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/radio-button).

![GTK RadioButton](https://codigoninja.dev/images/gtk/pygobject/widgets/radio-button.webp)

#### SearchBar

* [GTK SearchBar com  Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/search-bar/builder).
* [GTK SearchBar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/search-bar/glade).
* [GTK SearchBar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/search-bar).

![GTK SearchBar](https://codigoninja.dev/images/gtk/pygobject/widgets/search-bar.webp)

#### SearchEntry

* [GTK SearchEntry com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/search-entry/builder).
* [GTK SearchEntry com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/search-entry/glade).
* [GTK SearchEntry com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/search-entry).

![GTK SearchEntry](https://codigoninja.dev/images/gtk/pygobject/widgets/search-entry.webp)

#### Treeview

* [GTK TreeView editar célula Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/editable/builder).
* [GTK TreeView editar célula Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/editable/glade).
* [GTK TreeView editar célula Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/editable).

![GTK TreeView editar célula](https://codigoninja.dev/images/gtk/pygobject/widgets/treeview-editable.webp)

* [GTK TreeView filtro com botões no Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/filter/builder).
* [GTK TreeView filtro com botões no Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/filter/glade).
* [GTK TreeView filtro com botões no Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/filter).

![GTK TreeView ordenando pelo cabeçalho](https://codigoninja.dev/images/gtk/pygobject/widgets/treeview-filter.webp)

* [GTK TreeView ordenando pelo cabeçalho com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/sort/builder).
* [GTK TreeView ordenando pelo cabeçalho com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/sort/glade).
* [GTK TreeView ordenando pelo cabeçalho com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/treeview/sort).

![GTK TreeView ordenando pelo cabeçalho](https://codigoninja.dev/images/gtk/pygobject/widgets/treeview-sort.webp)

* [GTK EventBox com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/event-box/builder).
* [GTK EventBox com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/event-box/glade).
* [GTK EventBox com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/widgets/event-box).

---

## Código Libhandy

### ActionRow

* [Libhandy ActionRow com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/action-row/builder).
* [Libhandy ActionRow com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/action-row/glade).
* [Libhandy ActionRow com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/action-row).

![Libhandy ActionRow](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-action-row.webp)

### ApplicationWindow

* Libhandy ApplicationWindow. Disponível a partir da versão 1.0?

### Arrows

* Libhandy Arrows. Deprecated since version 0.0.12: Use e.g. Gtk.Image and CSS animation instead.

### Avatar

* [Libhandy Avatar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/avatar).

![Libhandy Avatar](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-avatar.webp)

### Carousel

* [Libhandy Carousel com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/carousel).

![Libhandy Carousel](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-carousel.webp)

### CarouselIndicatorDots

* [Libhandy CarouselIndicatorLines com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/carousel-indicator-dots).

![Libhandy CarouselIndicatorLines](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-carousel-indicator-dots.webp)

### CarouselIndicatorLines

* [Libhandy CarouselIndicatorLines com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/carousel-indicator-lines).

![Libhandy CarouselIndicatorLines](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-carousel-indicator-lines.webp)

### Column

HdyColumn foi trocado pelo HdyClamp a partir da versão 1.0.

* [Libhandy Column](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/column).

![Libhandy Column](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-column.webp)

### ComboRow

* [Libhandy ComboRow](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/combo-row).

![Libhandy ComboRow](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-combo-row.webp)

### Deck

* [Libhandy Deck](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/deck) (não sei implementar).

### Dialer
* Libhandy Dialer. Deprecated since version 0.0.12: use Handy.Keypad instead.

### DialerButton

* Libhandy DialerButton. Deprecated since version 0.0.12: This widget is considered a Handy.Dialer internal api.

### DialerCycleButton

* Libhandy DialerCycleButton. Deprecated since version 0.0.12: This widget is considered a Handy.Dialer internal api.

### Dialog

* [Libhandy Dialog](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/dialog).

![Libhandy Dialog](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-dialog.webp)

### ExpanderRow

* [Libhandy ExpanderRow](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/expander-row).

![Libhandy ExpanderRow](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-expander-row.webp)

### HeaderBar

* [Libhandy HeaderBar](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/headerbar).

![Libhandy HeaderBar](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-headerbar.webp)

### HeaderGroup

* [Libhandy HeaderGroup (Não sei implementar ainda)](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/headergroup).

### Keypad

* [Libhandy Keypad](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/keypad).

![Libhandy Keypad](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-keypad.webp)

### Leaflet

* [Libhandy Leaflet com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/leaflet).

![Libhandy Leaflet](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-leaflet.webp)

* [Libhandy Leaflet com Python sincronizando dois Leaflets](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/leaflet).

![Libhandy Leaflet](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-sync-leaflet.webp)

### SearchBar

* [Libhandy SearchBar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/search-bar).

![Libhandy SearchBar](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-search-bar.webp)

### Squeezer

* Libhandy squeezer. Não sei implementar.

### TitleBar

* [Libhandy TitleBar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/title-bar).

![Libhandy TitleBar](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-title-bar.webp)

### ViewSwitcher

* [Libhandy ViewSwitcher com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/view-switcher).

![Libhandy ViewSwitcher](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-view-switcher.webp)

### ViewSwitcherBar

* [Libhandy ViewSwitcherBar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/view-switcher-bar).

![Libhandy ViewSwitcherBar](https://codigoninja.dev/images/gtk/pygobject/widgets/libhandy-view-switcher-bar.webp)

### Window

* [Libhandy Window com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/window).

### WindowHandle

* [Libhandy WindowHandle com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/libhandy/window-handle).


