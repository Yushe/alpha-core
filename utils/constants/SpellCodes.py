from enum import IntEnum, IntFlag


class SpellTargetType(IntEnum):
    TARGET_TYPE_CASTER = 0x0
    TARGET_TYPE_UNIT = 0x1
    TARGET_TYPE_FRIENDLY = 0x2
    TARGET_TYPE_ENEMY = 0x3
    TARGET_TYPE_PARTY_MEMBER = 0x4
    TARGET_TYPE_ITEM = 0x5
    TARGET_TYPE_LOCATION = 0x6
    TARGET_TYPE_OBJECT = 0x7
    TARGET_TYPE_PET = 0x8
    TARGET_TYPE_MAINHAND_ITEM = 0x9
    TARGET_TYPE_OFFHAND_ITEM = 0xA
    TARGET_TYPE_PARTY = 0xB
    TARGET_TYPE_MULTIPLE_UNITS = 0xC
    TARGET_TYPE_MULTIPLE_ENEMIES = 0xD
    TARGET_TYPE_MULTIPLE_PARTY_MEMBERS = 0xE
    TARGET_TYPE_MASTER = 0xF
    NUM_SPELL_TARGET_TYPES = 0x10


class SpellCheckCastResult(IntEnum):
    SPELL_FAILED_AFFECTING_COMBAT = 0x0
    SPELL_FAILED_ALREADY_HAVE_CHARM = 0x1
    SPELL_FAILED_ALREADY_HAVE_SUMMON = 0x2
    SPELL_FAILED_ALREADY_OPEN = 0x3
    SPELL_FAILED_AURA_BOUNCED = 0x4
    SPELL_FAILED_BAD_IMPLICIT_TARGETS = 0x5
    SPELL_FAILED_BAD_TARGETS = 0x6
    SPELL_FAILED_CANT_BE_CHARMED = 0x7
    SPELL_FAILED_CANT_STEALTH = 0x8
    SPELL_FAILED_CASTER_AURASTATE = 0x9
    SPELL_FAILED_CASTER_DEAD = 0xA
    SPELL_FAILED_DONT_REPORT = 0xB
    SPELL_FAILED_EQUIPPED_ITEM = 0xC
    SPELL_FAILED_EQUIPPED_ITEM_CLASS = 0xD
    SPELL_FAILED_ERROR = 0xE
    SPELL_FAILED_FIZZLE = 0xF
    SPELL_FAILED_HUNGER_SATIATED = 0x10
    SPELL_FAILED_INTERRUPTED = 0x11
    SPELL_FAILED_INTERRUPTED_COMBAT = 0x12
    SPELL_FAILED_ITEM_ALREADY_ENCHANTED = 0x13
    SPELL_FAILED_ITEM_NOT_FOUND = 0x14
    SPELL_FAILED_ITEM_NOT_READY = 0x15
    SPELL_FAILED_LEVEL_REQUIREMENT = 0x16
    SPELL_FAILED_LINE_OF_SIGHT = 0x17
    SPELL_FAILED_LOWLEVEL = 0x18
    SPELL_FAILED_LOW_CASTLEVEL = 0x19
    SPELL_FAILED_MOVING = 0x1A
    SPELL_FAILED_NEED_AMMO = 0x1B
    SPELL_FAILED_NEED_AMMO_POUCH = 0x1C
    SPELL_FAILED_NEED_EXOTIC_AMMO = 0x1D
    SPELL_FAILED_NOPATH = 0x1E
    SPELL_FAILED_NOTSTANDING = 0x1F
    SPELL_FAILED_NOT_BEHIND = 0x20
    SPELL_FAILED_NOT_BEHIND_OR_SIDE = 0x21
    SPELL_FAILED_NOT_HERE = 0x22
    SPELL_FAILED_NOT_KNOWN = 0x23
    SPELL_FAILED_NOT_MOUNTED = 0x24
    SPELL_FAILED_NOT_READY = 0x25
    SPELL_FAILED_NOT_SHAPESHIFT = 0x26
    SPELL_FAILED_NOT_TRADING = 0x27
    SPELL_FAILED_NO_AMMO = 0x28
    SPELL_FAILED_NO_CHARGES_REMAIN = 0x29
    SPELL_FAILED_NO_ENDURANCE = 0x2A
    SPELL_FAILED_NO_PET = 0x2B
    SPELL_FAILED_NO_POWER = 0x2C
    SPELL_FAILED_ONLY_ABOVEWATER = 0x2D
    SPELL_FAILED_ONLY_DAYTIME = 0x2E
    SPELL_FAILED_ONLY_INDOORS = 0x2F
    SPELL_FAILED_ONLY_MOUNTED = 0x30
    SPELL_FAILED_ONLY_NIGHTTIME = 0x31
    SPELL_FAILED_ONLY_OUTDOORS = 0x32
    SPELL_FAILED_ONLY_SHAPESHIFT = 0x33
    SPELL_FAILED_ONLY_STEALTHED = 0x34
    SPELL_FAILED_ONLY_UNDERWATER = 0x35
    SPELL_FAILED_OUT_OF_RANGE = 0x36
    SPELL_FAILED_PACIFIED = 0x37
    SPELL_FAILED_REAGENTS = 0x38
    SPELL_FAILED_REQUIRES_SPELL_FOCUS = 0x39
    SPELL_FAILED_SILENCED = 0x3A
    SPELL_FAILED_SPELL_IN_PROGRESS = 0x3B
    SPELL_FAILED_SPELL_LEARNED = 0x3C
    SPELL_FAILED_SPELL_UNAVAILABLE = 0x3D
    SPELL_FAILED_STUNNED = 0x3E
    SPELL_FAILED_TARGETS_DEAD = 0x3F
    SPELL_FAILED_TARGET_AFFECTING_COMBAT = 0x40
    SPELL_FAILED_TARGET_AURASTATE = 0x41
    SPELL_FAILED_TARGET_ENEMY = 0x42
    SPELL_FAILED_TARGET_ENRAGED = 0x43
    SPELL_FAILED_TARGET_FRIENDLY = 0x44
    SPELL_FAILED_TARGET_IS_PLAYER = 0x45
    SPELL_FAILED_TARGET_NOT_DEAD = 0x46
    SPELL_FAILED_TARGET_NOT_IN_PARTY = 0x47
    SPELL_FAILED_TARGET_NO_POCKETS = 0x48
    SPELL_FAILED_THIRST_SATIATED = 0x49
    SPELL_FAILED_TOO_CLOSE = 0x4A
    SPELL_FAILED_TOTEMS = 0x4B
    SPELL_FAILED_TRY_AGAIN = 0x4C
    SPELL_FAILED_UNIT_NOT_ATSIDE = 0x4D
    SPELL_FAILED_UNIT_NOT_BEHIND = 0x4E
    SPELL_FAILED_UNIT_NOT_INFRONT = 0x4F
    SPELL_FAILED_NO_MOUNTS_ALLOWED = 0x50
    SPELL_FAILED_CHEST_IN_USE = 0x51
    SPELL_FAILED_NO_COMBO_POINTS = 0x52
    SPELL_FAILED_TARGET_NOT_PLAYER = 0x53
    SPELL_FAILED_TARGET_DUELING = 0x54
    SPELL_FAILED_NOTUNSHEATHED = 0x55
    SPELL_FAILED_NOT_FISHABLE = 0x56
    SPELL_FAILED_UNKNOWN = 0x57
    SPELL_NO_ERROR = 0xFF


