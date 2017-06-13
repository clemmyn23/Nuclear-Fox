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

class Kitsu:
    """Kitsu\'s bot management statistics utility"""

    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    @commands.group(pass_context=True, hidden=True)
    @checks.is_owner()
    async def kitsu(self, ctx):
        """Kitsu\'s BNS and bot dev utilities"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
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

    @kitsu.command(name="joinedvoice")
    @checks.is_owner()
    async def kitsu_joinedvoice(self):
        await self.bot.say("pulling data...")
        count = 0
        joined_msg = ''
        notjoined_msg = ''
        serverlist = list(self.bot.servers)
        for server in serverlist:
            vc = self.bot.voice_client_in(server)
            if vc == None:
                # await self.bot.say("bot not in voice in server {}".format(server.name))
                notjoined_msg += "bot not in voice in server {}\n".format(server.name)
            else:
                # await self.bot.say(">>> {} joined voice in server {}".format(vc.user.name, server.name))
                joined_msg += ">>> {} joined voice in server {}\n".format(vc.user.name, server.name)
                count += 1
        await self.bot.say(joined_msg)
        await self.bot.say(notjoined_msg)
        await self.bot.say("### joined voice channels in {}/{} servers".format(count, len(serverlist)))

def setup(bot):
    bot.add_cog(Kitsu(bot))
