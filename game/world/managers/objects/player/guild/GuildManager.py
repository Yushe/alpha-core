from struct import pack
from game.world.managers.GridManager import GridManager
from network.packet.PacketWriter import PacketWriter, OpCode
from utils.constants.ObjectCodes import GuildRank, GuildCommandResults, GuildTypeCommand, GuildEvents, GuildChatMessageTypes
from game.world.managers.objects.player.guild.GuildPendingInvite import GuildPendingInvite


class GuildManager(object):
    GUILD_COUNT = 0 # TODO, generate/recycle guild IDs when we have db persistance
    GUILDS = {}
    PENDING_INVITES = {}

    def __init__(self, guild_name):
        GuildManager.GUILD_COUNT += 1
        self.guild_id = GuildManager.GUILD_COUNT #int32
        self.guild_name = guild_name
        self.members = {}
        self.ranks = {}
        self.guild_master = None
        self.created_at = 0 #Date
        self.motd = ''
        GuildManager.GUILDS[self.guild_id] = self

    def set_guild_master(self, player_mgr):
        previous_gm = self.guild_master
        self.guild_master = player_mgr
        self.ranks[player_mgr.guid] = GuildRank.GUILDRANK_GUILD_MASTER

        if previous_gm:
            self.ranks[previous_gm.guid] = GuildRank.GUILDRANK_OFFICER
            data = pack('<2B', GuildEvents.GUILD_EVENT_LEADER_CHANGED, 2)
            name_bytes = PacketWriter.string_to_bytes(previous_gm.player.name)
            data += pack(
                '<%us' % len(name_bytes),
                name_bytes,
            )

            name_bytes = PacketWriter.string_to_bytes(player_mgr.player.name)
            data += pack(
                '<%us' % len(name_bytes),
                name_bytes,
            )

            packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_EVENT, data)
            self.send_message_to_guild(packet, GuildChatMessageTypes.G_MSGTYPE_ALL)

        player_mgr.set_dirty()

    def set_motd(self, motd):
        self.motd = motd

        data = pack('<2B', GuildEvents.GUILD_EVENT_MOTD, 1)
        motd_bytes = PacketWriter.string_to_bytes(self.motd)
        data += pack(
            '<%us' % len(motd_bytes),
            motd_bytes,
        )

        packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_EVENT, data)
        self.send_message_to_guild(packet, GuildChatMessageTypes.G_MSGTYPE_ALL)

    def is_member(self, player_mgr):
        return player_mgr.guid in self.members

    def add_new_member(self, player_mgr, is_guild_master=False):
        self.members[player_mgr.guid] = player_mgr
        player_mgr.guild_manager = self
        if is_guild_master:
            self.set_guild_master(player_mgr)
        else:
            self.ranks[player_mgr.guid] = GuildRank.GUILDRANK_INITIATE

        data = pack('<2B', GuildEvents.GUILD_EVENT_JOINED, 1)
        name_bytes = PacketWriter.string_to_bytes(player_mgr.player.name)
        data += pack(
            '<%us' % len(name_bytes),
            name_bytes,
        )

        packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_EVENT, data)
        self.send_message_to_guild(packet, GuildChatMessageTypes.G_MSGTYPE_ALL)
        player_mgr.set_dirty()

    def remove_member(self, player_mgr):
        data = pack('<2B', GuildEvents.GUILD_EVENT_REMOVED, 2)
        target_name_bytes = PacketWriter.string_to_bytes(player_mgr.player.name)
        data += pack(
            '<%us' % len(target_name_bytes),
            target_name_bytes,
        )

        remover_name_bytes = PacketWriter.string_to_bytes(self.guild_master.player.name)
        data += pack(
            '<%us' % len(remover_name_bytes),
            remover_name_bytes,
        )

        packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_EVENT, data)
        self.send_message_to_guild(packet, GuildChatMessageTypes.G_MSGTYPE_ALL)

        # Pop it at the end, so he gets the above message.
        self.members.pop(player_mgr.guid)
        self.ranks.pop(player_mgr)
        player_mgr.guild_manager = None
        player_mgr.set_dirty()

    def leave(self, player_mgr):
        data = pack('<2B', GuildEvents.GUILD_EVENT_LEFT, 1)

        leaver_name_bytes = PacketWriter.string_to_bytes(player_mgr.player.name)
        data += pack(
            '<%us' % len(leaver_name_bytes),
            leaver_name_bytes,
        )

        packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_EVENT, data)
        self.send_message_to_guild(packet, GuildChatMessageTypes.G_MSGTYPE_ALL)

        self.members.pop(player_mgr.guid)
        self.ranks.pop(player_mgr.guid)
        player_mgr.guild_manager = None
        player_mgr.set_dirty()

    def disband(self):
        data = pack('<2B', GuildEvents.GUILD_EVENT_DISBANDED, 1)

        leaver_name_bytes = PacketWriter.string_to_bytes(self.guild_master.player.name)
        data += pack(
            '<%us' % len(leaver_name_bytes),
            leaver_name_bytes,
        )

        packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_EVENT, data)
        self.send_message_to_guild(packet, GuildChatMessageTypes.G_MSGTYPE_ALL)

        for m in self.members.values():
            m.guild_manager = None
            m.set_dirty()

        GuildManager.GUILDS.pop(self.guild_id)
        self.members.clear()
        self.ranks.clear()

    # TODO: Handle different msg types/permissions
    def send_message_to_guild(self, packet, message_type=None):
        for member in self.members.values():
            member.session.request.sendall(packet)

    def invite_member(self, player_mgr, invited_player):
        if invited_player.guid not in GuildManager.PENDING_INVITES:
            GuildManager.PENDING_INVITES[invited_player.guid] = GuildPendingInvite(player_mgr, invited_player)
            return True
        return False

    def get_guild_rank(self, player_mgr):
        return self.ranks[player_mgr.guid]

    def promote_rank(self, player_mgr):
        if player_mgr == self.guild_master:
            return False

        current_rank = int(self.ranks[player_mgr.guid])
        if current_rank == int(GuildRank.GUILDRANK_OFFICER):
            return False
        else:
            self.ranks[player_mgr.guid] = GuildRank((current_rank - 1))


        data = pack('<2B', GuildEvents.GUILD_EVENT_PROMOTION, 2)

        target_name_bytes = PacketWriter.string_to_bytes(player_mgr.player.name)
        data += pack(
            '<%us' % len(target_name_bytes),
            target_name_bytes,
        )

        rank_name_bytes = PacketWriter.string_to_bytes(GuildRank.short_name(self.ranks[player_mgr.guid]))
        data += pack(
            '<%us' % len(rank_name_bytes),
            rank_name_bytes,
        )

        packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_EVENT, data)
        self.send_message_to_guild(packet, GuildChatMessageTypes.G_MSGTYPE_ALL)
        player_mgr.set_dirty()

    def demote_rank(self, player_mgr):
        if player_mgr == self.guild_master:
            return False

        current_rank = int(self.ranks[player_mgr.guid])
        if current_rank == int(GuildRank.GUILDRANK_INITIATE): #Use initiate as lowest for now
            return False
        else:
            self.ranks[player_mgr.guid] = GuildRank((current_rank + 1))

        data = pack('<2B', GuildEvents.GUILD_EVENT_DEMOTION, 2)
        target_name_bytes = PacketWriter.string_to_bytes(player_mgr.player.name)
        data += pack(
            '<%us' % len(target_name_bytes),
            target_name_bytes,
        )

        rank_name_bytes = PacketWriter.string_to_bytes(GuildRank.short_name(self.ranks[player_mgr.guid]))
        data += pack(
            '<%us' % len(rank_name_bytes),
            rank_name_bytes,
        )

        packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_EVENT, data)
        self.send_message_to_guild(packet, GuildChatMessageTypes.G_MSGTYPE_ALL)
        player_mgr.set_dirty()

    @staticmethod
    def create_guild(player_mgr, guild_name):
        if not player_mgr.guild_manager:
            player_mgr.guild_manager = GuildManager(guild_name)
            player_mgr.guild_manager.add_new_member(player_mgr, is_guild_master=True)
        else:
            GuildManager.send_guild_command_result(player_mgr, GuildTypeCommand.GUILD_CREATE_S, '', GuildCommandResults.GUILD_ALREADY_IN_GUILD)

    @staticmethod
    def send_guild_command_result(player_mgr, command_type, message, command):
        message_bytes = PacketWriter.string_to_bytes(message)
        data = pack(
            '<I%usI' % len(message_bytes),
            command_type,
            message_bytes,
            command,
        )

        packet = PacketWriter.get_packet(OpCode.SMSG_GUILD_COMMAND_RESULT, data)
        player_mgr.session.request.sendall(packet)
