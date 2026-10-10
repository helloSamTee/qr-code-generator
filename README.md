# QR Code Generator with Logo Overlay

This Python script generates a QR code from a URL or text. You can optionally add a logo in the center, choose the QR code color, and set the output file name.

## Prerequisites

Make sure you have Python installed on your machine. Install the required libraries using the following command:

```
pip install -r requirements.txt
```

## Usage

Run the script from this directory with a URL or text supplied through `--url`:

```bash
python qrcode-gen.py --url "https://example.com"
```

The command above creates `qrcode.png` in the current directory.

### Arguments

- `--url` (required): The URL or text to encode.
- `--logo`: Path to an image file to place in the center of the QR code.
- `--color`: QR code fill color. Defaults to `black`. Pillow color names and color values such as `#1d4ed8` are supported.
- `--destination`: Output file name without the `.png` extension. Defaults to `qrcode`.

### Examples

Generate a QR code with a custom color:

```bash
python qrcode-gen.py --url "https://example.com" --color red --destination example-red
```

Add a logo and save the result with a custom name:

```bash
python qrcode-gen.py --url "https://github.com/helloSamTee/qr-code-generator" --logo "path/to/githublogo.png" --color red --destination testing
```

This creates `testing.png`. The logo is resized and placed in the center of the QR code.

## Example

![mygithubqr](https://github.com/yaserrati/qr-code-generator/assets/88887542/fd046b7f-80a3-45b1-ac02-d1e64fef214e)


## Dependencies

- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)

## Credits

- [qrcode](https://github.com/lincolnloop/python-qrcode)
- [Pillow (PIL Fork)](https://github.com/python-pillow/Pillow)
