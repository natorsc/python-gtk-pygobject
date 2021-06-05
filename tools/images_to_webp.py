# -*- coding: utf-8 -*-
"""Convertendo formatos de imagem para webp.

[Google Webp](https://developers.google.com/speed/webp).

## Dependências

### Fedora

```bash
sudo dnf install libwebp-tools
```

### Ubuntu

```bash
sudo apt install webp
```
"""

from pathlib import Path
from subprocess import run


def gif_to_webp(file):
    current_path = file.parent
    file_webp = file.stem + '.webp'
    webp_path = current_path.joinpath('webp')
    output = webp_path.joinpath(file_webp)
    webp_path.mkdir(parents=True, exist_ok=True)

    cmd = [
        'gif2webp', '-quiet', '-lossy', '-q', '50', f'{file}', '-o', f'{output}'
    ]

    result = run(cmd)

    if result.stderr:
        print(result.stderr.decode())


def png_to_webp(file):
    current_path = file.parent
    file_webp = file.stem + '.webp'
    webp_path = current_path.joinpath('webp')
    output = webp_path.joinpath(file_webp)
    webp_path.mkdir(parents=True, exist_ok=True)

    cmd = [
        'cwebp', '-quiet', '-lossless', '-q', '50', f'{file}', '-o', f'{output}'
    ]

    result = run(cmd)

    if result.stderr:
        print(result.stderr.decode())


def jpg_to_webp(file):
    current_path = file.parent
    file_webp = file.stem + '.webp'
    webp_path = current_path.joinpath('webp')
    output = webp_path.joinpath(file_webp)
    webp_path.mkdir(parents=True, exist_ok=True)

    cmd = [
        'cwebp', '-quiet', '-lossless', '-q', '50', f'{file}', '-o', f'{output}'
    ]

    result = run(cmd)

    if result.stderr:
        print(result.stderr.decode())


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent

    png_files = BASE_DIR.rglob('*.png')
    gif_files = BASE_DIR.rglob('*.gif')
    jpg_files = BASE_DIR.rglob('*.jpg')

    for file in png_files:
        png_to_webp(file=file)

    for file in jpg_files:
        jpg_to_webp(file=file)

    for file in gif_files:
        gif_to_webp(file=file)

    print('Fim')
