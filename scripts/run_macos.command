#!/bin/zsh
set -e

APP_DIRECTORY="$(cd "$(dirname "$0")" && pwd)"
"$APP_DIRECTORY/timesheet-generator"
open "$APP_DIRECTORY/output"
