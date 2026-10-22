#!/bin/sh
# Fetch the official, unmodified AGPL-3.0 text into LICENSE (run once, on a machine with internet access).
set -e
cd "$(dirname "$0")/.."
curl -fsSL https://www.gnu.org/licenses/agpl-3.0.txt -o LICENSE
head -3 LICENSE
