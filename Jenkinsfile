pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root:root'
        }
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Arcade138/devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pip install pytest' // Ensure pytest is available
                sh 'pytest tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Use docker-in-docker or run this stage on a separate agent if needed
                echo 'Docker build will require a different agent with Docker installed'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Docker run will require a different agent with Docker installed'
            }
        }
    }
}
