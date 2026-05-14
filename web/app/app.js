const APP_BASE_URL = new URL(".", document.currentScript?.src || window.location.href);
const INDEX_URL = new URL("../../data/processed/web/card_explorer_index.json", APP_BASE_URL);

const SITE_COPY = {
  tag: "RB",
  title: "Riftboundaries",
  subtitle: "Riftbound Relations Explorer",
};

const FILTER_GROUPS = [
  { key: "sets", dataKey: "sets", title: "Set", limit: 24 },
  { key: "domains", dataKey: "domains", title: "Domain", limit: 16 },
  { key: "keywords", dataKey: "keywords", title: "Keyword", limit: 24 },
  { key: "triggers", dataKey: "triggers", title: "Trigger", limit: 24 },
  { key: "predicates", dataKey: "predicates", title: "Modifier", limit: 24 },
  { key: "energy", dataKey: "energy", title: "Energy", limit: 18 },
  { key: "might", dataKey: "might", title: "Might", limit: 18 },
];

let RELATION_TYPES = ["enabled_by", "enables", "similar_effect"];
let RELATION_LABELS = {
  enabled_by: "Enablers",
  enables: "Enabled Cards",
  similar_effect: "Similar Effects",
};

const BROAD_LANE = "broad";
const INITIAL_TABLE_ROW_LIMIT = 120;
const TABLE_ROW_INCREMENT = 120;
const layoutCopy = SITE_COPY;

const OFFICIAL_RARITY_ICONS = {
  common: {
    label: "Common",
    icon_url: "https://cmsassets.rgpub.io/sanity/images/dsfx7636/game_data_live/a088ae851d94b5c34aa4900e8ccb4cc103144dce-354x354.png",
  },
  uncommon: {
    label: "Uncommon",
    icon_url: "https://cmsassets.rgpub.io/sanity/images/dsfx7636/game_data_live/808205a0f070e479107a7655e622fe15a356275b-480x410.png",
  },
  rare: {
    label: "Rare",
    icon_url: "https://cmsassets.rgpub.io/sanity/images/dsfx7636/game_data_live/d90078e1ec2ef7cbcbba2be86da1b192c389581a-429x425.png",
  },
  epic: {
    label: "Epic",
    icon_url: "https://cmsassets.rgpub.io/sanity/images/dsfx7636/game_data_live/5e9799d87d0f8baa55f6d9bddb9750669a0f485b-455x419.png",
  },
  showcase: {
    label: "Showcase",
    icon_url: "https://cmsassets.rgpub.io/sanity/images/dsfx7636/game_data_live/a0e92b9edf3291fa62c9b35ffd6363de0d7947c0-376x426.png",
  },
};

const OFFICIAL_GLYPHS = {
  exhaust: "https://assetcdn.rgpub.io/public/live/riot-shared/player-experiences/riot-glyphs/rb/latest/exhaust.svg",
  might: "https://assetcdn.rgpub.io/public/live/riot-shared/player-experiences/riot-glyphs/rb/latest/might.svg",
  runeRainbow: "https://assetcdn.rgpub.io/public/live/riot-shared/player-experiences/riot-glyphs/rb/latest/rune_rainbow.svg",
};

function energyGlyphUrl(value) {
  return `https://assetcdn.rgpub.io/public/live/riot-shared/player-experiences/riot-glyphs/rb/latest/energy_${value}.svg`;
}

const KEYWORD_TONES = {
  accelerate: "green",
  action: "green",
  ambush: "green",
  hidden: "green",
  legion: "green",
  "quick-draw": "green",
  reaction: "green",
  repeat: "green",
  add: "teal",
  arrow: "teal",
  "double-arrow": "teal",
  deathknell: "leaf",
  deflect: "leaf",
  ganking: "leaf",
  hunt: "leaf",
  level: "leaf",
  temporary: "leaf",
  assault: "pink",
  backline: "pink",
  shield: "pink",
  tank: "pink",
  buff: "neutral",
  equip: "neutral",
  mighty: "neutral",
  predict: "neutral",
  stun: "neutral",
  unique: "neutral",
  vision: "neutral",
  weaponmaster: "neutral",
};

const state = {
  dataset: null,
  cards: [],
  cardsById: new Map(),
  relationShardCache: new Map(),
  officialIcons: {
    domains: new Map(),
    types: new Map(),
    rarities: new Map(Object.entries(OFFICIAL_RARITY_ICONS)),
  },
  selectedId: null,
  modalId: null,
  tableRowLimit: INITIAL_TABLE_ROW_LIMIT,
  searchText: "",
  filters: {
    sets: new Set(),
    domains: new Set(),
    types: new Set(),
    triggers: new Set(),
    keywords: new Set(),
    energy: new Set(),
    might: new Set(),
    predicates: new Set(),
  },
};

const root = document.querySelector("#variantApp");
let isRestoringHistory = false;

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function escapeAttr(value) {
  return escapeHtml(value);
}

function filtersSnapshot() {
  return Object.fromEntries(Object.entries(state.filters).map(([key, bucket]) => [key, [...bucket]]));
}

function restoreFilters(filters = {}) {
  for (const [key, bucket] of Object.entries(state.filters)) {
    bucket.clear();
    for (const value of filters[key] || []) bucket.add(value);
  }
}

