import discord


class DiscordApi(discord.Client):
    async def on_ready(self):
        print("bot is ready")

    async def on_message(self, message):
        if message.author == self.user:
            return  # ignore the bot itself to prevent feedback loop
        ret = ""
        if str(self.user.id) in message.content:
            instruction = self.instructions_extractor.help_instruction
        else:
            instruction = self.instructions_extractor.get_instruction(message.content)
        # auto run instructions is no instruction
        # self.database_interface.get_user(message.author.id)
        ret += instruction.run(message)
        if ret != "":
            await message.channel.send(ret)

    async def on_message_edit(self, before, after):
        pass

    def __init__(self, core, instructions_extractor, *args, **kwargs):
        self.core = core
        self.instructions_extractor = instructions_extractor
        super().__init__(*args, **kwargs)
