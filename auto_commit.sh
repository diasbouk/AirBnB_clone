#!/bin/bash


message="commit till 60"
content="  "

function gitPush ()
{
	git add .
	git commit -m "$1"
	git push origin main
}

for ((i = 0; i <= 3; i++)) do
  echo $content >> README.md
   # Changing readme by adding new white-spaces
   gitPush "$message $i"
  # echo " $ message $i" | gitpush
  # Passing message as input to gitpush command
done

# Dont forget to clean afterwards ==> deleted extra spaces on readme
