---

# :boom: Clean Meta 

<img src='QARNRCWJKCFAKLJFP.png'>

> Clean Meta is a Python script that removes the exif data from a file or a directory and changes the filename. This tool is useful for people who are concerned about their privacy and want to remove any metadata from their files.

---

## :scroll: Prerequisites

- In order to use Clean Meta, you must have exiftool installed on your Linux system. You can install exiftool by running the following command:


```bash
sudo apt-get install libimage-exiftool-perl
```

---

## :scroll: Installation

```bash
git clone https://github.com/0x1717/CleanMeta.git && cd CleanMeta/ && chmod +x cleanmeta.py
```

---

## :scroll: Usage

- Clean Meta has two arguments, `-f` and `-d`. The `-f` argument is used to remove exif data from a file, while the `-d` argument is used to remove exif data from a directory recursively.

---

### :pill: `-f` Argument

- The `-f` argument is used to remove exif data from a single file. To use the `-f` argument, run the following command:

```bash
python3 cleanmeta.py -f <file-path>
```

- For example:

```bash
python3 cleanmeta.py -f ~/Pictures/test_image.jpg
```

---

### :pill: `-d` Argument

- The `-d` argument is used to remove exif data from a directory recursively. To use the `-d` argument, run the following command:

```bash
python3 cleanmeta.py -d <directory-path>
```

- For example:

```bash
python3 cleanmeta.py -d ~/Pictures/
```

---

> #### Created by 0x1717 aka GYG3S
