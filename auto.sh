#!/bin/bash
cd docs
make html
cd ..
git add .
git commit -m "updated"
git push
