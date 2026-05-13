const INDEX_URL = "/data/processed/web/card_explorer_index.json";
const FEEDBACK_FORM_URL =
  "https://docs.google.com/forms/d/e/1FAIpQLSe6fiSBTrWdTlfs2E-GiFe_XETKuHV2ylteB52gwls8jkDOtA/formResponse";
const FEEDBACK_FORM_FIELD = "entry.102097080";
const FEEDBACK_COPY = {
  relation_feedback: {
    title: "Improve card relations",
    prompt: "Tell us about a missing, incorrect, too broad, or weak relation.",
    placeholder: "Example: This card should be connected to another card because...",
  },
  missing_relation: {
    title: "Missing relation?",
    prompt: "Tell us which card should be connected and why.",
    placeholder: "Example: This card should connect to another card because...",
  },
};
let RELATION_TYPES = ["enabled_by", "enables", "similar_effect"];
let RELATION_LABELS = {
  enabled_by: "Enablers",
  enables: "Enabled Cards",
  similar_effect: "Similar Effects",
};
const BROAD_LANE = "broad";
const state = {
  dataset: null,
  cards: [],
  cardsById: new Map(),
  relationShardCache: new Map(),
  selectedId: null,
  modalCardId: null,
  collapsedLanes: new Set(),
  feedback: {
    type: "relation_feedback",
    cardId: null,
  },
  filters: {
    domains: new Set(),
    types: new Set(),
    triggers: new Set(),
    keywords: new Set(),
    energy: new Set(),
    might: new Set(),
    predicates: new Set(),
  },
};

const els = {
  cardSearch: document.querySelector("#cardSearchInput"),
  focusSearchButton: document.querySelector("#focusSearchButton"),
  resultCount: document.querySelector("#resultCount"),
  datasetMeta: document.querySelector("#datasetMeta"),
  clearFilters: document.querySelector("#clearFilters"),
  openFilters: document.querySelector("#openFilters"),
  closeFilters: document.querySelector("#closeFilters"),
  filterBackdrop: document.querySelector("#filterBackdrop"),
  focusPanel: document.querySelector("#focusPanel"),
  relationsPanel: document.querySelector("#relationsPanel"),
  cardModal: document.querySelector("#cardModal"),
  closeCardModal: document.querySelector("#closeCardModal"),
  modalContent: document.querySelector("#modalContent"),
  feedbackPanel: document.querySelector("#feedbackPanel"),
  feedbackTitle: document.querySelector("#feedbackTitle"),
  feedbackPrompt: document.querySelector("#feedbackPrompt"),
  closeFeedback: document.querySelector("#closeFeedback"),
  feedbackText: document.querySelector("#feedbackText"),
  feedbackStatus: document.querySelector("#feedbackStatus"),
  feedbackSubmit: document.querySelector("#feedbackSubmit"),
};

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
  return `<span class="stat ${className}">${prefix} ${value}</span>`;
}

function relationTabCount(card, tab) {
  return card.relations.outgoing_high_signal_counts?.[tab] ?? card.relations.outgoing_counts[tab] ?? 0;
}

function relationTotal(card) {
  return RELATION_TYPES.reduce((sum, tab) => sum + relationTabCount(card, tab), 0);
}

function emptyRelationGroups() {
  return Object.fromEntries([...RELATION_TYPES, BROAD_LANE].map((type) => [type, []]));
}

function broadRelationCount(card) {
  return card.relations.outgoing_broad_counts
    ? Object.values(card.relations.outgoing_broad_counts).reduce((sum, count) => sum + count, 0)
    : (card.relations.outgoing || []).filter((relation) => isBroadRelation(relation)).length;
}

