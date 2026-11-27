# Textura no estilo do mapa de Gleason (1892): oceano claro com linhas de costa, terra creme, contorno marrom
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter,distance_transform_edt,map_coordinates,binary_opening
S='/tmp/tg/example/img/';W,H=4096,2048
wat=np.asarray(Image.open(S+'earth-water.png').convert('L').resize((W,H),Image.BILINEAR)).astype(np.float32)/255
topo=np.asarray(Image.open(S+'earth-topology.png').convert('L').resize((W,H),Image.BICUBIC)).astype(np.float32)/255
land=binary_opening(wat<0.5,iterations=1)
latg=np.linspace(90,-90,H)[:,None]*np.ones((1,W))
dl=distance_transform_edt(~land);di=distance_transform_edt(land)
ocean=np.zeros((H,W,3),np.float32)+np.array([200,224,229],np.float32)
for d0 in(4,9,15):
    band=np.exp(-((dl-d0)**2)/1.6)[...,None];ocean=ocean*(1-0.35*band)+np.array([120,165,185])*0.35*band
rng=np.random.default_rng(3);noise=gaussian_filter(rng.normal(0,1,(H//4,W//4)),2);noise=np.kron(noise,np.ones((4,4)))[:H,:W]
e=gaussian_filter(topo,1.5);gx=np.gradient(e,axis=1);gy=np.gradient(e,axis=0);sh=np.clip(1+(-gx-gy)*30,0.8,1.12)
base=np.array([236,221,170],np.float32)
tint=np.clip(0.5+noise*0.6,0,1)[...,None]
col=(base*(1-0.25*tint)+np.array([214,224,170],np.float32)*0.25*tint)*sh[...,None]
out=np.where(land[...,None],col,ocean)
ant=((latg<-60)&land)|(latg<-78);out[ant]=np.array([246,246,242],np.float32)
edge=(di<=1.6)&land;out[edge]=np.array([120,82,50],np.float32)
out=out*(1+0.025*noise[...,None]);out=np.clip(out,0,255)
N=2048;y,x=np.mgrid[0:N,0:N].astype(np.float32);u=(x+0.5)/N*2-1;v=(y+0.5)/N*2-1;r=np.hypot(u,v)
lat=90-180*np.clip(r,0,1);lon=np.degrees(np.arctan2(u,v));px=((lon+180)/360*W-0.5)%W;py=np.clip((90-lat)/180*H-0.5,0,H-1)
o=np.zeros((N,N,3),np.float32)
for c in range(3):o[...,c]=map_coordinates(out[...,c],[py,px],order=1,mode='wrap')
o[r>1.002]=0
Image.fromarray(o.astype(np.uint8)).save('/home/claude/planetarium/terra/gleason.jpg',quality=84,optimize=True,progressive=True)
Image.fromarray(o.astype(np.uint8)).resize((800,800)).save('/tmp/gl_prev.jpg')
