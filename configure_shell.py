#!/usr/bin/env python3
""" Write (or echo) configuration for user installs
"""

import os
import sys
import sysconfig
import re
from subprocess import check_output
from pathlib import Path

from argparse import ArgumentParser, RawDescriptionHelpFormatter

USER_PATH = Path('~').expanduser()

def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('-x', '--allow-existing', action='store_true',
                        help='Force config write even if dir already on PATH')
    return parser



def get_paths():
    path = os.path.os.environ['PATH']
    return [Path(p).resolve() for p in path.split(os.path.pathsep)]


def get_mac_shell():
    shell_info = check_output('dscl . -read ~/ UserShell',
                              shell=True, text=True).strip()
    return re.match(r'UserShell: (/\w+)+', shell_info).groups()[-1][1:]


def get_unix_shell():
    from getpass import getuser
    shell_info = check_output(f'getent passwd {getuser()}',
                              shell=True, text=True).strip()
    return shell_info.split(':')[-1].split('/')[-1]


def get_posix_configfile():
    is_mac = os.name == 'darwin'
    shell = get_mac_shell() if is_mac else get_unix_shell()
    if shell == 'bash':
        return USER_PATH / ('.bash_profile' if is_mac else '.bashrc')
    elif shell == 'zsh':
        return USER_PATH / '.zshrc'
    else:
        raise RuntimeError(f'Unexpected shell {shell}')


def set_windows_path(site_path):
    res = check_output(f'setx PATH "%PATH%;{site_path}',
                       shell=True,
                       text=True).strip()
    if not res.startswith('SUCCESS:'):
        raise RuntimeError(f'SETX failed: {res}')


def set_path_config(site_path):
    if os.name == 'nt':
        set_windows_path(site_path)
        return
    sp_rel = site_path.relative_to(USER_PATH)
    out_text = f'''
# Inserted by configure_shell
# Add Python --user script directory to PATH
export PATH="$PATH:${{HOME}}/{str(sp_rel)}"
'''
    config_path = get_posix_configfile()
    config_text = config_path.read_text()
    if not out_text in config_text:
        config_path.write_text(f'{config_text}\n{out_text}')


def main():
    parser = get_parser()
    args = parser.parse_args()
    site_path_str = sysconfig.get_path("scripts",f"{os.name}_user")
    site_path = Path(site_path_str).resolve()
    if not args.allow_existing and site_path in get_paths():
        print(f'{site_path} already appears to be on your PATH')
        sys.exit(1)
    set_path_config(site_path)
    print("""\
Now close all terminals and start a new terminal to load new config""")


if __name__ == '__main__':
    main()
