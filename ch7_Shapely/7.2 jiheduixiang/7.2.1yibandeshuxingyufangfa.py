# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from shapely.geometry import Point
Point(0,0).geom_type

Point(0,0).distance(Point(1,1))

donut = Point(0,0).buffer(2,0).difference(Point(0,0).buffer(1.0))
donut.centroid.wkt
donut.representative_point().wkt

#duidianzhuang
import os
from osgeo import ogr
import shapely
import shapely.geometry

driver = ogr.GetDriverByName('ESRI Shape')
out_shp ='world_borders.shp'
if os.path.exists(out_shp):
    driver.DeleteDatasource(out_shp)

newds = driver.CreateDataSource(out_shp)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)

ds = ogr.Open('world_borders.shp')

layer = ds.GetLayer(0)
feat = layer.GetNextFeature()
while feat:
    fid = feat.GetField('X')
    print(fid)
    geom = feat.GetGeometryRef()
    print(geom)
    pt = shapely.geometry.Point(geom.GetX(),geom.GetY())
    vv = pt.buffer(3.0)

    tmp_wkb = vv_wkb()

    new_geom = ogr.CreateGeometryFromWkb(tmp_wkb)
    new_feat = ogr.Feature(layernew.GetLayerDefn())
    new_feat.SetGeometry(new_geom)
    layernew.CreateFeature(new_feat)

    feat = layer.GetNextFeature()

newds.Destroy()