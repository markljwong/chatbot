#!/bin/bash

iii = 0;
for file in 'ls';
do mkdir output/${iii};
echo "unzip $file -d output/${iii}";
unzip -P abc $file -d output/${iii} > /dev/null; 
((iii++));
done

iii = 0;
for file in 'ls';
do mkdir output/${iii};
echo "$ {iii} unrar x $file output/${iii}";
unrar x $file output/${iii} > /dev/null; 
((iii++));
done