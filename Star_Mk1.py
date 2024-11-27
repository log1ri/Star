import discord, time, platform, random, asyncio, requests
from discord.ext import commands 
from discord import app_commands
from discord.ui import Button, View
from colorama import Back, Fore, Style
from datetime import datetime, timezone ,timedelta
from dotenv import load_dotenv
import os

client = commands.Bot(command_prefix="!", intents= discord.Intents.all())
load_dotenv()

@client.event
async def on_ready():
    prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:S UTC+8 ", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(prfx + "Logged in as      : " + Fore.YELLOW + client.user.name)
    print(prfx + "Bot id            : " + Fore.YELLOW + str(client.user.id))
    print(prfx + "Discord Version   : " + Fore.YELLOW + discord.__version__)
    print(prfx + "Python Versioni   : " + Fore.YELLOW + str(platform.python_version()))
    synced = await client.tree.sync()
    print(prfx +"Slash CMDs Synced : "+Fore.YELLOW + str(len(synced))+" Commands")
    await client.change_presence(status=discord.Status.idle,activity= discord.Game("Code"))
    client.add_view(Cf()) 

@client.command()
async def hello(ctx):
    await ctx.send("hello")

@client.command()
async def dm(ctx, member: discord.Member, *, content):  #!dm name message
    await member.send(content)
    
@client.tree.command(name="close",description="Shuts down the bot")
async def shutdown(interaction: discord.Interaction):
    await interaction.response.send_message("Shutting down the bot")
    await client.close()
    
@client.tree.command(name="cat",description="see some cat")#/
async def cat(interaction: discord.Interaction):
    os.getenv("API_TOKEN")
    API_KEY = os.getenv("cat_token")  # เปลี่ยนเป็น API Key ของคุณจาก TheCatAPI
    headers = {'x-api-key': API_KEY}
    
    res = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
    data = res.json()
    
    value = ["⸜(｡˃ ᵕ ˂ )⸝♡","ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧","(˶ᵔ ᵕ ᵔ˶)",">ᴗ<","≽^•⩊•^≼","( ˶ˆᗜˆ˵ )","( ^ω^ )","૮₍ ´˶• ᴥ •˶` ₎ა","*ฅ^•ﻌ•^ฅ*",
             "س(˶^▾^˶)س","(^≗ω≗^)","(๑•᎑•๑)ｳﾝ","(⌯'ᢍ'⌯ ^)∫","o( ^▾^˶ )o","(｡^•ㅅ•^｡)","(≡^∇^≡)","₍^""> · <"" ^₎"]
    choice = random.choice(value)
    
    cat_image_url = data[0]['url']
    embed = discord.Embed(title=f"``` **{choice}** ```", color=discord.Color.pink())
    embed.set_image(url=cat_image_url)
    await interaction.response.send_message(embed=embed)
 
@client.tree.command(name="dog",description="see some dog")#/
async def dog(interaction: discord.Interaction):
    API_KEY = os.getenv("dog_token")  # เปลี่ยนเป็น API Key ของคุณจาก TheCatAPI
    headers = {'x-api-key': API_KEY}
    
    res = requests.get('https://api.thedogapi.com/v1/images/search', headers=headers)
    data = res.json()
    
    value = ["⸜(｡˃ ᵕ ˂ )⸝♡","ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧","(˶ᵔ ᵕ ᵔ˶)",">ᴗ<","≽^•⩊•^≼","( ˶ˆᗜˆ˵ )","( ^ω^ )","૮₍ ´˶• ᴥ •˶` ₎ა","*ฅ^•ﻌ•^ฅ*",
             "س(˶^▾^˶)س","(^≗ω≗^)","(๑•᎑•๑)ｳﾝ","(⌯'ᢍ'⌯ ^)∫","o( ^▾^˶ )o","(｡^•ㅅ•^｡)","(≡^∇^≡)","₍^""> · <"" ^₎"]
    choice = random.choice(value)
    
    dog_image_url = data[0]['url']
    embed = discord.Embed(title=f"``` **{choice}** ```", color=discord.Color.pink())
    embed.set_image(url=dog_image_url)
    await interaction.response.send_message(embed=embed)   
    
