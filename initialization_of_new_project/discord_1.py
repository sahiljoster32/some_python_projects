import discord
import random
import pyjokes
from discord.ext import commands
bot = commands.Bot(command_prefix="$")


@bot.command(name="help_box")
async def help_box(context):
    help_box = discord.Embed(title="commands", description="commands that you can use ", color=0xff9933)
    help_box.add_field(name="jokes_neutral",value="gives random neutral jokes", inline=False)
    help_box.add_field(name="jokes_chuck",value="gives random chuck jokes", inline=False)
    help_box.add_field(name="kick", value="to kick a member anonymously", inline=False)
    help_box.add_field(name="ban", value="to ban a member anonymously", inline=False)
    help_box.add_field(name="author", value="to take info of author or owner", inline=False)
    help_box.add_field(name="motiv_quotes",value="to give random motivational quotes", inline=False)
    help_box.add_field(name="love_quotes",value="to give random love quotes", inline=False)
    help_box.set_footer(text="key for commands")
    help_box.set_author(name="`make sure you add $ to access the commands`")
    help_box.add_field(name="SOME EXTRA PERKS",value="hehe", inline=False)
    help_box.add_field(name="on deleting a message",value="it react on deleted mesaages", inline=False)
    help_box.add_field(name="on editing a message",value="it react on edited mesaages", inline=False)
    help_box.add_field(name="on message how old you are ?",value="surprise", inline=False)
    await context.message.channel.send(embed=help_box)


@bot.command(name="jokes_neutral")
async def jokesn(context):
    jokes1 = pyjokes.get_joke('en', 'neutral')
    general_channel = bot.get_channel(803958476685574181)
    await general_channel.send(f'`{jokes1}`')


@bot.command(name="jokes_chuck")
async def jokeschukc(context):
    jokes2 = pyjokes.get_joke('en', 'chuck')
    general_channel = bot.get_channel(803958476685574181)
    await general_channel.send(f'`{jokes2}`')


@bot.command(name='kick', pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):
    await member.kick()
    await context.send('user ' + member.display_name + ' is removed')


@bot.command(name='ban', pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(context, member: discord.Member):
    await member.ban()
    await context.send('user ' + member.display_name + ' is banned')


@bot.command(name="motiv_quotes")
async def motivational_quotes(context):
    motivational_quotes = ["Your limitation—it’s only your imagination.",
                           " Push yourself, because no one else is going to do it for you.",
                           " Sometimes later becomes never. Do it now.",
                           " Great things never come from comfort zones.",
                           "Dream it. Wish it. Do it.",
                           "Success doesn’t just find you. You have to go out and get it.",
                           " The harder you work for something, the greater you’ll feel when you achieve it.",
                           "Dream bigger. Do bigger.",
                           " Don’t stop when you’re tired. Stop when you’re done.",
                           " Wake up with determination. Go to bed with satisfaction.",
                           "Do something today that your future self will thank you for.",
                           "Little things make big days.",
                           " It’s going to be hard, but hard does not mean impossible.",
                           " Don’t wait for opportunity. Create it.",
                           " Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
                           "The key to success is to focus on goals, not obstacles.",
                           "Dream it. Believe it. Build it.",
                           "small milate jaoo large banate jaoo"]
    string_motiv = random.choice(motivational_quotes)
    general_channel = bot.get_channel(803958476685574181)
    await general_channel.send(f'`{string_motiv}`')


@bot.command(name="author")
async def author(context):
    author_box = discord.Embed(title="author's github", description="shelf of author",
                               url="https://github.com/sahiljoster32", color=0xff9933)
    author_box.add_field(name="studing in : MRU", value="**", inline=False)
    author_box.add_field(name="want to be in", value="CDS", inline=False)
    author_box.add_field(name="date of release \'of author\'😋",
                         value="2001.07.04", inline=False)
    author_box.set_footer(text="that's a footer")
    author_box.set_author(name="sahil_jhangar `shushi_teja`")
    await context.message.channel.send(embed=author_box)


@bot.command(name="love_quotes")
async def broken_quotes(context):
    broken_quotes = ["Stab the body and it heals, but injure the heart and the wound lasts a lifetime.",
                     "I’ve been heartbroken. I’ve broken hearts. That’s part of life, and its part of figuring out who you are so you can find the right partner.",
                     "Hearts can break. Yes, hearts can break. Sometimes I think it would be better if we died when they did, but we don’t.",
                     "Ever has it been that love knows not its own depth until the hour of separation.",
                     "The saddest thing about love is that not only that it cannot last forever, but that heartbreak is soon forgotten.",
                     "Love is the hardest drug to quit, but it is even harder when it is taken away.",
                     "Love is the hardest drug to quit, but it is even harder when it is taken away.",
                     "Sometimes, when one person is missing, the whole world seems depopulated.",
                     "Then his heart, now broken into a thousand pieces, slowly began to turn to ice.",
                     "There will be a time when you are forced to follow your heart away from someone you love.",
                     "Has someone made you heartbroken? Then, why are you still thinking of him?",
                     "Hearts will never be practical until they are made unbreakable.",
                     "When your heart is broken, you plant seeds in the cracks and you pray for rain.",
                     "I wish I were a little girl again, because skinned knees are easier to fix than broken heart.",
                     "I’m not supposed to miss you, I’m not supposed to care.",
                     "So it’s true, when all is said and done, grief is the price we pay for love.",
                     "Happiness is the china shop; love is the bull.",
                     "Sometimes you break your heart in the right way, if you know what I mean.",
                     "You flew off with the wings of my heart and left me flightless.",
                     "We are all Romeos looking for our Juliet, but never finding her."]
    string1 = random.choice(broken_quotes)
    general_channel = bot.get_channel(803958476685574181)
    await general_channel.send(f'`{string1}`')

# all message's editable commands


@bot.event
async def on_message_edit(before_message, after_message):
    general_channel = bot.get_channel(803958476685574181)
    await general_channel.send(f'`{before_message.content}`-->`{after_message.content}`')


@bot.event
async def on_disconnect():
    general_channel = bot.get_channel(803958476685574181)
    await general_channel.send('it`s time to leave ok bie bruh..........')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("$help_box for help_box"))
    general_channel = bot.get_channel(803958476685574181)
    await general_channel.send('bot at your service :-)')


@bot.event
async def on_message_delete(message):
    general_channel = bot.get_channel(803958476685574181)
    await general_channel.send(f'ummm hummm hope that\'s not the bad language {message.content}')


@bot.event
async def on_message(message):
    shami = message.content
    if shami.lower() == "how old you are ?":
        general_channel = bot.get_channel(803958476685574181)
        await general_channel.send('still counting , :_(')
    await bot.process_commands(message)
# all message edit ends here


bot.run('ODAzODQ2OTkxNjc0MDgxMzAx.YBDu2Q.GJQ5kRJ7izs1hhMQryIw4yCN5ZY')


# signed by sahil jhangar
