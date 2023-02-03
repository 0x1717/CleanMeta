---

# :boom: Clean Meta 

<img src='QARNRCWJKCFAKLJFP.png'>

> Clean Meta is a Python script that removes the exif (Exchangeable image file format) data from a file or a directory and changes the filename. It is useful for people who are concerned about their privacy and want to remove metadata from their files. The tool requires exiftool to be installed on the Linux system. Clean Meta has two arguments, `-f` and `-d`. The `-f` argument removes exif data from a single file, while the `-d` argument removes exif data from a directory recursively. The script uses the exiftool to remove exif data and generates a new filename using random characters. The new file name is used to store the file after removing the exif data.

> In the code, the MD5 (Message-Digest algorithm 5) hash function is used to identify and remove duplicates from the files within the directory when the `-d` argument is used. The MD5 function creates a unique hash value for a file, which can be used to identify duplicate files.

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
