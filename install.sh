#!/bin/bash
mkdir /opt/qrscan
cp ./scanner.py /opt/qrscan/
ln /opt/qrscan/scanner.py /usr/local/bin/qrscan
chmod +x /opt/qrscan/scanner.py
