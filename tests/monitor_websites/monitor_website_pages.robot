*** Settings ***
Resource    resources/monitor_website_pages_resource.robot
Force Tags    monitor_websites

*** Test Cases ***
Monitor Webpage With Periodical Schedule (Stackoverflow Login)
    [Template]    Monitor Webpage Page With Periodical Schedule
    ${STACKOVERFLOW_LOGIN_URL}    login-form    ${INTERVAL_SEC}

Monitor Webpage With Periodical Schedule (Stackoverflow Teams)
    [Template]    Monitor Webpage Page With Periodical Schedule
    ${STACKOVERFLOW_TEAMS_URL}    product-main-nav    ${INTERVAL_SEC}

Monitor Webpage With Periodical Schedule (403 Error)
    [Template]    Monitor Webpage Page With Periodical Schedule
    ${FOOBAR_URL}    login-form    ${INTERVAL_SEC}