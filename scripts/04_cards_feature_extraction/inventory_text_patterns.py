import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "processed" / "cards" / "normalized" / "cards_normalized.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "cards" / "inventory" / "cards_text_inventory.json"
DEFAULT_MARKDOWN = PROJECT_ROOT / "data" / "processed" / "cards" / "inventory" / "cards_text_inventory.md"


def repo_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


TEXT_SOURCE_FIELDS = ("rules_lines", "effect_lines")
EXAMPLE_LIMIT = 6
VARIANT_LIMIT = 10
TOP_LINE_LIMIT = 50
TOP_OPENING_LIMIT = 40
TOP_PARAMETERIZED_LIMIT = 50
TOP_UNCLASSIFIED_LIMIT = 50
TOP_OVERLAP_LIMIT = 50
TOP_UNIT_LIMIT = 60
TOP_PARAMETERIZED_UNIT_LIMIT = 60
TOP_UNCLASSIFIED_UNIT_LIMIT = 60
TOP_UNIT_OVERLAP_LIMIT = 60
TOP_COMPLEX_LINE_LIMIT = 40
HIGH_FAMILY_OVERLAP_THRESHOLD = 4
HIGH_UNIT_FAMILY_OVERLAP_THRESHOLD = 3

BRACKET_TOKEN_RE = re.compile(r"\[([^\]]+)\]")
BRACKET_SEQUENCE_RE = re.compile(r"^(?:\[[^\]]+\])+")
RB_SYMBOL_RE = re.compile(r":rb_[a-z0-9_]+:", re.I)
NUMBER_RE = re.compile(r"\d+")
OPENING_PUNCT_RE = re.compile(r"[,.;(]")
DASH_BOUNDARY_RE = re.compile(
    r"\s+[" + re.escape("-" + chr(0x2013) + chr(0x2014)) + r"](?:\s+|$)"
)
MOJIBAKE_EM_DASH = chr(0x00E2) + chr(0x20AC) + chr(0x201D)
UNIT_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
UNIT_DASH_SPLIT_RE = re.compile(
    r"\s+(?:-|[" + re.escape(chr(0x2013) + chr(0x2014)) + r"]|" + re.escape(MOJIBAKE_EM_DASH) + r")\s+"
)
UNIT_THEN_SPLIT_RE = re.compile(r",?\s+then\s+", re.I)
UNIT_AND_EFFECT_SPLIT_RE = re.compile(
    r",?\s+and\s+(?=(?:draw|channel|play|give|gain|return|ready|exhaust|recall|kill|heal|attach|discard|banish|score|stun|counter|move|look|search|reveal|choose|create|deal)\b)",
    re.I,
)
ACTIVATION_SYMBOL_DELIMITER_RE = re.compile(r"::\s+")
ACTIVATION_COLON_DELIMITER_RE = re.compile(r"^(.{1,120}?):\s+(.+)$")

FLAG_KEYS = [
    "contains_bracket_keyword",
    "contains_rb_symbol",
    "contains_number",
    "starts_when",
    "starts_if",
    "starts_while",
    "starts_this",
    "starts_you_may",
    "contains_cant_cannot",
    "contains_instead",
    "contains_additional",
]

