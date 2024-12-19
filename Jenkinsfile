pipeline {
    agent any
    
    stages {

        stage('Build') {
            steps {
                echo 'Building...'
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