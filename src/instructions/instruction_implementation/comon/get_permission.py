from itertools import product


class GetPermission:
    @staticmethod
    def check_if_owner(message):
        return message.author.id == message.guild.owner_id

    @staticmethod
    def __check_if_allowed_role(message, database_access):
        allowed_roles = database_access.get_trusted_roles(message.guild.id)
        user_roles = message.author.roles
        for (allowed_role, user_role) in product(allowed_roles, user_roles):
            if allowed_role.role_discord_id == user_role.id:
                return True
        return False

    @staticmethod
    def check_if_allowed(message, database_access):
        return GetPermission.check_if_owner(message) or GetPermission.__check_if_allowed_role(message, database_access)
