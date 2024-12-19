pipeline {
    agent any
    
    stages {

        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                #!/bin/bash
                cd /home/cristibtz/Flask-Postgres-Docker-App && sudo -u cristibtz /usr/bin/git pull
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                cd /home/cristibtz/Flask-Postgres-Docker-App && sudo -u cristibtz /usr/bin/docker compose up --build -d
                '''
            }
        }
    }
}