from src.discord_api import DiscordApi
from src.core_module import Core
from src.core_module.config.command_line_config import CommandLineConfig
from src.core_module.config.database_config import DatabaseConfig
from src.core_module.config.discord_config import DiscordConfig
from src.core_module.config.translate_config import TranslateConfig
from src.database.database_interface import DatabaseInterface
from src.utils.get_discord_token import GetDiscordToken
from src.instructions.instruction_management.instruction_extractor import InstructionExtractor
from src.instructions.instruction_management.instruction_referencer import InstructionReferencer
from src.instructions.instruction_management.instruction_container import InstructionContainer
from src.instructions.instruction_implementation.help import Help
from src.instructions.instruction_implementation.translate.translate import Translate
from src.instructions.instruction_implementation.auto_translation.auto_translation import AutoTranslation
from src.instructions.instruction_implementation.instruction_list import InstructionList
from src.instructions.instruction_implementation.list_languages import ListLanguages


def get_core() -> Core:
    commandline_config = CommandLineConfig(["!ot", "ouro-translator"])
    database_config = DatabaseConfig(DatabaseInterface())
    discord_config = DiscordConfig(GetDiscordToken.get_discord_token('discord_token.txt'))
    translate_config = TranslateConfig("=>")
    ret = Core(commandline_config, database_config, discord_config, translate_config)
    return ret


def get_instructions(keyword):
    help_instruction = Help()
    instruction_referencer = InstructionReferencer(help_instruction=help_instruction)
    instruction_referencer.add_instruction(InstructionContainer(["-t", "translate", "--translate"], Translate()))
    instruction_referencer.add_instruction(InstructionContainer(["-at", "auto-translation", "--auto-translation"], AutoTranslation()))
    instruction_referencer.add_instruction(InstructionContainer(["-h", "help", "--help"], help_instruction))
    instruction_referencer.add_instruction(InstructionContainer(["-l", "list", "--list"], InstructionList(instruction_referencer.get_instruction_list)))
    instruction_referencer.add_instruction(InstructionContainer(["-ll", "lang-list", "--lang-list"], ListLanguages()))
    return InstructionExtractor(keyword, instruction_referencer)


core = get_core()
instructions = get_instructions(core.command_line_config.keywords)
discord_api = DiscordApi(core, instructions)
discord_api.run()
