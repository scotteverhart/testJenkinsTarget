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
            'C:/Program Files (x86)/Jenkins/workspace/rstPipeline_myFirstPipeline-JID5IFHV7Y3MVMLJOQDNSJROSZMQLVMLKMMV6WEUY3FCLG7KWZJA/myTestFile.txt'
        }
    }
}