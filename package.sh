#!/bin/bash
CURRENT_DIR="$(pwd)"
cd ..
FILE="$(pwd)/BugChart.zip"
cd "$CURRENT_DIR"
zip "$FILE" *.*
cd venv/lib/python3.7/site-packages/
zip -g -r9 "$FILE" .
cd "$CURRENT_DIR"
aws lambda update-function-code --function-name "qaBugChart" --zip-file "fileb://$FILE"