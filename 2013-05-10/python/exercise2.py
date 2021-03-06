# exercise 2.py


#Generate the 2D profile curves of the car envelope in the three coordinate directions, 
#embed them in 3D (in the x=0, y=0 and z=0 planes, respectively, with the reference frame origin set 
#approximately at the car centroid) and mount them together in a "two-and-a-half-dimensional" (2.5D) or "pseudo-3D" model.

from pyplasm import *

domain = INTERVALS(1)(20)

#profile with y=0

def profile_xz():
	#control points
	#down
	fp0 = [[0.06*2,0,1.4],[0.06*2,0,0.9],[0.08*2,0,0.6],[0.11*2,0,0.3]]
	fp1 = [[0.11*2,0,0.3],[0.17*2,0,0.25],[0.5*2,0,0.16],[0.9*2,0,0.08]]
	#ruota anteriore
	fp2 = [[0.9*2,0,0.08],[0.8*2,0,0.8],[1*2,0,1.7],[1.2*2,0,2.1],[1.6*2,0,1.9],[1.8*2,0,1.5],[1.8*2,0,0]]
	fp10 = [[3.6,0,0],[7,0,0]]
	#ruota posteriore
	# fp11 = [[7.6,0,0],[0.8*2,0,0.8],[1*2,0,1.7],[1.2*2,0,2.1],[1.6*2,0,1.9],[1.8*2,0,1.5],[1.8*2,0,0]]
	#up
	fp3 = [[0.06*2,0,1.4],[0.45*2,0,2],[0.95*2,0,2.4],[1.4*2,0,2.6],[1.5*2,0,2.7],[1.7*2,0,2.6]]
	fp4 = [[3.4,0,2.6],[3.8,0,2.7],[4.2,0,3.3],[4.8,0,3.6],[4.7,0,3.8]]
	fp5 = [[4.7,0,3.8],[5.4,0,4],[6.1,0,4],[7,0,3.9]]
	fp6 = [[7,0,3.9],[7.1,0,3.7]]
	fp7 = [[7.1,0,3.7],[8.5,0,3.2],[9.2,0,2.9],[9.6,0,3],[10.1,0,3.1]]
	fp8 = [[10.1,0,3.1],[10,0,2.3],[10.2,0,2],[10.4,0,2]]
	fp9 = [[10.4,0,2],[10.2,0,1]]
	fp12 = [[10.2,0,1],[9.6,0,0.6],[9.3,0,0.3],[8.8,0,0]]

	#BEZIER CURVES
	fb0 = BEZIER(S1)(fp0)
	fb1 = BEZIER(S1)(fp1)
	fb2 = BEZIER(S1)(fp2)
	fb3 = BEZIER(S1)(fp3)
	fb4 = BEZIER(S1)(fp4)
	fb5 = BEZIER(S1)(fp5)
	fb6 = BEZIER(S1)(fp6)
	fb7 = BEZIER(S1)(fp7)
	fb8 = BEZIER(S1)(fp8)
	fb9 = BEZIER(S1)(fp9)
	fb10 = BEZIER(S1)(fp10)
	fb12 = BEZIER(S1)(fp12)

	# MAPPING
	fc0 = MAP(fb0)(domain)
	fc1 = MAP(fb1)(domain)
	fc2 = MAP(fb2)(domain)
	fc3 = MAP(fb3)(domain)
	fc4 = MAP(fb4)(domain)
	fc5 = MAP(fb5)(domain)
	fc6 = MAP(fb6)(domain)
	fc7 = MAP(fb7)(domain)
	fc8 = MAP(fb8)(domain)
	fc9 = MAP(fb9)(domain)
	fc10 = MAP(fb10)(domain)
	fc11 = T([1,3])([7-1.8,-0.08])(fc2)
	fc12 = MAP(fb12)(domain)
	# structuring
	side0 = STRUCT([fc0,fc1,fc2,fc3,fc4,fc5,fc6,fc7,fc8,fc9,fc10,fc12,fc11])
	side = STRUCT([side0, T([2])([5])(side0)])
	return side


