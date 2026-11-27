"""Helper voor de begrippenlijsten in scripts/begrippen/<vak>.py (heet bewust niet lib.py: figuren/lib.py bestaat al)."""


def b(les, begrip, uitleg, art=None, ook=()):
    """Eén begrip. les = id van de les (zoals in vragen.json), uitleg zonder het begrip zelf, art = wetsartikel(en),
    ook = andere antwoorden die de dictee goed rekent (afkorting, synoniem)."""
    assert begrip.strip() and uitleg.strip(), (les, begrip)
    if isinstance(ook, str):
        ook = (ook,)
    return dict(les=les, begrip=begrip.strip(), uitleg=uitleg.strip(), art=art, ook=list(ook))
