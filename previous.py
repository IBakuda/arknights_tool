already = {'orundum': 108100, 'originite': 211, 'headhuntingPermit': 51}

# Intermezzi
Intermezzi = {
    'darknights_memoir': 22 - 22,                  # 22 clear
    'a_walk_in_the_dark': 27 - 27,                 # 27 clear
    'under_tides': 28 - 28,                        # 28 clear
    'stultifera_navis': 36 - (8 * 2 + 4 + 11),     # 36
    'lone_trail': 40 - (16 + 8 * 2 + 8),           # 40
    'babel': 39 - (14 + 8 * 2 + 4 * 2 + 1),        # 39 clear
}
intermezzi = sum(Intermezzi.values())
print(f"intermezzi = {intermezzi}")

# Side Story
SideStory = {'grani_and_the_knights': 15 - 15,                    # 15 clear
             'Heart_of_surging_flame': 29 - 29,                   # 29 clear
             'code_of_brawl': 29 - (13 + 8 * 2),                  # 29 clear
             'twillight_of_woluminde': 32 - (15 + 8 * 2 + 1),     # 32 clear
             'the_great_chief_returns': 28 - (12 + 8 * 2),        # 28 clear
             'maria_nearl': 28 - (12 + 8 * 2),                    # 28 clear
             'mansfield_break': 27 - (11 + 8 * 2),                # 27 clear
             'who_is_real': 30 - (14 + 8 * 2),                    # 30 clear
             'dossoles_holiday': 40 - (15 + 8 * 2 + 9),           # 40 clear
             'near_light': 41 - (15 + 8 * 2 + 5 * 2),             # 42 clear
             'break_the_ice': 30 - (14 + 8 * 2),                  # 30 clear
             'invitation_to_wine': 28 - 28,                       # 28 clear
             'guide_ahead': 27 - (11 + 8 * 2),                    # 27 clear
             'lingering_echoes': 28 - (12 + 8 * 2),               # 28 clear
             'ideal_city': 37 - (12 + 8 * 2 + 4 * 2 + 1),         # 37 clear
             'dorothys_vision': 27 - (11 + 8 * 2),                # 27 clear
             'ii_siracusano': 40 - (14 + 8 * 2 + 5 * 2),          # 40 clear
             'where_vernal_wings_w_n_b': 29 - (29),               # 29 clear
             'what_the_fireling_casts': 0,                        # 29 clear
             'Operation_Lucent_Arrowhead': 0,                     # 29 clear
             'Here_A_People_Sows': 0,                             # 39 clear
             #'':,#
             }
sideStory = sum(SideStory.values())
print(f"sideStory = {sideStory}")

# MainTheme
MainTheme = {'m0': 29 - (11 * 2 + 7),           # 29 clear
             'm1': 25 - (10 * 2 + 5),           # 25 clear
             'm2': 36 - (10 * 2 + 16),          # 36 clear
             'm3': 24 - (8 * 2 + 8),            # 24 clear
             'm4': 30 - (10 * 2 + 10),          # 30 clear
             'm5': 34 - (10 * 2 + 14),          # 34 clear
             'm6': 40 - (13 * 2 + 11),          # 40
             'm7': 43 - (16 * 2 + 10),          # 43
             'm8': 44 - (16 * 2 + 13),          # 44
             'm9': 46 - (17 * 2 + 8),           # 46
             'm10': 38 - (16 * 2 + 6),          # 38
             'm11': 42 - (16 * 2 + 6),          # 42
             'm12': 44 - (17 * 2 + 6),          # 44
             'm13': 46 - (19 * 2 + 4),          # 46
             'm14': 48 - (18 * 2 + 8 + 4),      # 48 clear
             }
mainTheme = sum(MainTheme.values())
print(f"mainTheme = {mainTheme}")
for item in MainTheme.values():
    print(item)

last = (mainTheme + sideStory + intermezzi)
print(f"all that's left is to get {last}: in orundum = {last * 180}")
print()

print(f'mainTheme({mainTheme}) + '
      f'sideStory({sideStory}) + '
      f'intermezzi({intermezzi}) = '
      f'{mainTheme + sideStory + intermezzi}')

print(f'already have: {already['orundum']} + '
      f'originite: {already['originite']}({already['originite'] * 180}) = '
      f'{already['orundum'] + already['originite'] * 180}'
      f'({round(((already['orundum'] + already['originite'] * 180) / 600), 2)})')

print(round(((already['orundum'] + already['originite'] * 180) / 600), 2) + already['headhuntingPermit'])

print('-------------------------------')




