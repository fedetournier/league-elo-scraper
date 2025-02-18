from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import quote  # To encode player names to URL-encoded format

############### Player List ###############
server = "kr" # las, lan, kr, euw, na, ...
player_list = [
    "Hide on bush-KR1", "어리고싶다-KR1", "Oner-KR222", "T1 Gumayusi-KR1",
    "역천괴-Ker10", "T1 Smash-KR3", "JUGKlNG-kr", "허거덩-0303"
] # Format: name-TAG
###########################################

# Converts the player's rank and division into a numeric value for sorting
def elo_to_int(player):
    elo_values = {
        "NULL": -1, "Iron": 0, "Bronze": 1000, "Silver": 2000,
        "Gold": 3000, "Platinum": 4000, "Emerald": 5000,
        "Diamond": 6000, "Master": 7000, "Grandmaster": 8000,
        "Challenger": 9000
    }
    division_values = {"3": 100, "2": 200, "1": 300}
    
    base_elo = elo_values.get(player['elo'], -1)
    division_bonus = division_values.get(player['division'], 0)
    
    try:
        lp_value = int(player["pl"].split(" ")[1])
    except (IndexError, ValueError):
        lp_value = 0
    
    return base_elo + division_bonus + lp_value

# Attempts to find an element and return its text, or 'NULL' if it does not exist
def safe_find_element(driver, by, value):
    try:
        return driver.find_element(by, value).text
    except NoSuchElementException:
        return "NULL"

# Browser configuration
options = webdriver.EdgeOptions()
options.add_argument('--headless=new')  # no GUI mode
options.add_argument('--disable-extensions')
options.add_argument('--disable-component-extensions-with-background-pages')
options.add_argument("--log-level=3")  # Reduces the number of logs in the console
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Hides debugging logs
driver = webdriver.Edge(options=options)

data = []

print("Loading...")
for player in player_list:
    player_encoded = quote(player) # Encodes to URL-encoded format
    url = f"https://www.leagueofgraphs.com/en/summoner/{server}/{player_encoded}#championsData-soloqueue"
    driver.get(url)

    # Extract player information
    elo_text = safe_find_element(driver, By.XPATH, '//*[@id="mainContent"]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[1]')
    elo_parts = elo_text.split(" ") if elo_text != "NULL" else ["NULL", ""]
    rank = elo_parts[0]
    division = elo_parts[1] if len(elo_parts) > 1 else "NULL"

    pl = safe_find_element(driver, By.XPATH, '//*[@id="mainContent"]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[4]')
    wins = safe_find_element(driver, By.XPATH, '//*[@id="mainContent"]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[5]/span[1]')
    losses = safe_find_element(driver, By.XPATH, '//*[@id="mainContent"]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[5]/span[3]')
    lvl = safe_find_element(driver, By.XPATH, '//*[@id="pageContent"]/div[1]/div/div[2]/div')

    # Calculate winrate
    try:
        wins_number = int(wins.split(":")[1].strip()) if wins != "NULL" else 0
        losses_number = int(losses.split(":")[1].strip()) if losses != "NULL" else 0
        total = wins_number + losses_number
        wr = round((wins_number / total) * 100, 1) if total > 0 else 0
    except (IndexError, ValueError):
        wins_number, losses_number, total, wr = 0, 0, 0, 0
    
    # Store data
    data.append({
        'name': player, 'lvl': lvl, 'elo': rank, 'division': division,
        'pl': pl, 'wr': wr, 'wins': wins, 'losses': losses, 'total': total
    })

# Sort players by Elo
data.sort(reverse=True, key=elo_to_int)

# Print ranking
print("=" * 120)
print("Elo Ranking:")
print("=" * 120)
for player in data:
    print(f"{player['name']} {player['lvl']} | {player['elo']} {player['division']} {player['pl']} | "
          f"Total: {player['total']} WinRate {player['wr']}% {player['wins']} - {player['losses']}")
    print("-" * 120)

driver.quit()
