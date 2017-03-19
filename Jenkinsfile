pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	bat 'dir'
            }
        }
    }
	post {
        always {
            archive myTestFile.txt
        }
    }
}