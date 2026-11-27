# Gera cidades-mundo.json a partir do Natural Earth (domínio público):
# ne_10m_populated_places_simple.geojson -> [nome, lat, lon, população, min_zoom, capital_do_país]
import json, sys
src = sys.argv[1] if len(sys.argv) > 1 else "ne_10m_populated_places_simple.geojson"
d = json.load(open(src, encoding="utf-8"))
PT = {"Tokyo":"Tóquio","New York":"Nova York","Moscow":"Moscou","Beijing":"Pequim","London":"Londres","Mexico City":"Cidade do México","Seoul":"Seul","Istanbul":"Istambul","Rome":"Roma","Berlin":"Berlim","Lisbon":"Lisboa",
 "Johannesburg":"Joanesburgo","Cape Town":"Cidade do Cabo","Shanghai":"Xangai","Delhi":"Délhi","New Delhi":"Nova Délhi","Washington, D.C.":"Washington","Athens":"Atenas","Warsaw":"Varsóvia","Vienna":"Viena","Prague":"Praga",
 "Brussels":"Bruxelas","Copenhagen":"Copenhague","Stockholm":"Estocolmo","Geneva":"Genebra","Singapore":"Singapura","Jakarta":"Jacarta","Tehran":"Teerã","Baghdad":"Bagdá","Riyadh":"Riad","Jerusalem":"Jerusalém",
 "Havana":"Havana","Montevideo":"Montevidéu","Asunción":"Assunção","Kiev":"Kiev","Kyiv":"Kiev","Saint Petersburg":"São Petersburgo","St. Petersburg":"São Petersburgo","Munich":"Munique","Milan":"Milão","Naples":"Nápoles","Florence":"Florença",
 "Venice":"Veneza","Edinburgh":"Edimburgo","Mecca":"Meca","Cairo":"Cairo","Algiers":"Argel","Tunis":"Túnis","Rabat":"Rabat","Casablanca":"Casablanca","Ankara":"Ancara","Damascus":"Damasco","Beirut":"Beirute","Kabul":"Cabul",
 "Hanoi":"Hanói","Kathmandu":"Katmandu","Bucharest":"Bucareste","Budapest":"Budapeste","Belgrade":"Belgrado","Sofia":"Sófia","Zurich":"Zurique","Amsterdam":"Amsterdã","The Hague":"Haia","Seville":"Sevilha","Barcelona":"Barcelona",
 "Lyon":"Lyon","Marseille":"Marselha","Cologne":"Colônia","Hamburg":"Hamburgo","Frankfurt":"Frankfurt","Philadelphia":"Filadélfia","New Orleans":"Nova Orleans","Bogota":"Bogotá","Brasilia":"Brasília","Panama City":"Cidade do Panamá",
 "Guatemala":"Cidade da Guatemala","Kuala Lumpur":"Kuala Lumpur","Taipei":"Taipé","Osaka":"Osaka","Addis Ababa":"Adis Abeba","Dakar":"Dacar","Khartoum":"Cartum","Moscow":"Moscou","Krakow":"Cracóvia","Gdansk":"Gdańsk"}
out = []
for f in d["features"]:
    p = f["properties"]
    pop = int(p.get("pop_max") or 0)
    if pop < 15000 and not p.get("adm0cap"):
        continue
    out.append([PT.get(p["name"], p["name"]), round(p["latitude"], 3), round(p["longitude"], 3), pop, round(p.get("min_zoom") or 10, 1), 1 if p.get("adm0cap") else 0])
out.sort(key=lambda r: (r[4], -r[3]))
json.dump(out, open("cidades-mundo.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out))
