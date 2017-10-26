#Python script to create moorland line distance raster


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Moorland Line © RPA"

arcpy.gp.EucDistance_sa("Moorland Line © RPA","C:/Christoph/enBlanketBogModel/data/moorland_distance_inside.tif","#","50","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "moorland_line_inverse"


arcpy.gp.EucDistance_sa("moorland_line_inverse","C:/Christoph/enBlanketBogModel/data/moorland_distance_inside2.tif","#","50","#")

arcpy.gp.RasterCalculator_sa(""""moorland_distance_inside2.tif" * (-1)""","C:/Christoph/enBlanketBogModel/data/moorland_distance_inside_neg2.tif")

arcpy.gp.RasterCalculator_sa(""""moorland_distance_inside_neg2.tif" + "moorland_distance.tif"""","C:/Christoph/enBlanketBogModel/data/moorland_distance_all3.tif")