class SpellCastStatus(IntEnum):
    CAST_SUCCESS = 0x0
    CAST_SUCCESS_KEEP_TRACKING = 0x1  # (HasAttribute(SpellAttribute.TrackTargetInCast) || HasAttribute(SpellAttributeEx.TargetTrackWhileChanneling) ?
    CAST_FAILED = 0x2


class SpellMissReason(IntEnum):
    MISS_REASON_NONE = 0x0
    MISS_REASON_PHYSICAL = 0x1
    MISS_REASON_RESIST = 0x2
    MISS_REASON_IMMUNE = 0x3
    MISS_REASON_EVADED = 0x4
    MISS_REASON_DODGED = 0x5
    MISS_REASON_PARRIED = 0x6
    MISS_REASON_BLOCKED = 0x7
    MISS_REASON_TEMPIMMUNE = 0x8
    MISS_REASON_DEFLECTED = 0x9


class SpellTargetMask(IntFlag):
    SELF = 0
    UNIT = 0x2
    PLAYER = 0x8  # ImplicitTarget.SingleParty only
    ITEM = 0x10
    SOURCE_LOCATION = 0x20
    DEST_LOCATION = 0x40
    ENEMIES = 0x80
    UNIT_SELF = 0x100  # ?, ImplicitTarget.SingleFriend & & ImplicitTarget.None only
    UNIT_DEAD = 0x400
    GAMEOBJECT = 0x800
    TRADE_ITEM = 0x1000
    TARGET_STRING = 0x2000
    GAMEOBJECT_ITEM = 0x4000

    UNIT_TARGET_MASK = 0x802
    ITEM_TARGET_MASK = 0x1010

    # Note: masks are (value & mask) != 0

    CAN_TARGET_ME = 0x50A  # && (m_attributesEx & 0x80000) == 0
    CAN_TARGET_DEAD = 0x400
    CAN_TARGET_ENEMIES = 0x480
    CAN_TARGET_FRIENDS = 0x500
    CAN_TARGET_ITEMS = 0x4010
    CAN_TARGET_TERRAIN = 0x60
    CAN_TARGET_OBJECTS = 0x4800
    CAN_TARGET_PARTY = 0x408
    CAN_TARGET_UNITS = 0x58A


