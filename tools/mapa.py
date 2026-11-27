import numpy as np
from PIL import Image,ImageFilter
from scipy.ndimage import gaussian_filter,distance_transform_edt,map_coordinates,binary_opening
S='/tmp/tg/example/img/'
W,H=4096,2048
bm=np.asarray(Image.open(S+'earth-blue-marble.jpg').convert('RGB')).astype(np.float32)
wat=np.asarray(Image.open(S+'earth-water.png').convert('L').resize((W,H),Image.BILINEAR)).astype(np.float32)/255
topo=np.asarray(Image.open(S+'earth-topology.png').convert('L').resize((W,H),Image.BICUBIC)).astype(np.float32)/255
land=wat<0.5
land=binary_opening(land,iterations=1)
# cor da terra: Blue Marble suavizado e mais vivo
col=np.stack([gaussian_filter(bm[...,c],3) for c in range(3)],-1)
mx=col.max(-1,keepdims=True);mn=col.min(-1,keepdims=True);mean=col.mean(-1,keepdims=True)
ice=(mn[...,0]>150)&((mx-mn)[...,0]<50)
col=mean+(col-mean)*1.55;col=np.clip(col*1.18+8,0,255)
# puxa verdes e beges para uma paleta limpa
g=np.array([88,150,72],np.float32);t=np.array([206,184,128],np.float32)
dry=np.clip((col[...,0]-col[...,1]+20)/60,0,1)[...,None]
pal=g*(1-dry)+t*dry
col=col*0.35+pal*0.65
# relevo (sombra de colinas, luz do noroeste)
e=gaussian_filter(topo,1.2)
gx=np.gradient(e,axis=1);gy=np.gradient(e,axis=0)
shade=np.clip(1+(-gx*1+ -gy*1)*55,0.62,1.35)[...,None]
col=col*shade
col[ice]=np.array([240,246,250])*np.clip(shade[ice],0.85,1.1)
# oceano: azul limpo, mais claro perto da costa
d=distance_transform_edt(~land)
k=np.clip(d/14,0,1)[...,None]
ocean=np.array([44,98,150],np.float32)*(1-k)+np.array([22,58,104],np.float32)*k
out=np.where(land[...,None],col,ocean)
latg=np.linspace(90,-90,H)[:,None]*np.ones((1,W))
ant=(latg<-60)&land|(latg<-78)
sm=gaussian_filter(topo,3);gx2=np.gradient(sm,axis=1);gy2=np.gradient(sm,axis=0)
ish=np.clip(1+(-gx2-gy2)*25,0.9,1.06)
out[ant]=np.array([236,243,247],np.float32)*(0.96+0.04*np.clip((-latg[ant]-60)/30,0,1))[:,None]
# contorno fino da costa
edge=(distance_transform_edt(land)<=1.5)&land
out[edge]=out[edge]*0.82
out=np.clip(out,0,255)
eq=Image.fromarray(out.astype(np.uint8))
eq.resize((1024,512)).save('/tmp/mapa_eq_prev.jpg')
# reprojeta para o disco
N=2048;y,x=np.mgrid[0:N,0:N].astype(np.float32);u=(x+0.5)/N*2-1;v=(y+0.5)/N*2-1;r=np.hypot(u,v)
lat=90-180*np.clip(r,0,1);lon=np.degrees(np.arctan2(u,v))
px=((lon+180)/360*W-0.5)%W;py=np.clip((90-lat)/180*H-0.5,0,H-1)
o=np.zeros((N,N,3),np.float32)
for c in range(3):o[...,c]=map_coordinates(out[...,c],[py,px],order=1,mode='wrap')
o[r>1.002]=0
Image.fromarray(o.astype(np.uint8)).save('/home/claude/planetarium/terra/mapa.jpg',quality=86,optimize=True,progressive=True)
Image.fromarray(o.astype(np.uint8)).resize((800,800)).save('/tmp/mapa_prev.jpg')
