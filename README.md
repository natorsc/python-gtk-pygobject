> Em desenvolvimento e revisão

> **OBS**: Este repositório tem um arquivo `Pipfile`, o mesmo **não** funciona no Windows, isso porque a instalação do GTK e Python **DEVEM** ser feitas pelo **msys2**.

---

# GUI (graphical user interface) com Python e GTK

Tutoriais e pequenos exemplos de código.

## GTK

O GTK é um **toolkit multiplataforma** para a criação de interfaces gráficas.

Este toolkit utiliza [licença GNU LGPL](https://pt.wikipedia.org/wiki/GNU_Lesser_General_Public_License), o que permite a sua utilização para construção de softwares que seja livres ou proprietários.

Foi desenvolvido inicialmente para o [GIMP](https://www.gimp.org/) (GNU Image Manipulation Program), por isso foi batizado de **GIMP Toolkit** ou simplesmente **GTK**.

Originalmente criado por, Peter Mattis, Spencer Kimball e Josh MacDonald.

O GTK+ é comumente utilizado na elaboração de aplicativos para o ambiente de desktop [GNOME](https://www.gnome.org/), contudo por ser multiplataforma pode ser executado sem problemas em diversos sistemas operacionais e ambientes gráficos.

O toolkit é escrito em `C`, seu design é orientado a objeto com base no sistema de objetos da biblioteca `GLib`.

Existe o suporte (bindings) a diversas linguagens de programação, contudo as linguagem que são suportadas **oficialmente** (até o momento que escrevo) são:

-   C++.
-   JavaScript.
-   Python.
-   Vala.

## O que estou publicando?

A ideia é apenas **estudar** e documentar a construção de interfaces gráficas com GTK e Python.

Exemplos de código podem ser vistos na pasta `src` deste repositório.

> Em caso de problemas entre em contato para que o material possa ser melhorado.

# Tutoriais

- [Como instalar o msys2 no Windows (Obrigatório)](https://codigoninja.dev/2020/09/08/python-gtk-instalar-msys2-windows/).
- [Como instalar o PyGObject for Windows (não recomendado)](https://codigoninja.dev/2020/09/08/python-gtk-instalar-pygobject-windows/).
- [Configurando o ambiente de desenvolvimento](https://codigoninja.dev/2020/09/08/python-gtk-configurando-ambiente-desenvolvimento/).

## IDEs e RADs

- [Como Instalar o Gnome Builder](https://codigoninja.dev/2020/09/08/python-gtk-instalar-gnome-builder/).
- [Como Instalar o Gnome Glade](https://codigoninja.dev/2020/09/08/python-gtk-instalar-gnome-glade/).

## Purism Librem 5

- [Como Instalar a biblioteca libhandy](https://codigoninja.dev/2020/09/08/python-gtk-instalar-biblioteca-libhandy/).
- [Executando o PureOS (Phosh) via VM](https://codigoninja.dev/2020/09/08/python-gtk-pureos-phosh/).

## GTK

- [GTK icon browser](https://codigoninja.dev/2020/09/08/python-gtk-instalar-icon-browser/).
- [Como ativar o GtkInspector](https://codigoninja.dev/2020/09/08/python-gtk-ativar-gtkinspector/).
- [Criando uma janela com Python e GTK](https://codigoninja.dev/2020/09/08/python-gtk-criando-janela/).


## Criar executáveis

- [Criando executáveis com Cx_Freeze no Windows](https://codigoninja.dev/2020/09/08/python-gtk-criando-executavel-cxfreeze-windows/).
- [Criando executáveis com Cx_Freeze no Linux](https://codigoninja.dev/2020/09/08/python-gtk-criando-executavel-cxfreeze-linux/).

## Extra

- [Como instalar Python no Linux e Windows](https://codigoninja.dev/2020/09/07/instalar-linguagem-python-linux-windows/).

---

# Código

## GTK

### Janela principal

- [Lendo arquivos interface do Gnome Glade](./src/main-window/glade).
- [Lendo arquivos de interface do Gnome Builder](./src/main-window/builder).
- [Criando a janela com Python](./src/main-window).

### Signals e slots

- [Sinais e slots com arquivo de interface do Gnome Glade](./src/signals-and-slots/glade).
- [Sinais e slots com arquivo de interface do Gnome Builder](./src/signals-and-slots/builder).
- [Sinais e slots com arquivo com Python](./src/signals-and-slots).

### Diálogos

- [Diálogo personalizado (Gnome Builder)](./src/gtk/dialog/custom/builder).
- [Diálogo personalizado (Gnome Glade)](./src/gtk/dialog/custom/glade).
- [Diálogo personalizado (Python)](./src/gtk/dialog/custom).

![GTK diálogo personalizado](https://codigoninja.dev/media/git/pygobject/dialog-custom.png)

- [Diálogo de mensagem (Gnome Builder)](./src/gtk/dialog/message/builder).
- [Diálogo de mensagem (Gnome Glade)](./src/gtk/dialog/message/glade).
- [Diálogo de mensagem (Python)](./src/gtk/dialog/message).

![GTK diálogo de mensagem](https://codigoninja.dev/media/git/pygobject/dialog-message.png)

- [Diálogo para salvar arquivo (Gnome Builder)](./src/gtk/dialog/save_file/builder).
- [Diálogo para salvar arquivo (Gnome Glade)](./src/gtk/dialog/save_file/glade).
- [Diálogo para salvar arquivo (Python)](./src/gtk/dialog/save_file).

![GTK diálogo para salvar arquivo](https://codigoninja.dev/media/git/pygobject/dialog-save-file.png)

- [Diálogo para selecionar arquivo (Gnome Builder)](./src/gtk/dialog/select_file/builder).
- [Diálogo para selecionar arquivo (Gnome Glade)](./src/gtk/dialog/select_file/glade).
- [Diálogo para selecionar arquivo (Python)](./src/gtk/dialog/select_file).

![GTK diálogo para selecionar arquivo](https://codigoninja.dev/media/git/pygobject/dialog-select-file.png)

- [Diálogo para selecionar pasta (Gnome Builder)](./src/gtk/dialog/select_folder/builder).
- [Diálogo para selecionar pasta (Gnome Glade)](./src/gtk/dialog/select_folder/glade).
- [Diálogo para selecionar pasta (Python)](./src/gtk/dialog/select_folder).

![GTK diálogo para selecionar pasta](https://codigoninja.dev/media/git/pygobject/dialog-select-folder.png)

### Menus

- [GTK Menu](./src/menus/menu).

    ![GTK menu](./docs/imgs/menus/menu.png)
    
- [GTK Popover](./src/menus/popover).

    ![GTK popover](./docs/imgs/menus/popover.png)
    
- [GTK MenuBar](./src/menus/menubar).

    ![GTK menubar](./docs/imgs/menus/menubar.png)

- [GTK ToolBar](./src/menus/toolbar).

    ![GTK toolbar](./docs/imgs/menus/toolbar.png)


### Style

> **OBS**: Ao utilizar `background-color` deve-se utilizar `background-image: none;`.

> **OBS**: Ao utilizar somente `background` não é necessário utilizar `background-image: none;`.

> **OBS**: Alguns widgets utilizam uma imagem de fundo em alguns casos pode ser interessante remover essa imagem com `background-image: none;`.

- [Carregando uma arquivo css](./docs/style-load-css-file.md)
    
    ![Carregando uma arquivo css](./docs/imgs/style/python-load-custom-css-wayland.png)
    
- [Adicionar classe a um widget](./docs/style-add-class.md)
    
    ![Adicionar classe a um widget](./docs/imgs/style/widget-class.png)
    
- [Adicionar nome a um widget](./docs/style-add-name.md)
    
    ![Adicionar nome a um widget](./docs/imgs/style/widget-name.png)

- [Ativando e desativando o dark mode (modo escuro)](./docs/style-dark-mode.md).
    
    ![Ativando e desativando o dark mode (modo escuro)](./docs/imgs/style/dark-mode.gif)

- [Utilizando ícones standard e symbolic](./src/gnome-icons).
    
    ![Utilizando ícones standard e symbolic](./docs/imgs/icons/icons-standard-symbolic.png)

### Layouts

- [actionbar](./src/layouts/actionbar).
- [box_horizontal](./src/layouts/box_horizontal).
- [box_vertical](./src/layouts/box_vertical).
- [buttonbox](./src/layouts/buttonbox).
- [fixed](./src/layouts/fixed).
- [flowbox](./src/layouts/flowbox).
- [grid](./src/layouts/grid).
- [gtk_layout](./src/layouts/gtk_layout).
- [headerbar_layout](./src/layouts/headerbar).
- [listbox_layout](./src/layouts/listbox).
- [notebook_layout](./src/layouts/notebook).
- [overlay_layout](./src/layouts/overlay).
- [paned_layout_horizontal](./src/layouts/paned_horizontal).
- [paned-layout-vertical](./src/layouts/paned_vertical).
- [revealer_layout](./src/layouts/revealer).
- [stack_layout_stacksidebar](./src/layouts/stack_stacksidebar).
- [stack_layout_stackswitcher](./src/layouts/stack_switcher).

### Widgets

- [Radio button](./src/widgets/radio-button)
- [TargetEntry (drag and drop)](./src/drag-n-drop)
    
![TargetEntry (drag and drop)](./docs/imgs/drag-and-drop/drag-and-drop.gif)
    
- [GTK Entry](./src/widgets/entry):
    - [Auto completar ao digitar](./src/widgets/entry/autocomplete).
        
        ![Auto completar ao digitar](./docs/imgs/widgets/entry/autocomplete.gif)
        
    - [Pesquisar ao digitar](./src/widgets/entry/search).
    
        ![Pesquisar ao digitar](./docs/imgs/widgets/entry/search.gif)
        
- GTK TreeView:
    - [Ordenando itens ao clicar no cabeçalho da coluna](./src/widgets/treeview/sort).
        
        ![Ordenando itens ao clicar no cabeçalho da coluna](./docs/imgs/widgets/treeview/sort.gif)
        
    - [Realizado a edição do valor na celular](./src/widgets/treeview/editable).
        
        ![Realizado a edição do valor na celular](./docs/imgs/widgets/treeview/editable.gif)
    
    - [Utilizando filtro](./src/widgets/treeview/filter).
    
        ![Utilizando filtro](./docs/imgs/widgets/treeview/filter.gif)

---

## Purism Librem 5

### Widgets

- [action_row](./src/librem5-libhandy/action_row.py).
- [arrows](./src/librem5-libhandy/arrows.py).
- [column](./src/librem5-libhandy/column.py).
- [combo_row (não sei implementar ou ainda não funciona na versão que utilizei)]().
- [dialer](./src/librem5-libhandy/dialer.py).
- [dialer sem utilizar classe](./src/librem5-libhandy/dialer_without_class.py).
- [dialer_button](./src/librem5-libhandy/dialer_button.py).
- [dialer_cycle_button](./src/librem5-libhandy/dialer_cycle_button.py).
- [dialog](./src/librem5-libhandy/dialog.py).
- [dialog utilizando classe (os botões ficam direntes?)](./src/librem5-libhandy/dialog_with_class.py).
- enums.
- expander_row.
- header_bar.
- header_group.
- leaflet.
- mod.
- preferences_group.
- preferences_page.
- preferences_row.
- preferences_window.
- search_bar.
- squeezer.
- title_bar.
- value_object.
- versions.
- view_switcher_bar.
- view_switcher.