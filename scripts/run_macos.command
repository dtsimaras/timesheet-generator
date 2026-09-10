#!/bin/zsh

APP_DIRECTORY="$(cd "$(dirname "$0")" && pwd)"
RESULT="$("$APP_DIRECTORY/timesheet-generator")"
EXIT_CODE=$?

print -r -- "$RESULT"

if (( EXIT_CODE != 0 )); then
  print ""
  print "The timesheet was not created. Read the message above, fix config.json, then try again."
  read "?Press Enter to close this window. "
  exit "$EXIT_CODE"
fi

CREATED_FILE="${RESULT#Created: }"
if [[ -f "$CREATED_FILE" ]]; then
  open -R "$CREATED_FILE"
fi
