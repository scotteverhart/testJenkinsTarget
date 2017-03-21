pipeline {
    agent any
    stages {
        stage('build') {
            steps {
            	step {
            		git branch: 'myFirstPipeline', credentialsId: '7d589385-d9d8-4006-9571-e70538886a93', url: 'https://github.com/scotteverhart/myGitHubRepo.git/'
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