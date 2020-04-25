# Executando o PureOS (Phosh) via VM

> **OBS**: VM abreviação para **virtual machine** (máquina virtual).

A [Purism](https://puri.sm/) em seus notebooks e computadores utiliza o sistema operacional [PureOS](https://pureos.net/), o mesmo é uma distribuição Linux que utiliza como base o [Debian](https://www.debian.org/) juntamente com o ambiente de desktop [Gnome](https://www.gnome.org/).

Para o [Librem 5](https://puri.sm/products/librem-5/), que é um smartphone da empresa, é utilizada uma versão do PureOS que utilizar um protótipo de shell chamado [Phosh](https://source.puri.sm/Librem5/phosh) juntamente com um compositor que utiliza [Wayland](https://wayland.freedesktop.org/) chamado [Phoc](https://source.puri.sm/Librem5/phoc/).

Neste texto vamos ver como realizar o download do arquivo de disco e como utilizar este arquivo de disco no [Gnome Boxes](https://wiki.gnome.org/Apps/Boxes).

Veremos também que é possível utilizar essa VM para testar aplicativos construídos com [GTK](https://www.gtk.org/), em especifico aplicativos construídos com o [Gnome Builder](./install-gnome-builder.md) e empacotados em formato [Flatpak](https://flatpak.org/).

> Para saber mais sobre o Gnome Builder [clique aqui](./install-gnome-builder.md).

## Baixando o arquivo de disco

O primeiro passo para baixar o arquivo de disco que será utilizado no virtualizador é acessar o site de integração continua (CI server) do projeto:

[https://arm01.puri.sm/job/Images/job/Image%20Build/](https://arm01.puri.sm/job/Images/job/Image%20Build/)

Procure pelos históricos de builds que **estão em verde**:

![histórico de builds](./imgs/phosh/purism-ci.png)

Ao acessar o histórico de builds procure por arquivos do tipo `qemu-x86_64.qcow2`, caso não encontre este arquivo basta clicar no botão **Previous Build**:

![Procurando pelo arquivo qemu-x86_64.qcow2](./imgs/phosh/purism-ci-previous-build.png)

Ao localizar a imagem, basta fazer o download da mesma clicando sobre o nome:

![Localizando e realizando o download do arquivo de disco](./imgs/phosh/purism-download-qcow2.png)

Como o arquivo é do tipo `qcow2` é interessante utilizar `KVM/QEMU` para a virtualização, duas boas opções de virtualizadores para este caso são:

- [Gnome Boxes](https://wiki.gnome.org/Apps/Boxes) (que vem com algumas distribuições Linux).
- [virt-manager](https://virt-manager.org/).

Como estou utilizando o [Fedora](https://getfedora.org/pt_BR/) o Gnome Boxes já vem instalado por padrão, neste caso basta clicar no **ícone de soma** (**+**) e selecionar a opção **Criar uma máquina virtual...**:

![Adicionado uma nova máquina virtual no Gnome Boxes](./imgs/phosh/gnome-boxes-add-vm.png)

Em seguida clique na opção **Selecione um arquivo**:

![Não foi fornecido texto alternativo para esta imagem](./imgs/phosh/gnome-boxes-select-file.png)

Navegue até a pasta onde está o arquivo `qemu-x86_64.qcow2` e clique em **Abrir**:

![Selecionando o arquivo de disco](./imgs/phosh/gnome-boxes-select-disk.png)

Agora é exibida a tela onde podemos configurar a quantidade de memória RAM que será utilizada pela máquina virtual, por padrão a mesma utiliza 2 GiB, o qual é um bom valor. Clique em **Criar**:

![Criando a maquina virtual](./imgs/phosh/gnome-boxes-create-vm.png)

Aguarde **alguns minutos** até que seja exibida a tela de desbloqueio do sistema.

A senha para desbloqueio da tela é `123456`:

<img alt="Tela de desbloqueio do PureOS Phosh" src="./imgs/phosh/phosh-login-screen.png" width="180px" height="360px">

Ao realizar o desbloqueio é exibida a primeira tela de configuração, onde podemos definir o idioma para o sistema (por enquanto não está disponível o idioma português do brasil). Clique em **Next**:

<img alt="Selecionando o idioma" src="./imgs/phosh/phosh-language.png" width="180px" height="360px" >

Logo em seguida temos a tela de configuração do teclado, selecione o mais adequado e clique em **Next**:

<img alt="Selecionando o layout do teclado" src="./imgs/phosh/phosh-keyboard.png" width="180px" height="360px" >

Agora podemos configurar a privacidade, marque as opções que julgar interessantes para a **sua privacidade**. Clique em **Next**:

<img alt="Configuração de privacidade" src="./imgs/phosh/phosh-privacy.png" width="180px" height="360px" >

Caso queira configurar uma conta de **e-mail** ou do **NextCloud** este é o momento, caso contrario clique em **Skip**:

<img alt="Conectando contas online" src="./imgs/phosh/phosh-accounts.png" width="180px" height="360px" >

Por fim, clique em **Start Using your Librem 5** para começar a utilizar o sistema:

<img alt="Tela final da configuração" src="./imgs/phosh/phosh-start-using.png" width="180px" height="360px" >

Com o fim das configurações temos a tela inicial do sistema, onde podem ser vistos alguns apps:

<img alt="Tela inicial do sistema" src="./imgs/phosh/phosh-home-screen.png" width="180px" height="360px" >

Ao clicar na região do relógio temos uma área de notificações e algumas configurações rápidas:

<img alt="Área de notificação e configuração rápida do sistema" src="./imgs/phosh/phosh-notification-area.png" width="180px" height="360px" >

Assim como em sistemas Linux para desktop, podemos realizar diversas operações pelo terminal, basicamente são os mesmo comandos que se utilizariam em sistemas operacionais como Debian e Ubuntu:

<img alt="Executando o terminal no PureOS Phosh" src="./imgs/phosh/phosh-terminal.png" width="180px" height="360px" >

> **OBS**: Vale enfatizar que o **usuário padrão** é `purism` e a **senha** é `123456`.

Nos testes que realizei, a VM apresenta um comportamento bem estável e é muito interessante analisar a forma com que os aplicativos feitos com a biblioteca [libhandy](./install-purism-libhandy.md) (ou não) se comportam em telas pequenas.

## Deploy de um aplicativo na VM

O objetivo aqui **é apenas exemplificar** o processo de instalação de um aplicativo na VM.

Para isso vou utilizar o próprio aplicativo de exemplo que é criado quando se inciar um projeto no Gnome Builder.

> [Clique aqui](./install-gnome-builder.md) para ver como instalar e criar um projeto no Gnome Builder.

Criar um pacote Flatpak no Gnome Builder é extremamente simples, basta acessar o menu superior e clicar na opção **Exportar pacote**:

![Exportando pacote no Gnome Builder](./imgs/phosh/gnome-builder-export-package.png)

> **OBS**: Caso o botão não esteja disponível execute uma vez o projeto.

O processo de construção do pacote é exibido no terminal do Gnome Builder:

![Processo de construção do pacote Flatpak no terminal do Gnome builder](./imgs/phosh/gnome-builder-export-log.png)

Com o final do processo uma janela contendo os arquivos **costuma** ser aberta:

![Pasta contendo os arquivos gerados pelo Gnome Builder](./imgs/phosh/gnome-builder-export-folder.png)

Caso a janela não abra, basta verificar no terminal do Gnome Builder o caminho onde os arquivos foram gerados.

O caminho padrão costuma ser:

```bash
~/.var/app/org.gnome.Builder/cache/gnome-builder/projects/NomeDoProjeto/flatpak/staging/
```

A copia do pacote Flatpak (`br.natorsc.OlaMundo.flatpak`) é feita com o comando `scp`, para utilizar esse comando é necessário saber o **IP** da VM.

Para isso basta abrir um terminal na VM e digitar o comando `ip a` ou mesmo `ip a | grep inet`:

<img alt="Verificando o IP da VM" src="./imgs/phosh/phosh-get-vm-ip.png" width="180px" height="360px" >

Vale notar que não é necessário utilizar apenas o terminal da VM, também é possível se conectar a mesma utilizando-se **SSH**:

![Acessando VM por ssh](./imgs/phosh/phosh-ssh-connect.png)

> **OBS**: Utilize a forma que lhe for mais confortável.

Ao descobrir o IP da VM **abra um terminal no mesmo diretório** onde está o pacote Flatpak (`br.natorsc.OlaMundo.flatpak`) e execute:

```bash
scp br.natorsc.OlaMundo.flatpak purism@192.168.122.133:~/
```

![Copiando pacote Flatpak para a VM](./imgs/phosh/scp-package.png)

> **OBS**: Lembre-se de alterar o IP e o nome do pacote!

Após a cópia podemos verificar que o arquivo foi copiado para a VM utilizando o comando `ls`:

<img alt="Verificando pacote Flatpak na VM" src="./imgs/phosh/phosh-ls-flatpak-package.png" width="180px" height="360px" >

Agora que o aplicativo está na VM precisamos configurar o repositório [Flathub](https://flatpak.org/setup/) na VM, isso porque o aplicativo que copiamos no momento da instalação irá baixar o runtime e outros pacotes necessário para a sua execução.

O repositório Flathub pode ser adicionado utilizando-se:

```bash
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

Para confirmar se o repositório foi adicionando:

```bash
flatpak remotes
```

<img alt="Verificando se o repositório foi adicionado" src="./imgs/phosh/phosh-flatpak-remotes.png" width="180px" height="360px" >

Com o repositório configurado podemos instalar o aplicativo com o comando:

```
flatpak install br.natorsc.OlaMundo.flatpak
```

<img alt="Instalando o aplicativo" src="./imgs/phosh/phosh-install-app.png" width="180px" height="360px" >

Digite a senha do usuário `purism` (`123456`):

<img alt="Digitando a senha para instalação" src="./imgs/phosh/phosh-password-dialog.png" width="180px" height="360px" >

O instalador irá verificar e realizar o download do runtime necessário:

<img alt="Flatpak instalando o runtime necessário" src="./imgs/phosh/phosh-flatpak-install-runtime.png" width="180px" height="360px" >

E de outros pacotes pacotes necessários para sua execução:

<img alt="Flatpak instalando as dependências necessárias" src="./imgs/phosh/phosh-flatpak-install-dependencies.png" width="180px" height="360px" >

> Caso encontre um erro durante a instalação [clique aqui](#Erros)

A execução do aplicativo pode ser feita com o comando:

```bash
flatpak run br.natorsc.OlaMundo
```
<img alt="Aplicativo em execução na VM" src="./imgs/phosh/phosh-app-run.png" width="180px" height="360px" >

O aplicativo também pode ser executado pelo ícone que é exibido na tela inicial, caso o ícone não apareça na tela inicial reinicie a VM:

<img alt="Ícone do aplicativo na tela inicial do PureOS (Phosh)" src="./imgs/phosh/phosh-app-icon-home-screen.png" width="180px" height="360px" >

Com isso finalizamos esse passeio pelo PureOS com Phosh.

Caso encontre erros, ou mesmo inconsistências, entre em contato para que o conteúdo possa ser melhorado 🤓.

Dicas e criticas também são bem vindas 😁.

# Extra

## Erros

### Falta de espaço na VM

Ao tentar instalar o aplicativo na VM pode ser exibido o erro:

```bash
Error: Not enough disk space to complete this operation
```

<img alt="Erro ao tentar instalar o aplicativo" src="./imgs/phosh/phosh-disk-space-error.png" width="180px" height="360px" >

Este erro é porque o **tamanho da partição** está menor que o tamanho do disco virtual.

Para visualizar o tamanho do disco virtual ou até mesmo aumentar o seu tamanho basta acessar as configurações da VM:

![Aumentando o tamanho do disco virtual](./imgs/phosh/gnome-boxes-vm-config.png)

> **OBS**: Você não precisa aumentar o tamanho do disco ele é mais que suficiente o erro está no tamanho da partição.

Para corrigir (redimensionar) o tamanho da partição podemos utilizar uma imagem de boot do [Gparted](https://gparted.org/)

Para iniciar pela imagem do Gparted, basta acionar a mesma nas propriedades da VM:

![Adicionando iso do Gparted no Gnome Boxes](./imgs/phosh/gnome-boxes-add-gparted-iso.png)

Ao iniciar a VM pressione `Esc` e em seguida pressione o numero `3` (No meu Gnome Boxes a unidade de CD/DVD está no 3):

![Menu de boot do Gnome Boxes](./imgs/phosh/gnome-boxes-boot-menu.png)

Como resultado temos:

![Realizando boot pela imagem do Gparted](./imgs/phosh/gparted-menu-boot.png)

De boot normalmente e ao abrir o Gparted podemos verificar que a partição (`/dev/sda2` ⚠️) não está aproveitando todo o disco e é isso que está gerando o problema de espaço:

![Verificando o disco no Gparted](./imgs/phosh/gparted-partition-error.png)

Para corrigir clique com o **botão direito** sobre a partição com alerta, clique em **Verificar** e depois no **botão de check verde** (✅) para realizar a operação:

![Redimencionando a partição da VM](./imgs/phosh/gparted-patition-verify.png)

Após a verificação a partição já deve estar utilizando todo o espaço disponível:

![Partição da VM após a verificação](./imgs/phosh/gparted-partition-after-verify.png)

Desligue o Gparted e inicie novamente na VM.

Ao iniciar tente realizar a instalação novamente e a mesma deve ocorrer sem problemas 😎.