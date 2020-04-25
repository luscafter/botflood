# BotFlood

Tool to "flood" messaging and comment services. Currently, the tool is still in the development phase, containing only Facebook publications as the target of "floods", but soon it will have more applications, such as WhatsApp, Instagram, Discord, Twitter and YouTube.

## Prerequisites

>_Python 3, Selenium and GeckoDriver_.

### Debian and derivatives (Ubuntu):

```bash
$ sudo apt-get install python3
```

### Arch Linux and derivatives:
```bash
$ sudo pacman -S python3
```

### Red Hat and derivatives:
```bash
$ sudo yum install python3
```

### _Selenium and GeckoDriver:_

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [_Selenium_](https://selenium-python.readthedocs.io/installation.html).

```bash
$ sudo pip install selenium
```

And to finish installing the dependencies, we still need to add [GeckoDriver](https://selenium-python.readthedocs.io/installation.html#drivers).

Download the driver according to your browser by clicking on any of the links below.

* [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Firefox](https://github.com/mozilla/geckodriver/releases)
* [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

After selecting your browser, download the driver.

![GeckoDriver](https://user-images.githubusercontent.com/58787069/80259294-a4029500-865b-11ea-87e0-a85e42aa2263.png)

Navigate to the folder where you downloaded the driver, extract the file (in my case, I used the version _geckodriver-v0.26.0-linux64.tar.gz_) and move it to the /bin folder.

```bash
$ cd Downloads
$ tar -xvf geckodriver-v0.26.0-linux64.tar.gz
$ sudo mv geckodriver /bin
```

![Extrair-mover](https://user-images.githubusercontent.com/58787069/80260627-b3371200-865e-11ea-8b73-0d7d7a4f63f0.png)

## BotFlood

Now download the _BotFlood_ repository:

```bash
$ git clone https://github.com/luscafter/botflood.git
```

## Changes

Since most use Firefox, I used it to make it easier. If you use a different browser, change the following code snippet according to the driver's file name. Example:

```python
self.driver = webdriver.Firefox(executable_path="/bin/geckodriver")
```

## Usage

Finally, we can run our tool, example:

```bash
$ cd botflood
$ python3 bot_flood.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

If in doubt, you can send me a message! :D

## License
[MIT](https://choosealicense.com/licenses/mit/)
