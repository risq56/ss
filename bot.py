import discord
from discord.ext import commands
from discord import Option
bot = commands.Bot()
staff = 993283759753416745
token = "OTk5NDA4MTgyMTAxMjgyODU2.GowELp.LifNPm094ZZQ7wHzY36GiPMom5donKpjjv_F2k"

@bot.event
async def on_ready():
    print('Ready to generate')




"""@commands.has_permissions(administrator=True)"""
@commands.has_role(staff)
@bot.slash_command(description="whitelist someone")
async def whitelist(ctx,user: Option(discord.Member,"the person to whitelist",required=True,default=None)):
	mention = ctx.author.mention
	member = user
	role = discord.utils.get(ctx.guild.roles, name="whitelisted")
	await member.add_roles(role)
	embed=discord.Embed(title="Success", description=f"**{mention} has whitelisted {user.mention}**", color=0x9b1900)
	await ctx.respond(embed=embed, delete_after=5)
    
	 
@whitelist.error
async def whitelist_error(ctx,error):
	mention = ctx.author.mention
	if isinstance(error, commands.MissingRole):
		embed=discord.Embed(title="ERROR", description=f"**{mention} you do not have the role to whitelist**", color=0x9b1900)
		await ctx.respond(embed=embed, delete_after=5)

@commands.has_permissions(ban_members = True)
@bot.slash_command(description="whitelist someone")
async def ban(ctx,useer: Option(discord.Member,"the person to whitelist",required=True,default=None),reason: Option(str,"the reason of the ban",required=True,default=None)):
	mention = ctx.author.mention
	membere = useer
	await membere.ban(reason = reason)


	embed=discord.Embed(title="Success", description=f"**{mention} has whitelisted {user.mention}**", color=0x9b1900)
	await ctx.respond(embed=embed, delete_after=5)
"""@whitelist.error
async def whitelist_error(ctx,error):
	mention = ctx.author.mention
	if isinstance(error, commands.MissingRole):
		embed=discord.Embed(title="ERROR", description=f"**{mention} you do not have the role to whitelist**", color=0x9b1900)
		await ctx.respond(embed=embed, delete_after=5)"""




    
    
bot.run(token)
