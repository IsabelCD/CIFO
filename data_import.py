import pandas as pd

####EXAM dataset####
# Define the column widths
col_widths = [8, 42, 4, 3]

# Define the column names
col_names = ['exam', 'description', 'duration', 'department']

# Read the text file
df_exam = pd.read_fwf('exams', widths=col_widths, names=col_names)

# Print the dataframe
print(df_exam)
#print([len(df_exam[a][1]) for a in col_names])
 


####STUDENTS dataset####
col_widths = [10, 4]
col_names = ['student', 'course']
df_st = pd.read_fwf('students', widths=col_widths, names=col_names)
# Print the dataframe
#print(df_st)

#print([len(df_st[a][1]) for a in col_names])



####ENROLMENTS dataset##
col_widths = [10, 9]
col_names = ['student', 'exam']
df_en = pd.read_fwf('enrolements', widths=col_widths, names=col_names)
# Print the dataframe
#print(df_en)

#print([len(df_en[a][1]) for a in col_names])


####MERGING DATA####
merged= pd.merge(df_exam, df_en, how="inner", on='exam')
#print(merged)

####COINCIDENCES####
coincidences = [["C13563E1", "C13571E1", "C13572E1"],
                ["LK44FAE1", "LK44GAE1", "LK44SAE1"],
                ["LKC3FAE1", "LKC3GAE1", "LKC3SAE1", "LKC3RAE1"],
                ["C81IAAE1", "C81J1AE2", "C81J4AE2", "C81HAAE1"],
                ["C81HBAE1", "C81IBAE1", "C81J1AE1", "C81J2AE1", "C81J3AE1"],
                ["C81HCAE1", "C81ICAE1", "C81J2AE2" , "C81J4AE1", "C81J5AE1"],
                ["C81HDAE1", "C81IDAE1", "C81J3AE2", "C81J5AE2"],
                ["C81MJAE1", "C81MSAE1", "C82MCPE1"],
                ["C82BCSE1", "C82BUAE1"],
                ["C82MHAE1", "C82MJAE1"],
                ["R23102E1", "R23104E1"],
                ["F12I01E1", "F12X04E1", "F12X05E1"],
                ["F12O01E1", "F12X04E2"],
                ["F12P01E1", "F12P02E1", "F12P03E1", "F12X04E3"],
                ["F13I01E1", "F13I02E1", "F13X01E1"],
                ["F13O01E1", "F13O03E1"],
                ["F13X03E1", "F13X04E1"],
                ["M11341E1", "M11345E1"],
                ["M11343E1", "M11347E1"],
                ["M12353E1", "M13369E1"],
                ["H8A009E1", "H8A011E1"],
                ["Q31301E1", "Q3A301E1"],
                ["Q32302E1", "Q3A303E1"],
                ["H22C20E1", "H23C20E1", "H24C20E1", "H23CEOE1"],
                ["HG2J3BE1", "HGCEMME1"],
                ["HG3J5AE1", "HG3J5BE1"],
                ["HGCEMAE1", "HGCEMBE1", "HGCEMCE1"],
                ["G5P002E1", "C8CXESE1"],
                ["L31073E1", "L31107E1"],
                ["V7A101E1", "V7A117E1"],
                ["L11101E1", "L11102E1"],
                ["L11110E1", "L11111E1"],
                ["L11130E1", "L11140E1"],
                ["M11351E1",  "M11451E1"]
]




####ROOMS####
rooms= {0: ['TRENT-HALL', 125],
        1: ['TRENT-L19', 80],
        2: ['TRENT-B46', 40],
        3: ['COPSE-2', 40],
        4: ['COPSE-3', 50],
        5: ['COPSE-4', 35],
        6: ['COPSE-5', 30],
        7: ['COPSE-6', 25],
        8: ['PRTLND-GRND', 200],
        9: ['POPE-A13', 80],
        10: ['POPE-A14', 80],
        11: ['ART-LECTURE', 80],
        12: ['ART-SEMINAR', 15],
        13: ['SPORT-LGE1', 250],
        14: ['SPORT-LGE2', 230],
        15: ['SPORT-SMALL', 270]}
