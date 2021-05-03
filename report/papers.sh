#!/bin/sh

docker pull silviof/docker-pandoc &&
    pandoc="docker run -ti --rm -v ${PWD}:/source --rm silviof/docker-pandoc" &&
    $pandoc ./notes.md ./notes1.md -o ./out/main.pdf
