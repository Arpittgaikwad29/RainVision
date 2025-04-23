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
                sh 'python3 -m unittest test_predict.py'
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
