#!/usr/bin/env sh
set -eu

APP_DIRECTORY="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
"$APP_DIRECTORY/timesheet-generator"
xdg-open "$APP_DIRECTORY/output" >/dev/null 2>&1 || true