class SpellAttributes(IntEnum):
    SPELL_ATTR_PROC_FAILURE_BURNS_CHARGE = 0x00000001  # 0
    SPELL_ATTR_RANGED = 0x00000002  # 1 All ranged abilites have this flag
    SPELL_ATTR_ON_NEXT_SWING_1 = 0x00000004  # 2 on next swing
    SPELL_ATTR_REQ_EXOTIC_AMMO = 0x00000008  # 3
    SPELL_ATTR_IS_ABILITY = 0x00000010  # 4 isAbility
    SPELL_ATTR_TRADESPELL = 0x00000020  # 5 trade spells will be added by client to a sublist of profession spell
    SPELL_ATTR_PASSIVE = 0x00000040  # 6 Passive spell
    SPELL_ATTR_DO_NOT_DISPLAY = 0x00000080  # 7 can't be linked in chat?
    SPELL_ATTR_DO_NOT_LOG = 0x00000100  # 8 hide created item in tooltip (for effect=24)
    SPELL_ATTR_HELD_ITEM_ONLY = 0x00000200  # 9
    SPELL_ATTR_ON_NEXT_SWING_2 = 0x00000400  # 10 on next swing 2
    SPELL_ATTR_WEARER_CASTS_PROC_TRIGGER = 0x00000800  # 11
    SPELL_ATTR_DAYTIME_ONLY = 0x00001000  # 12 only useable at daytime not set in 2.4.2
    SPELL_ATTR_NIGHT_ONLY = 0x00002000  # 13 only useable at night not set in 2.4.2
    SPELL_ATTR_INDOORS_ONLY = 0x00004000  # 14 only useable indoors not set in 2.4.2
    SPELL_ATTR_OUTDOORS_ONLY = 0x00008000  # 15 Only useable outdoors.
    SPELL_ATTR_NOT_SHAPESHIFT = 0x00010000  # 16 Not while shapeshifted
    SPELL_ATTR_ONLY_STEALTHED = 0x00020000  # 17 Must be in stealth
    SPELL_ATTR_DO_NOT_STEALTH = 0x00040000  # 18
    SPELL_ATTR_LEVEL_DAMAGE_CALCULATION = 0x00080000  # 19 spelldamage depends on caster level
    SPELL_ATTR_STOP_ATTACK_TARGET = 0x00100000  # 20 Stop attack after use this spell (and not begin attack if use)
    SPELL_ATTR_IMPOSSIBLE_DODGE_PARRY_BLOCK = 0x00200000  # 21 Cannot be dodged/parried/blocked
    SPELL_ATTR_SET_TRACKING_TARGET = 0x00400000  # 22 SetTrackingTarget
    SPELL_ATTR_ALLOW_CAST_WHILE_DEAD = 0x00800000  # 23 castable while dead
    SPELL_ATTR_CASTABLE_WHILE_MOUNTED = 0x01000000  # 24 castable while mounted
    SPELL_ATTR_DISABLED_WHILE_ACTIVE = 0x02000000  # 25 Activate and start cooldown after aura fade or remove summoned creature or go
    SPELL_ATTR_AURA_IS_DEBUFF = 0x04000000  # 26
    SPELL_ATTR_CASTABLE_WHILE_SITTING = 0x08000000  # 27 castable while sitting
    SPELL_ATTR_CANT_USED_IN_COMBAT = 0x10000000  # 28 Cannot be used in combat
    SPELL_ATTR_UNAFFECTED_BY_INVULNERABILITY = 0x20000000  # 29 unaffected by invulnerability (hmm possible not...)
    SPELL_ATTR_HEARTBEAT_RESIST = 0x40000000  # 30 breakable by damage?
    SPELL_ATTR_CANT_CANCEL = 0x80000000  # 31 positive aura can't be canceled


