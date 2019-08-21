pipeline {
  agent {
    docker {
      image 'python:3.6'
      args '-u root:sudo'
    }

  }
  stages {
    stage('Create Pivotal Tracker Config File') {
      steps {
        withCredentials(bindings: [file(credentialsId: 'pivotal_config', variable: 'config')]) {
          sh 'cp $config pivotal_tracker/config.json'
        }

      }
    }
    stage('Get package pip2') {
      steps {
        sh 'apt-get update && apt-get install python-pip -y'
      }
    }
    stage('Install python2 requirements') {
      steps {
        sh 'pip2 install -r requirements.txt'
      }
    }
    stage('Test Pivotal Tracker on Python 2.7.16 - robotframework==latest') {
      post {
        always {
          sh 'mv test_results/log.html test_results/log_python2_robot_latest.html'
          archiveArtifacts(artifacts: 'test_results/log_python2_robot_latest.html', fingerprint: true)

        }

      }
      steps {
        sh 'python2 -m robot -d test_results/ --listener pivotal_tracker/libraries/pivotal_listener.py --loglevel DEBUG pivotal_tracker/robots/*/*.robot'
      }
    }
    stage('Install python2 robotframework==3.0.1') {
      steps {
        sh 'pip2 install robotframework==3.0.1'
      }
    }
    stage('Test Pivotal Tracker on Python 2.7.16 - robotframework==3.0.1') {
      post {
        always {
          sh 'mv test_results/log.html test_results/log_python2_robot_301.html'
          archiveArtifacts(artifacts: 'test_results/log_python2_robot_301.html', fingerprint: true)

        }

      }
      steps {
        sh 'python2 -m robot -d test_results/ --listener pivotal_tracker/libraries/pivotal_listener.py --loglevel DEBUG pivotal_tracker/robots/*/*.robot'
      }
    }
    stage('Install python3 requirements') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('Test Pivotal Tracker on Python 3.6.9 - robotframework==latest') {
      post {
        always {
          sh 'mv test_results/log.html test_results/log_python3_robot_latest.html'
          archiveArtifacts(artifacts: 'test_results/log_python3_robot_latest.html', fingerprint: true)

        }

      }
      steps {
        sh 'python3 -m robot -d test_results/ --listener pivotal_tracker/libraries/pivotal_listener.py --loglevel DEBUG pivotal_tracker/robots/*/*.robot'
      }
    }
    stage('Install python3 robotframework==3.0.1') {
      steps {
        sh 'pip3 install robotframework==3.0.1'
      }
    }
    stage('Test Pivotal Tracker on Python 3.6.9 - robotframework==3.0.1') {
      post {
        always {
          sh 'mv test_results/log.html test_results/log_python3_robot_301.html'
          archiveArtifacts(artifacts: 'test_results/log_python3_robot_301.html', fingerprint: true)

        }

      }
      steps {
        sh 'python3 -m robot -d test_results/ --listener pivotal_tracker/libraries/pivotal_listener.py --loglevel DEBUG pivotal_tracker/robots/*/*.robot'
      }
    }
  }
}