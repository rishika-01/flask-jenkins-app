pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Deploy') {
            steps {
                sh 'mkdir -p deployment'
                sh 'cp app.py deployment/'
                sh 'cp requirements.txt deployment/'
            }
        }
    }
}