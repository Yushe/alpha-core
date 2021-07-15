from struct import unpack

from database.dbc.DbcDatabaseManager import DbcDatabaseManager
from network.packet.PacketReader import PacketReader
from network.packet.PacketWriter import *


class CreateItemHandler(object):

    @staticmethod
    def handle(world_session, socket, reader: PacketReader) -> int:
        if len(reader.data) >= 4:  # Avoid handling empty item packet.
            if not world_session.player_mgr.is_gm:
                return 0

            item_id = unpack('<I', reader.data[:4])[0]
            world_session.player_mgr.inventory.add_item(item_id)

        return 0
