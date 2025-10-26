pipeline {
    agent any
    stages{
        stage('Checkout Code'){
            steps{
                    checkout scm
            }
        }
        stage('Extract data'){
            steps{
                bat "python extract.py"
            }
        }
    }
}