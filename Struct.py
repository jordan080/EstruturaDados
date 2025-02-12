class CovidLine:
  def __init__(self, ch, observation_date, province_state, country_region, last_update, confirmed, deaths, recovered):    
    self.ch = ch
    self.observation_date = observation_date
    self.province_state = province_state
    self.country_region = country_region
    self.last_update = last_update
    self.confirmed = confirmed
    self.deaths = deaths
    self.recovered = recovered

starwars = {
  "nodes": [
    {
      "name": "R2-D2",
      "value": 171,
      "colour": "#bde0f6"
    },
    {
      "name": "CHEWBACCA",
      "value": 145,
      "colour": "#A0522D"
    },
    {
      "name": "BB-8",
      "value": 40,
      "colour": "#eb5d00"
    },
    {
      "name": "QUI-GON",
      "value": 62,
      "colour": "#4f4fb1"
    },
    {
      "name": "NUTE GUNRAY",
      "value": 25,
      "colour": "#808080"
    },
    {
      "name": "PK-4",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "TC-14",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "OBI-WAN",
      "value": 148,
      "colour": "#48D1CC"
    },
    {
      "name": "DOFINE",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "RUNE",
      "value": 11,
      "colour": "#808080"
    },
    {
      "name": "TEY HOW",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "EMPEROR",
      "value": 52,
      "colour": "#191970"
    },
    {
      "name": "CAPTAIN PANAKA",
      "value": 20,
      "colour": "#808080"
    },
    {
      "name": "SIO BIBBLE",
      "value": 9,
      "colour": "#808080"
    },
    {
      "name": "JAR JAR",
      "value": 42,
      "colour": "#9a9a00"
    },
    {
      "name": "TARPALS",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "BOSS NASS",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "PADME",
      "value": 75,
      "colour": "#DDA0DD"
    },
    {
      "name": "RIC OLIE",
      "value": 12,
      "colour": "#808080"
    },
    {
      "name": "WATTO",
      "value": 9,
      "colour": "#808080"
    },
    {
      "name": "ANAKIN",
      "value": 132,
      "colour": "#ce3b59"
    },
    {
      "name": "SEBULBA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "JIRA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "SHMI",
      "value": 12,
      "colour": "#808080"
    },
    {
      "name": "C-3PO",
      "value": 151,
      "colour": "#FFD700"
    },
    {
      "name": "DARTH MAUL",
      "value": 6,
      "colour": "#808080"
    },
    {
      "name": "KITSTER",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "WALD",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "FODE/BEED",
      "value": 12,
      "colour": "#808080"
    },
    {
      "name": "JABBA",
      "value": 8,
      "colour": "#808080"
    },
    {
      "name": "GREEDO",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "VALORUM",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "MACE WINDU",
      "value": 23,
      "colour": "#808080"
    },
    {
      "name": "KI-ADI-MUNDI",
      "value": 7,
      "colour": "#808080"
    },
    {
      "name": "YODA",
      "value": 46,
      "colour": "#9ACD32"
    },
    {
      "name": "RABE",
      "value": 3,
      "colour": "#808080"
    },
    {
      "name": "BAIL ORGANA",
      "value": 24,
      "colour": "#808080"
    },
    {
      "name": "GENERAL CEEL",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "BRAVO TWO",
      "value": 6,
      "colour": "#808080"
    },
    {
      "name": "BRAVO THREE",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "CAPTAIN TYPHO",
      "value": 7,
      "colour": "#808080"
    },
    {
      "name": "SENATOR ASK AAK",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "ORN FREE TAA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "SOLA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "JOBAL",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "RUWEE",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "TAUN WE",
      "value": 8,
      "colour": "#808080"
    },
    {
      "name": "LAMA SU",
      "value": 9,
      "colour": "#808080"
    },
    {
      "name": "BOBA FETT",
      "value": 11,
      "colour": "#808080"
    },
    {
      "name": "JANGO FETT",
      "value": 6,
      "colour": "#808080"
    },
    {
      "name": "OWEN",
      "value": 11,
      "colour": "#808080"
    },
    {
      "name": "BERU",
      "value": 7,
      "colour": "#808080"
    },
    {
      "name": "CLIEGG",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "COUNT DOOKU",
      "value": 10,
      "colour": "#808080"
    },
    {
      "name": "SUN RIT",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "POGGLE",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "PLO KOON",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "ODD BALL",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "GENERAL GRIEVOUS",
      "value": 13,
      "colour": "#808080"
    },
    {
      "name": "FANG ZAR",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "MON MOTHMA",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "GIDDEAN DANU",
      "value": 3,
      "colour": "#808080"
    },
    {
      "name": "CLONE COMMANDER GREE",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "CLONE COMMANDER CODY",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "TION MEDON",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "CAPTAIN ANTILLES",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "DARTH VADER",
      "value": 59,
      "colour": "#000000"
    },
    {
      "name": "LUKE",
      "value": 161,
      "colour": "#3881e5"
    },
    {
      "name": "CAMIE",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "BIGGS",
      "value": 19,
      "colour": "#808080"
    },
    {
      "name": "LEIA",
      "value": 99,
      "colour": "#DCDCDC"
    },
    {
      "name": "MOTTI",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "TARKIN",
      "value": 13,
      "colour": "#808080"
    },
    {
      "name": "HAN",
      "value": 170,
      "colour": "#ff9400"
    },
    {
      "name": "DODONNA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "GOLD LEADER",
      "value": 15,
      "colour": "#808080"
    },
    {
      "name": "WEDGE",
      "value": 29,
      "colour": "#808080"
    },
    {
      "name": "RED LEADER",
      "value": 34,
      "colour": "#808080"
    },
    {
      "name": "RED TEN",
      "value": 9,
      "colour": "#808080"
    },
    {
      "name": "GOLD FIVE",
      "value": 9,
      "colour": "#808080"
    },
    {
      "name": "RIEEKAN",
      "value": 8,
      "colour": "#808080"
    },
    {
      "name": "DERLIN",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "ZEV",
      "value": 7,
      "colour": "#808080"
    },
    {
      "name": "PIETT",
      "value": 13,
      "colour": "#808080"
    },
    {
      "name": "OZZEL",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "DACK",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "JANSON",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "NEEDA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "LANDO",
      "value": 42,
      "colour": "#808080"
    },
    {
      "name": "JERJERROD",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "BIB FORTUNA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "BOUSHH",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "ADMIRAL ACKBAR",
      "value": 13,
      "colour": "#808080"
    },
    {
      "name": "LOR SAN TEKKA",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "POE",
      "value": 31,
      "colour": "#a15bea"
    },
    {
      "name": "KYLO REN",
      "value": 23,
      "colour": "#000000"
    },
    {
      "name": "CAPTAIN PHASMA",
      "value": 7,
      "colour": "#808080"
    },
    {
      "name": "FINN",
      "value": 64,
      "colour": "#07b19f"
    },
    {
      "name": "UNKAR PLUTT",
      "value": 6,
      "colour": "#808080"
    },
    {
      "name": "REY",
      "value": 57,
      "colour": "#ffe0af"
    },
    {
      "name": "GENERAL HUX",
      "value": 15,
      "colour": "#808080"
    },
    {
      "name": "LIEUTENANT MITAKA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "BALA-TIK",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "SNOKE",
      "value": 5,
      "colour": "#191970"
    },
    {
      "name": "MAZ",
      "value": 7,
      "colour": "#808080"
    },
    {
      "name": "SNAP",
      "value": 6,
      "colour": "#808080"
    },
    {
      "name": "ADMIRAL STATURA",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "YOLO ZIFF",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "COLONEL DATOO",
      "value": 4,
      "colour": "#808080"
    },
    {
      "name": "ELLO ASTY",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "JESS",
      "value": 5,
      "colour": "#808080"
    },
    {
      "name": "NIV LEK",
      "value": 4,
      "colour": "#808080"
    }
  ],
  "links": [
    {
      "source": 1,
      "target": 0,
      "value": 17
    },
    {
      "source": 2,
      "target": 0,
      "value": 2
    },
    {
      "source": 2,
      "target": 1,
      "value": 8
    },
    {
      "source": 7,
      "target": 0,
      "value": 28
    },
    {
      "source": 17,
      "target": 0,
      "value": 24
    },
    {
      "source": 3,
      "target": 0,
      "value": 13
    },
    {
      "source": 20,
      "target": 0,
      "value": 30
    },
    {
      "source": 0,
      "target": 19,
      "value": 3
    },
    {
      "source": 24,
      "target": 0,
      "value": 55
    },
    {
      "source": 26,
      "target": 0,
      "value": 2
    },
    {
      "source": 29,
      "target": 0,
      "value": 4
    },
    {
      "source": 11,
      "target": 0,
      "value": 5
    },
    {
      "source": 40,
      "target": 0,
      "value": 1
    },
    {
      "source": 51,
      "target": 0,
      "value": 1
    },
    {
      "source": 50,
      "target": 0,
      "value": 2
    },
    {
      "source": 36,
      "target": 0,
      "value": 3
    },
    {
      "source": 0,
      "target": 34,
      "value": 5
    },
    {
      "source": 67,
      "target": 0,
      "value": 34
    },
    {
      "source": 70,
      "target": 0,
      "value": 23
    },
    {
      "source": 65,
      "target": 0,
      "value": 1
    },
    {
      "source": 69,
      "target": 0,
      "value": 1
    },
    {
      "source": 66,
      "target": 0,
      "value": 2
    },
    {
      "source": 73,
      "target": 0,
      "value": 18
    },
    {
      "source": 88,
      "target": 0,
      "value": 5
    },
    {
      "source": 1,
      "target": 7,
      "value": 6
    },
    {
      "source": 24,
      "target": 1,
      "value": 39
    },
    {
      "source": 1,
      "target": 67,
      "value": 32
    },
    {
      "source": 1,
      "target": 73,
      "value": 77
    },
    {
      "source": 1,
      "target": 29,
      "value": 3
    },
    {
      "source": 1,
      "target": 70,
      "value": 48
    },
    {
      "source": 1,
      "target": 66,
      "value": 2
    },
    {
      "source": 1,
      "target": 80,
      "value": 1
    },
    {
      "source": 1,
      "target": 88,
      "value": 20
    },
    {
      "source": 48,
      "target": 1,
      "value": 2
    },
    {
      "source": 1,
      "target": 97,
      "value": 20
    },
    {
      "source": 1,
      "target": 99,
      "value": 13
    },
    {
      "source": 102,
      "target": 1,
      "value": 1
    },
    {
      "source": 1,
      "target": 104,
      "value": 2
    },
    {
      "source": 1,
      "target": 94,
      "value": 2
    },
    {
      "source": 1,
      "target": 95,
      "value": 3
    },
    {
      "source": 96,
      "target": 1,
      "value": 1
    },
    {
      "source": 2,
      "target": 94,
      "value": 8
    },
    {
      "source": 2,
      "target": 93,
      "value": 2
    },
    {
      "source": 2,
      "target": 99,
      "value": 17
    },
    {
      "source": 2,
      "target": 98,
      "value": 1
    },
    {
      "source": 2,
      "target": 97,
      "value": 15
    },
    {
      "source": 2,
      "target": 73,
      "value": 9
    },
    {
      "source": 102,
      "target": 2,
      "value": 1
    },
    {
      "source": 2,
      "target": 104,
      "value": 3
    },
    {
      "source": 2,
      "target": 70,
      "value": 3
    },
    {
      "source": 2,
      "target": 24,
      "value": 3
    },
    {
      "source": 4,
      "target": 3,
      "value": 1
    },
    {
      "source": 5,
      "target": 6,
      "value": 1
    },
    {
      "source": 7,
      "target": 6,
      "value": 1
    },
    {
      "source": 3,
      "target": 6,
      "value": 1
    },
    {
      "source": 7,
      "target": 3,
      "value": 26
    },
    {
      "source": 4,
      "target": 6,
      "value": 1
    },
    {
      "source": 8,
      "target": 4,
      "value": 1
    },
    {
      "source": 8,
      "target": 6,
      "value": 1
    },
    {
      "source": 4,
      "target": 9,
      "value": 8
    },
    {
      "source": 9,
      "target": 10,
      "value": 2
    },
    {
      "source": 4,
      "target": 10,
      "value": 1
    },
    {
      "source": 12,
      "target": 11,
      "value": 3
    },
    {
      "source": 11,
      "target": 13,
      "value": 1
    },
    {
      "source": 12,
      "target": 13,
      "value": 3
    },
    {
      "source": 14,
      "target": 3,
      "value": 22
    },
    {
      "source": 14,
      "target": 7,
      "value": 15
    },
    {
      "source": 14,
      "target": 15,
      "value": 2
    },
    {
      "source": 16,
      "target": 3,
      "value": 2
    },
    {
      "source": 16,
      "target": 7,
      "value": 2
    },
    {
      "source": 16,
      "target": 14,
      "value": 2
    },
    {
      "source": 11,
      "target": 4,
      "value": 6
    },
    {
      "source": 11,
      "target": 9,
      "value": 3
    },
    {
      "source": 4,
      "target": 13,
      "value": 2
    },
    {
      "source": 14,
      "target": 13,
      "value": 1
    },
    {
      "source": 12,
      "target": 14,
      "value": 7
    },
    {
      "source": 3,
      "target": 13,
      "value": 2
    },
    {
      "source": 12,
      "target": 3,
      "value": 9
    },
    {
      "source": 12,
      "target": 17,
      "value": 7
    },
    {
      "source": 17,
      "target": 3,
      "value": 16
    },
    {
      "source": 17,
      "target": 13,
      "value": 1
    },
    {
      "source": 12,
      "target": 7,
      "value": 7
    },
    {
      "source": 7,
      "target": 18,
      "value": 3
    },
    {
      "source": 14,
      "target": 18,
      "value": 1
    },
    {
      "source": 3,
      "target": 18,
      "value": 2
    },
    {
      "source": 12,
      "target": 18,
      "value": 2
    },
    {
      "source": 14,
      "target": 17,
      "value": 10
    },
    {
      "source": 3,
      "target": 19,
      "value": 6
    },
    {
      "source": 20,
      "target": 19,
      "value": 5
    },
    {
      "source": 17,
      "target": 19,
      "value": 3
    },
    {
      "source": 20,
      "target": 3,
      "value": 22
    },
    {
      "source": 20,
      "target": 17,
      "value": 41
    },
    {
      "source": 14,
      "target": 21,
      "value": 2
    },
    {
      "source": 20,
      "target": 21,
      "value": 2
    },
    {
      "source": 3,
      "target": 21,
      "value": 2
    },
    {
      "source": 17,
      "target": 21,
      "value": 2
    },
    {
      "source": 20,
      "target": 14,
      "value": 12
    },
    {
      "source": 20,
      "target": 22,
      "value": 2
    },
    {
      "source": 22,
      "target": 3,
      "value": 2
    },
    {
      "source": 22,
      "target": 17,
      "value": 1
    },
    {
      "source": 20,
      "target": 23,
      "value": 8
    },
    {
      "source": 14,
      "target": 23,
      "value": 3
    },
    {
      "source": 3,
      "target": 23,
      "value": 8
    },
    {
      "source": 17,
      "target": 23,
      "value": 5
    },
    {
      "source": 20,
      "target": 24,
      "value": 10
    },
    {
      "source": 24,
      "target": 17,
      "value": 12
    },
    {
      "source": 7,
      "target": 13,
      "value": 1
    },
    {
      "source": 25,
      "target": 11,
      "value": 3
    },
    {
      "source": 20,
      "target": 26,
      "value": 3
    },
    {
      "source": 20,
      "target": 27,
      "value": 2
    },
    {
      "source": 26,
      "target": 27,
      "value": 1
    },
    {
      "source": 14,
      "target": 26,
      "value": 1
    },
    {
      "source": 26,
      "target": 3,
      "value": 2
    },
    {
      "source": 14,
      "target": 27,
      "value": 1
    },
    {
      "source": 3,
      "target": 27,
      "value": 2
    },
    {
      "source": 20,
      "target": 7,
      "value": 46
    },
    {
      "source": 7,
      "target": 23,
      "value": 1
    },
    {
      "source": 24,
      "target": 19,
      "value": 1
    },
    {
      "source": 26,
      "target": 19,
      "value": 1
    },
    {
      "source": 24,
      "target": 3,
      "value": 1
    },
    {
      "source": 24,
      "target": 26,
      "value": 1
    },
    {
      "source": 26,
      "target": 17,
      "value": 1
    },
    {
      "source": 28,
      "target": 29,
      "value": 1
    },
    {
      "source": 29,
      "target": 23,
      "value": 1
    },
    {
      "source": 21,
      "target": 23,
      "value": 1
    },
    {
      "source": 20,
      "target": 29,
      "value": 1
    },
    {
      "source": 29,
      "target": 14,
      "value": 1
    },
    {
      "source": 29,
      "target": 17,
      "value": 1
    },
    {
      "source": 29,
      "target": 21,
      "value": 1
    },
    {
      "source": 29,
      "target": 3,
      "value": 1
    },
    {
      "source": 28,
      "target": 14,
      "value": 2
    },
    {
      "source": 28,
      "target": 17,
      "value": 1
    },
    {
      "source": 30,
      "target": 3,
      "value": 1
    },
    {
      "source": 20,
      "target": 30,
      "value": 1
    },
    {
      "source": 30,
      "target": 27,
      "value": 1
    },
    {
      "source": 26,
      "target": 23,
      "value": 1
    },
    {
      "source": 20,
      "target": 12,
      "value": 2
    },
    {
      "source": 20,
      "target": 18,
      "value": 4
    },
    {
      "source": 11,
      "target": 31,
      "value": 2
    },
    {
      "source": 11,
      "target": 14,
      "value": 5
    },
    {
      "source": 11,
      "target": 3,
      "value": 1
    },
    {
      "source": 14,
      "target": 31,
      "value": 1
    },
    {
      "source": 3,
      "target": 31,
      "value": 1
    },
    {
      "source": 32,
      "target": 3,
      "value": 2
    },
    {
      "source": 33,
      "target": 3,
      "value": 2
    },
    {
      "source": 3,
      "target": 34,
      "value": 3
    },
    {
      "source": 3,
      "target": 35,
      "value": 1
    },
    {
      "source": 33,
      "target": 32,
      "value": 4
    },
    {
      "source": 32,
      "target": 34,
      "value": 16
    },
    {
      "source": 20,
      "target": 32,
      "value": 9
    },
    {
      "source": 32,
      "target": 35,
      "value": 1
    },
    {
      "source": 33,
      "target": 34,
      "value": 4
    },
    {
      "source": 20,
      "target": 33,
      "value": 2
    },
    {
      "source": 33,
      "target": 35,
      "value": 1
    },
    {
      "source": 20,
      "target": 34,
      "value": 9
    },
    {
      "source": 35,
      "target": 34,
      "value": 1
    },
    {
      "source": 20,
      "target": 35,
      "value": 1
    },
    {
      "source": 36,
      "target": 11,
      "value": 6
    },
    {
      "source": 36,
      "target": 31,
      "value": 1
    },
    {
      "source": 7,
      "target": 34,
      "value": 20
    },
    {
      "source": 32,
      "target": 7,
      "value": 9
    },
    {
      "source": 33,
      "target": 7,
      "value": 1
    },
    {
      "source": 16,
      "target": 17,
      "value": 2
    },
    {
      "source": 25,
      "target": 4,
      "value": 3
    },
    {
      "source": 20,
      "target": 16,
      "value": 1
    },
    {
      "source": 16,
      "target": 12,
      "value": 1
    },
    {
      "source": 7,
      "target": 17,
      "value": 9
    },
    {
      "source": 11,
      "target": 37,
      "value": 1
    },
    {
      "source": 37,
      "target": 4,
      "value": 1
    },
    {
      "source": 25,
      "target": 37,
      "value": 1
    },
    {
      "source": 25,
      "target": 9,
      "value": 1
    },
    {
      "source": 38,
      "target": 18,
      "value": 4
    },
    {
      "source": 20,
      "target": 38,
      "value": 2
    },
    {
      "source": 37,
      "target": 14,
      "value": 1
    },
    {
      "source": 4,
      "target": 17,
      "value": 2
    },
    {
      "source": 8,
      "target": 10,
      "value": 1
    },
    {
      "source": 39,
      "target": 38,
      "value": 2
    },
    {
      "source": 39,
      "target": 18,
      "value": 2
    },
    {
      "source": 20,
      "target": 39,
      "value": 1
    },
    {
      "source": 11,
      "target": 17,
      "value": 5
    },
    {
      "source": 11,
      "target": 41,
      "value": 2
    },
    {
      "source": 11,
      "target": 42,
      "value": 2
    },
    {
      "source": 42,
      "target": 41,
      "value": 1
    },
    {
      "source": 11,
      "target": 32,
      "value": 3
    },
    {
      "source": 11,
      "target": 34,
      "value": 2
    },
    {
      "source": 11,
      "target": 33,
      "value": 1
    },
    {
      "source": 36,
      "target": 32,
      "value": 2
    },
    {
      "source": 36,
      "target": 34,
      "value": 8
    },
    {
      "source": 36,
      "target": 33,
      "value": 1
    },
    {
      "source": 40,
      "target": 14,
      "value": 1
    },
    {
      "source": 40,
      "target": 7,
      "value": 2
    },
    {
      "source": 20,
      "target": 40,
      "value": 3
    },
    {
      "source": 7,
      "target": 5,
      "value": 1
    },
    {
      "source": 20,
      "target": 13,
      "value": 1
    },
    {
      "source": 17,
      "target": 43,
      "value": 1
    },
    {
      "source": 20,
      "target": 43,
      "value": 1
    },
    {
      "source": 44,
      "target": 43,
      "value": 2
    },
    {
      "source": 45,
      "target": 43,
      "value": 1
    },
    {
      "source": 44,
      "target": 17,
      "value": 1
    },
    {
      "source": 17,
      "target": 45,
      "value": 1
    },
    {
      "source": 20,
      "target": 44,
      "value": 1
    },
    {
      "source": 20,
      "target": 45,
      "value": 3
    },
    {
      "source": 44,
      "target": 45,
      "value": 1
    },
    {
      "source": 7,
      "target": 46,
      "value": 5
    },
    {
      "source": 47,
      "target": 46,
      "value": 2
    },
    {
      "source": 47,
      "target": 7,
      "value": 6
    },
    {
      "source": 48,
      "target": 46,
      "value": 2
    },
    {
      "source": 48,
      "target": 49,
      "value": 3
    },
    {
      "source": 48,
      "target": 7,
      "value": 1
    },
    {
      "source": 49,
      "target": 46,
      "value": 1
    },
    {
      "source": 49,
      "target": 7,
      "value": 1
    },
    {
      "source": 24,
      "target": 50,
      "value": 4
    },
    {
      "source": 51,
      "target": 24,
      "value": 3
    },
    {
      "source": 24,
      "target": 52,
      "value": 1
    },
    {
      "source": 20,
      "target": 50,
      "value": 3
    },
    {
      "source": 20,
      "target": 51,
      "value": 1
    },
    {
      "source": 20,
      "target": 52,
      "value": 2
    },
    {
      "source": 51,
      "target": 50,
      "value": 4
    },
    {
      "source": 50,
      "target": 17,
      "value": 4
    },
    {
      "source": 52,
      "target": 50,
      "value": 2
    },
    {
      "source": 51,
      "target": 17,
      "value": 1
    },
    {
      "source": 51,
      "target": 52,
      "value": 1
    },
    {
      "source": 52,
      "target": 17,
      "value": 2
    },
    {
      "source": 36,
      "target": 7,
      "value": 8
    },
    {
      "source": 11,
      "target": 7,
      "value": 5
    },
    {
      "source": 7,
      "target": 41,
      "value": 1
    },
    {
      "source": 36,
      "target": 41,
      "value": 1
    },
    {
      "source": 36,
      "target": 14,
      "value": 1
    },
    {
      "source": 41,
      "target": 34,
      "value": 1
    },
    {
      "source": 14,
      "target": 34,
      "value": 1
    },
    {
      "source": 32,
      "target": 41,
      "value": 1
    },
    {
      "source": 14,
      "target": 32,
      "value": 1
    },
    {
      "source": 14,
      "target": 41,
      "value": 1
    },
    {
      "source": 32,
      "target": 17,
      "value": 2
    },
    {
      "source": 14,
      "target": 42,
      "value": 1
    },
    {
      "source": 53,
      "target": 17,
      "value": 3
    },
    {
      "source": 53,
      "target": 49,
      "value": 1
    },
    {
      "source": 55,
      "target": 54,
      "value": 2
    },
    {
      "source": 4,
      "target": 54,
      "value": 2
    },
    {
      "source": 4,
      "target": 55,
      "value": 2
    },
    {
      "source": 7,
      "target": 54,
      "value": 1
    },
    {
      "source": 7,
      "target": 55,
      "value": 1
    },
    {
      "source": 4,
      "target": 7,
      "value": 1
    },
    {
      "source": 53,
      "target": 7,
      "value": 3
    },
    {
      "source": 20,
      "target": 54,
      "value": 1
    },
    {
      "source": 20,
      "target": 55,
      "value": 1
    },
    {
      "source": 20,
      "target": 4,
      "value": 1
    },
    {
      "source": 20,
      "target": 53,
      "value": 3
    },
    {
      "source": 17,
      "target": 54,
      "value": 1
    },
    {
      "source": 53,
      "target": 54,
      "value": 1
    },
    {
      "source": 17,
      "target": 55,
      "value": 1
    },
    {
      "source": 53,
      "target": 55,
      "value": 1
    },
    {
      "source": 53,
      "target": 4,
      "value": 1
    },
    {
      "source": 53,
      "target": 32,
      "value": 2
    },
    {
      "source": 33,
      "target": 56,
      "value": 1
    },
    {
      "source": 53,
      "target": 34,
      "value": 2
    },
    {
      "source": 17,
      "target": 34,
      "value": 1
    },
    {
      "source": 53,
      "target": 11,
      "value": 2
    },
    {
      "source": 7,
      "target": 57,
      "value": 2
    },
    {
      "source": 20,
      "target": 57,
      "value": 2
    },
    {
      "source": 20,
      "target": 11,
      "value": 14
    },
    {
      "source": 58,
      "target": 7,
      "value": 2
    },
    {
      "source": 20,
      "target": 58,
      "value": 1
    },
    {
      "source": 20,
      "target": 36,
      "value": 2
    },
    {
      "source": 24,
      "target": 7,
      "value": 9
    },
    {
      "source": 24,
      "target": 11,
      "value": 2
    },
    {
      "source": 36,
      "target": 24,
      "value": 3
    },
    {
      "source": 36,
      "target": 17,
      "value": 5
    },
    {
      "source": 36,
      "target": 59,
      "value": 2
    },
    {
      "source": 36,
      "target": 60,
      "value": 2
    },
    {
      "source": 36,
      "target": 61,
      "value": 1
    },
    {
      "source": 59,
      "target": 17,
      "value": 2
    },
    {
      "source": 59,
      "target": 60,
      "value": 2
    },
    {
      "source": 59,
      "target": 61,
      "value": 1
    },
    {
      "source": 60,
      "target": 17,
      "value": 2
    },
    {
      "source": 61,
      "target": 17,
      "value": 1
    },
    {
      "source": 61,
      "target": 60,
      "value": 1
    },
    {
      "source": 40,
      "target": 17,
      "value": 2
    },
    {
      "source": 24,
      "target": 40,
      "value": 2
    },
    {
      "source": 62,
      "target": 34,
      "value": 1
    },
    {
      "source": 63,
      "target": 7,
      "value": 2
    },
    {
      "source": 7,
      "target": 64,
      "value": 1
    },
    {
      "source": 58,
      "target": 4,
      "value": 1
    },
    {
      "source": 20,
      "target": 63,
      "value": 1
    },
    {
      "source": 63,
      "target": 32,
      "value": 1
    },
    {
      "source": 63,
      "target": 34,
      "value": 1
    },
    {
      "source": 36,
      "target": 65,
      "value": 2
    },
    {
      "source": 36,
      "target": 3,
      "value": 1
    },
    {
      "source": 24,
      "target": 34,
      "value": 1
    },
    {
      "source": 66,
      "target": 11,
      "value": 7
    },
    {
      "source": 24,
      "target": 65,
      "value": 1
    },
    {
      "source": 68,
      "target": 67,
      "value": 2
    },
    {
      "source": 69,
      "target": 68,
      "value": 2
    },
    {
      "source": 69,
      "target": 67,
      "value": 4
    },
    {
      "source": 66,
      "target": 70,
      "value": 2
    },
    {
      "source": 51,
      "target": 67,
      "value": 3
    },
    {
      "source": 67,
      "target": 50,
      "value": 3
    },
    {
      "source": 24,
      "target": 67,
      "value": 29
    },
    {
      "source": 24,
      "target": 70,
      "value": 49
    },
    {
      "source": 70,
      "target": 67,
      "value": 26
    },
    {
      "source": 51,
      "target": 70,
      "value": 1
    },
    {
      "source": 67,
      "target": 7,
      "value": 22
    },
    {
      "source": 70,
      "target": 7,
      "value": 1
    },
    {
      "source": 71,
      "target": 72,
      "value": 2
    },
    {
      "source": 66,
      "target": 71,
      "value": 1
    },
    {
      "source": 66,
      "target": 72,
      "value": 7
    },
    {
      "source": 73,
      "target": 7,
      "value": 10
    },
    {
      "source": 73,
      "target": 67,
      "value": 43
    },
    {
      "source": 30,
      "target": 73,
      "value": 1
    },
    {
      "source": 73,
      "target": 29,
      "value": 1
    },
    {
      "source": 24,
      "target": 73,
      "value": 54
    },
    {
      "source": 70,
      "target": 71,
      "value": 1
    },
    {
      "source": 70,
      "target": 72,
      "value": 1
    },
    {
      "source": 73,
      "target": 70,
      "value": 69
    },
    {
      "source": 66,
      "target": 7,
      "value": 1
    },
    {
      "source": 74,
      "target": 75,
      "value": 1
    },
    {
      "source": 74,
      "target": 76,
      "value": 1
    },
    {
      "source": 74,
      "target": 67,
      "value": 1
    },
    {
      "source": 75,
      "target": 76,
      "value": 1
    },
    {
      "source": 75,
      "target": 67,
      "value": 1
    },
    {
      "source": 67,
      "target": 76,
      "value": 4
    },
    {
      "source": 69,
      "target": 70,
      "value": 1
    },
    {
      "source": 70,
      "target": 77,
      "value": 1
    },
    {
      "source": 67,
      "target": 77,
      "value": 3
    },
    {
      "source": 69,
      "target": 77,
      "value": 3
    },
    {
      "source": 69,
      "target": 24,
      "value": 1
    },
    {
      "source": 24,
      "target": 77,
      "value": 1
    },
    {
      "source": 77,
      "target": 76,
      "value": 3
    },
    {
      "source": 75,
      "target": 77,
      "value": 1
    },
    {
      "source": 69,
      "target": 76,
      "value": 2
    },
    {
      "source": 77,
      "target": 78,
      "value": 1
    },
    {
      "source": 69,
      "target": 75,
      "value": 1
    },
    {
      "source": 67,
      "target": 78,
      "value": 1
    },
    {
      "source": 73,
      "target": 80,
      "value": 3
    },
    {
      "source": 70,
      "target": 80,
      "value": 4
    },
    {
      "source": 24,
      "target": 81,
      "value": 1
    },
    {
      "source": 73,
      "target": 82,
      "value": 1
    },
    {
      "source": 24,
      "target": 80,
      "value": 1
    },
    {
      "source": 84,
      "target": 83,
      "value": 2
    },
    {
      "source": 66,
      "target": 83,
      "value": 8
    },
    {
      "source": 66,
      "target": 84,
      "value": 2
    },
    {
      "source": 81,
      "target": 70,
      "value": 1
    },
    {
      "source": 85,
      "target": 67,
      "value": 3
    },
    {
      "source": 86,
      "target": 76,
      "value": 2
    },
    {
      "source": 67,
      "target": 82,
      "value": 1
    },
    {
      "source": 66,
      "target": 87,
      "value": 1
    },
    {
      "source": 87,
      "target": 83,
      "value": 1
    },
    {
      "source": 67,
      "target": 34,
      "value": 6
    },
    {
      "source": 48,
      "target": 83,
      "value": 1
    },
    {
      "source": 48,
      "target": 66,
      "value": 3
    },
    {
      "source": 73,
      "target": 88,
      "value": 12
    },
    {
      "source": 88,
      "target": 70,
      "value": 12
    },
    {
      "source": 24,
      "target": 88,
      "value": 8
    },
    {
      "source": 66,
      "target": 88,
      "value": 4
    },
    {
      "source": 66,
      "target": 73,
      "value": 2
    },
    {
      "source": 48,
      "target": 88,
      "value": 2
    },
    {
      "source": 48,
      "target": 24,
      "value": 1
    },
    {
      "source": 24,
      "target": 66,
      "value": 1
    },
    {
      "source": 48,
      "target": 73,
      "value": 1
    },
    {
      "source": 48,
      "target": 70,
      "value": 1
    },
    {
      "source": 66,
      "target": 67,
      "value": 7
    },
    {
      "source": 88,
      "target": 67,
      "value": 6
    },
    {
      "source": 66,
      "target": 89,
      "value": 1
    },
    {
      "source": 90,
      "target": 24,
      "value": 2
    },
    {
      "source": 24,
      "target": 29,
      "value": 3
    },
    {
      "source": 29,
      "target": 67,
      "value": 2
    },
    {
      "source": 91,
      "target": 29,
      "value": 1
    },
    {
      "source": 91,
      "target": 24,
      "value": 2
    },
    {
      "source": 91,
      "target": 73,
      "value": 1
    },
    {
      "source": 91,
      "target": 70,
      "value": 1
    },
    {
      "source": 90,
      "target": 67,
      "value": 1
    },
    {
      "source": 90,
      "target": 29,
      "value": 1
    },
    {
      "source": 73,
      "target": 60,
      "value": 1
    },
    {
      "source": 92,
      "target": 73,
      "value": 2
    },
    {
      "source": 88,
      "target": 60,
      "value": 1
    },
    {
      "source": 92,
      "target": 88,
      "value": 5
    },
    {
      "source": 92,
      "target": 60,
      "value": 1
    },
    {
      "source": 24,
      "target": 60,
      "value": 1
    },
    {
      "source": 70,
      "target": 60,
      "value": 1
    },
    {
      "source": 67,
      "target": 60,
      "value": 1
    },
    {
      "source": 92,
      "target": 24,
      "value": 2
    },
    {
      "source": 92,
      "target": 70,
      "value": 2
    },
    {
      "source": 92,
      "target": 67,
      "value": 1
    },
    {
      "source": 11,
      "target": 67,
      "value": 3
    },
    {
      "source": 88,
      "target": 76,
      "value": 6
    },
    {
      "source": 92,
      "target": 76,
      "value": 1
    },
    {
      "source": 20,
      "target": 66,
      "value": 1
    },
    {
      "source": 20,
      "target": 67,
      "value": 1
    },
    {
      "source": 93,
      "target": 94,
      "value": 3
    },
    {
      "source": 95,
      "target": 93,
      "value": 1
    },
    {
      "source": 95,
      "target": 94,
      "value": 2
    },
    {
      "source": 96,
      "target": 95,
      "value": 1
    },
    {
      "source": 96,
      "target": 93,
      "value": 1
    },
    {
      "source": 96,
      "target": 94,
      "value": 1
    },
    {
      "source": 96,
      "target": 97,
      "value": 3
    },
    {
      "source": 100,
      "target": 95,
      "value": 5
    },
    {
      "source": 99,
      "target": 98,
      "value": 2
    },
    {
      "source": 97,
      "target": 94,
      "value": 11
    },
    {
      "source": 100,
      "target": 101,
      "value": 1
    },
    {
      "source": 95,
      "target": 101,
      "value": 2
    },
    {
      "source": 96,
      "target": 100,
      "value": 1
    },
    {
      "source": 97,
      "target": 99,
      "value": 29
    },
    {
      "source": 73,
      "target": 99,
      "value": 17
    },
    {
      "source": 97,
      "target": 73,
      "value": 23
    },
    {
      "source": 102,
      "target": 73,
      "value": 2
    },
    {
      "source": 102,
      "target": 99,
      "value": 1
    },
    {
      "source": 102,
      "target": 97,
      "value": 1
    },
    {
      "source": 100,
      "target": 103,
      "value": 3
    },
    {
      "source": 95,
      "target": 103,
      "value": 2
    },
    {
      "source": 73,
      "target": 104,
      "value": 4
    },
    {
      "source": 97,
      "target": 104,
      "value": 2
    },
    {
      "source": 104,
      "target": 99,
      "value": 2
    },
    {
      "source": 73,
      "target": 94,
      "value": 2
    },
    {
      "source": 70,
      "target": 94,
      "value": 3
    },
    {
      "source": 97,
      "target": 70,
      "value": 3
    },
    {
      "source": 95,
      "target": 99,
      "value": 4
    },
    {
      "source": 94,
      "target": 105,
      "value": 2
    },
    {
      "source": 92,
      "target": 94,
      "value": 1
    },
    {
      "source": 24,
      "target": 94,
      "value": 2
    },
    {
      "source": 106,
      "target": 94,
      "value": 1
    },
    {
      "source": 73,
      "target": 105,
      "value": 1
    },
    {
      "source": 92,
      "target": 105,
      "value": 1
    },
    {
      "source": 97,
      "target": 105,
      "value": 1
    },
    {
      "source": 70,
      "target": 105,
      "value": 1
    },
    {
      "source": 24,
      "target": 105,
      "value": 1
    },
    {
      "source": 106,
      "target": 105,
      "value": 1
    },
    {
      "source": 106,
      "target": 73,
      "value": 1
    },
    {
      "source": 92,
      "target": 97,
      "value": 1
    },
    {
      "source": 92,
      "target": 106,
      "value": 1
    },
    {
      "source": 24,
      "target": 97,
      "value": 1
    },
    {
      "source": 106,
      "target": 97,
      "value": 1
    },
    {
      "source": 106,
      "target": 70,
      "value": 2
    },
    {
      "source": 106,
      "target": 24,
      "value": 2
    },
    {
      "source": 96,
      "target": 73,
      "value": 2
    },
    {
      "source": 108,
      "target": 100,
      "value": 1
    },
    {
      "source": 109,
      "target": 94,
      "value": 3
    },
    {
      "source": 110,
      "target": 105,
      "value": 1
    },
    {
      "source": 73,
      "target": 95,
      "value": 3
    },
    {
      "source": 97,
      "target": 95,
      "value": 2
    },
    {
      "source": 110,
      "target": 111,
      "value": 2
    },
    {
      "source": 111,
      "target": 107,
      "value": 1
    },
    {
      "source": 111,
      "target": 94,
      "value": 2
    },
    {
      "source": 109,
      "target": 111,
      "value": 2
    },
    {
      "source": 110,
      "target": 107,
      "value": 1
    },
    {
      "source": 110,
      "target": 94,
      "value": 2
    },
    {
      "source": 109,
      "target": 110,
      "value": 2
    },
    {
      "source": 94,
      "target": 107,
      "value": 1
    },
    {
      "source": 109,
      "target": 107,
      "value": 1
    },
    {
      "source": 70,
      "target": 99,
      "value": 1
    },
    {
      "source": 67,
      "target": 99,
      "value": 1
    }
  ]
}
