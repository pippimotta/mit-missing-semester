#!/bin/bash

for i in {a..z}; do
  for j in {a..z}; do
    echo "$i$j" >> all_letters
  done
done
