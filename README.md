# Obsidian Flow shell theme
Modern Material Shell theme for GNOME DE. Based on [this](https://github.com/imarkoff/Marble-shell-theme)

![Available colors:](https://shields.io/badge/-Available%20colors:-0d1117?style=flat-square)
![red](https://shields.io/badge/-red-red?style=flat-square)
![yellow](https://shields.io/badge/-yellow-yellow?style=flat-square)
![green](https://shields.io/badge/-green-green?style=flat-square)
![blue](https://shields.io/badge/-blue-blue?style=flat-square)
![purple](https://shields.io/badge/-purple-purple?style=flat-square)
![or different Hue color.](https://shields.io/badge/-or%20different%20Hue%20color.-0d1117?style=flat-square)

## Screenshots

<details><summary>Click to view</summary>

![1](./readme-images/main.png?raw=true)
![2](./readme-images/overview.png?raw=true)
![3](./readme-images/quick-settings.png?raw=true)
![4](./readme-images/notifications-date-time.png?raw=true)
![5](./readme-images/modal-dialog.png?raw=true)

</details>

## Installation
#### The first option
Go here https://github.com/JustDeax/Obsidian-flow-shell-theme/releases/latest
and click on the **Obsidian-flow-shell-theme.zip** file.

#### The second option
**Requirements**
- GNOME 42-48
- [User Themes](https://extensions.gnome.org/extension/19/user-themes/ "User Themes") extension
- Python 3.10 or higher

1. Open the terminal.
2. Clone the git repository and change the directory:
```shell
git clone https://github.com/JustDeax/Obsidian-flow-shell-theme.git
cd Obsidian-flow-shell-theme
```
3. Run the program (install all accent colors, light and dark mode): 
```shell
python install.py -a
```
- [more vibrant color](./readme-images/qs-filled.png?raw=true) in active buttons:
```shell
python install.py -a --filled
``` 
4. After successful file creation open Extensions app, go to `User Themes - ··· - Settings`.
![0](./readme-images/user-themes-settings.png?raw=true)
5. Select the shell theme you want.

#### Install default color
| Option    | Description                  |
|-----------|------------------------------|
| -a, --all | Install all available colors |
| --red     | red theme only               |
| --yellow  | yellow theme only            |
| --green   | green theme only             |
| --blue    | blue theme only              |
| --purple  | purple theme only            |
| --gray    | gray theme only              |

> [!TIP]
> You can install several themes in one string: `python install.py --red --green --blue`

#### Install custom color
| Option | Secondary option | Description                              |
|--------|------------------|------------------------------------------|
| --hue  | (0 - 360)        | Generate theme from Hue prompt [0 - 360] |
| --name | NAME             | Custom theme name                        |

#### Theme colors
| Option   | Description                                                              |     |
| -------- | ------------------------------------------------------------------------ | --- |
| --filled | Make accent color [more vibrant](./readme-images/qs-filled.png?raw=true) |     |

#### Optional theme tweaks
| Option | Secondary option | Description                                                |
|--------|------------------|------------------------------------------------------------|
| --mode | light / dark     | light / dark theme only                                    |
| --sat  | (0 - 250)        | custom color saturation (<100 - reduce, >100 - increase)   |

#### Examples
| Command                                                   | Description                                                              |
|-----------------------------------------------------------|--------------------------------------------------------------------------|
| -a                                                        | Install all accent colors with light & dark mode                         |
| --all --mode dark                                         | Install all accent colors with dark mode only                            |
| --purple --mode=light                                     | Install purple accent color with light mode only                         |
| --hue 150 --name coldgreen                                | Install custom coldgreen accent color, light & dark mode                 |
| --red --green --sat=70                                    | red, green accent colors, 70% of the stock saturation                    |
| --hue=200 --name=grayblue --sat=50 --mode=dark            | custom grayblue accent color, 50% of the stock saturation, dark mode     |
| --gdm --blue --gdm-image /path/to/image.jpg --gdm-blur=40 | Install GDM theming in blue color with own GDM background image and blur |

> [!TIP]
> For updating the theme, run the `git pull` command in the `Obsidian-flow-shell-theme` directory and run the program again. 
> If this theme is used, updates will be applied automatically.

## GDM theme
**Requirements for GDM theme**
- `glib2-devel` (`libglib2.0-dev` on Debian-based distros).
- `imagemagick` (if you want to apply filters to the background image).

**Config:** 
`sudo python install.py --gdm --blue --filled --gdm-image /path/to/image.jpg --gdm-blur=40 --gdm-darken=30`

> [!WARNING]  
> I am not responsible for any damage caused by the installation of the theme. If you have any problems, please open an issue.

1. Open the terminal.
2. Go to the directory with the theme.
3. Run the program with the `--gdm` option
```shell
sudo python install.py --gdm (--your color) (--is filled)
```
- Example:
```shell
sudo python install.py --gdm --blue --filled
```
```shell
sudo python install.py --gdm --gray --gdm-image /path/to/image.jpg --gdm-blur=40 --gdm-darken=30
```
4. After successful file restart GDM service:
```shell
sudo systemctl restart gdm
```

- If you want to remove the theme or theme is broken, run the program with the `--remove` option:
```shell
sudo python install.py --gdm --remove
```
- If you got a death screen, you can switch to the console with the `Ctrl + Alt + F3` key combination, log in, go to the `Obsidian-flow-shell-theme` directory and run the command above. If it doesn't help, try reinstalling `gnome-shell` package.

**GDM tweaks**

| Option        | Secondary option         | Description                 |
|---------------|--------------------------|-----------------------------|
| --gdm-image   | /absolute/path/to/image/ | set background image to GDM |
| --gdm-blur    | 0+                       | apply blur to image (px)    |
| --gdm-darken  | 0 - 100                  | darken image (%)            |
| --gdm-lighten | 0 - 100                  | lighten image (%)           |

## Uninstallation / Reinstallation
- To remove the theme, run the program with the `--remove` option:
```shell
python install.py --remove
```
- To reinstall the theme, run the program with the `--reinstall` option:
```shell
python install.py --reinstall -a  # (other installation options)
```

