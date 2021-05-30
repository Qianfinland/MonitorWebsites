*** Settings ***
Resource          ../../../libraries/src/common_library_imports.robot


*** Keywords ***
Monitor Webpage Page With Periodical Schedule
    [Arguments]    ${test_url}    ${page_content}    ${interval_sec}
    Schedule Monitor Website    ${test_url}    ${page_content}    ${interval_sec}