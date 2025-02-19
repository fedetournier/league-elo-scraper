Web scraper that uses Selenium for Python to extract player information from League of Legends on the League of Graphs website. It displays data about their league, division, league points (LP), winrate, and other details, and sorts them according to their ELO.

## Features
- Automatically extracts player information from League of Graphs.
- Sorts players based on their current ELO.
- Calculates the winrate based on games won and lost.
- Uses Selenium for scraping automation.

## Requirements
- Python 3.
- Microsoft Edge installed along with the corresponding driver (msedgedriver), both in the same version. You can download it from:

  [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

Make sure to extract the file into the same directory as `script.py`.

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/fedetournier/league-elo-scraper.git
   cd league-elo-scraper
   ```
3. Extract msedgedriver in the folder league-elo-scraper.
4. Install the required dependencies:
   ```sh
   pip install selenium
   ```
5. Modify the player list and their server in `script.py` with the correct format:
   ```sh
   server = "" # las, lan, kr, euw, na, ...
   player_list = [""] # Format is name-TAG
   ```
6. Run the script:
   ```sh
   python script.py
   ```
7. The result will be displayed in the console with players sorted by their ELO. It should be something like:

```
========================================================================================================================
Elo Ranking:
========================================================================================================================
T1 Smash-KR3 T1 - (Mid)
Level 472 | Challenger 1752 LP: 1752 | Total: 207 WinRate 61.4% Wins: 127 - Losses: 80
------------------------------------------------------------------------------------------------------------------------
JUGKlNG-kr Gen.G Esports - (Jungler)
Level 624 | Challenger 1540 LP: 1540 | Total: 193 WinRate 62.2% Wins: 120 - Losses: 73
------------------------------------------------------------------------------------------------------------------------
허거덩-0303 Gen.G Esports - (Mid)
Level 666 | Challenger 1272 LP: 1272 | Total: 137 WinRate 65.0% Wins: 89 - Losses: 48
------------------------------------------------------------------------------------------------------------------------
어리고싶다-KR1 T1 - (Top)
Level 1238 | Challenger 1199 LP: 1199 | Total: 200 WinRate 58.5% Wins: 117 - Losses: 83
------------------------------------------------------------------------------------------------------------------------
T1 Gumayusi-KR1 T1 - (AD Carry)
Level 769 | Challenger 1090 LP: 1090 | Total: 280 WinRate 54.3% Wins: 152 - Losses: 128
------------------------------------------------------------------------------------------------------------------------
Oner-KR222 T1 - (Jungler)
Level 552 | Challenger 1076 LP: 1076 | Total: 157 WinRate 61.1% Wins: 96 - Losses: 61
------------------------------------------------------------------------------------------------------------------------
Hide on bush-KR1 T1 - (Mid)
Level 801 - #1,383 Ambessa | GrandMaster 857 LP: 857 | Total: 153 WinRate 60.1% Wins: 92 - Losses: 61
------------------------------------------------------------------------------------------------------------------------
역천괴-Ker10 T1 - (Support)
Level 899 - #635 Poppy | GrandMaster 744 LP: 744 | Total: 141 WinRate 57.4% Wins: 81 - Losses: 60
------------------------------------------------------------------------------------------------------------------------
```
