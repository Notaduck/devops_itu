#!/bin/sh

docker pull silviof/docker-pandoc &&
    pandoc="docker run --rm -v ${PWD}:/source --rm silviof/docker-pandoc" &&
    $pandoc -H options.sty ./main.md --toc ./system.md ./process.md ./lessons_learned.md -o ./out/main.pdf
