#!/bin/bash
#List all options the Http server will accept
curl -sX OPTIONS "$1"
