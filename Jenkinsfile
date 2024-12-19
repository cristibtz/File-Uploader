pipeline {
    agent any
    
    stages {

        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                #!/bin/bash
                cd /home/cristibtz/Flask-Postgres-Docker-App/.env .
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
                docker compose up --build -d
                '''
            }
        }
    }
}