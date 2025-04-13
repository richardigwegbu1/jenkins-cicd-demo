pipeline {
agent any
stages {
stage('Clone') {
steps {

git branch: 'main', url: 'https://github.com/richardigwegbu1/jenkins-cicd-demo.git'
}
}
stage('Install Dependencies') {
steps {
sh 'pip install -r requirements.txt'
}
}
stage('Run Tests') {
steps {
sh 'pytest tests'
}
}
stage('Deploy') {
steps {
sh 'cp app.py /var/www/html/'
}
}
}
}
