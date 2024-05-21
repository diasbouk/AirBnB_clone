#!/bin/bash

for ((i = 0; i <= 3; i++)) do
  echo "  " >> README.md
  echo "commit till 55 commit N $i" | gitpush
done
