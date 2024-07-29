from discord import Intents
from discord.ext.commands import Bot

"""
Dette er hoved filen som starter programmet.

Før du gjør noe annet må du dra til https://discord.com/developers/applications
Lag en ny app. Gi den et navn osv.
Gå til Bot siden og lag en bot.
Skru på de 3 instillignene som er under Privileged Gateway Intents seksjonen slik at boten har tilgang til ting i APIen.
Kopier din token og lim den inn under.

Deretter kan du gå til OAuth2 -> URL Generator
Trykk på bot, og kopier linken nederst på siden. Hvis du bruker den linken kan du invitere boten til din server.
"""

def main():
    bot = Bot(
        command_prefix = "!", # Bytt ut ! med det prefix tegnet du vil ha. Det kommer forran hver kommando for eksempel !ping
        case_insensitive = True,
        intents = Intents.all() #
    )

    bot.load_extensions("extensions") # Laster inn koden i hver av filene i extensions mappa.

    bot.run("") # Lim inn din bot token i strengen her.

if __name__ == "__main__":
    main()