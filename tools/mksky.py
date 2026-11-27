import json,sys
src=sys.argv[1];out=sys.argv[2]
S=json.load(open(src+'/stars.6.json'))['features']
N=json.load(open(src+'/starnames.json'))
L={f['id']:f['geometry']['coordinates'] for f in json.load(open(src+'/constellations.lines.json'))['features']}
C=json.load(open(src+'/constellations.json'))['features']
MW=json.load(open(src+'/milkyway.json'))['features']
PT={"And":"Andrômeda","Ant":"Máquina Pneumática","Aps":"Ave-do-Paraíso","Aqr":"Aquário","Aql":"Águia","Ara":"Altar","Ari":"Áries","Aur":"Cocheiro","Boo":"Boieiro","Cae":"Buril","Cam":"Girafa","Cnc":"Câncer","CVn":"Cães de Caça","CMa":"Cão Maior","CMi":"Cão Menor","Cap":"Capricórnio","Car":"Quilha","Cas":"Cassiopeia","Cen":"Centauro","Cep":"Cefeu","Cet":"Baleia","Cha":"Camaleão","Cir":"Compasso","Col":"Pomba","Com":"Cabeleira de Berenice","CrA":"Coroa Austral","CrB":"Coroa Boreal","Crv":"Corvo","Crt":"Taça","Cru":"Cruzeiro do Sul","Cyg":"Cisne","Del":"Golfinho","Dor":"Dourado","Dra":"Dragão","Equ":"Cavalo Menor","Eri":"Erídano","For":"Fornalha","Gem":"Gêmeos","Gru":"Grou","Her":"Hércules","Hor":"Relógio","Hya":"Hidra","Hyi":"Hidra Macho","Ind":"Índio","Lac":"Lagarto","Leo":"Leão","LMi":"Leão Menor","Lep":"Lebre","Lib":"Libra","Lup":"Lobo","Lyn":"Lince","Lyr":"Lira","Men":"Mesa","Mic":"Microscópio","Mon":"Unicórnio","Mus":"Mosca","Nor":"Esquadro","Oct":"Oitante","Oph":"Ofiúco","Ori":"Órion","Pav":"Pavão","Peg":"Pégaso","Per":"Perseu","Phe":"Fênix","Pic":"Pintor","Psc":"Peixes","PsA":"Peixe Austral","Pup":"Popa","Pyx":"Bússola","Ret":"Retículo","Sge":"Flecha","Sgr":"Sagitário","Sco":"Escorpião","Scl":"Escultor","Sct":"Escudo","Ser":"Serpente","Ser1":"Serpente","Ser2":"Serpente","Sex":"Sextante","Tau":"Touro","Tel":"Telescópio","Tri":"Triângulo","TrA":"Triângulo Austral","Tuc":"Tucano","UMa":"Ursa Maior","UMi":"Ursa Menor","Vel":"Vela","Vir":"Virgem","Vol":"Peixe Voador","Vul":"Raposa"}
OV={32349:"Sírius",30438:"Canopus",71683:"Alfa Centauri",69673:"Arcturus",91262:"Vega",24608:"Capela",24436:"Rígel",37279:"Prócion",7588:"Achernar",27989:"Betelgeuse",68702:"Hadar",97649:"Altair",60718:"Ácrux",21421:"Aldebarã",80763:"Antares",65474:"Spica",37826:"Pólux",113368:"Fomalhaut",102098:"Deneb",62434:"Mimosa",49669:"Régulo",11767:"Polaris",61084:"Gácrux",36850:"Castor",25336:"Bellatrix",26311:"Alnilam",26727:"Alnitak",25930:"Mintaka",27366:"Saiph",59747:"Imai"}
ra=lambda x:round(x%360,3)
stars=[];names={};hips=[];des={}
S.sort(key=lambda f:f['properties']['mag'])
for i,f in enumerate(S):
    lo,la=f['geometry']['coordinates'];p=f['properties']
    try: bv=round(float(p.get('bv') or 0.6),2)
    except: bv=0.6
    stars+= [ra(lo),round(la,3),round(p['mag'],2),bv]
    hid=f['id'];nm=OV.get(hid) or (N.get(str(hid),{}).get('name') or '')
    hips.append(hid);sn=N.get(str(hid),{})
    dd=(sn.get('bayer') or sn.get('flam') or '').strip()
    if dd and sn.get('c'): des[i]=dd+' '+sn['c']
    elif sn.get('desig') and sn.get('c'): des[i]=sn['desig']+' '+sn['c']
    if nm and (p['mag']<3.6 or hid in OV): names[i]=nm
cons=[]
for f in C:
    cid=f['id'];lines=L.get(cid)
    if not lines: continue
    segs=[[v for pt in line for v in (ra(pt[0]),round(pt[1],2))] for line in lines]
    lo,la=f['geometry']['coordinates']
    cons.append([cid,PT.get(cid,f['properties']['name']),ra(lo),round(la,2),segs])
mw=[]
for f in MW:
    lvl=int(f['id'][-1]);step=6 if lvl<=2 else 4
    for ring in f['geometry']['coordinates']:
        if len(ring)<12: continue
        pts=ring[::step]
        mw.append([lvl,[v for pt in pts for v in (ra(pt[0]),round(pt[1],1))]])
json.dump({"s":stars,"n":names,"c":cons,"mw":mw,"h":hips,"d":des},open(out,'w'),ensure_ascii=False,separators=(',',':'))
print(len(stars)//4,len(names),len(cons),len(mw))
missing=[k for k in PT if k not in [c[0] for c in cons]];print('sem linhas:',missing)
