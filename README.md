![Criando interfaces gráficas com Python (PyGObject) e Gtk 4](./docs/images/index/python-gtk-4-do-zero-ao-app-1600x840.webp "Criando interfaces gráficas com Python (PyGObject) e Gtk 4")

<br>

[![natorsc - gui-python-pygobject-gtk4](https://img.shields.io/static/v1?label=natorsc&message=gui-python-pygobject-gtk4&color=blue&logo=github)](https://github.com/natorsc/gui-python-pygobject-gtk4 "Ir para o repositório.")
&emsp;
[![stars - gui-python-pygobject-gtk4](https://img.shields.io/github/stars/natorsc/gui-python-pygobject-gtk4?style=social)](https://github.com/natorsc/gui-python-pygobject-gtk4)
&emsp;
[![forks - gui-python-pygobject-gtk4](https://img.shields.io/github/forks/natorsc/gui-python-pygobject-gtk4?style=social)](https://github.com/natorsc/gui-python-pygobject-gtk4)

[![License MIT](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://github.com/natorsc/gui-python-pygobject-gtk4)

# Criando interfaces gráficas com Python (PyGObject) e Gtk 4

## 📝 Descrição

Repositório criado para documentar e centralizar conteúdos, dicas, tutoriais e exemplos de código sobre a construção de interfaces gráficas com a linguagem de programação Python (PyGObject) e o toolkit gráfico Gtk 4.

---

## 📚 Documentação

🚨 Importante!

Para facilitar a navegação e consulta dos conteúdos contidos neste repositório, a documentação foi criada com [Sphinx](https://www.sphinx-doc.org/en/master/) + [Furo](https://github.com/pradyunsg/furo).

Acesse [https://gtk.justcode.com.br/](https://gtk.justcode.com.br/) para poder ver ao conteúdo completo.

---

## 🛠 Tecnologias utilizadas

Até o presente momento as seguintes tecnologias estão sendo utilizadas na construção do projeto:

[![Python](https://img.shields.io/static/v1?label=&message=Python&color=blue&logoColor=white&logo=python)](https://www.python.org/ "Ir para o site.")
&emsp;
[![PyGObject](https://img.shields.io/static/v1?label=&message=PyGObject&color=blue&logoColor=white&logo=pypi)](https://pypi.org/project/PyGObject/ "Ir para o PyPi.")
&emsp;
[![Sphinx](https://img.shields.io/static/v1?label=&message=Sphinx&color=blue&logoColor=white&logo=pypi)](https://pypi.org/project/Sphinx/ "Ir para o PyPi.")
&emsp;
[![Furo](https://img.shields.io/static/v1?label=&message=Furo&color=blue&logoColor=white&logo=pypi)](https://pypi.org/project/furo/ "Ir para o PyPi.")
&emsp;
[![Gtk](https://img.shields.io/static/v1?label=&message=Gtk&nbsp;4&color=blue&logoColor=white&logo=gnome)](https://www.gtk.org/ "Ir para o site.")
&emsp;
[![Gnome](https://img.shields.io/static/v1?label=&message=Gnome&color=blue&logoColor=white&logo=gnome)](https://www.gnome.org/ "Ir para o site.")
&emsp;
[![Flatpak](https://img.shields.io/static/v1?label=&message=Flatpak&color=blue&logoColor=white&logo=flathub)](https://flatpak.org/ "Ir para o site.")

---

## 🤓 Autor

Feito com 💙 por [Renato Cruz](https://github.com/natorsc) 🤜🤛 Entre em contato!

[![E-mail](https://img.shields.io/static/v1?label=&message=E-mail&color=blueviolet&logoColor=white&logo=gmail)](mailto:zkpcvm6dz@mozmail.com "Enviar e-mail.")
&emsp;
[![LinkedIn](https://img.shields.io/static/v1?label=&message=LinkedIn&color=blue&logoColor=white&logo=LinkedIn)](https://www.linkedin.com/in/natorsc "Entre em contato.")

Uma das playlist que costumo ouvir quando estou estudando ou "codando" 😁:

[![Spotify](https://img.shields.io/static/v1?label=&message=Spotify&color=darkgreen&logoColor=white&logo=spotify)](https://open.spotify.com/playlist/1xf3u29puXlnrWO7MsaHL5?si=A-LgwRJXSvOno_e6trpi5w&utm_source=copy-link "Acessar playlist.")

Sempre que possível escrevo tutoriais no meu blog pessoal 🚀:

[![Blog](https://img.shields.io/static/v1?label=&message=Blog&color=gray&logoColor=blue&logo=hashnode)](https://blog.codigoninja.dev/ "Ir para o blog.")

---

## 💝 Doações

### Ko-Fi

[![Ko-Fi](https://img.shields.io/static/v1?label=&message=Ko-Fi&color=orange&logoColor=white&logo=ko-fi)](https://ko-fi.com/natorsc "Ajude com uma doação.")

### Pix

<img src="./docs/images/donation/pix-qr-code.jpg" alt="drawing" width="150"/>

**Chave**: `b1839493-2afe-484d-9272-82a3e402b36f`

---

## 💡 Extra

### Poetry

#### requirements.txt

Para gerar o arquivo de dependências `requirements.txt` através do [Poetry](https://python-poetry.org/) utilizar o comando:

```bash
poetry export \
--without-hashes \
-f requirements.txt \
-o requirements.txt
```

Para gerar o arquivo com as dependências de desenvolvimento (`requirements-dev.txt`):

```bash
poetry export \
--with dev \
--without-hashes \
-f requirements.txt \
-o requirements-dev.txt
```

Dependências da documentação (`docs/requirements.txt`)

```bash
poetry export \
--only docs \
--without-hashes \
-f requirements.txt \
-o docs/data/requirements-doc.txt
```

Executar localmente a documentação:

```bash
python3 -m http.server -d docs/build/dirhtml
```

---
