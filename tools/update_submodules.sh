#!/bin/bash
# This is a bash script to update the current version of the submodules
# folder to point at the latest commit/changes made.

cd ..
echo "The current submodules version is:"
git submodule
echo "Heading into submodules directory"
cd submodules
echo "Updating the submodules folder to latest commit"
git pull
echo "Moving back into main directory"
cd ..
echo "Updated submodules version is:"
git submodule
echo ""
echo "Changes are not commited by this script."
echo "Please be sure to commit changes to git manually."
echo ""