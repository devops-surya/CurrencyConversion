def buildAndPushDockerImage(String imageName, String dockerCredsId, String dockerfilePath = '.') {
    echo "Building Docker Image: ${imageName}"

    sh """
        docker build -t ${imageName} ${dockerfilePath}
    """

    withCredentials([usernamePassword(credentialsId: dockerCredsId, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
        echo "Logging into Docker Hub with credentialsId: ${dockerCredsId}"
        sh """
            echo "\$DOCKER_PASS" | docker login -u "\$DOCKER_USER" --password-stdin
            docker push ${imageName}
        """
    }
}

