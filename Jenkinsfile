pipeline {
    agent any

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['DEV', 'TEST', 'PROD'], description: 'Select the target deployment environment')
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls the latest code from your repository
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running automated python unit tests..."
                # Run pytest to execute your test file
                bat 'pytest test_app.py'
            }
        }

        stage('Deploy to Environment') {
            steps {
                # Reads the parameter chosen by the user in the UI
                echo "Deploying the Online Examination System to the ${params.ENVIRONMENT} environment..."
                
                # Simulates the execution of the app in the chosen environment
                bat "python app.py" //khuzaifa
            }
        }
    }
}

