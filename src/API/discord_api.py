import discord
from src.instructions.instruction_implementation.generic_instructions.no_instruction import NoInstruction


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
        if type(instruction) is NoInstruction:
            for automated_instruction in self.automated_instructions:
                ret += automated_instruction.run(message)
        else:
            ret += instruction.run(message)
        if ret != "":
            await message.channel.send(ret)

    async def on_message_edit(self, before, after):
        pass

    def __init__(self, core, instructions_extractor, automated_instructions, *args, **kwargs):
        self.core = core
        self.instructions_extractor = instructions_extractor
        self.automated_instructions = automated_instructions
        super().__init__(*args, **kwargs)
