#!/bin/bash


# Temporary conversion of JavaScript ES6 to ES5. Once Firefox 45 comes out (Q1/Q2 2016),
# and all supported browsers support ES6 sufficiently ('class' in particular,
# see http://kangax.github.io/compat-table/es6/), one can remove this script and
# rename the *.es6.js files *.js, overwriting the existing files. Delete also node_modules, and run
# pip uninstall nodeenv.
#
# Run this script every time you update an *.es6.js file.

if ! hash babel 2>/dev/null;
then
pip install nodeenv
nodeenv -p

npm install -g babel babel-cli webpack
npm install babel-preset-es2015
fi

babel=$(which babel)
webpack=$(which webpack)

IFS=$'\n';

for file in $(find . -path ./node_modules -prune -o  -type f -name "*.es6.js" -print)
do
  dirname=$(dirname "$file")
  basename=$(basename "$file")
  outfilename="${basename%.es6.js}"
  tmpfile=$(mktemp)
  outfile="$dirname/$outfilename.js"
  echo "Converting $file to $outfile"
  $babel $file --presets es2015 >> $tmpfile
  $webpack $tmpfile $outfile
  rm $tmpfile
  sed -i "1i /* This file has been automatically generated. DO NOT EDIT IT. \n Changes will be overwritten. Edit $basename and run ./es6-compiler.sh */"  "$outfile"
done
