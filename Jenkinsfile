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
                bat "C:\\Users\\sanyu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe extract.py"
            }
        }
    }
}