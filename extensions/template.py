from discord.ext.commands import Cog, Bot, Context, command

"""
Her er en mal for deg slik at du kan dele koden opp i flere filer.
Du kan skrive kommando funksjoner i klassen under. Da vil de bli lastet inn av boten.
Bare klipp og lim denne koden hvis du vil ha flere filer.
Det har ingen betydning hvor mange filer du vil bruke så lenge de har forskjellige navn.
"""

def setup(bot):
    bot.add_cog(SkrivNavnetHer(bot))

class SkrivNavnetHer(Cog):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot

    """
    Det med @ under kalles en decorator.
    Den er en funksjon som tar inn funksjonen under som et argument og modifiserer den.
    Den har forskjellige argumenter som du kan se i dokumentasjon siden. Da skriver du dem inne i parantesene.
    
    Jeg har markert argumentet med en type. Vanligvis har det ingen betydning i Python.
    Men discord.py bruker det som et tegn på hvilke verdier du forventer å få, så det kan ha en betydning.
    """
    @command()
    async def skriv_kommando_navn_her(self, ctx: Context) -> None: # Navnet på funksjonen kan være for eksempel ping
        ...