@client.tree.command(name="goldprice",description="price today")#/
async def gold(interaction: discord.Interaction): 
    url = "https://api.chnwt.dev/thai-gold-api/latest"
    res = requests.get(url)

    data = res.json()    
    
    day = data["response"]["date"]
    times = data["response"]["update_time"]
    gold_buy = data["response"]["price"]["gold"]["buy"]
    gold_sell = data["response"]["price"]["gold"]["sell"]
    goldbar_buy = data["response"]["price"]["gold_bar"]["buy"]
    goldbar_sell = data["response"]["price"]["gold_bar"]["sell"]
    chg = data["response"]["price"]["change"]["compare_previous"]
    
    msg = (     
        f"{day} \n"
        f"-----------------------------------------\n"
        f"**ทองคำแท่ง (รับซื้อ)   :** `{goldbar_sell}` \n"
        f"**ทองคำแท่ง (ขายออก) :** `{goldbar_buy}` \n"
        f"-----------------------------------------\n"
        f"**ทองคำรูปพรรณ (รับซื้อ)  :** `{gold_sell}` \n"
        f"**ทองคำรูปพรรณ(ขายออก) :** `{gold_buy}` \n"
        f"-----------------------------------------\n"
        f"**วันนี้ ขึ้น/ลง :** `{chg}` \n"
        f"-----------------------------------------\n")
    
    embed = discord.Embed(title=f"**ราคาทอง \u200b : \u200b {day}**", color=discord.Color.yellow())
    embed.set_author(name='Gold_Thailand',url="https://www.goldtraders.or.th/",icon_url='https://i.pinimg.com/564x/c4/d9/aa/c4d9aaec9bfa5b380762d01cf2a43763.jpg')
    embed.add_field(name="ทองคำแท่ง (Bath)", value=(f"> รับซื้อ \u200b : \u200b `{goldbar_sell}`\n > ขายออก : `{goldbar_buy}`"),inline=False)
    embed.add_field(name="ทองคำรูปพรรณ (Bath)", value=(f"> รับซื้อ \u200b : \u200b `{gold_sell}`\n > ขายออก : `{gold_buy}`"),inline=False)
    embed.add_field(name="การปรับตัวของราคาทอง", value=(f"> ขึ้น/ลง \u200b : \u200b `{chg}`"),inline=False)
    #embed.set_footer(text="Gold_Thailand",icon_url="https://i.pinimg.com/564x/c4/d9/aa/c4d9aaec9bfa5b380762d01cf2a43763.jpg")
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="goldprice2",description="price today")#/
async def gold2(interaction: discord.Interaction): 
    url = "https://api.chnwt.dev/thai-gold-api/latest"
    res = requests.get(url)

    data = res.json()    
    
    day = data["response"]["date"]
    gold_buy = data["response"]["price"]["gold"]["buy"]
    gold_sell = data["response"]["price"]["gold"]["sell"]
    goldbar_buy = data["response"]["price"]["gold_bar"]["buy"]
    goldbar_sell = data["response"]["price"]["gold_bar"]["sell"]
    chg = data["response"]["price"]["change"]["compare_previous"]
    
    embed1 = discord.Embed(title=f"ทองคำแท่ง \u200b : \u200b {day}", color=discord.Color.yellow())
    embed1.set_thumbnail(url="https://i.pinimg.com/564x/13/08/fd/1308fddd09216ea58626af6ded641de6.jpg")
    embed1.add_field(name="รับซื้อ:", value=(f" ```{goldbar_sell}```"),inline=True)
    embed1.add_field(name="ขายออก:", value=(f" ```{goldbar_sell}```"),inline=True)
    
    embed2 = discord.Embed(title=f"ทองคำรูปพรรณ \u200b : \u200b {day}", color=discord.Color.yellow())
    embed2.set_thumbnail(url="https://i.pinimg.com/564x/c5/47/b0/c547b0e17ea2d94dba947b92ec0c436d.jpg")
    embed2.add_field(name="รับซื้อ:", value=(f" ```{gold_sell}```"),inline=True)
    embed2.add_field(name="ขายออก:", value=(f" ```{gold_buy}```"),inline=True)
    
    await interaction.response.send_message(embeds=[embed1, embed2])


def get_weather_data(city):
    key = os.getenv("weather_key")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=en"
    res = requests.get(url)   
    return res.json()
