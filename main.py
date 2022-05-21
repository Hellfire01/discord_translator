from src.API.discord_api import DiscordApi
from src.core_module import Core
from src.core_module.config.command_line_config import CommandLineConfig
from src.core_module.config.database_config import DatabaseConfig
from src.core_module.config.discord_config import DiscordConfig
from src.core_module.config.translate_config import TranslateConfig
from src.database.database_interface import DatabaseInterface
from src.utils.get_discord_token import GetDiscordToken
from src.logger.logger import Logger
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
    database_config = DatabaseConfig('database.db')
    database_access = DatabaseInterface(database_config)
    discord_config = DiscordConfig(GetDiscordToken.get_discord_token('discord_token.txt'))
    translate_config = TranslateConfig("=>")
    logger = Logger('log.txt')
    ret = Core(commandline_config, database_config, discord_config, translate_config, logger, database_access)
    return ret


def get_instructions(core):
    help_instruction = Help(core.commandline_config.first_keyword)
    ir = InstructionReferencer(core.commandline_config, help_instruction=help_instruction)
    ir.add_instruction(InstructionContainer(["-t", "translate", "--translate"], Translate(core.commandline_config, core.translate_config)))
    ir.add_instruction(InstructionContainer(["-at", "auto-translation", "--auto-translation"], AutoTranslation(core.commandline_config, core.database_access)))
    ir.add_instruction(InstructionContainer(["-h", "help", "--help"], help_instruction))
    ir.add_instruction(InstructionContainer(["-l", "list", "--list"], InstructionList(ir.get_instruction_list)))
    ir.add_instruction(InstructionContainer(["-ll", "lang-list", "--lang-list"], ListLanguages()))
    return InstructionExtractor(core.commandline_config.keywords, ir)


core_instance = get_core()
instructions = get_instructions(core_instance)
discord_api = DiscordApi(core_instance, instructions)
discord_api.run(core_instance.discord_config.discord_token)
