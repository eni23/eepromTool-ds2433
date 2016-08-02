#!/bin/bash

if [[ -n $3 ]]; then
  odf=$3
else
  odf=x1
fi

touch /tmp/cchex1 /tmp/cchex2

od -t $odf $1 > /tmp/cchex1
od -t $odf $2 > /tmp/cchex2

wdiff /tmp/cchex1 /tmp/cchex2 | colordiff
rm /tmp/cchex1 /tmp/cchex2
