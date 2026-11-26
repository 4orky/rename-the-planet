# Rename the Planet — make.fun bounty
# u-motasimfuad-rename-the-planet-094b0369
#
# The program writes one line, under 200 characters, that gives a planet
# of our solar system a funny new name and says why in the same breath,
# to /output/entry.txt.
#
# Candidates were drafted against the judge's brief, in order of weight:
#   1. names a planet with a funny new name and gives the why in the
#      same line; a name with no why loses to any entry on the subject
#   2. funny on the first read, the laugh coming from the idea, not from
#      a pun on the planet's real name alone
#   3. the why earns the name: it leans on that planet's own traits, so
#      it would not fit any other planet
#   4. fresh: a name and an angle the judge has not met before, not the
#      obvious pun anyone would reach for
#   5. tight: one line, every word doing work, no throat clearing
# Each candidate carries a hand-scored craft score (0-10 per criterion
# 2-5, summed below); selection is deterministic: highest score wins,
# ties go to the shorter text. The output is byte-identical on every run.
#
# Notes on the field: two of the five entries already in are Venus lines
# (a sauna joke and a group-project joke), so Venus angles were scored
# down on freshness even where the joke itself was strong.

CANDIDATES = [
    # score: funny 9, earns-name 10, fresh 9, tight 8 = 36
    # The Great Red Spot is a storm Jupiter has kept spinning for
    # roughly 300 years, a trait no other planet has. "Grudge-Holder"
    # is not a pun on "Jupiter" at all: the joke is the idea of a
    # planet nursing one grievance for three centuries.
    # REVISION (second pass): "and refuses" became "and still refuses" —
    # the extra beat lands the punchline harder and the line stays
    # well inside the gate at 111 characters.
    ("Jupiter is now 'The Grudge-Holder' — it has nursed the same "
     "storm for 300 years and still refuses to let it go.",
     36),
    # score: funny 9, earns-name 9, fresh 9, tight 8 = 35
    # A Venus day (243 Earth days) really is longer than a Venus year
    # (225 days). "Still yesterday" turns the fact into the punchline.
    # Marked down only because Venus is already the most-entered planet.
    ("Venus is now 'The Night Owl' — its day is longer than its year, "
     "so it is always technically still yesterday.",
     35),
    # score: funny 8, earns-name 9, fresh 9, tight 8 = 34
    # Neptune is the only planet found on paper first: mathematicians
    # predicted where it had to be before anyone saw it. The name
    # reframes a planet as schoolwork nobody wanted to do.
    ("Neptune is now 'The Math Homework' — the only planet found by "
     "solving equations before anyone actually saw it.",
     34),
    # score: funny 8, earns-name 9, fresh 8, tight 8 = 33
    # Uranus rolls around the Sun on its side, tilted about 98 degrees,
    # most likely knocked over by an ancient collision. The intern who
    # got knocked over on day one and just kept rolling is the same joke.
    ("Uranus is now 'The Intern' — knocked on its side on day one and "
     "has been rolling with it for 4.5 billion years.",
     33),
    # score: funny 8, earns-name 9, fresh 8, tight 8 = 33
    # Venus is the only planet that spins backwards. The contrarian who
    # insists everyone else is doing it wrong fits that one fact only.
    ("Venus is now 'The Contrarian' — the only planet that spins "
     "backwards and still insists everyone else is doing it wrong.",
     33),
    # score: funny 8, earns-name 9, fresh 7, tight 8 = 32
    # Jupiter's gravity really does swallow or deflect comets headed
    # inward, shielding the smaller planets. The bouncer who eats
    # trouble for a living is that job, humanised.
    ("Jupiter is now 'The Bouncer' — it eats comets for a living so "
     "the little planets can party in peace.",
     32),
    # score: funny 8, earns-name 9, fresh 7, tight 8 = 32
    # Jupiter has 95 known moons and its gravity herds comets. The
    # overprotective dad with too many kids to watch is the same shape.
    ("Jupiter is now 'The Overprotective Dad' — 95 moons, and it still "
     "follows every comet home to make sure it behaves.",
     32),
    # score: funny 8, earns-name 8, fresh 7, tight 8 = 31
    # Neptune has the fastest winds in the solar system, up to about
    # 2,100 km/h, and orbits 30 times farther out than Earth. A tantrum
    # nobody can hear is the distance doing the joke's work.
    ("Neptune is now 'The Drama Queen' — it throws 2,100 km/h tantrums "
     "30 times farther from the Sun than anyone can hear.",
     31),
    # score: funny 7, earns-name 8, fresh 7, tight 8 = 30
    # Mercury is the most cratered planet, pocked by impacts, and the
    # closest to the Sun. Freckles from standing too close to the Sun
    # without sunscreen is that fact as a school photo.
    ("Mercury is now 'The Freckled Kid' — covered in craters from "
     "standing too close to the Sun without sunscreen.",
     30),
    # score: funny 7, earns-name 9, fresh 7, tight 7 = 30
    # Uranus has the coldest atmosphere of any planet despite not being
    # the farthest out, and it lies on its side. The ice bath is both
    # facts in one image.
    ("Uranus is now 'The Ice Bath' — coldest atmosphere in the solar "
     "system, and it got that way by lying on its side.",
     30),
    # score: funny 7, earns-name 8, fresh 6, tight 7 = 28
    # Mercury laps the Sun in 88 days and swings hundreds of degrees
    # between day and night. The commuter who is always early and
    # always complaining about the weather is that orbit, humanised.
    ("Mercury is now 'The Commuter' — it laps the Sun in 88 days and "
     "still complains about the temperature swing.",
     28),
    # score: funny 7, earns-name 7, fresh 5, tight 7 = 26
    # Saturn's rings are its one unmistakable feature. The influencer
    # who wore one ring to a party 4 billion years ago leans on the
    # rings-as-jewellery angle, which is the first one anyone reaches for.
    ("Saturn is now 'The Influencer' — it wore one ring to a party 4 "
     "billion years ago and never took it off.",
     26),
]


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text.strip(), "candidate must be a single line"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 200, "entry.txt outside the gate"
    assert "\n" not in written.strip(), "entry.txt must be a single line"
    print(line)


if __name__ == "__main__":
    main()
