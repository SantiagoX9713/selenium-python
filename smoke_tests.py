from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from search_test import SearchTest

#Cargando la pruebas para después pasarla a la Test Suite
assertion_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

# Creando la Test Suite
smoke_test = TestSuite([assertion_test, search_test])
kwargs = {
    'output': 'smoke-report'
}
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)