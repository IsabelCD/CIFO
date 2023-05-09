import pandas as pd

####EXAM dataset####
# Define the column widths
col_widths = [8, 42, 4, 3]

# Define the column names
col_names = ['exam', 'description', 'duration', 'department']

# Read the text file
df_exam = pd.read_fwf('exams', widths=col_widths, names=col_names)

# Print the dataframe
#print(df_exam)
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


coincidences = {"C13563E1": ["C13571E1", "C13572E1"],
"LK44FAE1": ["LK44GAE1", "LK44SAE1"],
"LKC3FAE1": ["LKC3GAE1", "LKC3SAE1", "LKC3RAE1"],
"C81IAAE1": ["C81J1AE2", "C81J4AE2", "C81HAAE1"],
"C81HBAE1": ["C81IBAE1", "C81J1AE1", "C81J2AE1", "C81J3AE1"],
"C81HCAE1": ["C81ICAE1", "C81J2AE2" , "C81J4AE1", "C81J5AE1"],
"C81HDAE1": ["C81IDAE1", "C81J3AE2", "C81J5AE2"],
"C81MJAE1": ["C81MSAE1", "C82MCPE1"],
"C82BCSE1": ["C82BUAE1"],
"C82MHAE1": ["C82MJAE1"],
"R23102E1": ["R23104E1"],
"F12I01E1": ["F12X04E1", "F12X05E1"],
"F12O01E1": ["F12X04E2"],
"F12P01E1": ["F12P02E1", "F12P03E1", "F12X04E3"],
"F13I01E1": ["F13I02E1", "F13X01E1"],
"F13O01E1": ["F13O03E1"],
"F13X03E1": ["F13X04E1"],
"M11341E1": ["M11345E1"],
"M11343E1": ["M11347E1"],
"M12353E1": ["M13369E1"],
"H8A009E1": ["H8A011E1"],
"Q31301E1": ["Q3A301E1"],
"Q32302E1": ["Q3A303E1"],
"H22C20E1": ["H23C20E1", "H24C20E1", "H23CEOE1"],
"HG2J3BE1": ["HGCEMME1"],
"HG3J5AE1": ["HG3J5BE1"],
"HGCEMAE1": ["HGCEMBE1", "HGCEMCE1"],
"G5P002E1": ["C8CXESE1"],
"L31073E1": ["L31107E1"],
"V7A101E1": ["V7A117E1"],
"L11101E1": ["L11102E1"],
"L11110E1": ["L11111E1"],
"L11130E1": ["L11140E1"],
"M11351E1": [ "M11451E1"]
}


# Create a dictionary that maps each exam to a key based on the sub-lists in coincidences
exam_codes= merged['exam'].unique()

#isto muda o o exam column, eu quero criar uma nova e não mudar o exam
for key, values in coincidences.items():
    for value in values:
        merged.loc[merged['exam'] == value, 'exam'] = key

#depois é só dar um numero para cada valor unique dá com o ngroup em principio ou algo semelhante



####ROOMS####
rooms= {1: ['TRENT-HALL', 125],
        2: ['TRENT-L19', 80],
        3: ['TRENT-B46', 40],
        4: ['COPSE-2', 40],
        5: ['COPSE-3', 50],
        6: ['COPSE-4', 35],
        7: ['COPSE-5', 30],
        8: ['COPSE-6', 25],
        9: ['PRTLND-GRND', 200],
        10: ['POPE-A13', 80],
        11: ['POPE-A14', 80],
        12: ['ART-LECTURE', 80],
        13: ['ART-SEMINAR', 15],
        14: ['SPORT-LGE1', 250],
        15: ['SPORT-LGE2', 230],
        16: ['SPORT-SMALL', 270]}
