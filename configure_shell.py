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
    return parser


def get_paths():
    path = os.path.os.environ['PATH']
    return [Path(p).resolve() for p in path.split(os.path.pathsep)]


def get_mac_shell():
    shell_info = check_output('dscl . -read ~/ UserShell',
                              shell=True, text=True).strip()
    return re.match(r'UserShell: (/\w+)+', shell_info).groups()[-1][1:]


def get_mac_configfile():
    shell = get_mac_shell()
    if shell == 'bash':
        return USER_PATH / '.bash_profile'
    elif shell == 'zsh':
        return USER_PATH / '.zshrc'
    else:
        raise RuntimeError(f'Unpexpected shell {shell}')


def echo_windows_recipe(site_path):
    print('''\
Run the following commands in an Administrator Powershell window:

$site_path=python3 -c 'import os,sysconfig;print(sysconfig.get_path("scripts",f"{os.name}_user"))'
$user_path=[Environment]::GetEnvironmentVariable("PATH", "User")
[Environment]::SetEnvironmentVariable("PATH", "$user_path;$site_path", [System.EnvironmentVariableTarget]::User)

Then close all your Powershell tabs / windows and open a new Powershell window.
''')


def main():
    parser = get_parser()
    args = parser.parse_args()
    site_path_str = sysconfig.get_path("scripts",f"{os.name}_user")
    site_path = Path(site_path_str).resolve()
    if site_path in get_paths():
        print(f'{site_path} already appears to be on your PATH')
        sys.exit(1)
    if os.name == 'nt':
        echo_windows_recipe(site_path)
        sys.exit(0)
    sp_rel = site_path.relative_to(USER_PATH)
    out_text = f'''
# Inserted by configure_shell.py
# Add Python --user script directory to PATH
export PATH="$PATH:${{HOME}}/{str(sp_rel)}"
'''
    if sys.platform == 'darwin':
        config_path = get_mac_configfile()
        config_text = config_path.read_text()
        config_path.write_text(f'{config_text}\n{out_text}')
        sys.exit(0)
    raise RuntimeError(f'Unexpected platform {sys.platform}')


if __name__ == '__main__':
    main()
