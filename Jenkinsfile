pipeline {
agent any
stages {
stage('Clone') {
steps {
git 'https://github.com/YOUR_USERNAME/jenkins-cicd-demo.git'
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
