#!/bin/bash
npx serve docs&
inotifywait -r -m docs/markdown |
    while read path _ file; do
        ./update_slides.sh
    done
