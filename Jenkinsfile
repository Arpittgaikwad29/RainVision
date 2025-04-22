pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repo-name.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests added yet — add unit tests here!'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t rainfall-predictor .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 rainfall-predictor'
            }
        }
    }
}