class SpellAttributesEx(IntEnum):
    SPELL_ATTR_EX_DISMISS_PET_FIRST = 0x00000001  # 0
    SPELL_ATTR_EX_DRAIN_ALL_POWER = 0x00000002  # 1 use all power (Only paladin Lay of Hands and Bunyanize)
    SPELL_ATTR_EX_CHANNELED_1 = 0x00000004  # 2 channeled 1
    SPELL_ATTR_EX_CANT_BE_REDIRECTED = 0x00000008  # 3
    SPELL_ATTR_EX_NO_SKILL_INCREASE = 0x00000010  # 4
    SPELL_ATTR_EX_NOT_BREAK_STEALTH = 0x00000020  # 5 Not break stealth
    SPELL_ATTR_EX_CHANNELED_2 = 0x00000040  # 6 channeled 2
    SPELL_ATTR_EX_NEGATIVE = 0x00000080  # 7
    SPELL_ATTR_EX_NOT_IN_COMBAT_TARGET = 0x00000100  # 8 Spell req target not to be in combat state
    SPELL_ATTR_EX_MELEE_COMBAT_START = 0x00000200  # 9
    SPELL_ATTR_EX_NO_THREAT = 0x00000400  # 10 no generates threat on cast 100%
    SPELL_ATTR_EX_AURA_UNIQUE = 0x00000800  # 11
    SPELL_ATTR_EX_FAILURE_BREAKS_STEALTH = 0x00001000  # 12 pickpocketing
    SPELL_ATTR_EX_FARSIGHT = 0x00002000  # 13 related to farsight
    SPELL_ATTR_EX_CHANNEL_TRACK_TARGET = 0x00004000  # 14
    SPELL_ATTR_EX_DISPEL_AURAS_ON_IMMUNITY = 0x00008000  # 15 remove auras on immunity
    SPELL_ATTR_EX_IMMUNITY_HOSTILE_FRIENDLY_EFFECTS = 0x00010000  # 16 unaffected by school immunity
    SPELL_ATTR_EX_NO_AUTOCAST_AI = 0x00020000  # 17 for auras SPELL_AURA_TRACK_CREATURES SPELL_AURA_TRACK_RESOURCES and SPELL_AURA_TRACK_STEALTHED select non-stacking tracking spells
    SPELL_ATTR_EX_PREVENTS_ANIM = 0x00040000  # 18
    SPELL_ATTR_EX_CANT_TARGET_SELF = 0x00080000  # 19
    SPELL_ATTR_EX_REQ_TARGET_COMBO_POINTS = 0x00100000  # 20 Req combo points on target
    SPELL_ATTR_EX_THREAT_ON_MISS = 0x00200000  # 21
    SPELL_ATTR_EX_REQ_COMBO_POINTS = 0x00400000  # 22 Use combo points (in 4.x not required combo point target selected)
    SPELL_ATTR_EX_IGNORE_OWNER_DEATH = 0x00800000  # 23
    SPELL_ATTR_EX_IS_FISHING = 0x01000000  # 24 Req fishing pole
    SPELL_ATTR_EX_AURA_STAYS_AFTER_COMBAT = 0x02000000  # 25
    SPELL_ATTR_EX_REQUIRE_ALL_TARGETS = 0x04000000  # 26
    SPELL_ATTR_EX_REFUND_POWER = 0x08000000  # 27
    SPELL_ATTR_EX_DONT_DISPLAY_IN_AURA_BAR = 0x10000000  # 28
    SPELL_ATTR_EX_CHANNEL_DISPLAY_SPELL_NAME = 0x20000000  # 29
    SPELL_ATTR_EX_ENABLE_AT_DODGE = 0x40000000  # 30 overpower
    SPELL_ATTR_EX_CAST_WHEN_LEARNED = 0x80000000  # 31 battle stance


class SpellSchools(IntEnum):
    SPELL_SCHOOL_NORMAL = 0  # < Physical Armor
    SPELL_SCHOOL_HOLY = 1
    SPELL_SCHOOL_FIRE = 2
    SPELL_SCHOOL_NATURE = 3
    SPELL_SCHOOL_FROST = 4
    SPELL_SCHOOL_SHADOW = 5


class SpellSchoolMask(IntEnum):
    SPELL_SCHOOL_MASK_NONE = 0x00  # doesn't exist
    SPELL_SCHOOL_MASK_NORMAL = (1 << SpellSchools.SPELL_SCHOOL_NORMAL)  # PHYSICAL (Armor)
    SPELL_SCHOOL_MASK_HOLY = (1 << SpellSchools.SPELL_SCHOOL_HOLY)
    SPELL_SCHOOL_MASK_FIRE = (1 << SpellSchools.SPELL_SCHOOL_FIRE)
    SPELL_SCHOOL_MASK_NATURE = (1 << SpellSchools.SPELL_SCHOOL_NATURE)
    SPELL_SCHOOL_MASK_FROST = (1 << SpellSchools.SPELL_SCHOOL_FROST)
    SPELL_SCHOOL_MASK_SHADOW = (1 << SpellSchools.SPELL_SCHOOL_SHADOW)
    SPELL_SCHOOL_MASK_SPELL = (
                SPELL_SCHOOL_MASK_FIRE | SPELL_SCHOOL_MASK_NATURE | SPELL_SCHOOL_MASK_FROST | SPELL_SCHOOL_MASK_SHADOW)
    SPELL_SCHOOL_MASK_MAGIC = (SPELL_SCHOOL_MASK_HOLY | SPELL_SCHOOL_MASK_SPELL)
    SPELL_SCHOOL_MASK_ALL = (SPELL_SCHOOL_MASK_NORMAL | SPELL_SCHOOL_MASK_MAGIC)


class SpellState(IntEnum):
    SPELL_STATE_PREPARING = 0  # cast time delay period non channeled spell
    SPELL_STATE_CASTING = 1  # channeled time period spell casting state
    SPELL_STATE_FINISHED = 2  # cast finished to success or fail
    SPELL_STATE_DELAYED = 3  # spell casted but need time to hit target(s)


class CurrentSpellType(IntEnum):
    CURRENT_MELEE_SPELL = 0
    CURRENT_GENERIC_SPELL = 1
    CURRENT_CHANNELED_SPELL = 2


