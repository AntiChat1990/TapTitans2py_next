from tap_titans.utils.base import Struct, field

from tap_titans.models.player import Artifacts, Card, ClanScrolls, HeroWeapons, Pets


class PlayerArtifact(Struct):
    artifact_id: str
    is_enchanted: bool
    level: str


class PlayerBadgeCount(Struct):
    zero: int = field(name="0")
    one: int = field(name="1")
    two: int = field(name="2")
    three: int = field(name="3")
    four: int = field(name="4")


class PlayerCard(Struct):
    level: int
    quantity_received: int
    quantity_spent: int
    skill_name: Card


class PlayerClanScroll(Struct):
    level: int = field(name="Level")
    scroll_id: str = field(name="ScrollId")


class PlayerHeroWeapon(Struct):
    level: int = field(name="Level")
    hero_id: str = field(name="HelperID")


class PlayerPet(Struct):
    level: int
    pet_id: str


class PlayerSeasonalArtifact(Struct):
    artifact_id: str
    is_enchanted: bool
    level: str


class PlayerSkill(Struct):
    level: int
    skill_id: str

class BoostedCards(Struct):
    slot_number: int
    skill_name: str
    category: str
    boost_level: int


class PlayerTitanCard(Struct):
    titan_id: str
    level: int
    quantity_received: int
    quantity_spent: int


class PlayerRaidResearchTree(Struct):
    armor_damage: float | None = field(name="ArmorDamage", default=None)
    body_damage: float | None = field(name="BodyDamage", default=None)
    chest_damage: float | None = field(name="ChestDamage", default=None)
    head_damage: float | None = field(name="HeadDamage", default=None)
    limb_damage: float | None = field(name="LimbDamage", default=None)
    raid_enemy_1_damage: float | None = field(name="RaidEnemy1Damage", default=None)
    raid_enemy_2_damage: float | None = field(name="RaidEnemy2Damage", default=None)
    raid_enemy_3_damage: float | None = field(name="RaidEnemy3Damage", default=None)
    raid_enemy_4_damage: float | None = field(name="RaidEnemy4Damage", default=None)
    raid_enemy_5_damage: float | None = field(name="RaidEnemy5Damage", default=None)
    raid_enemy_6_damage: float | None = field(name="RaidEnemy6Damage", default=None)
    raid_enemy_7_damage: float | None = field(name="RaidEnemy7Damage", default=None)
    raid_enemy_8_damage: float | None = field(name="RaidEnemy8Damage", default=None)


class GemstoneRaidResearchBonuses(Struct):
    additionalProp1: float | None = field(name="additionalProp1", default=None)


class PlayerData(Struct):
    player_code: str | None = field(default=None)
    country_code: str | None = field(default=None)
    max_stage: int | None = field(default=None)
    crafting_shards_spent: int | None = field(default=None)
    raid_wildcard_count: int | None = field(default=None)
    current_card_currency: int | None = field(default=None)
    additive_relic_multiplier: int | None = field(default=None)
    relics_received: str | None = field(default=None)
    relics_spent: str | None = field(default=None)
    summon_level: int | None = field(default=None)
    name: str | None = field(default=None)
    total_tournaments: int | None = field(default=None)
    undisputed_count: int | None = field(default=None)
    titan_points: str | None = field(default=None)
    total_raid_player_xp: int | None = field(default=None)
    player_raid_level: int | None = field(default=None)
    total_card_level: int | None = field(default=None)
    equipment_set_count: int | None = field(default=None)
    total_pet_levels: int | None = field(default=None)
    total_skill_points: int | None = field(default=None)
    total_clan_scrolls: int | None = field(default=None)
    challenge_tournaments_participation: int | None = field(default=None)
    challenge_tournaments_undisputed_count: int | None = field(default=None)
    current_world_id: int | None = field(default=None)
    clan_code: str | None = field(default=None)
    clan_name: str | None = field(default=None)
    role: str | None = field(default=None)
    weekly_ticket_count: int | None = field(default=None)
    titan_cards: tuple[PlayerTitanCard, ...] | None = field(default=None)
    raid_research_tree : PlayerRaidResearchTree | None = field(default=None)
    raid_research_bonuses: PlayerRaidResearchBonuses | None = field(default=None)
    loyalty_level: int | None = field(default=None)
    daily_raid_tickets: int | None = field(default=None)
    _previous_rank: str | float | None = field(name="previous_rank", default=None) # This field is rarely a float, I think when it's a zero value.
    artifacts: tuple[PlayerArtifact, ...] | None = field(default=None)
    seasonal_relics_received: str | None = field(default=None)
    seasonal_relics_spent: str | None = field(default=None)
    seasonal_relic_multiplier: int | None = field(default=None)
    seasonal_artifacts: tuple[PlayerSeasonalArtifact, ...] | None = field(default=None)
    cards: tuple[PlayerCard, ...] | None = field(default=None)
    pets: tuple[PlayerPet, ...] | None = field(default=None)
    badge_count: PlayerBadgeCount | None = field(default=None)
    hero_weapon: tuple[PlayerHeroWeapon, ...] | None = field(default=None)
    clan_scroll: tuple[PlayerClanScroll, ...] | None = field(default=None)
    skill_tree: tuple[PlayerSkill, ...] | None = field(default=None)
    boosted_cards: tuple[BoostedCards, ...] | None = field(default=None)
    equipment_set: tuple[str, ...] | None = field(default=None)
    total_hero_weapons: int | None = field(name="total_helper_weapons", default=None)

    @property
    def previous_rank(self) -> str | None:
        if self._previous_rank is None:
            return None

        return str(self._previous_rank)
