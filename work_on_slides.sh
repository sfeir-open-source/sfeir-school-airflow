#!/bin/bash
npx serve docs
inotifywait -r -m -e modify docs/markdown | 
    while read path _ file; do 
        ./update_slides.sh
    done