class SpellEffects(IntEnum):
    SPELL_EFFECT_NONE = 0x0
    SPELL_EFFECT_INSTAKILL = 0x1
    SPELL_EFFECT_SCHOOL_DAMAGE = 0x2
    SPELL_EFFECT_DUMMY = 0x3
    # SPELL_EFFECT_PORTAL_TELEPORT = 0x4 #Not used
    SPELL_EFFECT_TELEPORT_UNITS = 0x5
    SPELL_EFFECT_APPLY_AURA = 0x6
    SPELL_EFFECT_POWER_DRAIN = 0x8
    SPELL_EFFECT_HEALTH_LEECH = 0x9
    SPELL_EFFECT_HEAL = 0xA
    SPELL_EFFECT_BIND = 0xB
    SPELL_EFFECT_PORTAL = 0xC
    # SPELL_EFFECT_RITUAL_BASE = 0xD #Not used
    # SPELL_EFFECT_RITUAL_SPECIALIZE = 0xE#Not used
    # SPELL_EFFECT_RITUAL_ACTIVATE_PORTAL = 0xF #Not used
    SPELL_EFFECT_QUEST_COMPLETE = 0x10
    SPELL_EFFECT_WEAPON_DAMAGE = 0x11
    SPELL_EFFECT_RESURRECT = 0x12
    SPELL_EFFECT_EXTRA_ATTACKS = 0x13
    SPELL_EFFECT_DODGE = 0x14
    SPELL_EFFECT_EVADE = 0x15
    SPELL_EFFECT_PARRY = 0x16
    SPELL_EFFECT_BLOCK = 0x17
    SPELL_EFFECT_CREATE_ITEM = 0x18
    SPELL_EFFECT_WEAPON = 0x19
    SPELL_EFFECT_DEFENSE = 0x1A
    SPELL_EFFECT_PERSISTENT_AREA_AURA = 0x1B
    SPELL_EFFECT_SUMMON = 0x1C
    SPELL_EFFECT_LEAP = 0x1D
    SPELL_EFFECT_ENERGIZE = 0x1E
    SPELL_EFFECT_WEAPON_PERC_DMG = 0x1F
    # SPELL_EFFECT_TRIGGER_MISSILE = 0x20 #Not used
    SPELL_EFFECT_OPEN_LOCK = 0x21
    SPELL_EFFECT_SUMMON_MOUNT = 0x22
    SPELL_EFFECT_APPLY_AREA_AURA = 0x23
    SPELL_EFFECT_LEARN_SPELL = 0x24
    SPELL_EFFECT_SPELL_DEFENSE = 0x25
    SPELL_EFFECT_DISPEL = 0x26
    SPELL_EFFECT_LANGUAGE = 0x27
    SPELL_EFFECT_DUAL_WIELD = 0x28
    SPELL_EFFECT_SUMMON_WILD = 0x29
    SPELL_EFFECT_SUMMON_GUARDIAN = 0x2A
    # SPELL_EFFECT_SKILL_RANK = 0x2B #Not used
    SPELL_EFFECT_SKILL_STEP = 0x2C
    # SPELL_EFFECT_SKILL_POTENTIAL = 0x2D #Not used
    SPELL_EFFECT_SPAWN = 0x2E
    SPELL_EFFECT_SPELL_CAST_UI = 0x2F
    SPELL_EFFECT_STEALTH = 0x30
    SPELL_EFFECT_DETECT = 0x31
    SPELL_EFFECT_SUMMON_OBJECT = 0x32
    # SPELL_EFFECT_FORCE_CRITICAL_HIT = 0x33 #Not used
    SPELL_EFFECT_GUARANTEE_HIT = 0x34
    SPELL_EFFECT_ENCHANT_ITEM_PERMANENT = 0x35
    SPELL_EFFECT_ENCHANT_ITEM_TEMPORARY = 0x36
    SPELL_EFFECT_TAME_CREATURE = 0x37
    SPELL_EFFECT_SUMMON_PET = 0x38
    SPELL_EFFECT_LEARN_PET_SPELL = 0x39
    SPELL_EFFECT_WEAPON_DAMAGE_PLUS = 0x3A
    SPELL_EFFECT_OPEN_LOCK_ITEM = 0x3B
    SPELL_EFFECT_PROFICIENCY = 0x3C
    SPELL_EFFECT_SEND_EVENT = 0x3D
    SPELL_EFFECT_POWER_BURN = 0x3E
    SPELL_EFFECT_THREAT = 0x3F
    SPELL_EFFECT_TRIGGER_SPELL = 0x40
    # SPELL_EFFECT_HEALTH_FUNNEL = 0x41 #Not used
    # SPELL_EFFECT_MANA_FUNNEL = 0x42 #Not used
    SPELL_EFFECT_HEAL_MAX_HEALTH = 0x43
    SPELL_EFFECT_INTERRUPT_CAST = 0x44
    SPELL_EFFECT_DISTRACT = 0x45
    SPELL_EFFECT_PULL = 0x46
    SPELL_EFFECT_PICKPOCKET = 0x47
    SPELL_EFFECT_ADD_FARSIGHT = 0x48
    SPELL_EFFECT_SUMMON_POSSESSED = 0x49
    SPELL_EFFECT_SUMMON_TOTEM = 0x4A
    # SPELL_EFFECT_HEAL_MECHANICAL = 0x4B #Not used
    SPELL_EFFECT_SUMMON_OBJECT_WILD = 0x4C
    SPELL_EFFECT_SCRIPT_EFFECT = 0x4D
    SPELL_EFFECT_ATTACK = 0x4E
    SPELL_EFFECT_SANCTUARY = 0x4F
    SPELL_EFFECT_ADD_COMBO_POINTS = 0x50
    SPELL_EFFECT_CREATE_HOUSE = 0x51
    SPELL_EFFECT_BIND_SIGHT = 0x52
    SPELL_EFFECT_DUEL = 0x53
    SPELL_EFFECT_STUCK = 0x54
    SPELL_EFFECT_SUMMON_PLAYER = 0x55
    SPELL_EFFECT_ACTIVATE_OBJECT = 0x56


