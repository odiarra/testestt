import pytest
import datetime
from jira_dest import *


@pytest.fixture(autouse=True, scope="module")
def jira_source_dest():
    source_url, source_login, source_passwd = "http://localhost:8090", "admin", "admin"
    dest_url, dest_login, dest_passwd = "http://localhost:8091", "admin", "admin"
    sudo, verify = True, False


    jira_source = jira(source_url,
                              basic_auth=(source_login, source_passwd),
                              max_retries=6,
                              sudo=sudo,
                              options={'verify': verify})
    jira_dest = jira(dest_url,
                            basic_auth=(dest_login, dest_passwd),
                            max_retries=6,
                            sudo=sudo,
                            options={'verify': verify})

    return jira_source, jira_dest