FAMILY_RULES: list[tuple[str, list[tuple[str, re.Pattern[str]]]]] = [
    (
        "counter_effect",
        [
            ("counter_word", re.compile(r"\bcounter(?:s|ed)?\b")),
        ],
    ),
    (
        "ready_exhaust_effect",
        [
            ("ready_word", re.compile(r"\bready\b|\breadied\b")),
            ("exhaust_word", re.compile(r"\bexhaust(?:s|ed|ing)?\b")),
        ],
    ),
    (
        "resource_add_ability",
        [
            ("add_resource_keyword", re.compile(r"\[add\]\s*:rb_[a-z0-9_]+:")),
            ("add_resources_reminder", re.compile(r"\badd resources\b")),
        ],
    ),
    (
        "choice_modal",
        [
            ("choose_one", re.compile(r"\bchoose one\b")),
            ("choose_up_to", re.compile(r"\bchoose up to\b")),
        ],
    ),
    (
        "stun_effect",
        [
            ("stun_keyword", re.compile(r"\[stun\]")),
            ("stun_word", re.compile(r"\bstun(?:s|ned|ning)?\b")),
        ],
    ),
    (
        "play_permission",
        [
            ("you_may_play_object", re.compile(r"\byou may play (?:me|this|it|them)\b")),
            ("may_play_this", re.compile(r"\bmay play this\b")),
            ("play_it", re.compile(r"\bplay it\b")),
            ("play_me_to_location", re.compile(r"\bplay me to\b")),
            ("play_from_zone", re.compile(r"\byou may play\b.*\bfrom\b")),
            ("passive_play_permission", re.compile(r"\b(?:can|may) be played to\b")),
            ("played_from_zone", re.compile(r"\bplayed from\b")),
        ],
    ),
    (
        "play_restriction",
        [
            ("cant_play", re.compile(r"\bcan't play\b|\bcannot play\b")),
            ("play_lockout", re.compile(r"\bopponents can't play\b|\bplayers can't play\b")),
        ],
    ),
    (
        "duration_modifier",
        [
            ("this_turn", re.compile(r"\bthis turn\b")),
            ("next_time", re.compile(r"\bthe next time\b")),
            ("for_as_long", re.compile(r"\bfor as long as\b")),
        ],
    ),
    (
        "target_selection",
        [
            ("choose_target", re.compile(r"\bchooses?\b")),
        ],
    ),
    (
        "keyword_modifier",
        [
            ("grant_keyword", re.compile(r"\b(?:give|gives|have|has|gain|gains|get|gets)\b.*\[[^\]]+\]")),
        ],
    ),
    (
        "buff_effect",
        [
            ("buff_word", re.compile(r"\bbuffs?\b|\bbuffed\b")),
        ],
    ),
    (
        "score_modifier",
        [
            ("score_points", re.compile(r"\bscore\b|\bscored\b|\bpoints?\b|\bvictory score\b")),
        ],
    ),
    (
        "symbol_option",
        [
            ("only_symbols", re.compile(r"^(?:\s|/|:rb_[a-z0-9_]+:)+$")),
        ],
    ),
    (
        "banish_effect",
        [
            ("banish_word", re.compile(r"\bbanish(?:es|ed|ing)?\b")),
        ],
    ),
    (
        "control_change",
        [
            ("gain_control", re.compile(r"\bgain control\b")),
            ("take_control", re.compile(r"\btake control\b")),
            ("lose_control", re.compile(r"\blose control\b")),
            ("control_until", re.compile(r"\bcontrol it until\b")),
            ("new_choices", re.compile(r"\bmake new choices\b")),
        ],
    ),
    (
        "usage_restriction",
        [
            ("use_only", re.compile(r"\buse only\b")),
            ("spend_only", re.compile(r"\bspend\b.*\bonly\b")),
        ],
    ),
    (
        "conditional_resolution",
        [
            ("if_you_do", re.compile(r"\bif you do\b")),
            ("when_they_do", re.compile(r"\bwhen they do\b")),
        ],
    ),
    (
        "turn_sequence",
        [
            ("extra_turn", re.compile(r"\btake a turn after\b")),
            ("turn_order", re.compile(r"\bstarting with the next player\b")),
        ],
    ),
    (
        "tag_reference",
        [
            ("tag_word", re.compile(r"\btags?\b")),
            ("known_tags", re.compile(r"\b(?:bird|cat|dog|poro|demacia|noxus|mech)\b")),
        ],
    ),
    (
        "modal_option",
        [
            ("single_card_type_option", re.compile(r"^(?:unit|gear|spell)$")),
            ("following_options", re.compile(r"\bdo one of the following\b|\bdo the following\b")),
        ],
    ),
    (
        "trait_identity",
        [
            ("identity_statement", re.compile(r"\bi am a\b|\bbecomes? a\b|\bis a\b")),
            ("mech_trait", re.compile(r"\bmech\b")),
            ("mighty_state", re.compile(r"\bmighty\b")),
        ],
    ),
    (
        "ability_sharing",
        [
            ("have_all_abilities", re.compile(r"\bhave all\b.*\babilities\b")),
            ("exhaust_abilities", re.compile(r":rb_exhaust: abilities")),
        ],
    ),
    (
        "deckbuilding_restriction",
        [
            ("deck_can_have", re.compile(r"\byour deck can have\b")),
        ],
    ),
    (
        "target_protection",
        [
            ("cant_be_chosen", re.compile(r"\bcan't be chosen\b|\bcannot be chosen\b")),
        ],
    ),
    (
        "type_exclusion",
        [
            ("not_cards", re.compile(r"\baren't cards\b|\bare not cards\b")),
            ("not_battlefield", re.compile(r"\baren't battlefield\b|\bare not battlefield\b")),
        ],
    ),
    (
        "contextual_clarification",
        [
            ("even_if", re.compile(r"\beven if\b")),
            ("including", re.compile(r"\bincluding\b|\bthis includes\b")),
        ],
    ),
    (
        "effect_suppression",
        [
            ("no_play_effects", re.compile(r"\bdon't get\b.*\beffects\b|\bdoesn't get\b.*\beffects\b")),
            ("play_effects", re.compile(r"\bplay effects\b")),
        ],
    ),
    (
        "entry_state",
        [
            ("enter_ready_or_exhausted", re.compile(r"\benters? (?:ready|exhausted)\b")),
            ("have_me_enter_ready", re.compile(r"\bhave me enter ready\b")),
        ],
    ),
    (
        "location_restriction",
        [
            ("here", re.compile(r"\bhere\b")),
            ("battlefield_location", re.compile(r"\b(?:at|to|from) a battlefield\b|\bbattlefield where\b")),
            ("base_location", re.compile(r"\b(?:in|to|from) (?:your|their|its|a) base\b")),
        ],
    ),
    (
        "movement_modifier",
        [
            ("move_word", re.compile(r"\bmove(?:s|d)?\b|\bmoving\b")),
            ("ganking_keyword", re.compile(r"\bganking\b")),
            ("recall_or_return", re.compile(r"\brecall\b|\breturn\b.*\bhands?\b")),
            ("put_into_hand", re.compile(r"\bput\b.*\bhand\b")),
            ("send_to_base", re.compile(r"\bsend (?:it|them) to base\b")),
        ],
    ),
    (
        "replacement_effect",
        [
            ("instead", re.compile(r"\binstead\b")),
            ("would", re.compile(r"\bwould\b")),
            ("rather_than", re.compile(r"\brather than\b")),
        ],
    ),
    (
        "effect_equivalence",
        [
            ("as_though", re.compile(r"\bas though\b")),
            ("counts_as", re.compile(r"\bcounts as\b")),
            ("is_also", re.compile(r"\bis also\b")),
            ("becomes", re.compile(r"\bbecomes?\b")),
            ("treated_as", re.compile(r"\btreated as\b")),
        ],
    ),
    (
        "hide_modifier",
        [
            ("hide_word", re.compile(r"\bhide\b|\bhidden\b")),
            ("trap_word", re.compile(r"\btrap\b")),
        ],
    ),
    (
        "copy_effect",
        [
            ("copy_word", re.compile(r"\bcopy\b|\bcopies\b|\bcopied\b|\bcopying\b")),
        ],
    ),
    (
        "combat_modifier",
        [
            ("attack_defend", re.compile(r"\battack(?:er|ing|s)?\b|\bdefend(?:er|ing|s)?\b")),
            ("combat", re.compile(r"\bcombat\b|\bcombat damage\b|\bexcess damage\b")),
            ("conquer_hold", re.compile(r"\bconquer\b|\bhold\b")),
            ("combat_keyword", re.compile(r"\[(?:assault|shield|tank|backline)[^\]]*\]")),
        ],
    ),
    (
        "trigger_modifier",
        [
            ("additional_time", re.compile(r"\badditional time\b|\bone additional\b")),
            ("repeat", re.compile(r"\brepeat\b")),
            ("trigger_word", re.compile(r"\btrigger(?:s|ed)?\b")),
            ("get_effect", re.compile(r"\bget the effect\b|\beffect again\b")),
        ],
    ),
    (
        "token_creation",
        [
            ("token_word", re.compile(r"\btokens?\b")),
            ("create_word", re.compile(r"\bcreate(?:s|d)?\b")),
            ("summon_word", re.compile(r"\bsummon(?:s|ed)?\b")),
        ],
    ),
    (
        "cost_modifier",
        [
            ("cost_word", re.compile(r"\bcosts?\b")),
            ("pay_word", re.compile(r"\bpay\b")),
            ("less_word", re.compile(r"\bless\b")),
            ("additional_cost", re.compile(r"\badditional cost\b")),
            ("spend_xp", re.compile(r"\bspend \d+ xp\b")),
            ("spent_resource", re.compile(r"\bspent\b.*:rb_[a-z0-9_]+:")),
        ],
    ),
    (
        "resource_generation",
        [
            ("channel_rune", re.compile(r"\bchannel(?:s|ed)? \d+ rune\b")),
            ("gain_xp", re.compile(r"\bgain \d+ xp\b")),
            ("gain_symbol_resource", re.compile(r"\bgain (?:\d+ )?:rb_[a-z0-9_]+:")),
        ],
    ),
    (
        "stat_modifier",
        [
            ("might_delta", re.compile(r"[+-]\d+\s*:rb_might:")),
            ("gets_delta", re.compile(r"\bgets? [+-]\d+")),
            ("give_delta", re.compile(r"\bgive\b.*[+-]\d+")),
            ("might_or_power", re.compile(r"\b(?:might|power)\b")),
        ],
    ),
    (
        "timing_window",
        [
            ("action_reaction", re.compile(r"^\[(?:action|reaction)\]")),
            ("play_timing", re.compile(r"\bplay any time\b|\bplay on your turn\b")),
            ("use_timing", re.compile(r"\buse on your turn\b")),
            ("phase_timing", re.compile(r"\bat the (?:start|end) of\b|\bbefore scoring\b")),
            ("as_you_play", re.compile(r"\bas you play\b")),
        ],
    ),
    (
        "keyword_reminder",
        [
            ("starts_with_bracketed_keyword", re.compile(r"^\[[^\]]+\]")),
        ],
    ),
    (
        "attachment_modifier",
        [
            ("attach_word", re.compile(r"\battach\b|\battached\b|\bdetach\b")),
            ("equip_word", re.compile(r"\bequip\b|\bequipment\b")),
        ],
    ),
    (
        "deck_manipulation",
        [
            ("draw_discard", re.compile(r"\bdraws?\b|\bdiscards?\b")),
            ("recycle", re.compile(r"\brecycles?\b")),
            ("top_deck", re.compile(r"\blook at the top\b|\bmain deck\b")),
            ("search_reveal", re.compile(r"\bsearch(?:es)?\b|\breveals?\b")),
            ("put_back", re.compile(r"\bput\b.*\bback\b")),
        ],
    ),
    (
        "damage_effect",
        [
            ("deal_damage", re.compile(r"\bdeal \d+\b|\bdamage\b")),
        ],
    ),
    (
        "removal_or_healing",
        [
            ("kill_heal_die", re.compile(r"\bkill(?:s|ed|ing)?\b|\bheal(?:s|ed|ing)?\b|\bdie\b|\bdies\b")),
        ],
    ),
    (
        "xp_progression",
        [
            ("xp_word", re.compile(r"\bxp\b")),
            ("level_word", re.compile(r"\blevel\b")),
        ],
    ),
]


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def clean_line(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value).strip())


