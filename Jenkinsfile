#!groovy
node() {
    stage('Checkout'){
       echo "Checking out source"
       checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/odiarra/testestt.git']]])
    }
    stage('Testing'){
        // Run tox with the tox-integration.ini file in the root of the repository
        echo "Running Tox integration script"
        try {

            bat 'tox --recreate -- --pyargs rep.jira.tests -v -m rep_jira_template --jira_dest_url http://localhost:8090 --jira_dest_login oumou  --jira_dest_passwd oumou  --jira_src_url http://localhost:8091 --jira_src_login oumou  --jira_src_passwd oumou'
        } finally {
            echo "Bad Test "
        }
    }
}


