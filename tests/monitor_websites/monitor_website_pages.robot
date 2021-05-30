*** Settings ***
Resource    resources/monitor_website_pages_resource.robot
Force Tags    monitor_websites

*** Test Cases ***
Monitor Webpage Page With Periodical Schedule
    [Template]    Monitor Webpage Page With Periodical Schedule
    ${STACKOVERFLOW_LOGIN_URL}    login-form    ${3}
    ${FOOBAR_URL}    login-form    ${3}
    ${STACKOVERFLOW_TEAMS_URL}    product-main-nav    ${3}
