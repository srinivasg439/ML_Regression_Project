# ML_Regression_Project
This is first ML project

### Software and account Requirement.

    1. [Github Account](https://github.com/)
    2. [Heroku Account](https://www.heroku.com/)
    3. [Vs Code IDE](https://code.visualstudio.com/download)
    4. [Git Cli](https://git-scm.com/downloads)

To create conda environment use below command in any commond prompt in your system
`````````````````````
conda create -p venv python==3.7 -y

To activate conda environment use below command in commond prompt
`````````````````````
conda activate <virtual-name>/

Need to create requirements.txt file under 'venv' folder or virtual environmet folder & install it in command promt
`````````````````````
pip install -r requirements.txt

To add files to git
````````
git add .

or 

git add <file-name>

>Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
`````````
git status

To check all version maintained by git
`````````
git log

To create version/commit all changes by git
```````
git commit -m "message"

To send version/commit changes to git
``````
git push origin main

To check remote url
``````
git remote -v

To setup CI/CD pipeline in HEROKU we need three information

1.HEROKU_EMAIL = srinivasg439@gmail.com
2.HEROKU_API_KEY = 27a24053-3df5-4f22-9087-4a960fb4e659
3.HEROKU_APP_NAME = ml-regression-first-app

Build Docker Image
`````````
docker build -t <image-name>:<tagname> .

>Note docker image name must be lowercase

To list docker image
```````
docker images

To run docker image
``````
docker run -p 5000:5000 -e PORT=5000

To check runnig container in docker 
``````
docker ps

To stop docker container
```````
docker stop <container-id>


