import cv2
import numpy as np

app = cv2.imread('apple.png')
org = cv2.imread('orange.jpg')
app = cv2.resize(app,(512,512))
org = cv2.resize(org,(512,512))
app_org = np.hstack((app[:,:int(512/2)],org[:,int(512/2):]))

'''
apple gaussian
'''
app_copy = app.copy()
gp_app = [app_copy] # generate gaussian pyramid

for i in range(6):
    app_copy = cv2.pyrDown(app_copy)
    gp_app.append(app_copy)

'''
orange gaussian
'''
org_copy = org.copy()
gp_org = [org_copy] # generate gaussian pyramid

for i in range(6):
    org_copy = cv2.pyrDown(org_copy)
    gp_org.append(org_copy)

'''
apple laplacian 
'''
app_copy = gp_app[5]
lp_app = [app_copy]
for i in range(5,0,-1):
    gp_expand_app = cv2.pyrUp(gp_app[i])
    lap_app = cv2.subtract(gp_app[i-1],gp_expand_app)
    lp_app.append(lap_app)

'''
orange laplacian 
'''
org_copy = gp_org[5]
lp_org = [org_copy]
for i in range(5,0,-1):
    gp_expand_org = cv2.pyrUp(gp_org[i])
    lap_org = cv2.subtract(gp_org[i-1],gp_expand_org)
    lp_org.append(lap_org)


# last step join the images
app_org_pyr = []
for la,lo in zip(lp_app,lp_org):
    row,col,rgb = la.shape
    construct = np.hstack((la[:,:int(col/2)],lo[:,int(col/2):]))
    app_org_pyr.append(construct)

'''RECONSTRUCT'''
app_org_re = app_org_pyr[0]
for i in range(1,6):
    app_org_re = cv2.pyrUp(app_org_re)
    app_org_re = cv2.add(app_org_pyr[i],app_org_re)

cv2.imshow('apple',app)
cv2.imshow('orange',org)
cv2.imshow('local_comb',app_org)
cv2.imshow('perfect_comb',app_org_re)
cv2.waitKey(0)