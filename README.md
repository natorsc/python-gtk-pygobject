> Em desenvolvimento e revisão

> **OBS**: Este repositório tem um arquivo `Pipfile` , o mesmo **não** funciona no Windows, isso porque a instalação do GTK e Python **DEVEM** ser feitas pelo **msys2**.

---

# GUI (graphical user interface) com Python e GTK

Tutoriais e pequenos exemplos de código.

## GTK

O GTK é um **toolkit multiplataforma** para a criação de interfaces gráficas.

Este toolkit utiliza [licença GNU LGPL](https://pt.wikipedia.org/wiki/GNU_Lesser_General_Public_License), o que permite a sua utilização para construção de softwares que seja livres ou proprietários.

Foi desenvolvido inicialmente para o [GIMP](https://www.gimp.org/) (GNU Image Manipulation Program), por isso foi batizado de **GIMP Toolkit** ou simplesmente **GTK**.

Originalmente criado por, Peter Mattis, Spencer Kimball e Josh MacDonald.

O GTK+ é comumente utilizado na elaboração de aplicativos para o ambiente de desktop [GNOME](https://www.gnome.org/), contudo por ser multiplataforma pode ser executado sem problemas em diversos sistemas operacionais e ambientes gráficos.

O toolkit é escrito em `C` , seu design é orientado a objeto com base no sistema de objetos da biblioteca `GLib` .

Existe o suporte (bindings) a diversas linguagens de programação, contudo as linguagem que são suportadas **oficialmente** (até o momento que escrevo) são:

* C++.
* JavaScript.
* Python.
* Vala.

## O que estou publicando?

A ideia é apenas **estudar** e documentar a construção de interfaces gráficas com GTK e Python.

Exemplos de código podem ser vistos na pasta `src` deste repositório.

> Em caso de problemas entre em contato para que o material possa ser melhorado.

---

# Tutoriais

* [Como instalar o msys2 no Windows (Obrigatório)](https://codigoninja.dev/2020/09/08/python-gtk-instalar-msys2-windows/).
* [Como instalar o PyGObject for Windows (não recomendado)](https://codigoninja.dev/2020/09/08/python-gtk-instalar-pygobject-windows/).
* [Configurando o ambiente de desenvolvimento](https://codigoninja.dev/2020/09/08/python-gtk-configurando-ambiente-desenvolvimento/).

## IDEs e RADs

* [Como Instalar o Gnome Builder](https://codigoninja.dev/2020/09/08/python-gtk-instalar-gnome-builder/).
* [Como Instalar o Gnome Glade](https://codigoninja.dev/2020/09/08/python-gtk-instalar-gnome-glade/).

## Purism Librem 5

* [Como Instalar a biblioteca libhandy](https://codigoninja.dev/2020/09/08/python-gtk-instalar-biblioteca-libhandy/).
* [Executando o PureOS (Phosh) via VM](https://codigoninja.dev/2020/09/08/python-gtk-pureos-phosh/).

## GTK

* [GTK icon browser](https://codigoninja.dev/2020/09/08/python-gtk-instalar-icon-browser/).
* [Como ativar o GtkInspector](https://codigoninja.dev/2020/09/08/python-gtk-ativar-gtkinspector/).
* [Criando uma janela com Python e GTK](https://codigoninja.dev/2020/09/08/python-gtk-criando-janela/).

## Criar executáveis

* [Criando executáveis com Cx_Freeze no Windows](https://codigoninja.dev/2020/09/08/python-gtk-criando-executavel-cxfreeze-windows/).
* [Criando executáveis com Cx_Freeze no Linux](https://codigoninja.dev/2020/09/08/python-gtk-criando-executavel-cxfreeze-linux/).

## Extra

* [Como instalar Python no Linux e Windows](https://codigoninja.dev/2020/09/07/instalar-linguagem-python-linux-windows/).

---

# Código

## GTK

### Janela principal

* [Lendo arquivos de interface do Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/main-window/builder).
* [Lendo arquivos interface do Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/main-window/glade).
* [Criando a janela com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/main-window).

![Python e GTK Janela principal](https://codigoninja.dev/media/git/pygobject/python-gtk-mainwindow.png)

### Layouts

* [Actionbar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/actionbar/builder).
* [Actionbar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/actionbar/glade).
* [Actionbar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/actionbar).

![Gtk layout do tipo actionbar](https://codigoninja.dev/media/git/pygobject/layout-action-bar.png)

* [Box horizontal com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box_horizontal/builder).
* [Box horizontal com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box_horizontal/glade).
* [Box horizontal com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box_horizontal).

![Gtk layout do tipo box horizontal](https://codigoninja.dev/media/git/pygobject/layout-box-horizontal.png)

* [Box vertical com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box_vertical).
* [Box vertical com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box_vertical).
* [Box vertical com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/box_vertical).

![Gtk layout do tipo box vertical](https://codigoninja.dev/media/git/pygobject/layout-box-vertical.png)

* [Button box com Gnome Bulder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/buttonbox/builder).
* [Button box com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/buttonbox/glade).
* [Button box com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/buttonbox).

![Gtk layout do tipo button box](https://codigoninja.dev/media/git/pygobject/layout-button-box.png)

* [Fixed com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/fixed/builder).
* [Fixed com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/fixed/Glade).
* [Fixed com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/fixed).

![Gtk layout do tipo fixed](https://codigoninja.dev/media/git/pygobject/layout-fixed.png)

* [Flowbox com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/flowbox/builder).
* [Flowbox com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/flowbox/glade).
* [Flowbox com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/flowbox).

![Gtk layout do tipo flow box](https://codigoninja.dev/media/git/pygobject/layout-flow-box.png)

* [Grid com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/grid/builder).
* [Grid com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/grid/glade).
* [Grid com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/grid).

![Gtk layout do tipo grid](https://codigoninja.dev/media/git/pygobject/layout-grid.png)

* [Layout com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/gtk_layout/builder).
* [Layout com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/gtk_layout/glade).
* [Layout com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/gtk_layout).

![Gtk layout do tipo layout](https://codigoninja.dev/media/git/pygobject/layout-gtk.png)

* [Headerbar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/headerbar/builder).
* [Headerbar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/headerbar/glade).
* [Headerbar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/headerbar).

![Gtk layout do tipo header bar](https://codigoninja.dev/media/git/pygobject/layout-header-bar.png)

* [Listbox com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/listbox/builder).
* [Listbox com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/listbox/glade).
* [Listbox com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/listbox).

![Gtk layout do tipo list box](https://codigoninja.dev/media/git/pygobject/layout-list-box.png)

* [Notebook com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/notebook/builder).
* [Notebook com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/notebook/builder).
* [Notebook com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/notebook).

![Gtk layout do tipo notebook](https://codigoninja.dev/media/git/pygobject/layout-notebook.png)

* [Overlay com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/overlay/builder).
* [Overlay com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/overlay/glade).
* [Overlay com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/overlay).

![Gtk layout do tipo overlay](https://codigoninja.dev/media/git/pygobject/layout-overlay.png)

* [Paned horizontal com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned_horizontal/builder).
* [Paned horizontal com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned_horizontal/glade).
* [Paned horizontal com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned_horizontal).

![Gtk layout do tipo paned horizontal](https://codigoninja.dev/media/git/pygobject/layout-paned-horizontal.png)

* [Paned vertical com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned_vertical/builder).
* [Paned vertical com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned_vertical/glade).
* [Paned vertical com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/paned_vertical).

![Gtk layout do tipo paned vertical](https://codigoninja.dev/media/git/pygobject/layout-paned-vertical.png)

* [Revealer com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/revealer/builder).
* [Revealer com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/revealer/glade).
* [Revealer com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/revealer).

![Gtk layout do tipo revealer](https://codigoninja.dev/media/git/pygobject/layout-revealer.png)

* [Stack e stacksidebar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack_stacksidebar/builder).
* [Stack e stacksidebar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack_stacksidebar/glade).
* [Stack e stacksidebar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack_stacksidebar).

![Gtk layout do tipo stack com stacksidebar](https://codigoninja.dev/media/git/pygobject/layout-stack-stacksidebar.png)

* [Stack e stackswitcher com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack_switcher/builder).
* [Stack e stackswitcher com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack_switcher/glade).
* [Stack e stackswitcher com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/layouts/stack_switcher).

![Gtk layout do tipo stack com stackswitcher](https://codigoninja.dev/media/git/pygobject/layout-stack-stackswitcher.png)

### Diálogos

* [Personalizado com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/custom/builder).
* [Personalizado com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/custom/glade).
* [Personalizado com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/custom).

![GTK diálogo personalizado](https://codigoninja.dev/media/git/pygobject/dialog-custom.png)

* [Mensagem com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/message/builder).
* [Mensagem com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/message/glade).
* [Mensagem com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/message).

![GTK diálogo de mensagem](https://codigoninja.dev/media/git/pygobject/dialog-message.png)

* [Salvar arquivo com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/save_file/builder).
* [Salvar arquivo com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/save_file/glade).
* [Salvar arquivo com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/save_file).

![GTK diálogo para salvar arquivo](https://codigoninja.dev/media/git/pygobject/dialog-save-file.png)

* [Selecionar arquivo Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_file/builder).
* [Selecionar arquivo Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_file/glade).
* [Selecionar arquivo Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_file).

![GTK diálogo para selecionar arquivo](https://codigoninja.dev/media/git/pygobject/dialog-select-file.png)

* [Selecionar pasta com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_folder/builder).
* [Selecionar pasta com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_folder/glade).
* [Selecionar pasta com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/dialog/select_folder).

![GTK diálogo para selecionar pasta](https://codigoninja.dev/media/git/pygobject/dialog-select-folder.png)

### Dialogo de impressão, configuração de página e exportar

* [Imprimindo e exportando para pdf com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/printer/builder)
* [Imprimindo e exportando para pdf com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/printer/glade)
* [Imprimindo e exportando para pdf com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/printer)

![GTK imprindo e exportand para pdf](https://codigoninja.dev/media/git/pygobject/dialog-printer.png)

### Drag and drop (Arrastar e soltar)

* [Com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/drag-and-drop/builder).
* [Com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/ddrag-and-drop/glade).
* [Com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/drag-and-drop).

![GTK drag and drop (arrastar e soltar)](https://codigoninja.dev/media/git/pygobject/drag-and-drop.png)

### Signals e slots

* [Com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/signals-and-slots/builder).
* [Com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/signals-and-slots/glade).
* [Com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/signals-and-slots).

![GTK signals e slots](https://codigoninja.dev/media/git/pygobject/signal-and-slots.png)

### Menus

* [GTK Menu com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menu/builder).
* [GTK Menu com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menu/glade).
* [GTK Menu com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menu).

![GTK menu](https://codigoninja.dev/media/git/pygobject/menu.gif)

* [GTK menu Popover com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/popover/builder).
* [GTK menu Popover com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/popover/glade).
* [GTK menu Popover com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/menus/gtk/popover). 

![GTK menu popover](https://codigoninja.dev/media/git/pygobject/menu-popover.gif)   

* [GTK MenuBar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menubar/builder).
* [GTK MenuBar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/menubar/glade).
* [GTK MenuBar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/menus/gtk/menubar).

![GTK menubar](https://codigoninja.dev/media/git/pygobject/menubar.gif)

* [GTK menu ToolBar com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/toolbar/builder).
* [GTK menu ToolBar com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/toolbar/glade).
* [GTK menu ToolBar com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/menus/toolbar/builder).

![GTK menu toolbar](https://codigoninja.dev/media/git/pygobject/menu-toolbar.png)

### Style

> **OBS**: Ao utilizar `background-color` deve-se utilizar `background-image: none;` .

> **OBS**: Ao utilizar somente `background` não é necessário utilizar `background-image: none;` .

> **OBS**: Alguns widgets utilizam uma imagem de fundo em alguns casos pode ser interessante remover essa imagem com `background-image: none;` .

* [Adicionar classe a um widget com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/class/builder)
* [Adicionar classe a um widget com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/class/glade)
* [Adicionar classe a um widget com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/class)

![GTK Adicionar classe a um widget](https://codigoninja.dev/media/git/pygobject/style-class.png)

* [Dark Mode (modo escuro) com Gnome Builder](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/darkmode/builder)
* [Dark Mode (modo escuro) com  com Gnome Glade](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/darkmode/glade)
* [Dark Mode (modo escuro) com  com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/style/darkmode)

![GTK Dark Mode (modo escuro)](https://codigoninja.dev/media/git/pygobject/style-dark-mode.gif)

---

# Revisar, atualizar e corrigir

* [Carregando uma arquivo css](./docs/style-load-css-file.md)

![Carregando uma arquivo css](./docs/imgs/style/python-load-custom-css-wayland.png)



* [Adicionar nome a um widget](./docs/style-add-name.md)


![Adicionar nome a um widget](./docs/imgs/style/widget-name.png)

* [Ativando e desativando o dark mode (modo escuro)](./docs/style-dark-mode.md).

![Ativando e desativando o dark mode (modo escuro)](./docs/imgs/style/dark-mode.gif)

* [Utilizando ícones standard e symbolic](https://github.com/natorsc/gui-python-gtk/tree/master/src/gnome-icons).

![Utilizando ícones standard e symbolic](./docs/imgs/icons/icons-standard-symbolic.png)

### Widgets

* [Radio button](https://github.com/natorsc/gui-python-gtk/tree/master/src/widgets/radio-button)
* [TargetEntry (drag and drop)](https://github.com/natorsc/gui-python-gtk/tree/master/src/drag-n-drop)

* [GTK Entry](https://github.com/natorsc/gui-python-gtk/tree/master/src/widgets/entry):
    - [Auto completar ao digitar](https://github.com/natorsc/gui-python-gtk/tree/master/src/widgets/entry/autocomplete).

![Auto completar ao digitar](./docs/imgs/widgets/entry/autocomplete.gif)

    - [Pesquisar ao digitar](https://github.com/natorsc/gui-python-gtk/tree/master/src/widgets/entry/search).

![Pesquisar ao digitar](./docs/imgs/widgets/entry/search.gif)

* GTK TreeView:
    - [Ordenando itens ao clicar no cabeçalho da coluna](https://github.com/natorsc/gui-python-gtk/tree/master/src/widgets/treeview/sort).

![Ordenando itens ao clicar no cabeçalho da coluna](./docs/imgs/widgets/treeview/sort.gif)

    - [Realizado a edição do valor na celular](https://github.com/natorsc/gui-python-gtk/tree/master/src/widgets/treeview/editable).

![Realizado a edição do valor na celular](./docs/imgs/widgets/treeview/editable.gif)

    - [Utilizando filtro](https://github.com/natorsc/gui-python-gtk/tree/master/src/widgets/treeview/filter).

![Utilizando filtro](./docs/imgs/widgets/treeview/filter.gif)

---

## Purism Librem 5

### Widgets

* [action_row](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/action_row.py).
* [arrows](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/arrows.py).
* [column](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/column.py).
* [combo_row (não sei implementar ou ainda não funciona na versão que utilizei)]().
* [dialer](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/dialer.py).
* [dialer sem utilizar classe](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/dialer_without_class.py).
* [dialer_button](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/dialer_button.py).
* [dialer_cycle_button](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/dialer_cycle_button.py).
* [dialog](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/dialog.py).
* [dialog utilizando classe (os botões ficam direntes?)](https://github.com/natorsc/gui-python-gtk/tree/master/src/librem5-libhandy/dialog_with_class.py).
* enums.
* expander_row.
* header_bar.
* header_group.
* leaflet.
* mod.
* preferences_group.
* preferences_page.
* preferences_row.
* preferences_window.
* search_bar.
* squeezer.
* title_bar.
* value_object.
* versions.
* view_switcher_bar.
* view_switcher.
