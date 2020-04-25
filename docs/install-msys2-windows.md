# Como instalar o msys2 no Windows

O msys2 permite a utilização do [Pacman](https://wiki.archlinux.org/index.php/Pacman_(Portugu%C3%AAs)) como gerenciador de pacotes no Windows.

Com sua instalação passamos a ter no Windows:

- Instalação e atualização de pacotes de forma simplificada.
- Gerenciamento de dependências ao instalar um novo pacote.
- Acesso a ferramentas como, **shell bash**, **Autotools**, etc.
- Construção de pacotes com **mingw-64** e **toolchains**.

Para realizar a instalação você deve acessar o [site oficial do msys2](https://www.msys2.org/):

![Site oficial do msys2](./imgs/msys2/msys2-site.png)

E realizar o download do pacote de acordo com a arquitetura do seu Windows, lembrando que:

- **x86_64**: Para Windows 64 bit.
- **i686**: Para Windows 32 bit.

![Verificando se o Windows é 32 ou 64 bits](./imgs/msys2/windows-architecture.png)

Com o fim do download basta dar **2 cliques** e o instalador será iniciado:

![Instalador do msys2 na pasta downloads do Windows](./imgs/msys2/msys2-download-folder.png)

Na primeira tela que é exibida clique em **Next**:

![Primeira tela do instalador do msys2](./imgs/msys2/msys2-install-00.png)

Agora podemos escolher onde o msys2 será instalado, **recomendo** que você deixe o caminho que é exibido no instalador. Clique em **Next**:

![Definindo o local de instalação do msys2](./imgs/msys2/msys2-install-01.png)

Na tela seguinte podemos escolher o nome do diretório no menu iniciar, novamente **recomendo** que você deixe o nome que é sugerido pelo instalador. Clique em **Next**:

![Definindo o nome da pasta do msys2 no menu iniciar do Windows](./imgs/msys2/msys2-install-02.png)

Com isso a instalação é iniciada, basta aguardar o final da mesma:

![Msys2 sendo instalado](./imgs/msys2/msys2-install-03.png)

Com o final da instalação podemos iniciar o terminal do msys2, basta marcar a opção **Run MYSYS2 xxBit now** e clicar em **Finish**:

![Instalação do msys2 finalizada](./imgs/msys2/msys2-install-04.png)

Assim que o terminal estiver aberto devemos iniciar a atualização dos pacotes, para isso execute o comando:

```bash
pacman -Syu
```

![Atualizando os pacotes do msys2 com pacman -Syu](./imgs/msys2/msys2-syu.png)

Com o fim da atualização pressione **Ctrl + C** e feche o terminal.

Após fechar o terminal o mesmo pode ser encontrado no menu iniciar do Windows. Selecione **MSYS2 MSYS**:

![Msys2 no menu iniciar do Windows](./imgs/msys2/msys2-start.png)

O aplicativo também pode ser localizado na pasta onde o msys2 foi instalado:

![Aplicativo do msys2 em sua pasta de instalação](./imgs/msys2/msys2-folder.png)

Com ele aberto vamos continuar as atualizações com o comando:

```bash
pacman -Su
```

![Atualizando o msys2 com o comando pacman -Su](./imgs/msys2/msys2-su.png)

Com isso finalizamos o processo de atualização dos pacotes.

> Os comandos a cima são apenas para atualização, você pode executá-los sempre que se **julgar necessário**, **cuidado** apenas com atualizações de versão do Python, visto que isso pode quebrar o projeto.

A sintaxe básica para realizar uma instalação de pacote no msys2 é:

```bash
pacman -S NomeDoPacote
```

Para localizar algum pacote pode ser utilizando o comando:

```bash
pacman -Ss NomeDoPacote
```

![Localizando um pacotes no msys2 com o comando pacman -Ss](./imgs/msys2/msys2-search-package.png)

Por fim, vamos instalar o [Git](https://git-scm.com/) no msys2, para isso:

```bash
pacman -S git
```

![Instalando o Git no msys2](./imgs/msys2/msys2-install-package.png)

Se nenhum erro for retornado, o git estará disponível **dentro** do terminal do msys2.

Cabe destacar que na pasta onde o msys2 foi instalado, existe uma pasta chama **home** e dentro da mesma existe uma pasta com o **seu nome de usuário**:

![Pasta home do msys2](./imgs/msys2/msys2-home-folder.png)

Pode ser muito interessante criar seus projetos dentro desta pasta, uma vez que o terminal do msys2 sempre abre essa localização quando inicia :wink:.