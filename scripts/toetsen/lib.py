# Helpers for the weekly practice tests (oefentoetsen). Each week file appends to T.
T = []
def mc(id, week, ond, vraag, opties, juist, uitleg):
    T.append(dict(id=id, week=week, onderdeel=ond, type="mc", vraag=vraag, opties=opties, juist=juist, uitleg=uitleg))
def op(id, week, ond, vraag, model, punten):
    T.append(dict(id=id, week=week, onderdeel=ond, type="open", vraag=vraag, modelantwoord=model, punten=punten))
def cs(id, week, ond, titel, casus, sub):
    T.append(dict(id=id, week=week, onderdeel=ond, type="casus", titel=titel, casus=casus,
                  subvragen=[dict(vraag=v, modelantwoord=m, punten=p) for (v, m, p) in sub]))
