pipeline {
    agent any

    environment {
        IMAGE_NAME = 'tejamvs/currency-conversion:latest'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/devops-surya/CurrencyConversion.git'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Trivy Image Scan') {
            steps {
                script {
                    echo 'Running Trivy vulnerability scan...'
                    sh '''
                        trivy image --severity CRITICAL,HIGH --exit-code 1 $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Docker Login and Push') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockercreds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            docker push $IMAGE_NAME
                        '''
                    }
                }
            }
        }

        stage('Run Container and Health Check') {
            steps {
                script {
                    echo 'Running container for health check...'
                    sh '''
                        docker run -d --name currency_app -p 8000:8000 $IMAGE_NAME
                        sleep 5
                        curl -f http://localhost:8000/ || (echo "Health check failed!" && exit 1)
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker containers and images...'
            sh '''
                docker rm -f currency_app || true
                docker rmi $IMAGE_NAME || true
            '''
        }
    }
}

