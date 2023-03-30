#!/bin/bash
#List all options the Http server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
