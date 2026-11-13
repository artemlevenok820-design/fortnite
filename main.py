from guard import safe_input
import json
import random

# 1. Загрузка данных и переводов из одного файла
with open("rewards.json", encoding="utf-8") as f:
    data = json.load(f)

REWARDS = data["rewards"]
TREASURE_MULTIPLIER = data["treasure_hour_multiplier"]
TEXTS = data["texts"]  # Забираем переводы отсюда же

# 2. Функция открытия сундука
def open_chest(multiplier=1.0):
    names = [r["name"] for r in REWARDS]
    weights = [r["weight"] * multiplier if r["rarity"] in ("rare", "ultra") else r["weight"] for r in REWARDS]
    return random.choices(names, weights=weights, k=1)[0]

# 3. Статистика
def load_stats():
    try:
        with open("stats.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"opened": 0, "ultra_found": False, "events": 0}

def save_stats(stats):
    with open("stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

# 4. Главный цикл
def main():
    # Выбор языка
    print(TEXTS["ru"]["choose_lang"])
    lang_choice = input("> ").strip()
    lang = "en" if lang_choice == "1" else "ru"
    t = TEXTS[lang]

    stats = load_stats()
    treasure_hour_active = False
    treasure_hour_turns_left = 0
    
    print(t["welcome"])
    print(t["controls"])

    while True:
        cmd = safe_input(t)

        if cmd == "q":
            break
        
        elif cmd == "r":
            print(t["reset_warn"].format(num=stats['opened']))
            print(t["reset_prompt"])
            
            confirm = input("> ").strip().lower()
            if confirm == "y":
                stats = {"opened": 0, "ultra_found": False, "events": 0}
                treasure_hour_active = False
                treasure_hour_turns_left = 0
                save_stats(stats)
                print(t["reset_ok"])
            else:
                print(t["reset_cancel"])
            continue

        # Логика игры
        stats["opened"] += 1
        
        if treasure_hour_active:
            if treasure_hour_turns_left > 0:
                treasure_hour_turns_left -= 1
            else:
                treasure_hour_active = False
                print(t["event_end"])
        
        if not treasure_hour_active and random.random() < 0.10:
            treasure_hour_active = True
            treasure_hour_turns_left = 5
            stats["events"] += 1
            print(t["event_start"])
            print(t["event_desc"].format(multiplier=TREASURE_MULTIPLIER, turns=treasure_hour_turns_left))

        current_multiplier = TREASURE_MULTIPLIER if treasure_hour_active else 1.0
        loot = open_chest(current_multiplier)
        
        if treasure_hour_active:
            print(t["chest_event"].format(num=stats['opened'], turns=treasure_hour_turns_left, loot=loot))
        else:
            print(t["chest_normal"].format(num=stats['opened'], loot=loot))

        if "магазин" in loot.lower() or "shop" in loot.lower():
            print(t["jackpot"].format(num=stats['opened']))
            stats["ultra_found"] = True
            break

        save_stats(stats)

    # Итоги при выходе
    save_stats(stats)
    print(t["total_opened"].format(num=stats['opened']))
    print(t["total_events"].format(num=stats.get('events', 0)))
    
    if not stats["ultra_found"]:
        print(t["no_jackpot"])

if __name__ == "__main__":
    main()