# VIEW(profile_xz())


#profile with x=0

def profile_yz():
	#generic control points
	p0 = [[0,0.7,0.07],[0,1.06,0.14],[0,1.57,0.16],[0,2.1,0.25]]
	p1 = [[0,2.1,0.25],[0,2.64,0.27]]
	p2 = [[0,0.7,0.07],[0,0.55,0.26],[0,0.51,1],[0,0.45,1.42],[0,0.61,1.5]]
	p3 = [[0,0.61,1.5],[0,0.83,1.6],[0,1.07,2],[0,1.2,2.3]]
	p4 = [[0,1.2,2.3], [0,1.47,2.4],[0,1.9,2.4],[0,2.3,2.5],[0,2.6,2.5]]

	# FRONT control points
	# values for cubic HERMITE
	fp0 = [[0,0.86,1.4],[0,1.6,1.15],[0,0.8,1],[0,0.3,-0.8]]
	# fp0 = [[0,0.86,1.6],[0,1.2,1.5],[0,1.36,1.39],[0,1.6,1.15]]
	

	fp1 = [[0,2.64,1.6],[0,1,1.6]]
	fp2 = [[0,1,1.6],[0,1,1.9],[0,1.2,2.1],[0,1.4,2.3]]
	fp3 = [[0,1.4,2.3],[0,2.1,2.3],[0,2.64,2.3]]

	#faro
	fp4 = [[0,0.7,1.3],[0,0.9,1.37],[0,1.1,1.3],[0,1.2,1.1],[0,1.2,1]]
	fp5 = [[0,1.2,1],[0,0.9,1],[0,0.7,1.2],[0,0.7,1.3]]

	#presa d'aria
	fp6 = [[0,0.8,0.5],[0,1,0.7],[0,1.5,0.7],[0,1.9,0.6],[0,2,0.4]]
	fp7 = [[0,2,0.4],[0,1.8,0.3],[0,1.1,0.3],[0,0.9,0.4],[0,0.8,0.5]]


	# RETRO control points
	rp0 = [[0,2.5,2.64],[0,1.4,2.4]]
	rp1 = [[0,1.4,2.4],[0,1.2,2.1],[0,1.5,1.8],[0,1.7,1.9]]
	rp2 = [[0,2.64,1.9],[0,1.8,1.9],[0,1.3,1.8],[0,0.7,1.7]]
	rp3 = [[0,0.7,1.7],[0,0.5,1.6],[0,0.6,1.2]]
	rp4 = [[0,0.4,1.6],[0,0.5,2],[0,0.8,2],[0,1.4,1.8]]


	# generic bezier curves
	b0 = BEZIER(S1)(p0)
	b1 = BEZIER(S1)(p1)
	b2 = BEZIER(S1)(p2)
	b3 = BEZIER(S1)(p3)
	b4 = BEZIER(S1)(p4)

	#front  curves
	fb0 = CUBICHERMITE(S1)(fp0)
	
	fb1 = BEZIER(S1)(fp1)
	fb2 = BEZIER(S1)(fp2)
	fb3 = BEZIER(S1)(fp3)
	fb4 = BEZIER(S1)(fp4)
	fb5 = BEZIER(S1)(fp5)
	fb6 = BEZIER(S1)(fp6)
	fb7 = BEZIER(S1)(fp7)

	#retro curves
	rb0 = BEZIER(S1)(rp0)
	rb1 = BEZIER(S1)(rp1)
	rb2 = BEZIER(S1)(rp2)
	rb3 = BEZIER(S1)(rp3)
	rb4 = BEZIER(S1)(rp4)

	# generic MAPPINGS
	c0 = MAP(b0)(domain)
	c1 = MAP(b1)(domain)
	c2 = MAP(b2)(domain)
	c3 = MAP(b3)(domain)
	c4 = MAP(b4)(domain)

	#front mappings
	fc0 = MAP(fb0)(domain)
	fc1 = MAP(fb1)(domain)
	fc2 = MAP(fb2)(domain)
	fc3 = MAP(fb3)(domain)
	fc4 = MAP(fb4)(domain)
	fc5 = MAP(fb5)(domain)
	fc6 = MAP(fb6)(domain)
	fc7 = MAP(fb7)(domain)

	#retro mappings
	rc0 = MAP(rb0)(domain)
	rc1 = MAP(rb1)(domain)
	rc2 = MAP(rb2)(domain)
	rc3 = MAP(rb3)(domain)
	rc4 = MAP(rb4)(domain)


	# generic structuring
	faro = T([2,3])([0.2,-0.1])(STRUCT([fc4,fc5]))
	front = STRUCT([fc0,fc1,fc2,fc3,fc6,fc7,faro])
	
	retro = STRUCT([rc0,rc1,rc2,rc3,rc4])
	
	g0 = STRUCT([c0,c1,c2,c3,c4,front])
	gr = STRUCT([c0,c1,c2,c3,c4,retro])
	
	# r_t front
	g1 = R([1,2])(PI)(g0)
	t_g1 = T([2])([5.2])(g1)
	
	#r_t retro
	g2 = R([1,2])(PI)(gr)
	t_g2 = T([2])([5.2])(g2)
	
	gen_f = STRUCT([g0,t_g1])
	gen_r = STRUCT([gr,t_g2])
	gen = STRUCT([gen_f,T([1])([10.8])(gen_r)])

	return gen


