import unittest
import pandas as pd
from mainclass import SalesAnalysis
from test.TestUtils import TestUtils
import os


class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = SalesAnalysis("sales_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")

    def test_pivot_and_summarize(self):
        """Test if the DataFrame is pivoted and summarized correctly."""
        try:
            summary = self.analysis.pivot_and_summarize()
            obj = not summary.empty
            self.test_obj.yakshaAssert("TestPivotAndSummarize", obj, "functional")
            print("TestPivotAndSummarize = Passed" if obj else "TestPivotAndSummarize = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestPivotAndSummarize", False, "functional")
            print("TestPivotAndSummarize = Failed")

    def test_export_updated_csv(self):
        """Check if the updated CSV file is saved correctly."""
        self.analysis.export_updated_csv()
        try:
            pd.read_csv("summary_sales_data.csv")
            obj = True
        except FileNotFoundError:
            obj = False
        self.test_obj.yakshaAssert("TestExportUpdatedCSV", obj, "functional")
        print("TestExportUpdatedCSV = Passed" if obj else "TestExportUpdatedCSV = Failed")