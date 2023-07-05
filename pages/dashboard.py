from pages.base_page import BasePage


class Dashboard(BasePage):
    logo_scouts_panel_xpath =
    "//*[@id=__next"]/div[1]/main/div[3]/div[1]/div/div[1]"

    strona_glowna_xpath =
    "//span[text()="Strona główna"]"

    gracze_xpath =
    "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"

    language_version_xpath =
    "//*[@id="__next]/div[1]/div/div/div/ul[2]/div[1]"

    wyloguj_xpath =
    "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"

    linki_pomocnicze_xpath =
    "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/h2"

    aktywnosc_xpath =
    "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h2"

    dodaj_gracza_xpath =
    "//span[text()="Dodaj gracza"]"

    ostatnio_stworzony_gracz_xpath =
    "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h6[1]"

    ostatnio_zaktualizowany_gracz_xpath =
    "//a[contains(@href, "pl/players/64a3002959040b463e2b5ac3/edit")]"

    ostatnio_stworzony_mecz_xpath =
    "//a[contains(@href, "/pl/players/6026d92156c79737b3f3c62a/edit")]"

    ostatnio_zaktualizowany_mecz_xpath =
    "//a[contains(@href, "/pl/players/62f02fa32d2b7461da157b0f/matches/64974080c333a8eb8b9af90e/edit")]"

    ostatnio_zaktualizowany_raport_xpath =
    "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h6[5]"


pass