# VIEW(profile_yz())


# profile xy (z=0)

def profile_xy():

	# generic contro points

	p0 = [[0,2.1,0],[0.1,1.4,0],[0.5,0.4,0],[0.9,0.2,0],[1.8,0,0]]
	p1 = [[1.8,0,0],[9.1,0,0]]
	p2 = [[9.1,0,0],[10,0.2,0],[10.3,0.7,0],[10.5,2.1,0]]

	# generic curves

	b0 = BEZIER(S1)(p0)
	b1 = BEZIER(S1)(p1)
	b2 = BEZIER(S1)(p2)

	# generic mapping

	c0 = MAP(b0)(domain)
	c1 = MAP(b1)(domain)
	c2 = MAP(b2)(domain)

	# generic structuring

	gen0 = STRUCT([c0,c1,c2])
	gen1 = STRUCT([gen0, T([2])([4.2])(R([2,3])(PI)(gen0))])


	# up control points

	up0 = [[0.38,2.1,0],[0.5,1.4,0],[1,1,0],[3,0.7,0]]
	up1 = [[2.8,2.1,0],[3,0.7,0],[3.5,0.5,0]]
	up2 = [[3.5,0.5,0],[4.7,0.8,0],[4.7,1.4,0],[4.7,2.1,0]]
	up3 = [[7,2.1,0],[6.9,1,0]]
	up4 = [[6.9,1,0], [7.5,0.8,0],[9,0.9,0],[10,1.1,0]]
	up5 = [[10,1.1,0], [10,2.1,0]]

	# up curves

	ub0 = BEZIER(S1)(up0)
	ub1 = BEZIER(S1)(up1)
	ub2 = BEZIER(S1)(up2)
	ub3 = BEZIER(S1)(up3)
	ub4 = BEZIER(S1)(up4)
	ub5 = BEZIER(S1)(up5)

	# up mapping

	uc0 = MAP(ub0)(domain)
	uc1 = MAP(ub1)(domain)
	uc2 = MAP(ub2)(domain)
	uc3 = MAP(ub3)(domain)
	uc4 = MAP(ub4)(domain)
	uc5 = MAP(ub5)(domain)

	#  structuring

	up0 = STRUCT([gen0,uc0,uc1,uc2,uc3,uc4,uc5])
	up1 = STRUCT([up0, T([2])([4.2])(R([2,3])(PI)(up0))])

	gen = STRUCT([gen1, T([3])([2.7])(R([1,3])(PI/20)(up1))])

	return gen



profile = STRUCT([profile_xz(), profile_yz(), profile_xy()])

VIEW(profile)