def get_country_data(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    response = requests.get(url,timeout=10)
    return response.json()

def convert_timezone_offset_to_utc(timezone_offset):
    utc_now = datetime(*time.gmtime()[:6])
    # timezone_offset อยู่ในหน่วยวินาที
    #utc_offset_hours = timezone_offset / 3600
    utc_offset = timedelta(seconds=timezone_offset)
    local_time = utc_now + utc_offset
    #return f"{'+' if utc_offset_hours >= 0 else ''}{int(utc_offset_hours)}"
    return f"```{local_time.strftime('%H:%M:%S')}```"

@client.tree.command(name="weather",description="Today's weather")
async def weatherinfo(interaction:discord.Interaction,city:str=None):
    await interaction.response.defer()
    if city == None:                 #กรณีที่ไม่ได้ @ ชื่อคนเข้ามา
        city = "bangkok"
    data = get_weather_data(city)
    weather_des = data["weather"][0]["description"]
    icon_code = data["weather"][0]["icon"]
    wind_speed = data["wind"]["speed"]
    
    
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    temp = data["main"]["temp"] 
    hum = data["main"]["humidity"] 
    today = datetime.now(timezone.utc)
    utc_offset = convert_timezone_offset_to_utc(data["timezone"])
    sys = data["sys"]
    
    country_data= get_country_data(sys["country"])  
    country_info = country_data[0]
    country_name = country_info["name"]["common"]
    country_flag = country_info["flags"]["png"]  
    country_time = country_info["timezones"]
    
    embed = discord.Embed(title=f"Weather Data: _ _ {city.capitalize()}", color=discord.Color.blue())
    embed.set_thumbnail(url=icon_url)
    embed.add_field(name="Temperature", value=(f"```{temp}°C```"), inline=True)
    embed.add_field(name="Humidity", value=(f"```{hum}%```"), inline=True)
    embed.add_field(name="The Weather", value=(f"```{weather_des}```"), inline=False)
    embed.add_field(name="Wind Speed", value=(f"```{wind_speed}m/s```"), inline=True)
    embed.add_field(name="Time", value=(utc_offset), inline=True)
    embed.set_image(url=country_flag)

    await interaction.followup.send(embed=embed)
    
@client.tree.command(name="userinfo",description="Send the information on a user")
async def userinfo(interaction:discord.Interaction,member:discord.Member=None):
    if member == None:                 #กรณีที่ไม่ได้ @ ชื่อคนเข้ามา
        member = interaction.user
    roles = [role for role in member.roles]
    embed = discord.Embed(title="***User Info***", description=f"Here's the user info on the user {member.mention}", color= discord.Color.green(), timestamp = datetime.now(timezone.utc))
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="**ID**",value= f"```{member.id}```")
    embed.add_field(name="**Name**",value= f"```{member.name}#{member.discriminator}```")
    embed.add_field(name="**Nickname**",value= f"```{member.display_name}```")
    embed.add_field(name="**Status**",value= f"```{member.status}```")
    embed.add_field(name="**Created at**" , value= f'`{member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p")}`')
    embed.add_field(name="**Joined at**" , value= f'`{member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p")}`')
    embed.add_field(name="Messages" , value= f"```0```")
    embed.add_field(name="Bot?" , value= f"```{member.bot}```")
    embed.add_field(name=f"**Roles({len(roles)})**", value= " ".join([role.mention for role in roles]),inline=False)
    
    await interaction.response.send_message(embed=embed,ephemeral=False)
    
@client.tree.command(name="serverinfo",description="Send the information on the server")
async def serverinfo(interaction:discord.Interaction):
    x= interaction.guild.member_count
    embed = discord.Embed(title="Server Info",description=f"Here's the server info on the server", color= discord.Color.green(),timestamp= datetime.now(timezone.utc))
    embed.set_thumbnail(url= interaction.guild.icon)
    embed.add_field(name="Members",value=f'```{interaction.guild.member_count}```',inline =True)
    embed.add_field(name="Owner",value= f"```{interaction.guild.owner.name}```",inline="True")
    embed.add_field(name="Channels",value=f"```{len(interaction.guild.text_channels)}texts||{len(interaction.guild.voice_channels)}voices```",inline=True)
    embed.add_field(name="Description",value= f"```{interaction.guild.description}```",inline=True)
    embed.add_field(name="Created At",value= f'```{interaction.guild.created_at.strftime("%a, %B %#d, %Y, %I:%M %p")}```',inline=True)
    await interaction.response.send_message(embed=embed,ephemeral=False)
  
@client.tree.command(name="math",description="Evaluates any math expression")
async def math(interaction:discord.Interaction,expression:str):
    symbols = ['+','-','*','/','%']
    if any(s in expression for s in symbols):
        calculated = eval(expression)
        embed = discord.Embed(title="Math Equation",description=f"Expresstion {expression}\n Answwer {calculated}",color= discord.Color.green(),timestamp= datetime.now(timezone.utc))
    else:
        await interaction.response.send_message("This isn't math problem")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="coinflip",description="Choose heads or tails")
