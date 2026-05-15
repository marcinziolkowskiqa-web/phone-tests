pipeline {
    agent any

    environment {
        ADB = 'C:\\Users\\MarcinZiółkowski\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe'
        PYTHON = 'C:\\Users\\MarcinZiółkowski\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe'
        APPIUM = 'C:\\Users\\MarcinZiółkowski\\AppData\\Roaming\\npm\\appium.cmd'

        ANDROID_HOME = 'C:\\Users\\MarcinZiółkowski\\AppData\\Local\\Android\\Sdk'
        ANDROID_SDK_ROOT = 'C:\\Users\\MarcinZiółkowski\\AppData\\Local\\Android\\Sdk'
        APPIUM_HOME = 'C:\\Users\\MarcinZiółkowski\\.appium'
        JAVA_HOME = 'C:\\Program Files\\Android\\Android Studio\\jbr'

        PROJECT_DIR = 'C:\\Temp\\phone_tests'
        APPIUM_LOG = 'C:\\Temp\\phone_tests\\appium.log'
    }

    stages {
        stage('Check environment') {
            steps {
                bat '"%ADB%" devices'
                bat '"%PYTHON%" --version'
                bat '"%APPIUM%" -v'
                bat '"%APPIUM%" driver list --installed'
                bat 'echo ANDROID_HOME=%ANDROID_HOME%'
            }
        }

        stage('Clean old results') {
            steps {
                dir("${env.PROJECT_DIR}") {
                    bat '''
                    if exist report.html del report.html
                    if exist screenshots rmdir /s /q screenshots
                    if exist appium.log del appium.log
                    '''
                }
            }
        }

        stage('Start Appium') {
            steps {
                dir("${env.PROJECT_DIR}") {
                    bat '''
                    start "Appium Server" /B cmd /c ""%APPIUM%" --log "%APPIUM_LOG%" --log-timestamp"
                    powershell -Command "Start-Sleep -Seconds 8"
                    curl http://127.0.0.1:4723/status
                    '''
                }
            }
        }

        stage('Run tests') {
            steps {
                dir("${env.PROJECT_DIR}") {
                    bat '"%PYTHON%" -m pytest -v -s --html=report.html --self-contained-html'
                }
            }
        }
    }

    post {
        always {
            bat 'taskkill /F /IM node.exe /T'

            dir("${env.PROJECT_DIR}") {
                archiveArtifacts artifacts: 'report.html,screenshots\\*.png,appium.log', allowEmptyArchive: true
            }
        }
    }
}