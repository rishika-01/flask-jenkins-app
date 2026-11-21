pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    .venv/bin/python -m unittest discover -s . -p "test_*.py"
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    mkdir -p deploy
                    cp app.py deploy/
                    cp requirements.txt deploy/
                    echo "Deployment successful"
                    ls -l deploy
                '''
            }
        }
    }
}