function selectedCard() {
  return state.selectedId ? state.cardsById.get(state.selectedId) || null : null;
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

function relationEvidenceText(relation) {
  const source = relation.evidence?.source || "";
  const target = relation.evidence?.target || "";
  if (source && target) return `${source} -> ${target}`;
  return source || target || "No evidence text";
}

function relationShardUrl(shardPath) {
  return new URL(shardPath, new URL(INDEX_URL, window.location.origin)).pathname;
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
  try {
    const shard = await loadRelationShard(card.relations.shard);
    card.relations.outgoing = shard?.cards?.[playId]?.outgoing || [];
  } catch (error) {
    card.relations.outgoing = [];
    card.relations.loadError = true;
    console.error(error);
  } finally {
    card.relations.loading = false;
    if (state.selectedId === playId) renderRelations();
  }
}

function cardMatchesRelationFilters(card) {
  if (!card) return false;
  if (state.filters.domains.size && !card.domain_ids.some((id) => state.filters.domains.has(id))) return false;
  if (state.filters.types.size && !card.card_type_ids.some((id) => state.filters.types.has(id))) return false;
  if (state.filters.triggers.size && !card.semantic.triggers.some((id) => state.filters.triggers.has(id))) return false;
  if (state.filters.keywords.size && !card.semantic.keywords.some((id) => state.filters.keywords.has(id))) return false;
  if (state.filters.energy.size && !state.filters.energy.has(String(card.energy))) return false;
  if (state.filters.might.size && !state.filters.might.has(String(card.might))) return false;
  if (state.filters.predicates.size && !card.semantic.predicates.some((id) => state.filters.predicates.has(id))) return false;
  return true;
}

function relationsByType(card) {
  const grouped = Object.fromEntries([...RELATION_TYPES, BROAD_LANE].map((type) => [type, []]));
  for (const relation of card?.relations.outgoing || []) {
    if (isBroadRelation(relation)) {
      const item = { relation, card: relatedCard(relation, card) };
      if (item.card && cardMatchesRelationFilters(item.card)) grouped[BROAD_LANE].push(item);
      continue;
    }
    if (!RELATION_TYPES.includes(relation.relation_type)) continue;
    const item = { relation, card: relatedCard(relation, card) };
    if (item.card && cardMatchesRelationFilters(item.card)) grouped[relation.relation_type].push(item);
  }
  for (const type of [...RELATION_TYPES, BROAD_LANE]) {
    grouped[type].sort((left, right) => {
      if (right.relation.strength !== left.relation.strength) return right.relation.strength - left.relation.strength;
      return left.card.name.localeCompare(right.card.name);
    });
  }
  return grouped;
}

function renderFilters(targetId, options, filterKey) {
  const target = document.querySelector(targetId);
  target.innerHTML = options
    .slice(0, filterKey === "keywords" || filterKey === "triggers" ? 30 : 999)
    .map((option) => {
      const active = state.filters[filterKey].has(option.id) ? " active" : "";
      return `<button class="chip${active}" type="button" data-filter="${filterKey}" data-value="${option.id}">${label(option.id)} <span>${option.count}</span></button>`;
    })
    .join("");
}

function setFiltersOpen(open) {
  document.body.classList.toggle("filters-open", open);
  els.filterBackdrop.hidden = !open;
}

function findFocusMatch(query) {
  const value = normalize(query);
  if (!value) return null;
  const matches = state.cards
    .filter((card) => normalize(card.name).includes(value) || String(card.search_text || "").includes(value))
    .sort((left, right) => {
      const leftName = normalize(left.name);
      const rightName = normalize(right.name);
      const leftExact = leftName === value ? 0 : 1;
      const rightExact = rightName === value ? 0 : 1;
      const leftStarts = leftName.startsWith(value) ? 0 : 1;
      const rightStarts = rightName.startsWith(value) ? 0 : 1;
      return (
        leftExact - rightExact ||
        leftStarts - rightStarts ||
        relationTotal(right) - relationTotal(left) ||
        left.name.localeCompare(right.name)
      );
    });
  return matches[0] || null;
}

function submitFocusSearch() {
  const match = findFocusMatch(els.cardSearch.value);
  if (!match) {
    els.cardSearch.setAttribute("aria-invalid", "true");
    return;
  }
  els.cardSearch.removeAttribute("aria-invalid");
  selectCard(match.play_id);
}

function renderFocus(card, grouped, total) {
  if (!card) {
    els.focusPanel.innerHTML = renderStartPanel();
    return;
  }
  els.focusPanel.innerHTML = `
    <article class="focus-card">
      <img src="${card.image_url}" alt="${card.name}" />
      <div class="focus-copy">
        <div class="kicker">${card.public_codes.join(", ") || "Card"}</div>
        <h2>${card.name}</h2>
        <div class="pill-row">
          ${card.domain_ids.map((item) => `<span class="pill">${label(item)}</span>`).join("")}
          ${card.card_type_ids.map((item) => `<span class="pill">${label(item)}</span>`).join("")}
        </div>
        <div class="stat-row">
          ${stat(card.energy, "energy", "Energy")}
          ${stat(card.might, "might", "Might")}
          ${stat(card.power, "power", "Power")}
        </div>
        <div class="rules">${card.rules_lines.concat(card.effect_lines).map((line) => `<div>${line}</div>`).join("")}</div>
      </div>
      <div class="focus-metrics">
        <span><strong>${total}</strong>Shown</span>
          ${RELATION_TYPES.map((type) => `<span><strong>${grouped[type].length}</strong>${RELATION_LABELS[type]}</span>`).join("")}
          <span><strong>${grouped[BROAD_LANE].length}</strong>Broad</span>
          <button class="focus-feedback" type="button" data-feedback-intent="missing_relation" data-feedback-card-id="${card.play_id}">Missing relation?</button>
        </div>
    </article>
  `;
}

function renderStartPanel() {
  const summary = state.dataset?.summary || {};
  return `
    <section class="start-panel">
      <div>
        <div class="kicker">Riftbound Relation Explorer</div>
        <h2>Search a focus card</h2>
        <p>Choose a card to inspect its enablers, enabled cards, and similar effects. The filters on the left apply after a focus card is selected.</p>
      </div>
      <div class="start-metrics">
        <span><strong>${summary.card_count || 0}</strong>Cards</span>
        <span><strong>${summary.fact_count || 0}</strong>Facts</span>
        <span><strong>${summary.relation_count || 0}</strong>Relations</span>
      </div>
    </section>
  `;
}

function relationCard(item, mode = "row") {
  const card = item.card;
  const relation = item.relation;
  const compact = mode === "compact" ? " compact" : "";
  return `
    <button class="relation-card${compact}" type="button" data-card-id="${card.play_id}">
      <img src="${card.image_url}" alt="${card.name}" loading="lazy" />
      <span>
        <strong>${card.name}</strong>
        <small>${card.domain_ids.map(label).join(" / ")} - ${card.card_type_ids.map(label).join(", ")}</small>
        <em>${isBroadRelation(relation) ? "Broad" : RELATION_LABELS[relation.relation_type]} - ${label(relation.match?.broad_reason || relation.match?.reason || "relation")} - ${relation.strength}</em>
        <small class="relation-evidence">${relationEvidenceText(relation)}</small>
      </span>
    </button>
  `;
}

function renderModalCard(card) {
  const total = relationTotal(card);
  return `
    <div class="modal-card">
      <img src="${card.image_url}" alt="${card.name}" />
      <div class="modal-copy">
        <div class="kicker">${card.public_codes.join(", ") || "Card"}</div>
        <h2 id="modalTitle">${card.name}</h2>
        <div class="pill-row">
          ${card.domain_ids.map((item) => `<span class="pill">${label(item)}</span>`).join("")}
          ${card.card_type_ids.map((item) => `<span class="pill">${label(item)}</span>`).join("")}
        </div>
        <div class="stat-row">
          ${stat(card.energy, "energy", "Energy")}
          ${stat(card.might, "might", "Might")}
          ${stat(card.power, "power", "Power")}
        </div>
        <div class="rules">${card.rules_lines.concat(card.effect_lines).map((line) => `<div>${line}</div>`).join("")}</div>
        <div class="semantic-block">
          ${card.semantic.variant_warning?.has_rule_variants ? `<span class="pill warning">Variant text</span>` : ""}
          ${card.semantic.triggers.map((item) => `<span class="pill">${label(item)}</span>`).join("")}
          ${card.semantic.outputs.map((item) => `<span class="pill">${label(item)}</span>`).join("")}
          ${card.semantic.keywords.map((item) => `<span class="pill">${label(item)}</span>`).join("")}
          ${card.semantic.predicates.slice(0, 12).map((item) => `<span class="pill">${label(item)}</span>`).join("")}
        </div>
        <div class="modal-metrics">
          ${RELATION_TYPES.map((type) => `<span><strong>${relationTabCount(card, type)}</strong>${RELATION_LABELS[type]}</span>`).join("")}
          <span><strong>${broadRelationCount(card)}</strong>Broad</span>
          <span><strong>${total}</strong>Total</span>
        </div>
        <button class="primary-action" type="button" data-view-related="${card.play_id}">View Related</button>
      </div>
    </div>
  `;
}

function openCardModal(playId) {
  const card = state.cardsById.get(playId);
  if (!card) return;
  state.modalCardId = playId;
  els.modalContent.innerHTML = renderModalCard(card);
  els.cardModal.hidden = false;
  document.body.classList.add("modal-open");
  els.closeCardModal.focus();
}

function closeCardModal() {
  state.modalCardId = null;
  els.cardModal.hidden = true;
  document.body.classList.remove("modal-open");
}

function configureFeedback(type = "relation_feedback", cardId = null) {
  const copy = FEEDBACK_COPY[type] || FEEDBACK_COPY.relation_feedback;
  const card = cardId ? state.cardsById.get(cardId) : null;
  state.feedback = { type, cardId };
  els.feedbackTitle.textContent = card && type === "missing_relation" ? `Missing relation for ${card.name}?` : copy.title;
  els.feedbackPrompt.textContent =
    card && type === "missing_relation"
      ? `Tell us which card should be related to ${card.name}, and why.`
      : copy.prompt;
  els.feedbackText.placeholder =
    card && type === "missing_relation"
      ? `Example: ${card.name} should connect to another card because...`
      : copy.placeholder;
}

function setFeedbackOpen(open) {
  els.feedbackPanel.hidden = !open;
  document.body.classList.toggle("feedback-open", open);
  if (open) els.feedbackText.focus();
}

function openFeedback(type = "relation_feedback", cardId = null) {
  configureFeedback(type, cardId);
  setFeedbackStatus("");
  setFeedbackOpen(true);
}

function setFeedbackStatus(message, status = "") {
  els.feedbackStatus.textContent = message;
  els.feedbackStatus.dataset.state = status;
}

function resetOverlays() {
  els.cardModal.hidden = true;
  els.filterBackdrop.hidden = true;
  els.feedbackPanel.hidden = true;
  document.body.classList.remove("modal-open", "filters-open", "feedback-open");
}

function renderLanes(card, grouped) {
  return `
    <section class="model model-lanes">
      <header class="model-header"><div><h3>Related Cards</h3><p>One section per relationship type, using the same left filters.</p></div></header>
      <div class="lanes">
        ${RELATION_TYPES.map(
          (type) => {
            const collapsed = state.collapsedLanes.has(type);
            return `
            <article class="lane${collapsed ? " collapsed" : ""}">
              <button class="lane-toggle" type="button" data-lane-toggle="${type}" aria-expanded="${!collapsed}">
                <span>${RELATION_LABELS[type]}</span>
                <strong>${grouped[type].length}</strong>
                <em>${collapsed ? "Expand" : "Minimize"}</em>
              </button>
              <div class="lane-body">${grouped[type].slice(0, 40).map((item) => relationCard(item, "compact")).join("") || emptyRelations()}</div>
            </article>
          `;
          },
        ).join("")}
        <article class="lane secondary${state.collapsedLanes.has(BROAD_LANE) ? " collapsed" : ""}">
          <button class="lane-toggle" type="button" data-lane-toggle="${BROAD_LANE}" aria-expanded="${!state.collapsedLanes.has(BROAD_LANE)}">
            <span>Broad Matches</span>
            <strong>${grouped[BROAD_LANE].length}</strong>
            <em>${state.collapsedLanes.has(BROAD_LANE) ? "Expand" : "Minimize"}</em>
          </button>
          <div class="lane-body">${grouped[BROAD_LANE].slice(0, 40).map((item) => relationCard(item, "compact")).join("") || emptyRelations()}</div>
        </article>
      </div>
    </section>
  `;
}

function emptyRelations(message = "No related cards match these filters") {
  return `<div class="empty-detail"><h2>${message}</h2></div>`;
}

function renderRelations() {
  const card = selectedCard();
  if (!card) {
    els.resultCount.textContent = "No focus card";
    els.datasetMeta.textContent = `${state.dataset.summary.card_count} cards, ${state.dataset.summary.fact_count} facts, ${state.dataset.summary.relation_count} relations`;
    renderFocus(null);
    els.relationsPanel.innerHTML = "";
    return;
  }
  if (card.relations.loadError) {
    els.resultCount.textContent = "Relations unavailable";
    els.datasetMeta.textContent = "Try selecting the card again later";
    renderFocus(card, emptyRelationGroups(), 0);
    els.relationsPanel.innerHTML = emptyRelations("Relations unavailable");
    return;
  }
  if (!Array.isArray(card.relations.outgoing)) {
    els.resultCount.textContent = "Loading relations";
    els.datasetMeta.textContent = `${state.dataset.summary.fact_count} facts, ${state.dataset.summary.high_signal_relation_count || state.dataset.summary.relation_count} high-signal relations`;
    renderFocus(card, emptyRelationGroups(), 0);
    els.relationsPanel.innerHTML = emptyRelations("Loading relations");
    return;
  }
  const grouped = relationsByType(card);
  const total = RELATION_TYPES.reduce((sum, type) => sum + grouped[type].length, 0);
  els.resultCount.textContent = `${total} high-signal related cards`;
  els.datasetMeta.textContent = `${state.dataset.summary.fact_count} facts, ${state.dataset.summary.high_signal_relation_count || state.dataset.summary.relation_count} high-signal relations`;
  renderFocus(card, grouped, total);
  els.relationsPanel.innerHTML = renderLanes(card, grouped);
}

function renderAll() {
  renderFilters("#domainFilters", state.dataset.filters.domains, "domains");
  renderFilters("#typeFilters", state.dataset.filters.card_types, "types");
  renderFilters("#triggerFilters", state.dataset.filters.triggers, "triggers");
  renderFilters("#keywordFilters", state.dataset.filters.keywords, "keywords");
  renderFilters("#energyFilters", state.dataset.filters.energy, "energy");
  renderFilters("#mightFilters", state.dataset.filters.might, "might");
  renderFilters("#predicateFilters", state.dataset.filters.predicates, "predicates");
  renderRelations();
}

function toggleFilter(key, value) {
  const bucket = state.filters[key];
  if (bucket.has(value)) bucket.delete(value);
  else bucket.add(value);
  renderAll();
}

function selectCard(playId) {
  state.selectedId = playId;
  const card = selectedCard();
  if (card) els.cardSearch.value = card.name;
  renderAll();
  ensureCardRelations(playId);
  setFiltersOpen(false);
  if (window.matchMedia("(max-width: 900px)").matches) {
    els.focusPanel.scrollIntoView({ block: "start", behavior: "smooth" });
  }
}

function clearExplorer() {
  state.selectedId = null;
  state.collapsedLanes.clear();
  els.cardSearch.value = "";
  els.cardSearch.removeAttribute("aria-invalid");
  for (const bucket of Object.values(state.filters)) bucket.clear();
  closeCardModal();
  renderAll();
}

function selectedFilterSummary() {
  const activeFilters = Object.entries(state.filters)
    .filter(([, values]) => values.size)
    .map(([key, values]) => `${label(key)}: ${[...values].map(label).join(", ")}`);
  return activeFilters.length ? activeFilters.join(" | ") : "None";
}

function buildFeedbackBody(suggestion) {
  const card = state.feedback.cardId ? state.cardsById.get(state.feedback.cardId) || selectedCard() : selectedCard();
  const summary = state.dataset?.summary || {};
  return [
    `Feedback type: ${label(state.feedback.type)}`,
    "Suggestion:",
    suggestion,
    "",
    "Context:",
    `URL: ${window.location.href}`,
    `Focus card: ${card ? `${card.name} (${card.play_id})` : "None"}`,
    `Filters: ${selectedFilterSummary()}`,
    `Dataset: ${summary.card_count || "Unknown"} cards, ${summary.relation_count || "Unknown"} relations`,
    `Submitted at: ${new Date().toISOString()}`,
  ].join("\n");
}

async function submitFeedback(event) {
  event.preventDefault();
  const suggestion = els.feedbackText.value.trim();
  if (!suggestion) {
    els.feedbackText.setAttribute("aria-invalid", "true");
    setFeedbackStatus("Write a suggestion first.", "error");
    return;
  }

  const formData = new FormData();
  formData.append(FEEDBACK_FORM_FIELD, buildFeedbackBody(suggestion));

  els.feedbackSubmit.disabled = true;
  setFeedbackStatus("Sending...", "");
  try {
    await fetch(FEEDBACK_FORM_URL, {
      method: "POST",
      mode: "no-cors",
      body: formData,
    });
    els.feedbackText.value = "";
    els.feedbackText.removeAttribute("aria-invalid");
    setFeedbackStatus("Sent. Thanks.", "success");
  } catch (error) {
    setFeedbackStatus("Could not send right now.", "error");
    console.error(error);
  } finally {
    els.feedbackSubmit.disabled = false;
  }
}

document.addEventListener("click", (event) => {
  const filter = event.target.closest("[data-filter]");
  if (filter) toggleFilter(filter.dataset.filter, filter.dataset.value);

  const laneButton = event.target.closest("[data-lane-toggle]");
  if (laneButton) {
    if (!window.matchMedia("(max-width: 1120px)").matches) return;
    const lane = laneButton.dataset.laneToggle;
    if (state.collapsedLanes.has(lane)) state.collapsedLanes.delete(lane);
    else state.collapsedLanes.add(lane);
    renderRelations();
    return;
  }

  const cardButton = event.target.closest("[data-card-id]");
  if (cardButton) openCardModal(cardButton.dataset.cardId);

  const feedbackButton = event.target.closest("[data-feedback-intent]");
  if (feedbackButton) {
    openFeedback(feedbackButton.dataset.feedbackIntent, feedbackButton.dataset.feedbackCardId || state.selectedId);
  }

  const viewRelatedButton = event.target.closest("[data-view-related]");
  if (viewRelatedButton) {
    closeCardModal();
    selectCard(viewRelatedButton.dataset.viewRelated);
  }
});

els.cardSearch.addEventListener("input", () => els.cardSearch.removeAttribute("aria-invalid"));
els.cardSearch.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    submitFocusSearch();
  }
});
els.focusSearchButton.addEventListener("click", submitFocusSearch);
els.openFilters.addEventListener("click", () => setFiltersOpen(true));
els.closeFilters.addEventListener("click", () => setFiltersOpen(false));
els.filterBackdrop.addEventListener("click", () => setFiltersOpen(false));
els.closeCardModal.addEventListener("click", closeCardModal);
els.cardModal.addEventListener("click", (event) => {
  if (event.target === els.cardModal) closeCardModal();
});
els.clearFilters.addEventListener("click", () => {
  clearExplorer();
});
els.closeFeedback.addEventListener("click", () => setFeedbackOpen(false));
els.feedbackText.addEventListener("input", () => {
  els.feedbackText.removeAttribute("aria-invalid");
  if (els.feedbackStatus.dataset.state === "error") setFeedbackStatus("");
});
els.feedbackPanel.addEventListener("submit", submitFeedback);

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    setFeedbackOpen(false);
    closeCardModal();
    setFiltersOpen(false);
  }
});

async function init() {
  resetOverlays();
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
  state.cards = state.dataset.cards;
  state.cardsById = new Map(state.cards.map((card) => [card.play_id, card]));
  state.relationShardCache.clear();
  state.selectedId = null;
  els.cardSearch.value = "";
  renderAll();
}

init().catch((error) => {
  els.focusPanel.innerHTML = `<div class="empty-detail"><h2>Dataset unavailable</h2></div>`;
  els.resultCount.textContent = "Load failed";
  console.error(error);
});
