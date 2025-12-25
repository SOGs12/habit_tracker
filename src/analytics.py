from datetime import datetime, date, timedelta
from typing import List, Dict, Tuple, Optional

def _to_dt(iso: str) -> date:
    """Convert ISO string to a date object."""
    return datetime.fromisoformat(iso).date()

def _period_key(periodicity: str, dt: date) -> str:
    """Return a normalized key for daily or weekly periodicity."""
    if periodicity == "daily":
        return dt.isoformat()
    elif periodicity == "weekly":
        y, w, _ = dt.isocalendar()
        return f"{y}-W{w:02d}"
    else:
        raise ValueError("periodicity must be 'daily' or 'weekly'")

def list_all_habits(habits: List[Dict]) -> List[str]:
    """Return a list of habit names."""
    return [h["name"] for h in habits]

def filter_by_periodicity(habits: List[Dict], periodicity: str) -> List[Dict]:
    """Filter habits by periodicity."""
    return [h for h in habits if h["periodicity"] == periodicity]

def longest_streak_for_habit(habit: Dict, completions: List[Dict]) -> int:
    """Compute the longest streak for a single habit."""
    pid = habit["id"]
    p = habit["periodicity"]

    # Collect unique period keys
    keys = sorted({
        _period_key(p, _to_dt(c["completion_date"]))
        for c in completions if c["habit_id"] == pid
    })
    if not keys:
        return 0

    def next_key(k: str, p: str) -> str:
        if p == "daily":
            d = date.fromisoformat(k)
            return (d + timedelta(days=1)).isoformat()
        else:  # weekly
            y, w = k.split("-W")
            y, w = int(y), int(w)
            monday = date.fromisocalendar(y, w, 1)
            ny, nw, _ = (monday + timedelta(days=7)).isocalendar()
            return f"{ny}-W{nw:02d}"

    best = cur = 1
    for prev, curr in zip(keys, keys[1:]):
        if curr == next_key(prev, p):  # ✅ pass p here
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best  # ✅ fixed indentation

def longest_streak_all(habits: List[Dict], completions: List[Dict]) -> Tuple[Optional[Dict], int]:
    """Compute the habit with the longest streak among all habits."""
    if not habits:
        return None, 0
    streaks = [(h, longest_streak_for_habit(h, completions)) for h in habits]
    hmax, smax = max(streaks, key=lambda t: t[1])
    return hmax, smax

