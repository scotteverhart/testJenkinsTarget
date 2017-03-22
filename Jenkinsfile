pipeline {
    agent any
    stages {
    	stage('scm checkout') {
    		steps {
    			checkout([$class: 'GitSCM', branches: [[name: '*/myFirstPipeline']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '7d589385-d9d8-4006-9571-e70538886a93', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
    		}
    	}	
        stage('build') {
            steps {	
                bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	bat 'dir'
            	bat "echo 'protocol=https'"
            	bat "echo 'host=https://github.com/scotteverhart'"
            	bat "git config user.name=Scott Everhart"
            	bat "git config user.email=scott.everhart1@gmail.com"
            	bat 'git tag -a "myFirstTag" -m "FromJenkins"'
            	bat 'git push --tags'
            	input message: 'Approval required to begin gitTest build', ok: 'Approve', submitterParameter: 'ApprovingSubmitter'
            	build 'gitTest'
           	}
        }
    }
	post {
        always {
        	echo 'archiving files'
            archive '*.txt'
            echo 'archiving complete'
        }
    }
}