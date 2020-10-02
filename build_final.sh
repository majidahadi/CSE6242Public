#!/bin/bash

rm -rf team-49-final 
mkdir team-49-final
mkdir team-49-final/DOC
mkdir team-49-final/CODE

#README/
cp ./README.txt team-49-final/

#DOC/
cp ./docs/team-49-report.pdf team-49-final/DOC/
cp ./docs/team-49-poster.pdf team-49-final/DOC/

#SRC/
cp -r ./api team-49-final/CODE/api
cp -r ./db team-49-final/CODE/db
cp -r ./RhymeViz\ Vizualizations/ team-49-final/CODE/RhymeViz\ Vizualizations/

rm team-49-final.zip
cd team-49-final
zip -r ../team-49-final.zip *
cd ..