@app_commands.choices(choices=[app_commands.Choice(name="heads",value="heads"),app_commands.Choice(name="tails",value="tails")])
async def coinflip(interaction:discord.Interaction,choices:app_commands.Choice[str]):
    values = ["heads","tails"]
    comChoice = random.choice(values)
    # if choices not in values:
    #     await interaction.response.send_message("Please send heads or tails")
    
    if comChoice == choices.value:
        answer = f"You guessed correctly,\n it was {choices.value}"
    elif comChoice != choices.value:
        answer = f"You guessed incorrectly,\n it was {comChoice}"
    embed = discord.Embed(title="CoinFlip",description= answer, color= discord.Color.yellow())
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="roll",description="Rolls a dice")
async def roll(interaction:discord.Interaction,max:int=6):
    number = random.randint(1,max)
    embed = discord.Embed(title="Roll Result",description=f"result = {number}",color= discord.Color.yellow())
    await interaction.response.send_message(embed=embed)

#####
@client.tree.command(name="choice",description="chooses a value")
async def choose(interaction:discord.Interaction,arg1:str,arg2:str,arg3:str):
    arguments = [arg1,arg2,arg3]
    choice = random.choice(arguments)
    thinking = await interaction.response.send_message(":clock1:Thinking...")
    await asyncio.sleep(0.2)
    for i in range(4):
        await thinking.edit(content=f":clock{i+1}: Thinking...")
        await asyncio.sleep(0.2)
    await interaction.response.send_message(choice)
          
######
@client.tree.command(name="guess", description="Guessing game!")
async def guess(interaction:discord.Interaction,max:int=10):
    MAX_GUESSES = 5
    number = random.randint(1,max)
    await interaction.response.send_message(f"Guessing game started!\nPlease guess a number between **1-{max}**\nYou have **{MAX_GUESSES}** guesses")
    def check(m):
        return m.author == interaction.user and m.channel == interaction.channel
    for i in range(MAX_GUESSES):
        guess = await client.wait_for("message", check=check)
        try:
            int(guess.content)
            if guess.content == str(number):
                await interaction.channel.send(f"You guessed correctly, it took you **{i+1}** tries")
                break
            elif guess.content >= str(number):
                await interaction.channel.send(f"Lower!")   
            elif guess.conten <= str(number):
                await interaction.channel.send(f"Higher!")  
        except:
            await interaction.channel.send("Please send a number!")  
    else:
        await interaction.channel.send(f"Game Lost ! You have run out of tries\nYou only get **{MAX_GUESSES}** guesses")
    
    

#3 function การทำงาน--------------------------------------------------------------------------------------------------------------------------------
async def heads_or_tails(interaction,choice):
    computer_choice = random.choice(["heads","tails"])
    if computer_choice == choice:
        await interaction.response.send_message(content=f"You chose Correctly! It was {computer_choice}")
    else:
        await interaction.response.send_message(content=f"You chose Inorrectly! It was {computer_choice}")

#2.function สำหรับสร้างปุ่่ม  
class Cf(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="heads",style=discord.ButtonStyle.red,custom_id="1") #style
    async def heads(self,interaction: discord.Interaction,Button: discord.ui.Button):
        await heads_or_tails(interaction,"heads")
        
    @discord.ui.button(label="tails",style=discord.ButtonStyle.green,custom_id="2") #style
    async def tails(self,interaction: discord.Interaction,Button: discord.ui.Button):
        await heads_or_tails(interaction,"tails")   

# class PersistentViewBot(commands.Bot):
#     def __init__(self):
#         intents = discord.Intents().all()
#         super().__init__(command_prefix=commands.when_mentioned_or('!'),intents=intents)
#     async def setup_hook(self) -> None:
#         self.add_view(Cf())
#         await self.tree.sync()
#client = PersistentViewBot()

#1.function หลัก
@client.tree.command(name="cf")
async def cf(interaction:discord.Interaction):
    embed = discord.Embed(title="**Coin_Flip**",description=f"Please choose **Heads** or **Tails**", color= discord.Color.yellow(),timestamp= datetime.now(timezone.utc))
    #await interaction.response.send_message(content="Please choose **Heads** or **Tails**",view=Cf()) 
    await interaction.response.send_message(embed=embed,view=Cf())
#
    
    
class SelectMenu(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label="Youtube",description="notified",emoji="▶️"),
                   discord.SelectOption(label="Twitch",description="notified",emoji="📺"),
                   discord.SelectOption(label="Twitter",description="notified",emoji="🐦‍⬛")]
        super().__init__(placeholder="What roles do you want?",options=options,min_values=1,max_values=3)    
    async def callback(self,interaction:discord.Interaction):
        values =", ".join(self.values)
        await interaction.response.send_message(content=f"Sucessfully given you **{values}** roles")
class Select(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectMenu())
    
@client.tree.command(name="select")
async def select(interaction:discord.Interaction):
    await interaction.response.send_message(content="Select your roles",view=Select())  
    
    

client.run(os.getenv("client_token"))