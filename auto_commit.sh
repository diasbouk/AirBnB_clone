#!/bin/bash

for ((i = 0; i <= 5; i++)) do
  echo "  " >> README.md
  echo "commit till 55" | gitpush
done
