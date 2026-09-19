import unittest

from issue_boundary_evidence.extract import extract_packages, extract_stack_modules


class PackageExtractionTests(unittest.TestCase):
    def test_extracts_import_install_and_plugin_names(self):
        text = """
        import joblib
        from awkward_pandas.core import AwkwardExtensionArray
        pip install pytest-rerunfailures
        The OpenBLAS backend is active.
        """
        packages = extract_packages(text)
        self.assertIn("joblib", packages)
        self.assertIn("awkward_pandas", packages)
        self.assertIn("pytest-rerunfailures", packages)
        self.assertIn("OpenBLAS", packages)

    def test_extracts_stack_trace_package(self):
        text = 'File "/tmp/venv/lib/python3.13/site-packages/numpy/linalg/_linalg.py", line 10, in inv'
        self.assertIn("numpy", extract_stack_modules(text))

    def test_plain_prose_is_not_a_stack_trace(self):
        self.assertEqual(extract_stack_modules("This fails in a plugin and comes from the runtime."), [])


if __name__ == "__main__":
    unittest.main()
