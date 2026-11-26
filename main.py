# Rename the Planet — make.fun bounty u-motasimfuad-rename-the-planet-094b0369
# One line, under 200 characters, that gives a planet of our solar system
# a funny new name and the reason for it in the same breath, written to
# /output/entry.txt. Twelve one-liners were drafted by hand and scored
# against the judge's brief, heaviest first: humour that lands on first
# reading, from the idea rather than a pun on the planet's real name; a
# reason that belongs to that planet alone, so the line fits nowhere else;
# a fresh angle, not the first joke anyone would reach for; one tight line
# with no filler. Each entry carries its hand-scored total below; the
# winner is the highest total, ties broken toward the shorter line, so the
# output never varies between runs. Field note: two of the five entries
# already in are Venus lines (a sauna joke and a group-project joke), so
# Venus angles were marked down on freshness even when the joke was strong.
# One more guardrail from the brief: the name and the reason must land in
# the same line — a funny name with the why left out scores below any
# entry that carries both.

from pathlib import Path

ENTRIES = [
    # Jupiter "The Grudge-Holder": funny 9, earns-name 10, fresh 9, tight 8 = 36
    # The Great Red Spot is a storm Jupiter has kept spinning for
    # roughly 300 years, a trait no other planet has. "Grudge-Holder"
    # is not a pun on "Jupiter" at all: the joke is the idea of a
    # planet nursing one grievance for three centuries.
    # REVISION (second pass): "and refuses" became "and still refuses" —
    # the extra beat lands the punchline harder and the line stays
    # well inside the gate at 111 characters.
    ("Jupiter is now 'The Grudge-Holder' — it has nursed the same "
     "storm for 300 years and still refuses to let it go.", 36),
    # Venus "The Night Owl": funny 9, earns-name 9, fresh 9, tight 8 = 35
    # A Venus day (243 Earth days) really is longer than a Venus year
    # (225 days). "Still yesterday" turns the fact into the punchline.
    # Marked down only because Venus is already the most-entered planet.
    ("Venus is now 'The Night Owl' — its day is longer than its year, "
     "so it is always technically still yesterday.", 35),
    # Neptune "The Math Homework": funny 8, earns-name 9, fresh 9, tight 8 = 34
    # Neptune is the only planet found on paper first: mathematicians
    # predicted where it had to be before anyone saw it. The name
    # reframes a planet as schoolwork nobody wanted to do.
    ("Neptune is now 'The Math Homework' — the only planet found by "
     "solving equations before anyone actually saw it.", 34),
    # Uranus "The Intern": funny 8, earns-name 9, fresh 8, tight 8 = 33
    # Uranus rolls around the Sun on its side, tilted about 98 degrees,
    # most likely knocked over by an ancient collision. The intern who
    # got knocked over on day one and just kept rolling is the same joke.
    ("Uranus is now 'The Intern' — knocked on its side on day one and "
     "has been rolling with it for 4.5 billion years.", 33),
    # Venus "The Contrarian": funny 8, earns-name 9, fresh 8, tight 8 = 33
    # Venus is the only planet that spins backwards. The contrarian who
    # insists everyone else is doing it wrong fits that one fact only.
    ("Venus is now 'The Contrarian' — the only planet that spins "
     "backwards and still insists everyone else is doing it wrong.", 33),
    # Jupiter "The Bouncer": funny 8, earns-name 9, fresh 7, tight 8 = 32
    # Jupiter's gravity really does swallow or deflect comets headed
    # inward, shielding the smaller planets. The bouncer who eats
    # trouble for a living is that job, humanised.
    ("Jupiter is now 'The Bouncer' — it eats comets for a living so "
     "the little planets can party in peace.", 32),
    # Jupiter "The Overprotective Dad": funny 8, earns-name 9, fresh 7, tight 8 = 32
    # Jupiter has 95 known moons and its gravity herds comets. The
    # overprotective dad with too many kids to watch is the same shape.
    ("Jupiter is now 'The Overprotective Dad' — 95 moons, and it still "
     "follows every comet home to make sure it behaves.", 32),
    # Neptune "The Drama Queen": funny 8, earns-name 8, fresh 7, tight 8 = 31
    # Neptune has the fastest winds in the solar system, up to about
    # 2,100 km/h, and orbits 30 times farther out than Earth. A tantrum
    # nobody can hear is the distance doing the joke's work.
    ("Neptune is now 'The Drama Queen' — it throws 2,100 km/h tantrums "
     "30 times farther from the Sun than anyone can hear.", 31),
    # Mercury "The Freckled Kid": funny 7, earns-name 8, fresh 7, tight 8 = 30
    # Mercury is the most cratered planet, pocked by impacts, and the
    # closest to the Sun. Freckles from standing too close to the Sun
    # without sunscreen is that fact as a school photo.
    ("Mercury is now 'The Freckled Kid' — covered in craters from "
     "standing too close to the Sun without sunscreen.", 30),
    # Uranus "The Ice Bath": funny 7, earns-name 9, fresh 7, tight 7 = 30
    # Uranus has the coldest atmosphere of any planet despite not being
    # the farthest out, and it lies on its side. The ice bath is both
    # facts in one image.
    ("Uranus is now 'The Ice Bath' — coldest atmosphere in the solar "
     "system, and it got that way by lying on its side.", 30),
    # Mercury "The Commuter": funny 7, earns-name 8, fresh 6, tight 7 = 28
    # Mercury laps the Sun in 88 days and swings hundreds of degrees
    # between day and night. The commuter who is always early and
    # always complaining about the weather is that orbit, humanised.
    ("Mercury is now 'The Commuter' — it laps the Sun in 88 days and "
     "still complains about the temperature swing.", 28),
    # Saturn "The Influencer": funny 7, earns-name 7, fresh 5, tight 7 = 26
    # Saturn's rings are its one unmistakable feature. The influencer
    # who wore one ring to a party 4 billion years ago leans on the
    # rings-as-jewellery angle, which is the first one anyone reaches for.
    ("Saturn is now 'The Influencer' — it wore one ring to a party 4 "
     "billion years ago and never took it off.", 26)]


def select_entry(entries):
    for line, total in entries:
        assert 1 <= len(line) <= 200, "entry outside the 200-character gate"
        assert line.strip() != "", "blank entry"
        assert "\n" not in line.strip(), "entry must stay on one line"
    return max(entries, key=lambda item: (item[1], -len(item[0])))[0]


def run():
    line = select_entry(ENTRIES)
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")
    # Read it back: the gate reads this file, not stdout.
    written = target.read_text(encoding="utf-8")
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 200, "entry.txt outside the gate"
    assert "\n" not in written.strip(), "entry.txt must be a single line"
    print(line)


run()
