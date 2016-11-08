import discord
import re
import aiohttp
import asyncio
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from __main__ import send_cmd_help
from urllib.parse import quote
from .utils.chat_formatting import *


try:
    from bs4 import BeautifulSoup
    isSoupAvail = True
except:
    isSoupAvail = False


class Kitsu:
    """Kitsu\'s BNS and bot dev utilities"""

    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    @commands.group(pass_context=True, hidden=True)
    async def kitsu(self, ctx):
        """Kitsu\'s BNS and bot dev utilities"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            return

    @kitsu.command(name="encode", pass_context=True)
    @checks.is_owner()
    async def kitsu_debug_encode(self, ctx, *text):
        if text == ():
            await send_cmd_help(ctx)
        else:
            await self.bot.say(text)
            await self.bot.say(quote(" ".join(map(str, text)), safe=''))
        return

    @kitsu.command(name="botservers", pass_context=True)
    @checks.is_owner()
    async def kitsu_botservers(self, ctx):
        """detailed stats for all joined servers"""
        for server in list(self.bot.servers):

            # """Shows server's informations"""
            # server = ctx.message.server
            online = str(len([m.status for m in server.members if str(m.status) == "online" or str(m.status) == "idle"]))
            total_users = str(len(server.members))
            text_channels = len([x for x in server.channels if str(x.type) == "text"])
            voice_channels = len(server.channels) - text_channels

            data = "```\n"
            data += "Name: {}\n".format(server.name)
            data += "ID: {}\n".format(server.id)
            data += "Region: {}\n".format(server.region)
            data += "Users: {}/{}\n".format(online, total_users)
            data += "Text channels: {}\n".format(text_channels)
            data += "Voice channels: {}\n".format(voice_channels)
            data += "Roles: {}\n".format(len(server.roles))
            passed = (ctx.message.timestamp - server.created_at).days
            data += "Created: {} ({} days ago)\n".format(server.created_at, passed)
            data += "Owner: {}\n".format(server.owner)
            if server.icon_url != "":
                data += "Icon:"
                data += "```"
                data += server.icon_url
            else:
                data += "```"
            await self.bot.say(data)

    @kitsu.command(name="servermems", pass_context=True)
    @checks.is_owner()
    async def kitsu_servermems(self, ctx):
        """Lists members in server"""
        owner = ctx.message.author
        servers = list(self.bot.servers)
        server_list = {}
        msg = ""
        for i in range(0, len(servers)):
            server_list[str(i)] = servers[i]
            msg += "{}: {}\n".format(str(i), servers[i].name)
        msg += "\nListing server members for #: (timeout 10)"
        for page in pagify(msg, ['\n']):
            await self.bot.say(page)

        # while msg != None:
        msg = await self.bot.wait_for_message(author=owner, timeout=10)
        if msg != None:
            msg = msg.content.strip()
            if msg in server_list.keys():

                memlist = ""
                for i in server_list[msg].members:
                    memlist += "{} name={}             nick={}\n".format(i.id, i.name, i.nick)
                for page in pagify(memlist, ['\n']):
                    await self.bot.say("```" + page + "```")

            # else:
            #     break
        # else:
        #     break


    @kitsu.command(name="user")
    async def kitsu_user(self, *text):
        """BNS character details docstring"""
        await self.bot.say("TODO: char details parser. [{}]".format(text))
        return

    @kitsu.command(name="alts", pass_context=True)
    async def kitsu_alts(self, ctx, *text):
        """BNS account alts parser"""

        if text == ():
            await send_cmd_help(ctx)
            return

        name = quote(" ".join(map(str, text)), safe='')
        url = "http://na-bns.ncsoft.com/ingame/bs/character/search/info?c=" + name
        # url = "http://na-bns.ncsoft.com/ingame/bs/character/profile?c=" + name
        try:
            with aiohttp.Timeout(5):
                async with aiohttp.get(url) as resp:
                    if resp.status != 200:
                        multiline = "{}\nBNS server potato #1 (http resp status {})".format(url, resp.status)
                        await self.bot.say(multiline)
                        return

                    soup = BeautifulSoup(await resp.text(), 'html.parser')
        except Exception as e:
            await self.bot.say("BNS server potato #02: {}".format(e))
            return

        numresults = 0
        try:
            # soup = BeautifulSoup(open('charsearch2.html'), 'html.parser')
            a = soup.body.find('div', id="container").find('div', id="contents").find('p', class_="schResult")
            a.strong.unwrap()    # there are two <strong> tags
            numresults = int(a.strong.string)
            a.strong.unwrap()
            schResult = ''.join(a.contents)
        except Exception as e:
            print("unknown parsing error. send help.\n{}".format(e))

        if numresults == 0:
            await self.bot.say("{}".format(schResult))
            return

        try:
            # ==STRUCTURE==
            # accountname   (parsed from alts)
            # user          (abstract)
            # - mainchar
            # - - mainchar_name
            # - - mainchar_stats
            # - alts

            # print("** parsing main")
            user = soup.body.find('div', id='container').find('div', class_='searchList')

            mainchar = user.ul.li.dl
            mainchar_name = mainchar.dt.a
            mainchar_stats = mainchar.find('dd', class_='desc').ul.contents
            for i in mainchar_stats:
                if i == "\n":
                    mainchar_stats.remove(i)

            # print("** parsing alts")
            accountname = user.find('dd', class_='other').dl.dt.strong
            alts = user.find('dd', class_='other').dl.find('dd', class_='desc2').ul.find_all('a')

            # print("*************** info")
            multiline = ""
            multiline += "{}\n".format(schResult)
            multiline += ("Account:\n  {}\n".format(accountname.string))
            multiline += ("Main:\n  {}\n".format(mainchar_name.string))
            # multiline += ("    {}\n".format(mainchar_name.get("href")))
            for i in mainchar_stats:
                multiline += ("  {}\n".format(i.string))
            multiline += ("Other characters:\n")
            for i in alts:
                multiline += ("  {}\n".format(i.string))
                # multiline += ("    {}\n".format(i.get("href")))

            # print(multiline)
            await self.bot.say("```{}```".format(multiline))

        except Exception as e:
            await self.bot.say("parsing error. send help\n{}".format(e))

        return

    @kitsu.command(name = "bopae")
    async def kitsu_bopae(self, *text):
        if text == ():
            return self.kitsu_help()

        name = quote(" ".join(map(str, text)), safe='')
        url = "http://na-bns.ncsoft.com/ingame/bs/character/profile?c=" + name

        async with aiohttp.get(url) as resp:
            if resp.status != 200:
                multiline = "{}\n".format(url)
                multiline += "BNS server potato (http resp status {})".format(resp.status)
                # await self.bot.say(multiline)
                return multiline
            soup = BeautifulSoup(await resp.text(), 'html.parser')

        try:
            wall = soup.body.find(id="container").find(id="contents").find(class_="characterInfo")
            wall = wall.find(class_="itemArea").find(class_="wrapGem").find(class_="gemIcon").find("map")
            multiline = "Requested name [{}]\n".format(name)
            multiline += "{}\n".format(url)
            slot = 1
            for piece in wall.find_all("area"):
                try:
                    multiline += "slot #{}: {}, \titem-ID {}\n".format(slot, piece["alt"], piece["item-data"])
                except:
                    multiline += "slot #{}: empty\n".format(slot)
                slot += 1
            return multiline
        except:
            return "Unable to find character [{}]".format(name)


def setup(bot):
    if isSoupAvail:
        bot.add_cog(Kitsu(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
