#!/bin/bash


message="commit till 60"
content="  "
number_of_commits=0
function gitPush ()
{
	git add .
	git commit -m "$1"
	git push origin main
}


for ((i = 0; i <= $number_of_commits; i++)) do

   # Changing readme by adding new white-spaces
  echo $content >> README.md

  # Passing message as input to gitpush commando
  gitPush "$message $i"

done

# Dont forget to clean afterwards ==> deleted extra spaces on readme
