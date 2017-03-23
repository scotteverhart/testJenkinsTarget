pipeline {
    agent any
    stages {
        stage('build') {
            steps {	
               checkout([$class: 'GitSCM', branches: [[name: '*/myFirstPipeline']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' f0710d02-6c89-44fc-b360-d5a04f0eac4a', url: 'git@github.com:scotteverhart/myGitHubRepo.git']]])
                bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	bat 'dir'
			    bat "git tag -a 'tag_from_jenkins' -m 'Jenkins'"
			    bat 'git push git@github.com:scotteverhart/myGitHubRepo.git --tags'
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