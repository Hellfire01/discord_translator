from src.API.discord_api import DiscordApi
from src.API.google_translate_api import GoogleTranslateApi
from src.core_module import Core
from src.core_module.config.command_line_config import CommandLineConfig
from src.core_module.config.database_config import DatabaseConfig
from src.core_module.config.discord_config import DiscordConfig
from src.core_module.config.translate_config import TranslateConfig
from src.core_module.config.google_api_config import GoogleApiConfig
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
from src.instructions.instruction_implementation.auto_translation.automated.automated_translation_exec import AutomatedTranslationExec
from src.instructions.instruction_implementation.trusted_roles.trusted_roles import TrustedRoles
from src.security.security_filters import SecurityFilter
from src.security.filters.no_urls_filter import NoUrlsFilter
from src.security.filters.no_tags_filter import NoTagsFilter


def get_core() -> Core:
    commandline_config = CommandLineConfig(["!ot", "ouro-translator"])
    discord_config = DiscordConfig(GetDiscordToken.get_discord_token('discord_token.txt'))
    translate_config = TranslateConfig("=>")
    logger = Logger('log.txt')
    database_config = DatabaseConfig('database.db')
    database_access = DatabaseInterface(database_config, logger)
    google_api_config = GoogleApiConfig(api_sleep=1, max_message_len=2000, max_len_error_message="I apologise, I cannot translate more than 2000 characters at once")
    gtapi = GoogleTranslateApi(google_api_config)
    security_filters = get_security_filters()
    ret = Core(commandline_config, database_config, discord_config, translate_config, logger, database_access, google_api_config, gtapi, security_filters)
    return ret


def get_instructions(core):
    help_instruction = Help(core.commandline_config.first_keyword)
    ir = InstructionReferencer(core.commandline_config, help_instruction=help_instruction)
    ir.add_instruction(InstructionContainer(["-t", "translate", "--translate"], Translate(core.commandline_config, core.translate_config, core.google_translate_api)))
    ir.add_instruction(InstructionContainer(["-at", "auto-translation", "--auto-translation"], AutoTranslation(core.commandline_config, core.database_access)))
    ir.add_instruction(InstructionContainer(["-h", "help", "--help"], help_instruction))
    ir.add_instruction(InstructionContainer(["-l", "list", "--list"], InstructionList(ir.get_instruction_list)))
    ir.add_instruction(InstructionContainer(["-ll", "lang-list", "--lang-list"], ListLanguages()))
    ir.add_instruction(InstructionContainer(["-tr", "trusted-roles", "--trusted-roles"], TrustedRoles(core.commandline_config, core.database_access)))
    return InstructionExtractor(core.commandline_config.keywords, ir)


def get_list_of_automated_instructions(core):
    ret = []
    ret.append(AutomatedTranslationExec(core.logger, core.database_access, core.commandline_config, core.google_translate_api))
    return ret


def get_security_filters():
    ret = SecurityFilter()
    ret.add_filter(NoUrlsFilter())
    ret.add_filter(NoTagsFilter())
    return ret


core_instance = get_core()
instructions = get_instructions(core_instance)
automated_instructions = get_list_of_automated_instructions(core_instance)
discord_api = DiscordApi(core_instance, instructions, automated_instructions)
discord_api.run(core_instance.discord_config.discord_token)
