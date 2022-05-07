from src.discord_api import DiscordApi
from src.global_settings import GlobalSettings
from src.database.database_interface import DatabaseInterface
from src.instructions.instruction_management.instruction_extractor import InstructionExtractor
from src.instructions.instruction_management.instruction_referencer import InstructionReferencer
from src.instructions.instruction_management.instruction_container import InstructionContainer
from src.instructions.instructions.help import Help
from src.instructions.instructions.translate.translate import Translate
from src.instructions.instructions.instruction_list import InstructionList
from src.instructions.instructions.list_languages import ListLanguages


def get_instructions(keyword):
    instruction_referencer = InstructionReferencer(help_instruction=help_instruction)
    instruction_referencer.add_instruction(InstructionContainer(["-t", "translate", "--translate"], Translate()))
    instruction_referencer.add_instruction(InstructionContainer(["-h", "help", "--help"], help_instruction))
    instruction_referencer.add_instruction(InstructionContainer(["-l", "list", "--list"], InstructionList(instruction_referencer.get_instruction_list)))
    instruction_referencer.add_instruction(InstructionContainer(["-ll", "lang-list", "--lang-list"], ListLanguages()))
    return InstructionExtractor(keyword, instruction_referencer)


global_settings = GlobalSettings.get_instance()
global_settings.set_values(instruction_keyword=["!ot", "ouro-translator"],
                           discord_token_filename='discord_token.txt',
                           translate_splitter="=>")
database_interface = DatabaseInterface()
help_instruction = Help()
discord_api = DiscordApi(database_interface, get_instructions(global_settings.instruction_keyword))
discord_api.run(global_settings.discord_token)
