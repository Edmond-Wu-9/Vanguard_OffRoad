import pandas as pd 

#def product_coverage(jobber_file, aces_file):

#Read the Jobber File 
jobber_df = pd.read_excel('jobber.xlsx', usecols=[2,4,5,6,7])
jobber_df = jobber_df.drop(index=[0,1])
jobber_df.columns = ["Part Number","Start Year","End Year","Make","Model"]
#print(jobber_df)

#Read the Aces File
aces_df = pd.read_excel('aces_ss.xlsx', usecols=[1,8,9,10,12])
aces_df.columns = ["Part Number","Year","Make","Model", "Submodel"]
aces_df = aces_df.drop(index=[0,1,2])
#print(aces_df)

#Filter out aces sheet with Part Number , Make, Model 
aces_grouped = aces_df.groupby(["Part Number" , "Make" , "Model", "Submodel"]).agg(years=("Year", list))

#Merge both jobber and aces file together 
merged_df = jobber_df.merge(aces_grouped, on=["Part Number","Make","Model"], how="left")

def get_unique_years(row):
  """
  Extracts unique years within the range specified by Start Year and End Year.
  Returns:
    list: A list of unique years within the specified range, handling different data types.
  """
  try:
    start_year = int(row["Start Year"])
    end_year = int(row["End Year"])
  except ValueError:
    print(f"WARNING: Invalid values for Start Year ({row['Start Year']}) or End Year ({row['End Year']}) in row {row.name}")
    return []  # Return an empty list if conversion fails

  return list(range(start_year, end_year + 1))


# Check for duplicate years and store in a new column
# Have to create a list in order to check for dups
def get_unique_years(row):
    return list(range(row["Start Year"], row["End Year"] + 1))

merged_df["Has Duplicates"] = merged_df.apply(
    lambda row: len(set(get_unique_years(row))) != len(get_unique_years(row)), axis=1
)

print(merged_df["Has Duplicates"])

# # Check for mismatch: jobber range not fully covered by ACES years
# merged_df["Mismatch"] = merged_df.apply(
#     lambda row: any(year not in row["unique_years"] for year in range(row["Year Start"], row["Year End"] + 1)), axis=1
# )

# # Highlight mismatched part numbers
# merged_df["ACES Coverage Mismatch"] = merged_df.apply(
#     lambda row: any(year not in get_unique_years(row) for year in row["year"]), axis=1
# )

# result_df = merged_df[["Part Number", "Start Year", "End Year", "Make", "Model", "Years", "Has Duplicates", "ACES Coverage Mismatch"]]
# result_df.columns = ["Part Number", "Start Year", "End Year", "Make", "Model", "Years", "Has Duplicates", "ACES Coverage Mismatch"]

# print(result_df)