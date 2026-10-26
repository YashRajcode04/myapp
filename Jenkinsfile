pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'yashraj0409'
        IMAGE_NAME = "${DOCKERHUB_USER}/myapp"
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/YashRajcode04/myapp.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl apply -f k8s/deployment.yaml"
            }
        }
    }
}