function historySnapshot() {
  return {
    selectedId: state.selectedId,
    modalId: state.modalId,
    searchText: state.searchText,
    tableRowLimit: state.tableRowLimit,
    filters: filtersSnapshot(),
  };
}

function historyUrl(snapshot) {
  const url = new URL(window.location.href);
  url.searchParams.delete("q");
  if (snapshot.selectedId) url.searchParams.set("card", snapshot.selectedId);
  else url.searchParams.delete("card");
  if (snapshot.modalId) url.searchParams.set("modal", snapshot.modalId);
  else url.searchParams.delete("modal");
  url.hash = "";
  return url.href;
}

function sameHistoryState(left, right) {
  return JSON.stringify(left || {}) === JSON.stringify(right || {});
}

function commitHistory(mode = "push") {
  if (isRestoringHistory || !state.dataset) return;
  const snapshot = historySnapshot();
  if (sameHistoryState(snapshot, history.state)) return;
  const method = mode === "replace" ? "replaceState" : "pushState";
  history[method](snapshot, "", historyUrl(snapshot));
}

function snapshotFromUrl() {
  const params = new URLSearchParams(window.location.search);
  const selectedId = params.get("card");
  const modalId = params.get("modal");
  const fallbackQuery = params.get("q") || window.location.hash.slice(1);
  const matchedCard = selectedId ? state.cardsById.get(selectedId) : findFocusMatch(fallbackQuery);
  return {
    selectedId: matchedCard?.play_id || null,
    modalId: modalId && state.cardsById.has(modalId) ? modalId : null,
    searchText: matchedCard?.name || "",
    tableRowLimit: INITIAL_TABLE_ROW_LIMIT,
    filters: Object.fromEntries(Object.keys(state.filters).map((key) => [key, []])),
  };
}

function restoreHistorySnapshot(snapshot) {
  const next = snapshot || snapshotFromUrl();
  const selectedId = next.selectedId && state.cardsById.has(next.selectedId) ? next.selectedId : null;
  const modalId = next.modalId && state.cardsById.has(next.modalId) ? next.modalId : null;
  state.selectedId = selectedId;
  state.modalId = modalId;
  state.searchText = next.searchText || (selectedId ? state.cardsById.get(selectedId)?.name || "" : "");
  state.tableRowLimit = next.tableRowLimit || INITIAL_TABLE_ROW_LIMIT;
  restoreFilters(next.filters);
  render();
  if (selectedId) ensureCardRelations(selectedId);
}

function normalize(value) {
  return String(value || "").trim().toLowerCase();
}

