#!/bin/bash
# This script combines header, problem, and footer into README.md

# If header exists, include it
if [ -f README.header.md ]; then
    cat README.header.md > README.md
fi

# Always include problems.md
cat problems.md >> README.md

# If footer exists, include it
if [ -f README.footer.md ]; then
    cat README.footer.md >> README.md
fi