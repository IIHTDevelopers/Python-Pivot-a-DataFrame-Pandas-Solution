import pandas as pd

class SalesAnalysis:
    def __init__(self, file_path):
        """Load CSV data into a Pandas DataFrame."""
        self.df = pd.read_csv(file_path)

    def display_head(self):
        """Return the first 5 rows of the DataFrame."""
        return self.df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.df.info()

    def pivot_and_summarize(self):
        """Pivot the DataFrame and compute multiple aggregate functions."""
        pivot_df = self.df.pivot_table(
            index="Category",
            values=["Units_Sold", "Price"],
            aggfunc={
                "Units_Sold": "sum",
                "Price": ["sum", "mean"]
            }
        )
        pivot_df["Total_Revenue"] = pivot_df["Units_Sold"]["sum"] * pivot_df["Price"]["mean"]
        pivot_df["Product_Count"] = self.df.groupby("Category")["Product_ID"].nunique()
        return pivot_df

    def export_updated_csv(self, output_file="summary_sales_data.csv"):
        """Save the summarized DataFrame to a new CSV file."""
        pivot_df = self.pivot_and_summarize()
        pivot_df.to_csv(output_file)
