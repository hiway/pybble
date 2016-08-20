#!/usr/bin/env bash

echo "[pybble] Preparing..."
transcrypt -p .none app.py
echo "[pybble] Copying app to app.js..."
cat __javascript__/app.min.js > app.js
echo "[pybble] Done."
