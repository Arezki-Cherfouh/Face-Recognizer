#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_face_recognizer..."
wine "run_face_recognizer" || ./"run_face_recognizer" "$@"