class SpellInterruptFlags(IntEnum):
    SPELL_INTERRUPT_FLAG_MOVEMENT = 0x01
    SPELL_INTERRUPT_FLAG_DAMAGE = 0x02
    SPELL_INTERRUPT_FLAG_INTERRUPT = 0x04
    SPELL_INTERRUPT_FLAG_AUTOATTACK = 0x08
    SPELL_INTERRUPT_FLAG_ABORT_ON_DMG = 0x10  # _complete_ interrupt on direct damage
    # SPELL_INTERRUPT_UNK             = 0x20               # unk 564 of 727 spells having this spell start with "Glyph"


class SpellChannelInterruptFlags(IntEnum):
    CHANNEL_FLAG_DAMAGE = 0x0002
    CHANNEL_FLAG_MOVEMENT = 0x0008
    CHANNEL_FLAG_TURNING = 0x0010
    CHANNEL_FLAG_DAMAGE2 = 0x0080
    CHANNEL_FLAG_DELAY = 0x4000


class SpellAuraInterruptFlags(IntEnum):
    AURA_INTERRUPT_FLAG_UNK0 = 0x00000001  # 0    removed when getting hit by a negative spell?
    AURA_INTERRUPT_FLAG_DAMAGE = 0x00000002  # 1    removed by any damage
    AURA_INTERRUPT_FLAG_UNK2 = 0x00000004  # 2
    AURA_INTERRUPT_FLAG_MOVE = 0x00000008  # 3    removed by any movement
    AURA_INTERRUPT_FLAG_TURNING = 0x00000010  # 4    removed by any turning
    AURA_INTERRUPT_FLAG_ENTER_COMBAT = 0x00000020  # 5    removed by entering combat
    AURA_INTERRUPT_FLAG_NOT_MOUNTED = 0x00000040  # 6    removed by unmounting
    AURA_INTERRUPT_FLAG_NOT_ABOVEWATER = 0x00000080  # 7    removed by entering water
    AURA_INTERRUPT_FLAG_NOT_UNDERWATER = 0x00000100  # 8    removed by leaving water
    AURA_INTERRUPT_FLAG_NOT_SHEATHED = 0x00000200  # 9    removed by unsheathing
    AURA_INTERRUPT_FLAG_UNK10 = 0x00000400  # 10
    AURA_INTERRUPT_FLAG_UNK11 = 0x00000800  # 11
    AURA_INTERRUPT_FLAG_UNK12 = 0x00001000  # 12   removed by attack?
    AURA_INTERRUPT_FLAG_UNK13 = 0x00002000  # 13
    AURA_INTERRUPT_FLAG_UNK14 = 0x00004000  # 14
    AURA_INTERRUPT_FLAG_UNK15 = 0x00008000  # 15   removed by casting a spell?
    AURA_INTERRUPT_FLAG_UNK16 = 0x00010000  # 16
    AURA_INTERRUPT_FLAG_MOUNTING = 0x00020000  # 17   removed by mounting
    AURA_INTERRUPT_FLAG_NOT_SEATED = 0x00040000  # 18   removed by standing up (used by food and drink mostly and sleep/Fake Death like)
    AURA_INTERRUPT_FLAG_CHANGE_MAP = 0x00080000  # 19   leaving map/getting teleported
    AURA_INTERRUPT_FLAG_IMMUNE_OR_LOST_SELECTION = 0x00100000  # 20   removed by auras that make you invulnerable or make other to loose selection on you
    AURA_INTERRUPT_FLAG_UNK21 = 0x00200000  # 21
    AURA_INTERRUPT_FLAG_UNK22 = 0x00400000  # 22
    AURA_INTERRUPT_FLAG_ENTER_PVP_COMBAT = 0x00800000  # 23   removed by entering pvp combat
    AURA_INTERRUPT_FLAG_DIRECT_DAMAGE = 0x01000000  # 24   removed by any direct damage


class ShapeshiftForms(IntEnum):
    SHAPESHIFT_FORM_NONE = 0x0
    SHAPESHIFT_FORM_CAT = 0x1
    SHAPESHIFT_FORM_TREE = 0x2
    SHAPESHIFT_FORM_FLYING = 0x3
    SHAPESHIFT_FORM_AQUATIC = 0x4
    SHAPESHIFT_FORM_BEAR = 0x5
    SHAPESHIFT_FORM_AMBIENT = 0x6
    SHAPESHIFT_FORM_GHOUL = 0x7
    SHAPESHIFT_FORM_ZZOLDPLAINSWOLF = 0x8
    SHAPESHIFT_FORM_GHOSTWOLF = 0x10
    SHAPESHIFT_FORM_BATTLESTANCE = 0x11
    SHAPESHIFT_FORM_DEFENSIVESTANCE = 0x12
    SHAPESHIFT_FORM_BERSERKERSTANCE = 0x13


