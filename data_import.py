import pandas as pd

####EXAM dataset####
# Define the column widths
col_widths = [8, 42, 4, 3]

# Define the column names
col_names = ['exam', 'description', 'duration', 'department']

# Read the text file
df_exam = pd.read_fwf('../exams', widths=col_widths, names=col_names)

# Print the dataframe
#print(df_exam)
#print([len(df_exam[a][1]) for a in col_names])
 


####STUDENTS dataset####
col_widths = [10, 4]
col_names = ['student', 'course']
df_st = pd.read_fwf('../students', widths=col_widths, names=col_names)
# Print the dataframe
#print(df_st)

#print([len(df_st[a][1]) for a in col_names])



####ENROLMENTS dataset##
col_widths = [10, 9]
col_names = ['student', 'exam']
df_en = pd.read_fwf('../enrolements', widths=col_widths, names=col_names)
# Print the dataframe
#print(df_en)

#print([len(df_en[a][1]) for a in col_names])


####COINCIDENCES####
coincidences = [["LK44FAE1", "LK44GAE1", "LK44SAE1"],
                ["LKC3FAE1", "LKC3GAE1", "LKC3SAE1", "LKC3RAE1"],
                ["C81IAAE1", "C81J1AE2", "C81J4AE2", "C81HAAE1"],
                ["C81HBAE1", "C81IBAE1", "C81J1AE1", "C81J2AE1", "C81J3AE1"],
                ["C81HCAE1", "C81ICAE1", "C81J2AE2" , "C81J4AE1", "C81J5AE1"],
                ["C81HDAE1", "C81IDAE1", "C81J3AE2", "C81J5AE2"],
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
                ["M11351E1",  "M11451E1"],
                ['Q4A106E1', "Q4A219E1"],
                ["K4C280E1", "K4C290E1"],
                ["D22227E1", "D23336E1"],
                ["Q82024E1", "Q82028E1"],
                ["G53LCTE1", "G5BSBBE1"],
                ["V12116E1", "V13111E1"],
                ["H3CFM3E1", "H3CTSEE1"],
                ["F321E4E1", "F331X5E1"],
                ["C81MJAE1", "C82MCPE1"],
                ["R4A119E1", "R4B107E1"],
                ["LK10KBE1","LKB2JAE1","LKB2SAE1"],
                ["LKA1IAE1","LKA1JAE1","LKA1RAE1"],
                ["M33036E1","M3B049E1","M3B062E1"],
                ["Q8B075E1","Q8B076E1","Q8B341E1"],
                ["B12320E1","B13103E1","D23315E1", "D23360E1"],
                ["F321C6E1","F321Q9E1","F331M9E1", "F331X3E1", "F331Z8E1"],
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

####HOURS####
hours = {
    0: {'day': '23-01-1995', 'time': '9:00', 'duration': 3},
    1: {'day': '23-01-1995', 'time': '13:30', 'duration': 3},
    2: {'day': '23-01-1995', 'time': '16:30', 'duration': 3},
    3: {'day': '24-01-1995', 'time': '9:00', 'duration': 3},
    4: {'day': '24-01-1995', 'time': '13:30', 'duration': 3},
    5: {'day': '24-01-1995', 'time': '16:30', 'duration': 3},
    6: {'day': '25-01-1995', 'time': '9:00', 'duration': 3},
    7: {'day': '25-01-1995', 'time': '13:30', 'duration': 3},
    8: {'day': '25-01-1995', 'time': '16:30', 'duration': 3},
    9: {'day': '26-01-1995', 'time': '9:00', 'duration': 3},
    10: {'day': '26-01-1995', 'time': '13:30', 'duration': 3},
    11: {'day': '26-01-1995', 'time': '16:30', 'duration': 3},
    12: {'day': '27-01-1995', 'time': '9:00', 'duration': 3},
    13: {'day': '27-01-1995', 'time': '13:30', 'duration': 3},
    14: {'day': '27-01-1995', 'time': '16:30', 'duration': 3},
    15: {'day': '28-01-1995', 'time': '9:00', 'duration': 3},
    16: {'day': '30-01-1995', 'time': '9:00', 'duration': 3},
    17: {'day': '30-01-1995', 'time': '13:30', 'duration': 3},
    18: {'day': '30-01-1995', 'time': '16:30', 'duration': 3},
    19: {'day': '31-01-1995', 'time': '9:00', 'duration': 3},
    20: {'day': '31-01-1995', 'time': '13:30', 'duration': 3},
    21: {'day': '31-01-1995', 'time': '16:30', 'duration': 3},
    22: {'day': '01-02-1995', 'time': '9:00', 'duration': 3},
    23: {'day': '01-02-1995', 'time': '13:30', 'duration': 3},
    24: {'day': '01-02-1995', 'time': '16:30', 'duration': 3},
    25: {'day': '02-02-1995', 'time': '9:00', 'duration': 3},
    26: {'day': '02-02-1995', 'time': '13:30', 'duration': 3},
    27: {'day': '02-02-1995', 'time': '16:30', 'duration': 3},
    28: {'day': '03-02-1995', 'time': '9:00', 'duration': 3},
    29: {'day': '03-02-1995', 'time': '13:30', 'duration': 3},
    30: {'day': '03-02-1995', 'time': '16:30', 'duration': 3},
    31: {'day': '04-02-1995', 'time': '9:00', 'duration': 3},
    32: {'day': '06-02-1995', 'time': '9:00', 'duration': 3},
    33: {'day': '06-02-1995', 'time': '13:30', 'duration': 3},
    34: {'day': '06-02-1995', 'time': '16:30', 'duration': 3},
    35: {'day': '07-02-1995', 'time': '9:00', 'duration': 3},
    36: {'day': '07-02-1995', 'time': '13:30', 'duration': 3},
    37: {'day': '07-02-1995', 'time': '16:30', 'duration': 3},
    38: {'day': '08-02-1995', 'time': '9:00', 'duration': 3},
    39: {'day': '08-02-1995', 'time': '13:30', 'duration': 3},
    40: {'day': '08-02-1995', 'time': '16:30', 'duration': 3},
    41: {'day': '09-02-1995', 'time': '9:00', 'duration': 3},
    42: {'day': '09-02-1995', 'time': '13:30', 'duration': 3},
    43: {'day': '09-02-1995', 'time': '16:30', 'duration': 3},
    44: {'day': '10-02-1995', 'time': '9:00', 'duration': 3},
    45: {'day': '10-02-1995', 'time': '13:30', 'duration': 3},
    46: {'day': '10-02-1995', 'time': '16:30', 'duration': 3},
    47: {'day': '11-02-1995', 'time': '9:00', 'duration': 3},
    48: {'day': '13-02-1995', 'time': '9:00', 'duration': 3},
    49: {'day': '13-02-1995', 'time': '13:30', 'duration': 3},
    50: {'day': '13-02-1995', 'time': '16:30', 'duration': 3},
}
hours_keys = {'23-01-1995': [0, 1, 2],
              '24-01-1995': [3, 4, 5],
              '25-01-1995': [6, 7, 8],
              '26-01-1995': [9, 10, 11],
              '27-01-1995': [12, 13, 14],
              '28-01-1995': [15],
              '30-01-1995': [16, 17, 18],
              '31-01-1995': [19, 20, 21],
              '01-02-1995': [22, 23, 24],
              '02-02-1995': [25, 26, 27],
              '03-02-1995': [28, 29, 30],
              '04-02-1995': [31],
              '06-02-1995': [32, 33, 34],
              '07-02-1995': [35, 36, 37],
              '08-02-1995': [38, 39, 40],
              '09-02-1995': [41, 42, 43],
              '10-02-1995': [44, 45, 46],
              '11-02-1995': [47],
              '13-02-1995': [48, 49, 50]}


