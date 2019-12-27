#!/bin/bash
echo
if [ $1 == '-s' ]; then
    python3 main.py small.json
else
    echo "First one:"
    python3 main.py example1.json >test1.json
    echo
    echo "Second one:"
    python3 main.py example2.json
    echo
    echo "Third one:"
    python3 main.py example3.json
    echo
    echo "Small one:"
    python3 main.py small.json
fi