class AuraTypes(IntEnum):  # from cmangos-classic; entries over 88 don't exist in spell.dbc
    SPELL_AURA_NONE = 0
    SPELL_AURA_BIND_SIGHT = 1
    SPELL_AURA_MOD_POSSESS = 2
    SPELL_AURA_PERIODIC_DAMAGE = 3
    SPELL_AURA_DUMMY = 4
    SPELL_AURA_MOD_CONFUSE = 5
    SPELL_AURA_MOD_CHARM = 6
    SPELL_AURA_MOD_FEAR = 7
    SPELL_AURA_PERIODIC_HEAL = 8
    SPELL_AURA_MOD_ATTACKSPEED = 9
    SPELL_AURA_MOD_THREAT = 10
    SPELL_AURA_MOD_TAUNT = 11
    SPELL_AURA_MOD_STUN = 12
    SPELL_AURA_MOD_DAMAGE_DONE = 13
    SPELL_AURA_MOD_DAMAGE_TAKEN = 14
    SPELL_AURA_DAMAGE_SHIELD = 15
    SPELL_AURA_MOD_STEALTH = 16
    SPELL_AURA_MOD_STEALTH_DETECT = 17
    SPELL_AURA_MOD_INVISIBILITY = 18
    SPELL_AURA_MOD_INVISIBILITY_DETECTION = 19
#    SPELL_AURA_OBS_MOD_HEALTH = 20
#    SPELL_AURA_OBS_MOD_MANA = 21
    SPELL_AURA_MOD_RESISTANCE = 22
    SPELL_AURA_PERIODIC_TRIGGER_SPELL = 23
    SPELL_AURA_PERIODIC_ENERGIZE = 24
    SPELL_AURA_MOD_PACIFY = 25
    SPELL_AURA_MOD_ROOT = 26
    SPELL_AURA_MOD_SILENCE = 27
    SPELL_AURA_REFLECT_SPELLS = 28
    SPELL_AURA_MOD_STAT = 29
    SPELL_AURA_MOD_SKILL = 30
    SPELL_AURA_MOD_INCREASE_SPEED = 31
    SPELL_AURA_MOD_INCREASE_MOUNTED_SPEED = 32
    SPELL_AURA_MOD_DECREASE_SPEED = 33
    SPELL_AURA_MOD_INCREASE_HEALTH = 34
    SPELL_AURA_MOD_INCREASE_ENERGY = 35
    SPELL_AURA_MOD_SHAPESHIFT = 36
    SPELL_AURA_EFFECT_IMMUNITY = 37
    SPELL_AURA_STATE_IMMUNITY = 38
    SPELL_AURA_SCHOOL_IMMUNITY = 39
    SPELL_AURA_DAMAGE_IMMUNITY = 40
    SPELL_AURA_DISPEL_IMMUNITY = 41
    SPELL_AURA_PROC_TRIGGER_SPELL = 42
    SPELL_AURA_PROC_TRIGGER_DAMAGE = 43
    SPELL_AURA_TRACK_CREATURES = 44
    SPELL_AURA_TRACK_RESOURCES = 45
#    SPELL_AURA_46 = 46
    SPELL_AURA_MOD_PARRY_PERCENT = 47
#    SPELL_AURA_48 = 48
    SPELL_AURA_MOD_DODGE_PERCENT = 49
#    SPELL_AURA_MOD_BLOCK_SKILL = 50
    SPELL_AURA_MOD_BLOCK_PERCENT = 51
    SPELL_AURA_MOD_CRIT_PERCENT = 52
    SPELL_AURA_PERIODIC_LEECH = 53
    SPELL_AURA_MOD_HIT_CHANCE = 54
#    SPELL_AURA_MOD_SPELL_HIT_CHANCE = 55
    SPELL_AURA_TRANSFORM = 56
    SPELL_AURA_MOD_SPELL_CRIT_CHANCE = 57
    SPELL_AURA_MOD_INCREASE_SWIM_SPEED = 58
    SPELL_AURA_MOD_DAMAGE_DONE_CREATURE = 59
    SPELL_AURA_MOD_PACIFY_SILENCE = 60
    SPELL_AURA_MOD_SCALE = 61
#    SPELL_AURA_PERIODIC_HEALTH_FUNNEL = 62
    SPELL_AURA_PERIODIC_MANA_FUNNEL = 63
    SPELL_AURA_PERIODIC_MANA_LEECH = 64
    SPELL_AURA_MOD_CASTING_SPEED_NOT_STACK = 65
    SPELL_AURA_FEIGN_DEATH = 66
    SPELL_AURA_MOD_DISARM = 67
    SPELL_AURA_MOD_STALKED = 68
    SPELL_AURA_SCHOOL_ABSORB = 69
