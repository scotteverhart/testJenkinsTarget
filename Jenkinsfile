pipeline {
    agent any
    stages {
        stage('build') {
            steps {	
               checkout([$class: 'GitSCM', branches: [[name: '*/myFirstPipeline']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '7d589385-d9d8-4006-9571-e70538886a93', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
                bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	bat 'dir'
				 withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'bb6b58d8-95ee-4709-966e-09d702139ebd', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
				    sh("git tag -a some_tag -m 'Jenkins'")
				    sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@<REPO> --tags')
				}
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