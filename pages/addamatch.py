class AddAMatch(BasePage):
    my_team_xpath = "//input[starts-with(@name, 'myTeam')]"
    enemy_team_xpath = "//input[starts-with(@name, enemyTeam')]"
    zdobyte_gole_xpath = "*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    stracone_gole_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/label"
    data_xpath = "*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    mecz_domowy_xpath = "*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[2]"
    mecz_wyjazdowy_xpath = "*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[2]"
    tshirt_color_xpath = "//*[contains(@name, 'tshirt')]"
    league_xpath = "//*[contains(@name, 'league')]"
    czas_gry_xpath = "//@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    numer_xpath = "*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    webmatch_xpath = "//input[starts-with(@name, 'webMatch')]"
    general_xpath = "*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    rating_xpath = "//input[starts-with(@name, 'rating')]"
    submit_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"

pass