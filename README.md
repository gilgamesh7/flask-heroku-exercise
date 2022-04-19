# flask_heroku_exercise

## Course Link
[Real Python Course Link](https://realpython.com/flask-by-example-part-1-project-setup/)

## Github to course material
[Python Flask heroku Example](https://github.com/realpython/materials/tree/master/python-flask-example-heroku)

## Heroku Help
[Prerequisites](https://devcenter.heroku.com/articles/git#prerequisites-install-git-and-the-heroku-cli)

## To run locally
FLASK_ENV=development flask run

## Install Heroku CLI
brew tap heroku/brew && brew install heroku

## Instantiate remote GIT
(As of 17/04/2022 , the dashboard has been disabled for OAUTH - only CLI available) <br> <br>
heroku git:remote -a flask-heroku-exercise
<br> 
To Check : git remote -v
<br>

## Deploy
(To be done after pushing GIT through CLI as above) <br>
git push heroku main 

## To Run
https://flask-heroku-exercise.herokuapp.com
<br> OR <br>
heroku run
<br>