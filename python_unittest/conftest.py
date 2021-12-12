from datetime import datetime
from py.xml import html
import pytest
import sys
import logging


def pytest_html_report_title(report):
    ''' modifying the title  of html report'''
    report.title = "My PyTest Title"
    pass

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    ''' modifying the summary in pytest environment'''
    # prefix.extend([html.h3("Adding prefix message")])
    # summary.extend([html.h3("Adding summary message")])
    # postfix.extend([html.h3("Adding postfix message")])
    pass    


def pytest_configure(config):
    ''' modifying the table pytest environment'''
    # print(sys._getframe(0).f_code.co_name)
    # # getting user name
    # from pwd import getpwuid
    # from os import getuid

    # username = getpwuid(getuid())[0]

    # # getting python version
    # from platform import python_version
    # py_version = python_version()
    # # overwriting old parameters with  new parameters
    # config._metadata =  {
    #     "user_name": username,
    #     "python_version": py_version,
    #     "date": "오늘"
    # }
    pass
    

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        # extra.append(pytest_html.extras.url('./assets/image.png'))
        #extra.append(pytest_html.extras.text(item.name))

        # extra.append(pytest_html.extras.text('some string', name='Different title'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


