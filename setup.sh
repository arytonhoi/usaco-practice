#!/bin/bash

if [ -n "$1" ]; then
    prog_name="$1"
    file_name="$prog_name.py"

    cp _template.py "$file_name"
    sed -i '' -e "s/template/$prog_name/g" "$file_name"
    echo "Created $file_name ..."

    mv *.in "$prog_name.in"
    mv *.out "$prog_name.out"
    echo "Done"
else
    echo "Give the filename"
fi