function label(value) {
  return String(value || "")
    .replaceAll("_", " ")
    .replaceAll("/", " / ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

function stat(value, className, prefix) {
  if (value === null || value === undefined) return "";
  return `<span class="stat ${className}"><b>${escapeHtml(value)}</b>${escapeHtml(prefix)}</span>`;
}

function selectedCard() {
  return state.selectedId ? state.cardsById.get(state.selectedId) || null : null;
}

function relationTabCount(card, tab) {
  return card?.relations?.outgoing_high_signal_counts?.[tab] ?? card?.relations?.outgoing_counts?.[tab] ?? 0;
}

function relationTotal(card) {
  return RELATION_TYPES.reduce((sum, tab) => sum + relationTabCount(card, tab), 0);
}

function broadRelationCount(card) {
  if (!card) return 0;
  return card.relations?.outgoing_broad_counts
    ? Object.values(card.relations.outgoing_broad_counts).reduce((sum, count) => sum + count, 0)
    : 0;
}

function relationShardUrl(shardPath) {
  return new URL(shardPath, INDEX_URL).href;
}

async function loadRelationShard(shardPath) {
  if (!shardPath) return null;
  if (!state.relationShardCache.has(shardPath)) {
    const request = fetch(relationShardUrl(shardPath)).then((response) => {
      if (!response.ok) throw new Error(`Relation shard unavailable: ${shardPath}`);
      return response.json();
    });
    state.relationShardCache.set(shardPath, request);
  }
  try {
    return await state.relationShardCache.get(shardPath);
  } catch (error) {
    state.relationShardCache.delete(shardPath);
    throw error;
  }
}

async function ensureCardRelations(playId) {
  const card = state.cardsById.get(playId);
  if (!card || (Array.isArray(card.relations?.outgoing) && !card.relations.loadError)) return;
  card.relations.loading = true;
  card.relations.loadError = false;
  delete card.relations.outgoing;
  render();
  try {
    const shard = await loadRelationShard(card.relations.shard);
    card.relations.outgoing = shard?.cards?.[playId]?.outgoing || [];
  } catch (error) {
    card.relations.outgoing = [];
    card.relations.loadError = true;
    console.error(error);
  } finally {
    card.relations.loading = false;
    render();
  }
}

function emptyRelationGroups() {
  return Object.fromEntries([...RELATION_TYPES, BROAD_LANE].map((type) => [type, []]));
}

function relatedId(relation, card) {
  return relation.source_play_id === card.play_id ? relation.target_play_id : relation.source_play_id;
}

function relatedCard(relation, card) {
  return state.cardsById.get(relatedId(relation, card));
}

function isBroadRelation(relation) {
  const broadReasons = new Set(state.dataset?.manifest?.broad_policy?.broad_reasons || []);
  return Boolean(relation.match?.broad || relation.match?.broad_reason || broadReasons.has(relation.match?.reason));
}

function cardMatchesRelationFilters(card) {
  if (!card) return false;
  const semantic = card.semantic || {};
  if (state.filters.sets.size && !(card.sets || []).some((set) => state.filters.sets.has(set.id))) return false;
  if (state.filters.domains.size && !(card.domain_ids || []).some((id) => state.filters.domains.has(id))) return false;
  if (state.filters.types.size && !(card.card_type_ids || []).some((id) => state.filters.types.has(id))) return false;
  if (state.filters.triggers.size && !(semantic.triggers || []).some((id) => state.filters.triggers.has(id))) return false;
  if (state.filters.keywords.size && !(semantic.keywords || []).some((id) => state.filters.keywords.has(id))) return false;
  if (state.filters.energy.size && !state.filters.energy.has(String(card.energy))) return false;
  if (state.filters.might.size && !state.filters.might.has(String(card.might))) return false;
  if (state.filters.predicates.size && !(semantic.predicates || []).some((id) => state.filters.predicates.has(id))) return false;
  return true;
}

function relationsByType(card) {
  const grouped = emptyRelationGroups();
  for (const relation of card?.relations?.outgoing || []) {
    const item = { relation, card: relatedCard(relation, card) };
    if (!item.card || !cardMatchesRelationFilters(item.card)) continue;
    if (isBroadRelation(relation)) {
      grouped[BROAD_LANE].push(item);
      continue;
    }
    if (RELATION_TYPES.includes(relation.relation_type)) grouped[relation.relation_type].push(item);
  }

  for (const type of [...RELATION_TYPES, BROAD_LANE]) {
    grouped[type].sort((left, right) => {
      if (right.relation.strength !== left.relation.strength) return right.relation.strength - left.relation.strength;
      return left.card.name.localeCompare(right.card.name);
    });
  }
  return grouped;
}

function flatRelations(grouped, includeBroad = true) {
  const types = includeBroad ? [...RELATION_TYPES, BROAD_LANE] : RELATION_TYPES;
  return types.flatMap((type) => grouped[type].map((item) => ({ ...item, lane: type })));
}

function findFocusMatch(query) {
  const value = normalize(query);
  if (!value) return null;
  return state.cards
    .filter((card) => normalize(card.name).includes(value) || String(card.search_text || "").includes(value))
    .sort((left, right) => {
      const leftName = normalize(left.name);
      const rightName = normalize(right.name);
      return (
        (leftName === value ? 0 : 1) - (rightName === value ? 0 : 1) ||
        (leftName.startsWith(value) ? 0 : 1) - (rightName.startsWith(value) ? 0 : 1) ||
        relationTotal(right) - relationTotal(left) ||
        left.name.localeCompare(right.name)
      );
    })[0] || null;
}

function searchSuggestions(query, limit = 8) {
  const value = normalize(query);
  if (!value) return [];
  return state.cards
    .filter((card) => normalize(card.name).includes(value))
    .sort((left, right) => {
      const leftName = normalize(left.name);
      const rightName = normalize(right.name);
      return (
        (leftName === value ? 0 : 1) - (rightName === value ? 0 : 1) ||
        (leftName.startsWith(value) ? 0 : 1) - (rightName.startsWith(value) ? 0 : 1) ||
        left.name.localeCompare(right.name)
      );
    })
    .slice(0, limit);
}

function parsePublicCode(code) {
  const text = String(code || "");
  const match = text.match(/^([A-Z]+)-(\d+)([a-z*]*)\/(\d+)/i);
  if (match) {
    return {
      setId: match[1].toUpperCase(),
      number: Number(match[2]),
      suffix: match[3] || "",
      total: Number(match[4]),
      code: text,
    };
  }
  const tokenMatch = text.match(/^([A-Z]+)-T(\d+)$/i);
  if (tokenMatch) {
    return {
      setId: tokenMatch[1].toUpperCase(),
      number: 100000 + Number(tokenMatch[2]),
      suffix: "T",
      total: Number.POSITIVE_INFINITY,
      code: text,
    };
  }
  return {
    setId: "ZZZ",
    number: Number.POSITIVE_INFINITY,
    suffix: "",
    total: Number.POSITIVE_INFINITY,
    code: text,
  };
}

function comparePublicCodeRanks(left, right) {
  return (
    left.setId.localeCompare(right.setId) ||
    left.number - right.number ||
    left.suffix.localeCompare(right.suffix) ||
    left.total - right.total ||
    left.code.localeCompare(right.code)
  );
}

function cardPublicCodeRank(card) {
  const ranks = sortedPublicCodeRanks(card);
  if (!ranks.length) return parsePublicCode("");
  if (state.filters.sets.size) {
    const matchingRank = ranks.find((rank) => state.filters.sets.has(rank.setId));
    if (matchingRank) return matchingRank;
  }
  return ranks[0];
}

function sortedPublicCodeRanks(card) {
  return (card?.public_codes || []).map(parsePublicCode).sort(comparePublicCodeRanks);
}

function cardPublicCodesText(card) {
  const ranks = sortedPublicCodeRanks(card);
  if (!state.filters.sets.size) return ranks.map((rank) => rank.code).join(", ");
  const matching = ranks.filter((rank) => state.filters.sets.has(rank.setId));
  const rest = ranks.filter((rank) => !state.filters.sets.has(rank.setId));
  return [...matching, ...rest].map((rank) => rank.code).join(", ");
}

function compareCardsBySetCode(left, right) {
  return comparePublicCodeRanks(cardPublicCodeRank(left), cardPublicCodeRank(right)) || left.name.localeCompare(right.name);
}

function searchBox(placeholder = "Search a card") {
  return `
    <form class="search-box" data-search-form>
      <input id="cardSearchInput" type="search" value="${escapeAttr(state.searchText)}" placeholder="${escapeAttr(placeholder)}" autocomplete="off" />
      <button type="submit">Inspect</button>
      <div class="search-suggestions" data-search-suggestions hidden></div>
    </form>
  `;
}

function renderSearchSuggestions(form) {
  const input = form?.querySelector("input[type='search']");
  const panel = form?.querySelector("[data-search-suggestions]");
  if (!input || !panel) return;
  const suggestions = searchSuggestions(input.value);
  if (!suggestions.length) {
    panel.hidden = true;
    panel.innerHTML = "";
    return;
  }
  panel.innerHTML = suggestions
    .map((card) => {
      return `
        <button class="search-suggestion" type="button" data-suggestion-card="${escapeAttr(card.play_id)}">
          <img src="${escapeAttr(card.image_url)}" alt="${escapeAttr(card.name)}" loading="lazy" />
          <span>
            <strong>${escapeHtml(card.name)}</strong>
            <small>${escapeHtml((card.domain_ids || []).map(label).join(" / "))} - ${escapeHtml((card.card_type_ids || []).map(label).join(", "))}</small>
          </span>
          <em>${escapeHtml(relationTotal(card))}</em>
        </button>
      `;
    })
    .join("");
  panel.hidden = false;
}

function hideSearchSuggestions(form = null) {
  const panels = form
    ? form.querySelectorAll("[data-search-suggestions]")
    : document.querySelectorAll("[data-search-suggestions]");
  panels.forEach((panel) => {
    panel.hidden = true;
    panel.innerHTML = "";
  });
}

function brandBlock() {
  return `
    <a class="brand" href="./" aria-label="Riftboundaries home">
      <span class="brand-mark" aria-hidden="true">
        <img src="./assets/logos/mark-knot.svg" alt="" />
      </span>
      <span>
        <strong>${escapeHtml(layoutCopy.title)}</strong>
        <small>${escapeHtml(layoutCopy.subtitle)}</small>
      </span>
    </a>
  `;
}

function filterOptionLabel(option) {
  return option?.name || option?.label || label(option?.id);
}

function filterOptions(group) {
  if (group.key !== "sets") return state.dataset?.filters?.[group.dataKey] || [];
  const sets = new Map();
  for (const card of state.cards || []) {
    for (const set of card.sets || []) {
      if (!set?.id) continue;
      const existing = sets.get(set.id) || { id: set.id, name: set.name || label(set.id), count: 0 };
      existing.count += 1;
      sets.set(set.id, existing);
    }
  }
  return [...sets.values()].sort((left, right) => filterOptionLabel(left).localeCompare(filterOptionLabel(right)));
}

function tableFilterDropdowns() {
  const groups = FILTER_GROUPS.map((group) => {
    const selected = state.filters[group.key].size;
    const options = filterOptions(group);
    return `
      <details class="filter-dropdown">
        <summary>
          <span>${escapeHtml(group.title)}</span>
          <b>${selected ? `${selected} selected` : "All"}</b>
        </summary>
        <div class="filter-menu">
          ${options
            .map((option) => {
              const checked = state.filters[group.key].has(option.id) ? " checked" : "";
              return `
                <label>
                  <input type="checkbox" data-filter-check="${escapeAttr(group.key)}" value="${escapeAttr(option.id)}"${checked} />
                  <span>${escapeHtml(filterOptionLabel(option))}</span>
                </label>
              `;
            })
            .join("")}
        </div>
      </details>
    `;
  }).join("");
  return `<div class="table-dropdowns">${groups}</div>`;
}

function pills(items = []) {
  return items.map((item) => `<span class="pill">${escapeHtml(label(item))}</span>`).join("");
}

function cssToken(value) {
  return normalize(value).replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "unknown";
}

function officialIconUrl(item) {
  return item?.icon_url || item?.icon?.url || item?.value?.icon?.url || "";
}

function officialChipIcon(item, type) {
  const id = cssToken(item?.id || item);
  if (type === "domain") return officialIconUrl(item) || state.officialIcons.domains.get(id)?.icon_url || "";
  if (type === "type") return officialIconUrl(item) || state.officialIcons.types.get(id)?.icon_url || "";
  if (type === "rarity") return officialIconUrl(item) || state.officialIcons.rarities.get(id)?.icon_url || "";
  return officialIconUrl(item);
}

function officialIconGroup(type) {
  if (type === "domain") return state.officialIcons.domains;
  if (type === "type") return state.officialIcons.types;
  if (type === "rarity") return state.officialIcons.rarities;
  return null;
}

function collectOfficialIcons(cards) {
  state.officialIcons.domains = new Map();
  state.officialIcons.types = new Map();
  state.officialIcons.rarities = new Map(Object.entries(OFFICIAL_RARITY_ICONS));
  for (const card of cards || []) {
    for (const domain of card.domains || []) {
      const iconUrl = officialIconUrl(domain);
      if (domain?.id && iconUrl) state.officialIcons.domains.set(domain.id, { label: domain.name || label(domain.id), icon_url: iconUrl });
    }
    for (const type of card.card_types || []) {
      const iconUrl = officialIconUrl(type);
      if (type?.id && iconUrl) state.officialIcons.types.set(type.id, { label: type.name || label(type.id), icon_url: iconUrl });
    }
  }
}

function gameIconChip(item, type) {
  const id = item?.id || item;
  const text = item?.name || item?.label || officialIconGroup(type)?.get(id)?.label || label(id);
  const iconUrl = officialChipIcon(item, type);
  const icon = iconUrl
    ? `<img src="${escapeAttr(iconUrl)}" alt="" loading="lazy" />`
    : type === "domain"
      ? `<span class="game-chip-symbol domain-${escapeAttr(cssToken(id))}"></span>`
      : "";
  return `<span class="game-chip ${escapeAttr(type)} ${escapeAttr(type)}-${escapeAttr(cssToken(id))}">${icon}<b>${escapeHtml(text)}</b></span>`;
}

function gameTextChip(text, type = "tag") {
  const id = text?.id || text;
  const iconUrl = officialChipIcon(text, type);
  const icon = iconUrl ? `<img src="${escapeAttr(iconUrl)}" alt="" loading="lazy" />` : "";
  const textLabel = text?.name || text?.label || officialIconGroup(type)?.get(id)?.label || label(id);
  return `<span class="game-chip ${escapeAttr(type)} ${escapeAttr(type)}-${escapeAttr(cssToken(id))}">${icon}<b>${escapeHtml(textLabel)}</b></span>`;
}

function keywordMeta(keyword) {
  const clean = String(keyword || "").trim();
  if (clean === ">") return { slug: "arrow", tone: "teal", text: ">", title: "Activated ability" };
  if (clean === ">>") return { slug: "double-arrow", tone: "teal", text: ">>", title: "Upgraded activated ability" };
  const slug = cssToken(clean.replace(/\d+/g, "").trim());
  return {
    slug,
    tone: KEYWORD_TONES[slug] || "neutral",
    text: clean,
    title: clean,
  };
}

function richRuleToken(token, options = {}) {
  if (token.startsWith("[") && token.endsWith("]")) {
    const keyword = keywordMeta(token.slice(1, -1));
    const actionCue = options.actionCue ? " with-action-cue" : "";
    const title = options.actionCue ? `${keyword.title} activated ability` : keyword.title;
    return `<span class="game-keyword keyword-${escapeAttr(keyword.slug)} tone-${escapeAttr(keyword.tone)}${actionCue}" title="${escapeAttr(title)}">${escapeHtml(keyword.text)}</span>`;
  }
  if (token === ":rb_might:") return `<img class="game-symbol might" src="${escapeAttr(OFFICIAL_GLYPHS.might)}" alt="Might" loading="lazy" />`;
  if (token === ":rb_power:") return `<span class="game-icon power" aria-label="Power"></span>`;
  if (token === ":rb_exhaust:") return `<img class="game-symbol exhaust" src="${escapeAttr(OFFICIAL_GLYPHS.exhaust)}" alt="Exhaust" loading="lazy" />`;
  const energy = token.match(/^:rb_energy_(\d+):$/);
  if (energy) {
    const energyValue = Number(energy[1]);
    if (energyValue >= 1 && energyValue <= 12) {
      return `<img class="game-symbol energy" src="${escapeAttr(energyGlyphUrl(energyValue))}" alt="${escapeAttr(`${energyValue} Energy`)}" loading="lazy" />`;
    }
    return `<span class="game-cost energy">${escapeHtml(energy[1])}</span>`;
  }
  const rune = token.match(/^:rb_rune_([a-z_]+):$/);
  if (rune) {
    const runeId = rune[1];
    if (runeId === "rainbow") {
      return `<img class="game-symbol rune-rainbow" src="${escapeAttr(OFFICIAL_GLYPHS.runeRainbow)}" alt="Rainbow rune" loading="lazy" />`;
    }
    const domainIcon = state.officialIcons.domains.get(runeId)?.icon_url;
    if (domainIcon) {
      return `<span class="game-rune icon-rune rune-${escapeAttr(cssToken(runeId))}" title="${escapeAttr(label(runeId))}"><img src="${escapeAttr(domainIcon)}" alt="" loading="lazy" /></span>`;
    }
    return `<span class="game-rune rune-${escapeAttr(cssToken(runeId))}" title="${escapeAttr(label(runeId))}"></span>`;
  }
  return escapeHtml(token);
}

function richRuleLine(line) {
  const parts = String(line || "").split(/(\[[^\]]+\]|:rb_[a-z0-9_]+:)/g).filter((part) => part !== "");
  const rendered = [];
  for (let index = 0; index < parts.length; index += 1) {
    const part = parts[index];
    const isBracketToken = part.startsWith("[") && part.endsWith("]");
    const canAttachArrow = isBracketToken && part !== "[>]" && part !== "[>>]" && parts[index + 1] === "[>]";
    if (canAttachArrow) {
      rendered.push(richRuleToken(part, { actionCue: true }));
      index += 1;
      continue;
    }
    rendered.push(richRuleToken(part));
  }
  return rendered.join("");
}

function richRulesText(card, limit = 8) {
  return (card?.rules_lines || [])
    .concat(card?.effect_lines || [])
    .slice(0, limit)
    .map((line) => `<p>${richRuleLine(line)}</p>`)
    .join("");
}

function modalStat(labelText, value, icon = "") {
  if (value === null || value === undefined) value = "-";
  return `
    <span class="game-stat">
      <small>${escapeHtml(labelText)}</small>
      <b>${icon}${escapeHtml(value)}</b>
    </span>
  `;
}

function modalInfo(labelText, value) {
  if (!value) return "";
  return `
    <span class="modal-info-item">
      <small>${escapeHtml(labelText)}</small>
      <b>${escapeHtml(value)}</b>
    </span>
  `;
}

function relationBadge(type) {
  return type === BROAD_LANE ? "Broad" : RELATION_LABELS[type] || label(type);
}

function loadingRelations(card) {
  if (!card) return "";
  if (card.relations?.loadError) return `<div class="empty-state">Relations unavailable</div>`;
  if (!Array.isArray(card.relations?.outgoing)) return `<div class="empty-state">Loading relations</div>`;
  return "";
}

function tableItems(grouped, card) {
  return card
    ? flatRelations(grouped, true)
    : state.cards
        .filter(cardMatchesRelationFilters)
        .sort(compareCardsBySetCode)
        .map((listedCard) => ({ card: listedCard, lane: "listing", relation: null }));
}

function visibleTableItems(items, card) {
  return items.slice(0, card ? 80 : state.tableRowLimit);
}

function tableRows(items) {
  return items
    .map((item) => {
      const relation = item.relation;
      return `
        <tr role="button" tabindex="0" data-open-card="${escapeAttr(item.card.play_id)}">
          <td><img src="${escapeAttr(item.card.image_url)}" alt="${escapeAttr(item.card.name)}" loading="lazy" /></td>
          <td><strong>${escapeHtml(item.card.name)}</strong><small>${escapeHtml(cardPublicCodesText(item.card))}</small></td>
          <td>${escapeHtml(item.lane === "listing" ? "Card" : relationBadge(item.lane))}</td>
          <td>${escapeHtml((item.card.domain_ids || []).map(label).join(" / "))}</td>
          <td>${escapeHtml((item.card.card_type_ids || []).map(label).join(", "))}</td>
          <td>${escapeHtml(item.card.energy ?? "")}</td>
          <td>${escapeHtml(item.card.might ?? "")}</td>
          <td>${escapeHtml(relation?.strength ?? relationTotal(item.card))}</td>
          <td>${escapeHtml(relation ? label(relation.match?.broad_reason || relation.match?.reason || "") : `${relationTotal(item.card)} high-signal`)}</td>
        </tr>
      `;
    })
    .join("");
}

function tableLoadMore(card, shown, total) {
  if (card || shown >= total) return "";
  return `
    <div class="table-load-more">
      <span>Showing ${escapeHtml(shown)} of ${escapeHtml(total)} cards</span>
      <button type="button" data-action="load-more-table">Load more</button>
    </div>
  `;
}

function tableFocusCard(card) {
  if (!card) return "";
  return `
    <section class="table-focus">
      <button class="table-focus-card" type="button" data-open-card="${escapeAttr(card.play_id)}">
        <img src="${escapeAttr(card.image_url)}" alt="${escapeAttr(card.name)}" loading="lazy" />
        <span class="table-focus-copy">
          <small>Focus Card</small>
          <strong>${escapeHtml(card.name)}</strong>
          <em>${escapeHtml((card.public_codes || []).join(", ") || "Card")}</em>
          <span class="table-focus-tags">${pills(card.domain_ids)}${pills(card.card_type_ids)}</span>
          <span class="table-focus-rules">${(card.rules_lines || []).slice(0, 2).map((line) => richRuleLine(line)).join(" ")}</span>
        </span>
        <span class="table-focus-stats">
          ${stat(card.energy, "energy", "Energy")}
          ${stat(card.might, "might", "Might")}
          ${stat(card.power, "power", "Power")}
        </span>
      </button>
    </section>
  `;
}

function cardDetailModal() {
  const card = state.modalId ? state.cardsById.get(state.modalId) : null;
  if (!card) return "";
  const semantic = card.semantic || {};
  const primarySet = card.sets?.[0]?.name || card.sets?.[0]?.id || "";
  const rarity = (card.rarity_ids || []).map(label).join(", ");
  return `
    <div class="table-modal-backdrop" data-action="close-modal">
      <article class="table-modal" role="dialog" aria-modal="true" aria-labelledby="tableModalTitle">
        <div class="table-modal-actions">
          <button class="modal-view-relations" type="button" data-view-relations="${escapeAttr(card.play_id)}">View Relations</button>
          <button class="table-modal-close" type="button" data-action="close-modal" aria-label="Close card details">&times;</button>
        </div>
        <section class="table-modal-art">
          <img src="${escapeAttr(card.image_url)}" alt="${escapeAttr(card.name)}" />
        </section>
        <section class="table-modal-copy">
          <div class="modal-title-block">
            <span class="eyebrow">${escapeHtml((card.public_codes || []).join(", ") || "Card")}</span>
            <h2 id="tableModalTitle">${escapeHtml(card.name)}</h2>
          </div>
          <div class="game-chip-row">
            ${(card.card_types || []).map((item) => gameIconChip(item, "type")).join("")}
            ${(card.domains || []).map((item) => gameIconChip(item, "domain")).join("")}
            ${(card.rarity_ids || []).slice(0, 2).map((item) => gameTextChip(item, "rarity")).join("")}
          </div>
          <div class="game-chip-row tags">
            ${(card.tags || []).slice(0, 8).map((item) => gameTextChip(item, "tag")).join("")}
          </div>
          <div class="game-stats">
            ${modalStat("Energy", card.energy)}
            ${modalStat("Power", card.power)}
            ${modalStat("Might", card.might, card.might === null || card.might === undefined ? "" : `<img class="game-symbol might" src="${escapeAttr(OFFICIAL_GLYPHS.might)}" alt="" loading="lazy" />`)}
          </div>
          <section class="modal-section">
            <h3>Description</h3>
            <div class="game-rules">${richRulesText(card, 8)}</div>
          </section>
          <section class="modal-section">
            <h3>Card Information</h3>
            <div class="modal-info-grid">
              ${modalInfo("Set", primarySet)}
              ${modalInfo("Rarity", rarity)}
              ${modalInfo("Card Number", (card.collector_numbers || []).join(", "))}
              ${modalInfo("Relation Total", String(relationTotal(card)))}
            </div>
          </section>
          <section class="modal-section semantic">
            <h3>Semantic Tags</h3>
            <div class="semantic-strip">
              ${(semantic.keywords || []).slice(0, 8).map((item) => gameTextChip(item, "keyword-chip")).join("")}
              ${(semantic.triggers || []).slice(0, 8).map((item) => gameTextChip(item, "trigger")).join("")}
              ${(semantic.outputs || []).slice(0, 8).map((item) => gameTextChip(item, "output")).join("")}
            </div>
          </section>
          <div class="modal-metrics" aria-label="Relation counts">
            ${RELATION_TYPES.map((type) => `<span><b>${relationTabCount(card, type)}</b>${escapeHtml(relationBadge(type))}</span>`).join("")}
            <span><b>${broadRelationCount(card)}</b>Broad</span>
            <span><b>${relationTotal(card)}</b>Total</span>
          </div>
        </section>
      </article>
    </div>
  `;
}

function renderTable(card, grouped) {
  const relationLoading = loadingRelations(card);
  const allItems = relationLoading ? [] : tableItems(grouped, card);
  const visibleItems = visibleTableItems(allItems, card);
  return `
    <div class="table-shell">
      <header class="table-header">
        ${brandBlock()}
        ${searchBox("Search card database")}
        <button type="button" data-action="clear">Clear</button>
      </header>
      <section class="table-filters">${tableFilterDropdowns()}</section>
      ${tableFocusCard(card)}
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Art</th>
              <th>Card</th>
              <th>Relation</th>
              <th>Domain</th>
              <th>Type</th>
              <th>Energy</th>
              <th>Might</th>
              <th>Score</th>
              <th>Reason</th>
            </tr>
          </thead>
          <tbody>${relationLoading ? "" : tableRows(visibleItems)}</tbody>
        </table>
        ${relationLoading}
      </div>
      ${tableLoadMore(card, visibleItems.length, allItems.length)}
      ${cardDetailModal()}
    </div>
  `;
}

function render() {
  if (!state.dataset) {
    root.innerHTML = `<div class="boot">Loading dataset</div>`;
    return;
  }
  const card = selectedCard();
  const grouped = card && Array.isArray(card.relations?.outgoing) ? relationsByType(card) : emptyRelationGroups();
  document.title = `${layoutCopy.title} - ${layoutCopy.subtitle}`;
  root.innerHTML = renderTable(card, grouped);
}

function setSelected(playId, options = {}) {
  const card = state.cardsById.get(playId);
  if (!card) return;
  state.selectedId = playId;
  state.modalId = null;
  state.searchText = card.name;
  state.tableRowLimit = INITIAL_TABLE_ROW_LIMIT;
  render();
  commitHistory(options.history || "push");
  ensureCardRelations(playId);
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function submitSearch(form) {
  const input = form.querySelector("input[type='search']");
  const query = input?.value || "";
  const match = findFocusMatch(query);
  if (!match) {
    input?.setAttribute("aria-invalid", "true");
    return;
  }
  input?.removeAttribute("aria-invalid");
  setSelected(match.play_id);
}

function toggleFilter(key, value) {
  const bucket = state.filters[key];
  if (!bucket) return;
  if (bucket.has(value)) bucket.delete(value);
  else bucket.add(value);
  state.tableRowLimit = INITIAL_TABLE_ROW_LIMIT;
  render();
  commitHistory("push");
}

function clearAll() {
  state.selectedId = null;
  state.modalId = null;
  state.tableRowLimit = INITIAL_TABLE_ROW_LIMIT;
  state.searchText = "";
  for (const bucket of Object.values(state.filters)) bucket.clear();
  render();
  commitHistory("push");
}

function openCardDetails(playId, options = {}) {
  if (!state.cardsById.has(playId)) return;
  state.modalId = playId;
  render();
  commitHistory(options.history || "push");
}

function closeCardDetails(options = {}) {
  if (!state.modalId) return;
  state.modalId = null;
  render();
  commitHistory(options.history || "replace");
}

document.addEventListener("submit", (event) => {
  const form = event.target.closest("[data-search-form]");
  if (!form) return;
  event.preventDefault();
  hideSearchSuggestions(form);
  submitSearch(form);
});

document.addEventListener("input", (event) => {
  if (event.target.matches("#cardSearchInput")) {
    state.searchText = event.target.value;
    event.target.removeAttribute("aria-invalid");
    renderSearchSuggestions(event.target.closest("[data-search-form]"));
  }
});

document.addEventListener("focusin", (event) => {
  if (event.target.matches("#cardSearchInput")) {
    renderSearchSuggestions(event.target.closest("[data-search-form]"));
  }
});

document.addEventListener("change", (event) => {
  const checkbox = event.target.closest("[data-filter-check]");
  if (!checkbox) return;
  const bucket = state.filters[checkbox.dataset.filterCheck];
  if (!bucket) return;
  if (checkbox.checked) bucket.add(checkbox.value);
  else bucket.delete(checkbox.value);
  state.tableRowLimit = INITIAL_TABLE_ROW_LIMIT;
  render();
  commitHistory("push");
});

document.addEventListener("click", (event) => {
  const suggestion = event.target.closest("[data-suggestion-card]");
  if (suggestion) {
    hideSearchSuggestions();
    setSelected(suggestion.dataset.suggestionCard);
    return;
  }

  if (!event.target.closest("[data-search-form]")) hideSearchSuggestions();

  const filter = event.target.closest("[data-filter]");
  if (filter) {
    toggleFilter(filter.dataset.filter, filter.dataset.value);
    return;
  }

  const detailTarget = event.target.closest("[data-open-card]");
  if (detailTarget) {
    openCardDetails(detailTarget.dataset.openCard);
    return;
  }

  const viewRelations = event.target.closest("[data-view-relations]");
  if (viewRelations) {
    setSelected(viewRelations.dataset.viewRelations, { history: "replace" });
    return;
  }

  const cardButton = event.target.closest("[data-select-card]");
  if (cardButton) {
    setSelected(cardButton.dataset.selectCard);
    return;
  }

  const action = event.target.closest("[data-action]");
  if (action?.dataset.action === "clear") {
    clearAll();
    return;
  }
  if (action?.dataset.action === "load-more-table") {
    state.tableRowLimit += TABLE_ROW_INCREMENT;
    render();
    commitHistory("replace");
    return;
  }
  if (action?.dataset.action === "close-modal" && (event.target === action || action.classList.contains("table-modal-close"))) {
    closeCardDetails();
    return;
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    closeCardDetails();
    hideSearchSuggestions();
  }
  if (event.key !== "Enter" && event.key !== " ") return;
  const detailTarget = event.target.closest("[data-open-card]");
  if (!detailTarget) return;
  event.preventDefault();
  openCardDetails(detailTarget.dataset.openCard);
});

window.addEventListener("popstate", (event) => {
  if (!state.dataset) return;
  isRestoringHistory = true;
  restoreHistorySnapshot(event.state);
  isRestoringHistory = false;
});

async function init() {
  render();
  const response = await fetch(INDEX_URL);
  state.dataset = await response.json();
  const relationManifest = state.dataset.manifest?.relation_types || {};
  RELATION_TYPES = Object.entries(relationManifest)
    .filter(([, config]) => config.default_visible !== false)
    .map(([type]) => type);
  if (!RELATION_TYPES.length) RELATION_TYPES = ["enabled_by", "enables", "similar_effect"];
  RELATION_LABELS = Object.fromEntries(
    RELATION_TYPES.map((type) => [type, relationManifest[type]?.label || label(type)]),
  );
  state.cards = state.dataset.cards || [];
  state.cardsById = new Map(state.cards.map((card) => [card.play_id, card]));
  collectOfficialIcons(state.cards);
  const params = new URLSearchParams(window.location.search);
  const initialCard = state.cardsById.get(params.get("card")) || findFocusMatch(params.get("q") || window.location.hash.slice(1));
  const initialModal = params.get("modal") && state.cardsById.has(params.get("modal")) ? params.get("modal") : null;
  if (initialCard || initialModal) {
    state.selectedId = initialCard?.play_id || null;
    state.searchText = initialCard?.name || "";
    state.modalId = initialModal;
    render();
    commitHistory("replace");
    if (initialCard) ensureCardRelations(initialCard.play_id);
    return;
  }
  render();
  commitHistory("replace");
}

init().catch((error) => {
  console.error(error);
  root.innerHTML = `<div class="boot error">Dataset unavailable</div>`;
});
