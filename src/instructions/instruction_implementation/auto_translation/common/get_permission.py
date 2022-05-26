

class GetPermission:
    @staticmethod
    def __check_if_owner(message):
        return message.author.id == message.guild.owner_id

    @staticmethod
    def __check_if_allowed_role(message):
        return False

    @staticmethod
    def check_if_allowed(message):
        return GetPermission.__check_if_owner(message) or GetPermission.__check_if_allowed_role(message)
