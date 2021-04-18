from network.packet.PacketReader import *
from game.world.managers.objects.player.ChannelManager import ChannelManager


class ChannelAnnounceHandler(object):

    @staticmethod
    def handle(world_session, socket, reader):
        channel = PacketReader.read_string(reader.data, 0).strip().capitalize()
        ChannelManager.toggle_announce(channel, world_session.player_mgr)
        return 0
