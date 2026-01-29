import pandas as pd

# Load RNA-seq count data
file_path = "/content/GSE60424_GEOSubmit_FC1to11_normalized_counts.txt.gz"

df = pd.read_csv(file_path, sep="\t", index_col=0)

# Show basic info
print("Shape of dataset:", df.shape)
print("\nFirst 5 genes:")
print(df.head())