def normalize_text(value: Any) -> str:
    text = unicodedata.normalize("NFKC", clean_line(value))
    replacements = {
        chr(0x2018): "'",
        chr(0x2019): "'",
        chr(0x201C): '"',
        chr(0x201D): '"',
        chr(0x2013): "-",
        chr(0x2014): "-",
        MOJIBAKE_EM_DASH: "-",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return re.sub(r"\s+", " ", text.strip()).casefold()


def parameterize_line(normalized_line: str) -> str:
    text = RB_SYMBOL_RE.sub("{rb_symbol}", normalized_line)
    text = re.sub(r"\[([^\]\d]+?)\s+\d+\]", r"[\1 {number}]", text)
    text = NUMBER_RE.sub("{number}", text)
    return re.sub(r"\s+", " ", text.strip())


def split_parenthetical_blocks(line: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    cursor = 0
    for match in re.finditer(r"\(([^()]*)\)", line):
        before = line[cursor : match.start()].strip()
        if before:
            blocks.append((before, "main"))
        reminder = match.group(1).strip()
        if reminder:
            blocks.append((reminder, "reminder"))
        cursor = match.end()

    after = line[cursor:].strip()
    if after:
        blocks.append((after, "main"))
    return blocks or [(line, "main")]


def split_activation(segment: str) -> list[tuple[str, str]]:
    match = ACTIVATION_SYMBOL_DELIMITER_RE.search(segment)
    if match:
        prefix = segment[: match.start() + 1].strip(" ,")
        suffix = segment[match.end() :].strip()
        if prefix and suffix and is_activation_cost(prefix):
            return [(prefix, "activation_cost"), (suffix, "main")]

    match = ACTIVATION_COLON_DELIMITER_RE.match(segment)
    if not match:
        return [(segment, "main")]

    prefix = match.group(1).strip()
    suffix = match.group(2).strip()
    if re.search(r":rb_[a-z0-9_]+$", normalize_text(prefix)):
        return [(segment, "main")]
    if prefix and suffix and is_activation_cost(prefix):
        return [(prefix, "activation_cost"), (suffix, "main")]
    return [(segment, "main")]


def is_activation_cost(text: str) -> bool:
    normalized = normalize_text(text)
    if ":rb_" in normalized:
        return True
    if re.search(r"\b(?:exhaust|spend|pay|discard|kill this|banish this|sacrifice)\b", normalized):
        return True
    if re.search(r"^\[(?:action|reaction)\](?:\[>\])?", normalized):
        return True
    return False


def split_main_unit_text(segment: str) -> list[str]:
    parts = [segment]
    for splitter in [UNIT_DASH_SPLIT_RE, UNIT_SENTENCE_SPLIT_RE, UNIT_THEN_SPLIT_RE, UNIT_AND_EFFECT_SPLIT_RE]:
        next_parts = []
        for part in parts:
            next_parts.extend(piece.strip() for piece in splitter.split(part) if piece.strip())
        parts = next_parts
    cleaned = [part.strip(" ;") for part in parts]
    return [part for part in cleaned if re.search(r"[A-Za-z0-9\[]", part)]


def unit_kind(unit_text: str, context: str) -> str:
    if context == "reminder":
        return "reminder"
    if context == "activation_cost":
        return "activation_cost"

    normalized = normalize_text(unit_text)
    if re.fullmatch(r"\[(?:action|reaction)\](?:\[>\])?", normalized):
        return "timing"
    if re.fullmatch(r"\[[^\]]+\](?:\[>\])?", normalized):
        return "keyword_marker"
    if starts_with_phrase(normalized, "choose one"):
        return "choice_header"
    if starts_with_phrase(normalized, "when") or normalized.startswith("at the start") or normalized.startswith("at the end"):
        return "timing"
    if starts_with_phrase(normalized, "if") or starts_with_phrase(normalized, "while") or starts_with_phrase(normalized, "as"):
        return "condition"
    if "can't" in normalized or "cannot" in normalized or re.search(r"\bonly\b|\bmust\b", normalized):
        return "restriction"
    return "effect"


def text_unit(unit_text: str, context: str, unit_index: int) -> dict[str, Any]:
    normalized_unit = normalize_text(unit_text)
    kind = unit_kind(unit_text, context)
    family_suggestions = candidate_family_suggestions(normalized_unit)
    if kind == "activation_cost" and not any(item["family"] == "cost_modifier" for item in family_suggestions):
        family_suggestions.append({"family": "cost_modifier", "reasons": ["activation_cost_context"]})
    return {
        "unit_index": unit_index,
        "unit_text": clean_line(unit_text),
        "normalized_unit": normalized_unit,
        "parameterized_unit": parameterize_line(normalized_unit),
        "unit_kind": kind,
        "candidate_families": [item["family"] for item in family_suggestions],
        "candidate_family_reasons": {
            item["family"]: item["reasons"] for item in family_suggestions
        },
    }


def derive_text_units(line: str) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    for block_text, block_context in split_parenthetical_blocks(line):
        if block_context == "reminder":
            for part in split_main_unit_text(block_text):
                units.append(text_unit(part, "reminder", len(units)))
            continue

        for activation_text, activation_context in split_activation(block_text):
            if activation_context == "activation_cost":
                units.append(text_unit(activation_text, "activation_cost", len(units)))
                continue
            for part in split_main_unit_text(activation_text):
                units.append(text_unit(part, "main", len(units)))

    return units or [text_unit(line, "main", 0)]


def starts_with_phrase(normalized_line: str, phrase: str) -> bool:
    return normalized_line == phrase or normalized_line.startswith(phrase + " ")


def line_opening(line: str) -> str:
    text = clean_line(line).replace(MOJIBAKE_EM_DASH, " - ")
    if not text:
        return ""

    bracket_match = BRACKET_SEQUENCE_RE.match(text)
    if bracket_match:
        return bracket_match.group(0)

    split_positions = []
    punct_match = OPENING_PUNCT_RE.search(text)
    dash_match = DASH_BOUNDARY_RE.search(text)
    if punct_match:
        split_positions.append(punct_match.start())
    if dash_match:
        split_positions.append(dash_match.start())

    if split_positions:
        opening = text[: min(split_positions)].strip()
    else:
        words = text.split()
        opening = " ".join(words[:8]) if len(words) > 8 else text

    return opening.rstrip(":").strip()


def superficial_flags(line: str, normalized_line: str) -> dict[str, bool]:
    return {
        "contains_bracket_keyword": bool(BRACKET_TOKEN_RE.search(line)),
        "contains_rb_symbol": bool(RB_SYMBOL_RE.search(line)),
        "contains_number": bool(NUMBER_RE.search(line)),
        "starts_when": starts_with_phrase(normalized_line, "when"),
        "starts_if": starts_with_phrase(normalized_line, "if"),
        "starts_while": starts_with_phrase(normalized_line, "while"),
        "starts_this": starts_with_phrase(normalized_line, "this"),
        "starts_you_may": starts_with_phrase(normalized_line, "you may"),
        "contains_cant_cannot": bool(re.search(r"\b(?:can't|cannot)\b", normalized_line)),
        "contains_instead": bool(re.search(r"\binstead\b", normalized_line)),
        "contains_additional": bool(re.search(r"\badditional\b", normalized_line)),
    }


def surface_tokens(line: str) -> dict[str, list[str]]:
    return {
        "bracket_keywords": [match.group(1).strip() for match in BRACKET_TOKEN_RE.finditer(line)],
        "rb_symbols": [match.group(0) for match in RB_SYMBOL_RE.finditer(line)],
        "numbers": [match.group(0) for match in NUMBER_RE.finditer(line)],
    }


def candidate_family_suggestions(normalized_line: str) -> list[dict[str, Any]]:
    suggestions = []
    for family, rules in FAMILY_RULES:
        reasons = [reason for reason, pattern in rules if pattern.search(normalized_line)]
        if reasons:
            suggestions.append({"family": family, "reasons": reasons})
    return suggestions


def card_example(card: dict[str, Any], source_field: str, line_index: int) -> dict[str, Any]:
    example = {
        "play_id": card["play_id"],
        "name": card["name"],
        "source_field": source_field,
        "line_index": line_index,
    }
    public_codes = card.get("public_codes")
    if public_codes:
        example["public_code"] = public_codes[0]
    return example


def add_example(bucket: dict[str, Any], card: dict[str, Any], source_field: str, line_index: int) -> None:
    seen_cards = bucket["_example_card_ids"]
    play_id = card["play_id"]
    if play_id in seen_cards or len(bucket["_examples"]) >= EXAMPLE_LIMIT:
        return
    seen_cards.add(play_id)
    bucket["_examples"].append(card_example(card, source_field, line_index))


def build_inventory(cards: list[dict[str, Any]]) -> dict[str, Any]:
    buckets: dict[str, dict[str, Any]] = {}
    text_line_count = 0
    cards_with_text: set[str] = set()

    for card in cards:
        for source_field in TEXT_SOURCE_FIELDS:
            for line_index, raw_line in enumerate(card.get(source_field, [])):
                line = clean_line(raw_line)
                if not line:
                    continue

                text_line_count += 1
                cards_with_text.add(card["play_id"])
                normalized_line = normalize_text(line)
                parameterized = parameterize_line(normalized_line)
                opening = line_opening(line)
                normalized_opening = normalize_text(opening)

                if normalized_line not in buckets:
                    flags = superficial_flags(line, normalized_line)
                    family_suggestions = candidate_family_suggestions(normalized_line)
                    text_units = derive_text_units(line)
                    buckets[normalized_line] = {
                        "original_line": line,
                        "normalized_line": normalized_line,
                        "parameterized_line": parameterized,
                        "opening": opening,
                        "normalized_opening": normalized_opening,
                        "flags": flags,
                        "surface_tokens": surface_tokens(line),
                        "candidate_families": [item["family"] for item in family_suggestions],
                        "candidate_family_reasons": {
                            item["family"]: item["reasons"] for item in family_suggestions
                        },
                        "text_units": text_units,
                        "_frequency": 0,
                        "_source_field_counts": Counter(),
                        "_card_ids": set(),
                        "_variant_counts": Counter(),
                        "_examples": [],
                        "_example_card_ids": set(),
                    }

                bucket = buckets[normalized_line]
                bucket["_frequency"] += 1
                bucket["_source_field_counts"][source_field] += 1
                bucket["_card_ids"].add(card["play_id"])
                bucket["_variant_counts"][line] += 1
                add_example(bucket, card, source_field, line_index)

    line_records = []
    for bucket in buckets.values():
        source_field_counts = dict(sorted(bucket["_source_field_counts"].items()))
        variants = [
            {"line": line, "frequency": count}
            for line, count in bucket["_variant_counts"].most_common(VARIANT_LIMIT)
        ]
        record = {
            "original_line": bucket["original_line"],
            "normalized_line": bucket["normalized_line"],
            "parameterized_line": bucket["parameterized_line"],
            "frequency": bucket["_frequency"],
            "source_fields": sorted(source_field_counts),
            "source_field_counts": source_field_counts,
            "distinct_card_count": len(bucket["_card_ids"]),
            "example_cards": bucket["_examples"],
            "opening": bucket["opening"],
            "normalized_opening": bucket["normalized_opening"],
            "flags": bucket["flags"],
            "surface_tokens": bucket["surface_tokens"],
            "candidate_families": bucket["candidate_families"],
            "candidate_family_reasons": bucket["candidate_family_reasons"],
            "text_units": bucket["text_units"],
            "text_unit_count": len(bucket["text_units"]),
            "original_line_variants": variants,
            "_card_ids": bucket["_card_ids"],
        }
        line_records.append(record)

    line_records.sort(key=lambda item: (-item["frequency"], item["normalized_line"]))

    summary = build_summary(cards, text_line_count, cards_with_text, line_records)
    openings = build_opening_summary(line_records)
    parameterized_lines = build_parameterized_line_summary(line_records)
    families = build_family_summary(line_records)
    unclassified_lines = select_unclassified_lines(line_records)
    high_family_overlap_lines = select_high_family_overlap_lines(line_records)
    unit_inventory = build_text_unit_inventory(line_records)
    summary.update(unit_inventory["summary"])

    for record in line_records:
        del record["_card_ids"]

    return {
        "inputs": {
            "cards": repo_path(DEFAULT_INPUT),
            "card_count": len(cards),
            "source_fields": list(TEXT_SOURCE_FIELDS),
        },
        "summary": summary,
        "candidate_families": families,
        "openings": openings,
        "parameterized_lines": parameterized_lines,
        "text_units": unit_inventory["text_units"],
        "parameterized_units": unit_inventory["parameterized_units"],
        "unclassified_units": unit_inventory["unclassified_units"],
        "high_family_overlap_units": unit_inventory["high_family_overlap_units"],
        "complex_lines_decomposed": unit_inventory["complex_lines_decomposed"],
        "unclassified_lines": unclassified_lines,
        "high_family_overlap_lines": high_family_overlap_lines,
        "lines": line_records,
    }


def build_summary(
    cards: list[dict[str, Any]],
    text_line_count: int,
    cards_with_text: set[str],
    line_records: list[dict[str, Any]],
) -> dict[str, Any]:
    source_field_counts: Counter[str] = Counter()
    flag_occurrences: Counter[str] = Counter()
    flag_unique_lines: Counter[str] = Counter()
    family_occurrences: Counter[str] = Counter()
    family_unique_lines: Counter[str] = Counter()
    family_count_distribution: dict[int, dict[str, int]] = defaultdict(
        lambda: {"occurrence_count": 0, "unique_normalized_line_count": 0}
    )
    unclassified_occurrence_count = 0
    unclassified_unique_count = 0
    high_overlap_occurrence_count = 0
    high_overlap_unique_count = 0

    for record in line_records:
        for source_field, count in record["source_field_counts"].items():
            source_field_counts[source_field] += count
        for flag in FLAG_KEYS:
            if record["flags"].get(flag):
                flag_occurrences[flag] += record["frequency"]
                flag_unique_lines[flag] += 1
        for family in record["candidate_families"]:
            family_occurrences[family] += record["frequency"]
            family_unique_lines[family] += 1
        family_count = len(record["candidate_families"])
        family_count_distribution[family_count]["occurrence_count"] += record["frequency"]
        family_count_distribution[family_count]["unique_normalized_line_count"] += 1
        if family_count == 0:
            unclassified_occurrence_count += record["frequency"]
            unclassified_unique_count += 1
        if family_count >= HIGH_FAMILY_OVERLAP_THRESHOLD:
            high_overlap_occurrence_count += record["frequency"]
            high_overlap_unique_count += 1

    return {
        "card_count": len(cards),
        "cards_with_text_count": len(cards_with_text),
        "text_line_count": text_line_count,
        "unique_normalized_line_count": len(line_records),
        "unique_parameterized_line_count": len(
            {record["parameterized_line"] for record in line_records}
        ),
        "source_field_counts": dict(sorted(source_field_counts.items())),
        "unclassified_line_count": unclassified_unique_count,
        "unclassified_occurrence_count": unclassified_occurrence_count,
        "high_family_overlap_threshold": HIGH_FAMILY_OVERLAP_THRESHOLD,
        "high_family_overlap_line_count": high_overlap_unique_count,
        "high_family_overlap_occurrence_count": high_overlap_occurrence_count,
        "candidate_family_count_distribution": {
            str(count): family_count_distribution[count]
            for count in sorted(family_count_distribution)
        },
        "flag_counts": {
            flag: {
                "occurrence_count": flag_occurrences[flag],
                "unique_normalized_line_count": flag_unique_lines[flag],
            }
            for flag in FLAG_KEYS
        },
        "candidate_family_counts": {
            family: {
                "occurrence_count": family_occurrences[family],
                "unique_normalized_line_count": family_unique_lines[family],
            }
            for family in sorted(family_occurrences)
        },
    }


def build_opening_summary(line_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[str, dict[str, Any]] = {}
    for record in line_records:
        key = record["normalized_opening"]
        if key not in buckets:
            buckets[key] = {
                "opening": record["opening"],
                "normalized_opening": key,
                "frequency": 0,
                "unique_normalized_line_count": 0,
                "source_field_counts": Counter(),
                "card_ids": set(),
                "examples": [],
            }
        bucket = buckets[key]
        bucket["frequency"] += record["frequency"]
        bucket["unique_normalized_line_count"] += 1
        bucket["card_ids"].update(record["_card_ids"])
        for source_field, count in record["source_field_counts"].items():
            bucket["source_field_counts"][source_field] += count
        if len(bucket["examples"]) < EXAMPLE_LIMIT:
            bucket["examples"].append(
                {
                    "line": record["original_line"],
                    "frequency": record["frequency"],
                    "example_cards": record["example_cards"][:2],
                }
            )

    rows = []
    for bucket in buckets.values():
        rows.append(
            {
                "opening": bucket["opening"],
                "normalized_opening": bucket["normalized_opening"],
                "frequency": bucket["frequency"],
                "unique_normalized_line_count": bucket["unique_normalized_line_count"],
                "distinct_card_count": len(bucket["card_ids"]),
                "source_field_counts": dict(sorted(bucket["source_field_counts"].items())),
                "examples": bucket["examples"],
            }
        )
    rows.sort(key=lambda item: (-item["frequency"], item["normalized_opening"]))
    return rows


def build_parameterized_line_summary(line_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[str, dict[str, Any]] = {}
    for record in line_records:
        key = record["parameterized_line"]
        if key not in buckets:
            buckets[key] = {
                "parameterized_line": key,
                "frequency": 0,
                "unique_normalized_line_count": 0,
                "source_field_counts": Counter(),
                "candidate_family_counts": Counter(),
                "card_ids": set(),
                "examples": [],
            }
        bucket = buckets[key]
        bucket["frequency"] += record["frequency"]
        bucket["unique_normalized_line_count"] += 1
        bucket["card_ids"].update(record["_card_ids"])
        for source_field, count in record["source_field_counts"].items():
            bucket["source_field_counts"][source_field] += count
        for family in record["candidate_families"]:
            bucket["candidate_family_counts"][family] += record["frequency"]
        if len(bucket["examples"]) < EXAMPLE_LIMIT:
            bucket["examples"].append(
                {
                    "line": record["original_line"],
                    "frequency": record["frequency"],
                    "candidate_families": record["candidate_families"],
                    "example_cards": record["example_cards"][:2],
                }
            )

    rows = []
    for bucket in buckets.values():
        rows.append(
            {
                "parameterized_line": bucket["parameterized_line"],
                "frequency": bucket["frequency"],
                "unique_normalized_line_count": bucket["unique_normalized_line_count"],
                "distinct_card_count": len(bucket["card_ids"]),
                "source_field_counts": dict(sorted(bucket["source_field_counts"].items())),
                "candidate_family_counts": dict(bucket["candidate_family_counts"].most_common()),
                "examples": bucket["examples"],
            }
        )
    rows.sort(
        key=lambda item: (
            -item["frequency"],
            -item["unique_normalized_line_count"],
            item["parameterized_line"],
        )
    )
    return rows


def build_family_summary(line_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[str, dict[str, Any]] = {}
    for record in line_records:
        for family in record["candidate_families"]:
            if family not in buckets:
                buckets[family] = {
                    "family": family,
                    "frequency": 0,
                    "unique_normalized_line_count": 0,
                    "card_ids": set(),
                    "examples": [],
                }
            bucket = buckets[family]
            bucket["frequency"] += record["frequency"]
            bucket["unique_normalized_line_count"] += 1
            bucket["card_ids"].update(record["_card_ids"])
            if len(bucket["examples"]) < EXAMPLE_LIMIT:
                bucket["examples"].append(
                    {
                        "line": record["original_line"],
                        "frequency": record["frequency"],
                        "reasons": record["candidate_family_reasons"].get(family, []),
                        "example_cards": record["example_cards"][:2],
                    }
                )

    rows = []
    for bucket in buckets.values():
        rows.append(
            {
                "family": bucket["family"],
                "occurrence_count": bucket["frequency"],
                "unique_normalized_line_count": bucket["unique_normalized_line_count"],
                "distinct_card_count": len(bucket["card_ids"]),
                "examples": bucket["examples"],
            }
        )
    rows.sort(key=lambda item: (-item["occurrence_count"], item["family"]))
    return rows


def public_line_record(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "frequency": record["frequency"],
        "distinct_card_count": record["distinct_card_count"],
        "source_fields": record["source_fields"],
        "opening": record["opening"],
        "original_line": record["original_line"],
        "normalized_line": record["normalized_line"],
        "parameterized_line": record["parameterized_line"],
        "candidate_families": record["candidate_families"],
        "candidate_family_count": len(record["candidate_families"]),
        "flags": record["flags"],
        "example_cards": record["example_cards"],
    }


def select_unclassified_lines(line_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = [public_line_record(record) for record in line_records if not record["candidate_families"]]
    rows.sort(key=lambda item: (-item["frequency"], item["normalized_line"]))
    return rows[:TOP_UNCLASSIFIED_LIMIT]


def select_high_family_overlap_lines(line_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = [
        public_line_record(record)
        for record in line_records
        if len(record["candidate_families"]) >= HIGH_FAMILY_OVERLAP_THRESHOLD
    ]
    rows.sort(key=lambda item: (-item["candidate_family_count"], -item["frequency"], item["normalized_line"]))
    return rows[:TOP_OVERLAP_LIMIT]


def build_text_unit_inventory(line_records: list[dict[str, Any]]) -> dict[str, Any]:
    unit_buckets: dict[str, dict[str, Any]] = {}
    parameterized_buckets: dict[str, dict[str, Any]] = {}
    total_occurrences = 0

    for line_record in line_records:
        for unit in line_record["text_units"]:
            total_occurrences += line_record["frequency"]
            add_unit_to_bucket(unit_buckets, unit["normalized_unit"], unit, line_record)
            add_unit_to_bucket(parameterized_buckets, unit["parameterized_unit"], unit, line_record)

    text_units = finalize_unit_buckets(unit_buckets, "normalized_unit")
    parameterized_units = finalize_unit_buckets(parameterized_buckets, "parameterized_unit")
    kind_counts = build_unit_kind_counts(text_units)
    family_count_distribution = build_unit_family_count_distribution(text_units)

    unclassified_units = [
        public_unit_record(unit)
        for unit in text_units
        if not unit["candidate_families"]
    ][:TOP_UNCLASSIFIED_UNIT_LIMIT]
    high_family_overlap_units = [
        public_unit_record(unit)
        for unit in text_units
        if unit["candidate_family_count"] >= HIGH_UNIT_FAMILY_OVERLAP_THRESHOLD
    ][:TOP_UNIT_OVERLAP_LIMIT]

    summary = {
        "text_unit_occurrence_count": total_occurrences,
        "unique_normalized_unit_count": len(text_units),
        "unique_parameterized_unit_count": len(parameterized_units),
        "unclassified_unit_count": sum(1 for unit in text_units if not unit["candidate_families"]),
        "unclassified_unit_occurrence_count": sum(
            unit["occurrence_count"] for unit in text_units if not unit["candidate_families"]
        ),
        "high_unit_family_overlap_threshold": HIGH_UNIT_FAMILY_OVERLAP_THRESHOLD,
        "high_unit_family_overlap_count": sum(
            1 for unit in text_units if unit["candidate_family_count"] >= HIGH_UNIT_FAMILY_OVERLAP_THRESHOLD
        ),
        "high_unit_family_overlap_occurrence_count": sum(
            unit["occurrence_count"]
            for unit in text_units
            if unit["candidate_family_count"] >= HIGH_UNIT_FAMILY_OVERLAP_THRESHOLD
        ),
        "unit_kind_counts": kind_counts,
        "unit_family_count_distribution": family_count_distribution,
    }

    return {
        "summary": summary,
        "text_units": text_units,
        "parameterized_units": parameterized_units,
        "unclassified_units": unclassified_units,
        "high_family_overlap_units": high_family_overlap_units,
        "complex_lines_decomposed": select_complex_lines_decomposed(line_records),
    }


def add_unit_to_bucket(
    buckets: dict[str, dict[str, Any]],
    key: str,
    unit: dict[str, Any],
    line_record: dict[str, Any],
) -> None:
    if key not in buckets:
        buckets[key] = {
            "unit_text": unit["unit_text"],
            "normalized_unit": unit["normalized_unit"],
            "parameterized_unit": unit["parameterized_unit"],
            "unit_kind_counts": Counter(),
            "candidate_family_counts": Counter(),
            "candidate_family_reasons": defaultdict(Counter),
            "occurrence_count": 0,
            "line_keys": set(),
            "card_ids": set(),
            "examples": [],
        }

    bucket = buckets[key]
    bucket["occurrence_count"] += line_record["frequency"]
    bucket["line_keys"].add(line_record["normalized_line"])
    bucket["card_ids"].update(line_record["_card_ids"])
    bucket["unit_kind_counts"][unit["unit_kind"]] += line_record["frequency"]
    for family in unit["candidate_families"]:
        bucket["candidate_family_counts"][family] += line_record["frequency"]
        for reason in unit["candidate_family_reasons"].get(family, []):
            bucket["candidate_family_reasons"][family][reason] += line_record["frequency"]

    if len(bucket["examples"]) < EXAMPLE_LIMIT:
        bucket["examples"].append(
            {
                "unit_text": unit["unit_text"],
                "unit_kind": unit["unit_kind"],
                "line": line_record["original_line"],
                "line_frequency": line_record["frequency"],
                "example_cards": line_record["example_cards"][:2],
            }
        )


def finalize_unit_buckets(buckets: dict[str, dict[str, Any]], key_name: str) -> list[dict[str, Any]]:
    rows = []
    for key, bucket in buckets.items():
        candidate_family_reasons = {
            family: [reason for reason, _count in reasons.most_common()]
            for family, reasons in bucket["candidate_family_reasons"].items()
        }
        candidate_family_counts = dict(bucket["candidate_family_counts"].most_common())
        candidate_families = list(candidate_family_counts)
        row = {
            key_name: key,
            "unit_text": bucket["unit_text"],
            "normalized_unit": bucket["normalized_unit"],
            "parameterized_unit": bucket["parameterized_unit"],
            "occurrence_count": bucket["occurrence_count"],
            "unique_normalized_line_count": len(bucket["line_keys"]),
            "distinct_card_count": len(bucket["card_ids"]),
            "unit_kind_counts": dict(bucket["unit_kind_counts"].most_common()),
            "primary_unit_kind": bucket["unit_kind_counts"].most_common(1)[0][0],
            "candidate_families": candidate_families,
            "candidate_family_count": len(candidate_families),
            "candidate_family_counts": candidate_family_counts,
            "candidate_family_reasons": candidate_family_reasons,
            "examples": bucket["examples"],
        }
        rows.append(row)

    rows.sort(
        key=lambda item: (
            -item["occurrence_count"],
            -item["unique_normalized_line_count"],
            item[key_name],
        )
    )
    return rows


def build_unit_kind_counts(text_units: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    occurrence_counts: Counter[str] = Counter()
    unique_counts: Counter[str] = Counter()
    for unit in text_units:
        for kind, count in unit["unit_kind_counts"].items():
            occurrence_counts[kind] += count
            unique_counts[kind] += 1
    return {
        kind: {
            "occurrence_count": occurrence_counts[kind],
            "unique_normalized_unit_count": unique_counts[kind],
        }
        for kind in sorted(occurrence_counts)
    }


def build_unit_family_count_distribution(text_units: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    distribution: dict[int, dict[str, int]] = defaultdict(
        lambda: {"occurrence_count": 0, "unique_normalized_unit_count": 0}
    )
    for unit in text_units:
        family_count = unit["candidate_family_count"]
        distribution[family_count]["occurrence_count"] += unit["occurrence_count"]
        distribution[family_count]["unique_normalized_unit_count"] += 1
    return {str(count): distribution[count] for count in sorted(distribution)}


def public_unit_record(unit: dict[str, Any]) -> dict[str, Any]:
    return {
        "unit_text": unit["unit_text"],
        "normalized_unit": unit["normalized_unit"],
        "parameterized_unit": unit["parameterized_unit"],
        "occurrence_count": unit["occurrence_count"],
        "unique_normalized_line_count": unit["unique_normalized_line_count"],
        "distinct_card_count": unit["distinct_card_count"],
        "primary_unit_kind": unit["primary_unit_kind"],
        "unit_kind_counts": unit["unit_kind_counts"],
        "candidate_families": unit["candidate_families"],
        "candidate_family_count": unit["candidate_family_count"],
        "candidate_family_counts": unit["candidate_family_counts"],
        "examples": unit["examples"],
    }


def select_complex_lines_decomposed(line_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = [
        {
            **public_line_record(record),
            "text_unit_count": record["text_unit_count"],
            "text_units": record["text_units"],
        }
        for record in line_records
        if record["text_unit_count"] > 1
    ]
    rows.sort(
        key=lambda item: (
            -item["text_unit_count"],
            -item["candidate_family_count"],
            -item["frequency"],
            item["normalized_line"],
        )
    )
    return rows[:TOP_COMPLEX_LINE_LIMIT]


def md_escape(value: Any) -> str:
    text = str(value).replace("\n", " ")
    return text.replace("|", "\\|")


def markdown_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        output.append("| " + " | ".join(md_escape(value) for value in row) + " |")
    return output


def markdown_report(inventory: dict[str, Any]) -> str:
    summary = inventory["summary"]
    lines = [
        "# Cards Text Inventory",
        "",
        "Pure inventory of card text lines from `data/processed/cards/normalized/cards_normalized.json`.",
        "It does not read extracted facts, reports, or web relations. Candidate families are heuristic suggestions only.",
        "",
        "## Summary",
        "",
        f"- Cards: {summary['card_count']}",
        f"- Cards with text: {summary['cards_with_text_count']}",
        f"- Text lines: {summary['text_line_count']}",
        f"- Unique normalized lines: {summary['unique_normalized_line_count']}",
        f"- Unique parameterized lines: {summary['unique_parameterized_line_count']}",
        f"- Text unit occurrences: {summary['text_unit_occurrence_count']}",
        f"- Unique normalized units: {summary['unique_normalized_unit_count']}",
        f"- Unique parameterized units: {summary['unique_parameterized_unit_count']}",
        f"- Lines without candidate family: {summary['unclassified_line_count']} unique / {summary['unclassified_occurrence_count']} occurrences",
        f"- Lines with {summary['high_family_overlap_threshold']}+ candidate families: {summary['high_family_overlap_line_count']} unique / {summary['high_family_overlap_occurrence_count']} occurrences",
        f"- Units without candidate family: {summary['unclassified_unit_count']} unique / {summary['unclassified_unit_occurrence_count']} occurrences",
        f"- Units with {summary['high_unit_family_overlap_threshold']}+ candidate families: {summary['high_unit_family_overlap_count']} unique / {summary['high_unit_family_overlap_occurrence_count']} occurrences",
        f"- Source fields: {json.dumps(summary['source_field_counts'], ensure_ascii=False, sort_keys=True)}",
        "",
        "## Surface Flags",
        "",
    ]

    flag_rows = [
        [
            flag,
            data["occurrence_count"],
            data["unique_normalized_line_count"],
        ]
        for flag, data in sorted(
            summary["flag_counts"].items(),
            key=lambda item: (-item[1]["occurrence_count"], item[0]),
        )
    ]
    lines.extend(markdown_table(["Flag", "Occurrences", "Unique lines"], flag_rows))

    lines.extend(["", "## Candidate Family Suggestions", ""])
    family_rows = [
        [
            item["family"],
            item["occurrence_count"],
            item["unique_normalized_line_count"],
            item["distinct_card_count"],
        ]
        for item in inventory["candidate_families"]
    ]
    lines.extend(markdown_table(["Family", "Occurrences", "Unique lines", "Cards"], family_rows))

    lines.extend(["", "## Candidate Family Count Distribution", ""])
    distribution_rows = [
        [
            count,
            data["occurrence_count"],
            data["unique_normalized_line_count"],
        ]
        for count, data in summary["candidate_family_count_distribution"].items()
    ]
    lines.extend(markdown_table(["Family count", "Occurrences", "Unique lines"], distribution_rows))

    lines.extend(["", "## Unit Kind Counts", ""])
    unit_kind_rows = [
        [
            kind,
            data["occurrence_count"],
            data["unique_normalized_unit_count"],
        ]
        for kind, data in sorted(
            summary["unit_kind_counts"].items(),
            key=lambda item: (-item[1]["occurrence_count"], item[0]),
        )
    ]
    lines.extend(markdown_table(["Unit kind", "Occurrences", "Unique units"], unit_kind_rows))

    lines.extend(["", "## Unit Candidate Family Count Distribution", ""])
    unit_distribution_rows = [
        [
            count,
            data["occurrence_count"],
            data["unique_normalized_unit_count"],
        ]
        for count, data in summary["unit_family_count_distribution"].items()
    ]
    lines.extend(markdown_table(["Family count", "Occurrences", "Unique units"], unit_distribution_rows))

    lines.extend(["", "## Top Openings", ""])
    opening_rows = [
        [
            item["opening"],
            item["frequency"],
            item["unique_normalized_line_count"],
            item["distinct_card_count"],
            json.dumps(item["source_field_counts"], ensure_ascii=False, sort_keys=True),
        ]
        for item in inventory["openings"][:TOP_OPENING_LIMIT]
    ]
    lines.extend(markdown_table(["Opening", "Occurrences", "Unique lines", "Cards", "Sources"], opening_rows))

    lines.extend(["", "## Top Parameterized Lines", ""])
    parameterized_rows = [
        [
            item["frequency"],
            item["unique_normalized_line_count"],
            item["distinct_card_count"],
            item["parameterized_line"],
            ", ".join(item["candidate_family_counts"].keys()),
        ]
        for item in inventory["parameterized_lines"][:TOP_PARAMETERIZED_LIMIT]
    ]
    lines.extend(
        markdown_table(
            ["Occurrences", "Unique lines", "Cards", "Parameterized line", "Candidate families"],
            parameterized_rows,
        )
    )

    lines.extend(["", "## Top Atomic Units", ""])
    unit_rows = [
        [
            item["occurrence_count"],
            item["unique_normalized_line_count"],
            item["distinct_card_count"],
            item["primary_unit_kind"],
            item["unit_text"],
            item["parameterized_unit"],
            ", ".join(item["candidate_families"]),
        ]
        for item in inventory["text_units"][:TOP_UNIT_LIMIT]
    ]
    lines.extend(
        markdown_table(
            [
                "Occurrences",
                "Lines",
                "Cards",
                "Kind",
                "Unit",
                "Parameterized unit",
                "Candidate families",
            ],
            unit_rows,
        )
    )

    lines.extend(["", "## Top Parameterized Atomic Units", ""])
    parameterized_unit_rows = [
        [
            item["occurrence_count"],
            item["unique_normalized_line_count"],
            item["distinct_card_count"],
            item["primary_unit_kind"],
            item["parameterized_unit"],
            ", ".join(item["candidate_family_counts"].keys()),
        ]
        for item in inventory["parameterized_units"][:TOP_PARAMETERIZED_UNIT_LIMIT]
    ]
    lines.extend(
        markdown_table(
            ["Occurrences", "Lines", "Cards", "Kind", "Parameterized unit", "Candidate families"],
            parameterized_unit_rows,
        )
    )

    lines.extend(["", "## Top Repeated Lines", ""])
    repeated_rows = [
        [
            item["frequency"],
            item["distinct_card_count"],
            ", ".join(item["source_fields"]),
            item["opening"],
            item["parameterized_line"],
            ", ".join(item["candidate_families"]),
            item["original_line"],
        ]
        for item in inventory["lines"][:TOP_LINE_LIMIT]
    ]
    lines.extend(
        markdown_table(
            [
                "Occurrences",
                "Cards",
                "Sources",
                "Opening",
                "Parameterized line",
                "Candidate families",
                "Original line",
            ],
            repeated_rows,
        )
    )

    lines.extend(["", "## Lines Without Candidate Family", ""])
    if inventory["unclassified_lines"]:
        unclassified_rows = [
            [
                item["frequency"],
                item["distinct_card_count"],
                item["opening"],
                item["parameterized_line"],
                item["original_line"],
            ]
            for item in inventory["unclassified_lines"]
        ]
        lines.extend(
            markdown_table(
                ["Occurrences", "Cards", "Opening", "Parameterized line", "Original line"],
                unclassified_rows,
            )
        )
    else:
        lines.append("- None.")

    lines.extend(["", "## Atomic Units Without Candidate Family", ""])
    if inventory["unclassified_units"]:
        unclassified_unit_rows = [
            [
                item["occurrence_count"],
                item["unique_normalized_line_count"],
                item["primary_unit_kind"],
                item["parameterized_unit"],
                item["unit_text"],
            ]
            for item in inventory["unclassified_units"]
        ]
        lines.extend(
            markdown_table(
                ["Occurrences", "Lines", "Kind", "Parameterized unit", "Unit"],
                unclassified_unit_rows,
            )
        )
    else:
        lines.append("- None.")

    lines.extend(
        [
            "",
            f"## Atomic Units With {summary['high_unit_family_overlap_threshold']}+ Candidate Families",
            "",
        ]
    )
    if inventory["high_family_overlap_units"]:
        unit_overlap_rows = [
            [
                item["candidate_family_count"],
                item["occurrence_count"],
                item["primary_unit_kind"],
                ", ".join(item["candidate_families"]),
                item["unit_text"],
            ]
            for item in inventory["high_family_overlap_units"]
        ]
        lines.extend(
            markdown_table(
                ["Family count", "Occurrences", "Kind", "Candidate families", "Unit"],
                unit_overlap_rows,
            )
        )
    else:
        lines.append("- None.")

    lines.extend(["", "## Complex Lines Decomposed", ""])
    if inventory["complex_lines_decomposed"]:
        for item in inventory["complex_lines_decomposed"]:
            lines.extend(
                [
                    "",
                    f"### {item['opening']} ({item['frequency']} occurrences, {item['text_unit_count']} units)",
                    "",
                    item["original_line"],
                    "",
                ]
            )
            unit_rows = [
                [
                    unit["unit_index"],
                    unit["unit_kind"],
                    ", ".join(unit["candidate_families"]),
                    unit["unit_text"],
                ]
                for unit in item["text_units"]
            ]
            lines.extend(markdown_table(["Index", "Kind", "Candidate families", "Unit"], unit_rows))
    else:
        lines.append("- None.")

    lines.extend(
        [
            "",
            f"## Lines With {summary['high_family_overlap_threshold']}+ Candidate Families",
            "",
        ]
    )
    if inventory["high_family_overlap_lines"]:
        overlap_rows = [
            [
                item["candidate_family_count"],
                item["frequency"],
                item["opening"],
                ", ".join(item["candidate_families"]),
                item["original_line"],
            ]
            for item in inventory["high_family_overlap_lines"]
        ]
        lines.extend(
            markdown_table(
                ["Family count", "Occurrences", "Opening", "Candidate families", "Original line"],
                overlap_rows,
            )
        )
    else:
        lines.append("- None.")

    lines.extend(["", "## Candidate Family Examples", ""])
    for family in inventory["candidate_families"]:
        lines.extend(["", f"### {family['family']}", ""])
        example_rows = [
            [
                example["frequency"],
                ", ".join(example["reasons"]),
                example["line"],
            ]
            for example in family["examples"]
        ]
        lines.extend(markdown_table(["Occurrences", "Reasons", "Line"], example_rows))

    lines.append("")
    return "\n".join(lines)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown_report(payload), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inventory raw card text patterns without using extracted facts or reports."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Input normalized cards JSON.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output text inventory JSON.")
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN, help="Output text inventory Markdown.")
    args = parser.parse_args()

    cards = read_json(args.input)
    inventory = build_inventory(cards)
    inventory["inputs"]["cards"] = repo_path(args.input)

    write_json(args.output, inventory)
    write_markdown(args.markdown, inventory)

    summary = inventory["summary"]
    print(f"[OK] cards: {summary['card_count']}")
    print(f"[OK] text lines: {summary['text_line_count']}")
    print(f"[OK] unique normalized lines: {summary['unique_normalized_line_count']}")
    print(f"[OK] unique normalized units: {summary['unique_normalized_unit_count']}")
    print(f"[OK] output: {args.output}")
    print(f"[OK] markdown: {args.markdown}")


if __name__ == "__main__":
    main()
