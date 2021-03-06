# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

#yibande
Point(0,0).has_z
Point(0,0,0).has_z

LinearRing([(1,0),(1,1),(0,0)]).is_ccw

ring= LinearRing([(0,0),(1,1),(1,0)])
ring.is_ccw
ring.coords = list(ring.coords)[::-1]
ring.is_ccw

Point().is_empty
Point(0,0).is_empty

from operator import attrgetter
empties = filter(attrgetter('is_empty'),[Point(),Point(0,0)])
len(empties)

LineString([(0,0),(1,1),(1,-1)]).is_ring
LinearString([(0,0),(1,1),(1,-1)]).is_ring

LineString([(0,0),(1,1),(1,-1),(0,1)]).is_simple

MultiPolygon([Point(0,0).buffer(2.0),Point(1,1).biffer(2.0)]).is_valid



