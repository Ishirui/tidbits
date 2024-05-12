#!/bin/sh

# https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# VSCode settings.json
cp "$HOME/.config/Code/User/settings.json" "$SCRIPT_DIR/vscode/settings.json"