#    SPELL_AURA_EXTRA_ATTACKS = 70
    SPELL_AURA_MOD_SPELL_CRIT_CHANCE_SCHOOL = 71
#    SPELL_AURA_MOD_POWER_COST_SCHOOL_PCT = 72
    SPELL_AURA_MOD_POWER_COST_SCHOOL = 73
    SPELL_AURA_REFLECT_SPELLS_SCHOOL = 74
    SPELL_AURA_MOD_LANGUAGE = 75
    SPELL_AURA_FAR_SIGHT = 76
    SPELL_AURA_MECHANIC_IMMUNITY = 77
    SPELL_AURA_MOUNTED = 78
    SPELL_AURA_MOD_DAMAGE_PERCENT_DONE = 79
    SPELL_AURA_MOD_PERCENT_STAT = 80
    SPELL_AURA_SPLIT_DAMAGE_PCT = 81
    SPELL_AURA_WATER_BREATHING = 82
    SPELL_AURA_MOD_BASE_RESISTANCE = 83
    SPELL_AURA_MOD_REGEN = 84
    SPELL_AURA_MOD_POWER_REGEN = 85
    SPELL_AURA_CHANNEL_DEATH_ITEM = 86
    SPELL_AURA_MOD_DAMAGE_PERCENT_TAKEN = 87
    SPELL_AURA_MOD_HEALTH_REGEN_PERCENT = 88


class AuraSlots(IntEnum):
    AURA_SLOT_POSITIVE_AURA_START = 0  # 40 positive slots
    AURA_SLOT_HARMFUL_AURA_START = 40  # 16 harmful slots
    AURA_SLOT_PASSIVE_AURA_START = 56
    AURA_SLOT_END = 191  # Unlimited - not written to unit


class SpellImplicitTargets(IntEnum):
    TARGET_NOTHING = 0
    TARGET_SELF = 1
    TARGET_RANDOM_ENEMY_CHAIN_IN_AREA = 2  # Only one spell has this one but regardless it's a target type after all
    TARGET_UNIT_NEAR_CASTER = 4
    TARGET_PET = 5
    TARGET_CHAIN_DAMAGE = 6
    TARGET_AREAEFFECT_CUSTOM = 8
    TARGET_INNKEEPER_COORDINATES = 9  # Used in teleport to innkeeper spells
    TARGET_11 = 11  # Only used by "Word of Recall Other" (4)
    TARGET_ALL_ENEMY_IN_AREA = 15
    TARGET_ALL_ENEMY_IN_AREA_INSTANT = 16
    TARGET_TABLE_X_Y_Z_COORDINATES = 17  # Used in teleport spells and some other
    TARGET_EFFECT_SELECT = 18  # Highly depends on the spell effect
    TARGET_AROUND_CASTER_PARTY = 20
    TARGET_SELECTED_FRIEND = 21
    TARGET_AROUND_CASTER_ENEMY = 22  # Used only in TargetA target selection dependent from TargetB
    TARGET_SELECTED_GAMEOBJECT = 23
    TARGET_INFRONT = 24
    TARGET_DUEL_VS_PLAYER = 25  # Used when part of spell is casted on another target
    TARGET_GAMEOBJECT_AND_ITEM = 26
    TARGET_MASTER = 27  # not tested
    TARGET_AREA_EFFECT_ENEMY_CHANNEL = 28
    TARGET_ALL_FRIENDLY_UNITS_AROUND_CASTER = 30  # In TargetB used only with TARGET_ALL_AROUND_CASTER and in self casting range in TargetA
    TARGET_ALL_FRIENDLY_UNITS_IN_AREA = 31
    TARGET_MINION = 32  # Summons your pet to you.
    TARGET_ALL_PARTY = 33
    TARGET_ALL_PARTY_AROUND_CASTER_2 = 34  # Used in Tranquility
    TARGET_SINGLE_PARTY = 35
    TARGET_ALL_HOSTILE_UNITS_AROUND_CASTER = 36
    TARGET_AREAEFFECT_PARTY = 37  # Power infuses the target's party increasing their Shadow resistance by $s1 for $d.
    TARGET_SCRIPT = 38
    TARGET_SELF_FISHING = 39  # Equip a fishing pole and find a body of water to fish.
    TARGET_GAMEOBJECT_SCRIPT_NEAR_CASTER = 40  # 7728, 7729

class SpellMissInfo(IntEnum):
    MISS_NONE = 0x0
    MISS_PHYSICAL = 0x1
    MISS_RESIST = 0x2
    MISS_IMMUNE = 0x3
    MISS_EVADED = 0x4
    MISS_DODGED = 0x5
    MISS_PARRIED = 0x6
    MISS_BLOCKED = 0x7
    MISS_TEMPIMMUNE = 0x8
    MISS_DEFLECTED = 0x9
    MISS_NUMMISSTYPES = 0xA


class SpellDamageType(IntEnum):
    SPELL_TYPE_NONMELEE = 0
    SPELL_TYPE_DOT = 1
    SPELL_TYPE_HEAL = 2
    SPELL_TYPE_HEALDOT = 3
