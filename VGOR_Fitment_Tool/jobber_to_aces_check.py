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
aces_grouped.to_csv("findings.txt", index = False , sep='\t')
print("Results saved to: findings.txt")

#Merge both jobber and aces file together 
merged_df = jobber_df.merge(aces_grouped, on=["Part Number","Make","Model"], how="left")


