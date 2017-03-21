pipeline {
    agent any
    stages {
        stage('build') {
            steps {
            	step {
                	bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
                }
                step {
            		bat 'dir'
            	}
            }
        }
    }
	post {
        always {
            archive '**/myTestFile.txt'
        }
    }
}