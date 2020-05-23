#원격에 있는 git 을 로컬로 copy 한다. 
git clone https://github.com/kibua20/devDocs

#수정할 파일을 만든다
vim hellow.py

#git commit을 만든다.
git add .
git commit -m "Initial commit"

#git 현재 상태를 확인한다. .
git status

#원격 저장소에 수정한 내용을 push한다.
git push origin master
