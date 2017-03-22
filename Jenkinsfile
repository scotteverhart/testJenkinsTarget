pipeline {
    agent any
    stages {
        stage('build') {
            steps {	
               checkout([$class: 'GitSCM', branches: [[name: '*/myFirstPipeline']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' f0710d02-6c89-44fc-b360-d5a04f0eac4a', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
                bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	bat 'dir'
				 withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: ' f0710d02-6c89-44fc-b360-d5a04f0eac4a', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
				    bat "git tag -a some_tag -m 'Jenkins'"
				    bat 'git push https://${GIT_USERNAME}:${GIT_PASSWORD}@<REPO> --tags'
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