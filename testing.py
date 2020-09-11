import pandas as pd

df = pd.read_csv("test.csv")

better_cols = ['Last Name', 'First Name', 'Username', 'Student ID', 'Last Access', 'Availability', '01', 'V1', 'V2', 'V3', 'V4', 'F1', 'F2', 'F3', 'F4', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'A1', 'A2', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'P1', 'P2', 'P3', 'C1', 'C2', 'C3', 'C4', 'C5']

df.columns = better_cols

print(df)
