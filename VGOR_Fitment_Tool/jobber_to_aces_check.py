import pandas as pd 

#def product_coverage(jobber_file, aces_file):

#Creates the Jobber Year Range 
def g(df):
    df['Jobber Year Range'] = df['Start Year'].astype(str) + ' - ' + df['End Year'].astype(str)
    return df

#Read the Jobber File 
jobber_df = pd.read_excel('jobber.xlsx', usecols=[2,4,5,6,7])
jobber_df = jobber_df.drop(index=[0,1])
jobber_df.columns = ["Part Number","Start Year","End Year","Make","Model"]
jobber_df = jobber_df.dropna(subset=["Start Year", "End Year"])
jobber_df = g(jobber_df)


#Read the Aces File
aces_df = pd.read_excel('aces_ss.xlsx', usecols=[1,8,9,10,12])
aces_df.columns = ["Part Number","Year","Make","Model", "Submodel"]
aces_df = aces_df.drop(index=[0,1,2])


#Merge both jobber and aces file together 
merged_df = pd.merge(aces_df, jobber_df[['Part Number','Make','Model','Jobber Year Range']], left_on=["Part Number", "Make", "Model"], right_on=["Part Number", "Make", "Model"],how='left')
merged_group = merged_df.groupby(["Part Number", "Make", "Model", "Submodel","Jobber Year Range"])['Year'].apply(list)
merged_group = merged_group.reset_index()
merged_group.columns = [["Part Number", "Make", "Model", "Submodel","Jobber Year Range","Year"]]
merged_group.to_excel("merged_data.xlsx", index=False)


# Check for duplicate years and store in a new column
# Have to create a list in order to check for dups
# def get_unique_years(row):
#    return list(range(row["Start Year"], row["End Year"] + 1))

# merged_df["Has Duplicates"] = merged_df.apply(
#    lambda row: len(set(get_unique_years(row))) == len(get_unique_years(row)), axis=1
# )

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