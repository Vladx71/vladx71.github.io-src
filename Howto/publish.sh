cd /home/vlad/git/ghpages/
#make html && make serve
make publish
cd output
git add .
git commit -m "$1"
git push -u origin master
cd ..
echo '*.pyc' >> .gitignore #don't need pyc files
git add .
git commit -m "$1"
git push -u origin master

