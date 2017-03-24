pipeline {
    agent any
    stages {
        stage('build') {
            steps {	
               checkout([$class: 'GitSCM', branches: [[name: '*/myFirstPipeline']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' bb6b58d8-95ee-4709-966e-09d702139ebd', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
                bat "git checkout myFirstPipeline"
                bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	bat 'dir'
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'bb6b58d8-95ee-4709-966e-09d702139ebd', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
				    bat 'git config --global user.name "scott everhart"'
				    bat 'git config --global user.email "scott.everhart1@gmail.com"'
				    bat "git pull origin myFirstPipeline"
				    bat "git add *.txt"
				    bat 'git tag -a "tag_name_${env.BUILD_NUMBER}" -m "tag From Jenkins"'
				    bat "git commit -m 'FromJenkinsPipeline'"
				    bat "git push --tags"
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