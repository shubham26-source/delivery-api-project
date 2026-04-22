pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/shubham26-source/delivery-api-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t delivery-api .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f delivery-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name delivery-container delivery-api'
            }
        }
    }
}