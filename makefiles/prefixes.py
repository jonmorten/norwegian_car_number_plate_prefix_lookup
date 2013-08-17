# -- coding: utf-8 --
import sqlite3
from sys import argv

script, db_file = argv
prefixes = [
    [
        ['AA', 'AB', 'AC'],
        ['AF', 'AH', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW'],
        ['AD', 'AE'],
        ['AJ', 'AK', 'AL', 'AN', 'AP'],
        ['AX', 'AY', 'AZ', 'BA', 'BB', 'FN']
    ],
    [
        ['BC', 'BD', 'BE', 'BF', 'BH', 'BJ', 'BK'],
        ['BL', 'BN', 'BP', 'BR', 'BS', 'BT', 'BU', 'BV', 'BX', 'BY', 'BZ', 'CA', 'CB'],
        ['CC', 'CE', 'CF', 'CH', 'CJ', 'CK', 'CL', 'CN', 'CP', 'CR', 'CS', 'CT', 'CU'],
        ['CV', 'CX', 'CY', 'CZ']
    ],
    [
        ['DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DH', 'DJ', 'DK', 'DL', 'DN', 'DP', 'DR', 'DS', 'DT', 'DU', 'DV', 'DX', 'DY', 'DZ', 'EA', 'EB', 'EC', 'ED', 'EE', 'EF', 'EH', 'EJ', 'EK', 'EN', 'EP', 'ER', 'ES', 'ET', 'EU', 'EV', 'EX', 'EY', 'EZ', 'FA', 'FB', 'FC', 'FD', 'FE']
    ],
    [
        ['FS', 'FT', 'FU', 'FV', 'FX', 'FY', 'FZ', 'HA'],
        ['HB', 'HC', 'HD', 'HE'],
        ['HF', 'HH'],
        ['HJ', 'HK', 'HL', 'HN', 'HP', 'HR']
    ],
    [
        ['HS', 'HT', 'HU', 'HV', 'HX'],
        ['HZ', 'JA', 'JB'],
        ['JC', 'JD', 'JE', 'JF', 'JH', 'JJ', 'JK', 'JL', 'JN', 'JP'],
        ['JR', 'JS', 'JT']
    ],
    [
        ['JU', 'JV', 'JX', 'JY', 'JZ', 'KA'],
        ['KB', 'KC', 'KD'],
        ['KE', 'KF', 'KH', 'KJ', 'KK', 'KL', 'KN', 'KP', 'KR', 'KS'],
        ['KT', 'KU', 'KV', 'KX', 'KY']
    ],
    [
        ['KZ', 'LA', 'LB', 'LC', 'LD'],
        ['LH', 'LJ', 'LK', 'LL', 'LN', 'LP', 'LR'],
        ['LS', 'LT', 'LU', 'LV', 'LX', 'NA', 'NB', 'NC'],
        ['LY', 'LZ']
    ],
    [
        ['ND', 'NE', 'NF', 'NH', 'NJ', 'NK', 'NL', 'NN', 'NP', 'NR', 'NT', 'NU'],
        ['NV', 'NX', 'NY', 'NZ'],
        ['PA', 'PB']
    ],
    [
        ['PC', 'PD', 'PE', 'PF', 'PH', 'PJ', 'PK'],
        ['PL', 'LF']
    ],
    [
        ['PN', 'PP', 'PR', 'PS', 'PT', 'PU', 'PV'],
        ['PX', 'PY', 'PZ', 'RC', 'RD'],
        ['RA', 'RB']
    ],
    [
        ['RE', 'RF', 'RH', 'RJ', 'RK', 'RL', 'RN', 'RP', 'RR', 'RS', 'RT', 'RU', 'RV', 'RX', 'RY'],
        ['RZ', 'SA', 'SB'],
        ['SC', 'SD', 'SE', 'SF', 'SH', 'SJ', 'SK', 'SL']
    ],
    [
        ['SN', 'SP', 'SR', 'SS', 'ST', 'SU', 'SV', 'SX', 'SY', 'SZ', 'TA', 'TB', 'TC', 'TD', 'TE'],
        ['TF', 'TH', 'TJ', 'TK'],
        ['TL', 'TN', 'TP', 'TR'],
        ['TS', 'TT', 'TU']
    ],
    [
        ['TV', 'TX', 'TY', 'TZ'],
        ['UA', 'UB'],
        ['UC', 'UD']
    ],
    [
        ['UE', 'UF', 'UH', 'UJ', 'UK', 'UL', 'UG'],
        ['UN', 'UP'],
        ['UR', 'US', 'UT', 'UU', 'UV'],
        ['UX', 'UY', 'UZ', 'VA'],
        ['VB', 'VC']
    ],
    [
        ['FP', 'VD', 'VE', 'VF', 'VH', 'VJ', 'VK', 'VL', 'VN', 'VP', 'VR'],
        ['VS', 'VT', 'VU', 'VV'],
        ['VX', 'VY', 'VZ'],
        ['XA', 'XB', 'XC']
    ],
    [
        ['XD', 'XE', 'XF', 'XH', 'XJ'],
        ['XK', 'XL'],
        ['XN', 'XP'],
        ['XR', 'XS', 'XT', 'XU']
    ],
    [
        ['XV', 'XX', 'XY', 'XZ'],
        ['YA', 'YB', 'YC', 'YD'],
        ['YE', 'YF', 'YH', 'YJ'],
        ['YK', 'YL'],
        ['YN', 'YP', 'YR', 'YS'],
        ['YT', 'YY'],
        ['YU', 'YV', 'YX']
    ],
    [
        ['FK'],
        ['YZ', 'ZA', 'ZB'],
        ['ZC', 'ZE', 'ZH', 'ZK', 'ZL'],
        ['ZN'],
        ['ZD', 'ZF', 'ZJ']
    ],
    [
        ['FR', 'LE', 'ZP', 'ZR'],
        ['ZS'],
        ['ZT', 'ZU', 'ZV', 'ZW', 'ZY'],
        ['ZX'],
        ['ZZ']
    ]
]

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

area_i = 1
for i in range(len(prefixes)):
    for ii in range(len(prefixes[i])):
        for iii in range(len(prefixes[i][ii])):
            input = "INSERT INTO prefix VALUES (null,'%s',%d,0)" % (prefixes[i][ii][iii], area_i)
            cursor.execute(input)
        area_i += 1

connection.commit()
connection.close()
