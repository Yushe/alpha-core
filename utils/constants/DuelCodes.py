from enum import IntEnum


class DUEL_STATUS(IntEnum):
    DUEL_STATUS_OUTOFBOUNDS = 0,
    DUEL_STATUS_INBOUNDS = 1

class DUEL_STATE(IntEnum):
    DUEL_STATE_REQUESTED = 0,
    DUEL_STATE_STARTED = 1,
    DUEL_STATE_FINISHED = 3

class DUEL_WINNER(IntEnum):
    DUEL_WINNER_KNOCKOUT = 0,
    DUEL_WINNER_RETREAT = 1
