# This file installs Obsidian Flow shell theme for GNOME DE
# by JustDeax
import os
import shutil

from scripts import config
from scripts.install import ArgumentsDefiner
from scripts.install.colors_definer import ColorsDefiner
from scripts.install.global_theme_installer import GlobalThemeInstaller
from scripts.install.local_theme_installer import LocalThemeInstaller
from scripts.utils.gnome import apply_gnome_theme
from scripts.utils.logger.console import Console


def main():
    colors_definer = ColorsDefiner(config.colors_json)
    args = ArgumentsDefiner(colors_definer.colors).parse()

    installer_class = GlobalThemeInstaller if args.gdm else LocalThemeInstaller
    installer = installer_class(args, colors_definer)

    if args.gdm:
        if os.getuid() != 0:
            Console().Line().error(
                "Global installation requires root privileges. Please run the script as root.")
            return

    if args.remove or args.reinstall:
        installer.remove()

    if not args.remove:
        installer.install()

    if not args.gdm and not args.remove:
        apply_gnome_theme()


if __name__ == "__main__":
    try:
        main()
    finally:
        shutil.rmtree(config.temp_folder, ignore_errors=True)
