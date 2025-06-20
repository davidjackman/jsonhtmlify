#!/usr/bin/env python3
# filepath: /Users/david/htmldictify/html-table-generator/run_tests.py
"""
Comprehensive test runner for the HTML Table Generator.
This script runs all test suites and provides detailed reporting.
"""

import sys
import unittest
import time
from io import StringIO


def run_test_suite(test_module_name, description):
    """Run a specific test suite and return results."""
    print(f"\n{'='*60}")
    print(f"Running {description}")
    print(f"{'='*60}")
    
    # Capture test output
    test_output = StringIO()
    
    # Load and run the test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(test_module_name)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(
        stream=test_output,
        verbosity=2,
        failfast=False
    )
    
    start_time = time.time()
    result = runner.run(suite)
    end_time = time.time()
    
    # Print results
    output = test_output.getvalue()
    print(output)
    
    # Summary
    print(f"\nSummary for {description}:")
    print(f"  Tests run: {result.testsRun}")
    print(f"  Failures: {len(result.failures)}")
    print(f"  Errors: {len(result.errors)}")
    print(f"  Time: {end_time - start_time:.2f} seconds")
    
    if result.failures:
        print(f"  Failed tests:")
        for test, traceback in result.failures:
            print(f"    - {test}")
    
    if result.errors:
        print(f"  Error tests:")
        for test, traceback in result.errors:
            print(f"    - {test}")
    
    return result


def main():
    """Run all test suites."""
    print("HTML Table Generator - Comprehensive Test Suite")
    print("=" * 60)
    
    # Test suites to run
    test_suites = [
        ("tests.test_table_generator", "Core Functionality Tests"),
        ("tests.test_examples", "Usage Example Tests"),
        ("tests.test_performance", "Performance Tests")
    ]
    
    total_tests = 0
    total_failures = 0
    total_errors = 0
    total_time = 0
    
    overall_start = time.time()
    
    # Run each test suite
    for module_name, description in test_suites:
        try:
            result = run_test_suite(module_name, description)
            total_tests += result.testsRun
            total_failures += len(result.failures)
            total_errors += len(result.errors)
        except Exception as e:
            print(f"Error running {description}: {e}")
            total_errors += 1
    
    overall_end = time.time()
    total_time = overall_end - overall_start
    
    # Overall summary
    print(f"\n{'='*60}")
    print("OVERALL TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Total tests run: {total_tests}")
    print(f"Total failures: {total_failures}")
    print(f"Total errors: {total_errors}")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Success rate: {((total_tests - total_failures - total_errors) / total_tests * 100):.1f}%" if total_tests > 0 else "N/A")
    
    # Exit with appropriate code
    if total_failures > 0 or total_errors > 0:
        print(f"\n❌ Tests FAILED - {total_failures} failures, {total_errors} errors")
        sys.exit(1)
    else:
        print(f"\n✅ All tests PASSED!")
        sys.exit(0)


if __name__ == "__main__":
    main()
