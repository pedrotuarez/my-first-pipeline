pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Construyendo proyecto...'
                bat 'python -m compileall src'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                bat 'python -m unittest discover -s tests'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente.'
        }

        failure {
            echo 'El Pipeline ha fallado.'
        }
    }
}