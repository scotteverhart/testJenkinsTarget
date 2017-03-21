pipeline {
    agent any
    stages {
        stage('build') {
            steps {
            	step('run python'){
                	bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
                }
                step('list directory'){
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