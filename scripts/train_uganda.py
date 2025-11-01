import arcpy
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.PointsToLine(
    Input_Features=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_points.kml\Points",
    Output_Feature_Class=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_line",
    Line_Field=None,
    Sort_Field=None,
    Close_Line="NO_CLOSE",
    Line_Construction_Method="CONTINUOUS",
    Attribute_Source="NONE",
    Transfer_Fields=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.Project(
    in_dataset="kabwangsi_line",
    out_dataset=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_line_Project",
    out_coor_system='PROJCS["Adindan_UTM_Zone_36N",GEOGCS["GCS_Adindan",DATUM["D_Adindan",SPHEROID["Clarke_1880_RGS",6378249.145,293.465]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",33.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    transform_method=None,
    in_coor_system='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],VERTCS["EGM96_height",VDATUM["EGM96_Geoid"],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]',
    preserve_shape="NO_PRESERVE_SHAPE",
    max_deviation=None,
    vertical="NO_VERTICAL"
)
arcpy.ImportToolbox(r"@\3D Analyst Tools.tbx")
arcpy.ddd.InterpolateShape(
    in_surface="n01_e034_1arc_v3.tif",
    in_feature_class="kabwangsi_line_Project",
    out_feature_class=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\path_3D",
    sample_distance=None,
    z_factor=1,
    method="BILINEAR",
    vertices_only="DENSIFY",
    pyramid_level_resolution=0,
    preserve_features="EXCLUDE"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.ProjectRaster(
    in_raster="n01_e034_1arc_v3.tif",
    out_raster=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\n01_e034_1arc__ProjectRaster",
    out_coor_system='PROJCS["Adindan_UTM_Zone_36N",GEOGCS["GCS_Adindan",DATUM["D_Adindan",SPHEROID["Clarke_1880_RGS",6378249.145,293.465]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",33.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    resampling_type="NEAREST",
    cell_size="30,8317365299026 30,8317365299026",
    geographic_transform=None,
    Registration_Point=None,
    in_coor_system='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]',
    vertical="NO_VERTICAL"
)
arcpy.ImportToolbox(r"@\3D Analyst Tools.tbx")
arcpy.ddd.InterpolateShape(
    in_surface="n01_e034_1arc__ProjectRaster",
    in_feature_class="kabwangsi_line_Project",
    out_feature_class=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\n01_e034_1arc__InterpolateSh",
    sample_distance=None,
    z_factor=1,
    method="BILINEAR",
    vertices_only="DENSIFY",
    pyramid_level_resolution=0,
    preserve_features="EXCLUDE"
)
arcpy.ImportToolbox(r"@\3D Analyst Tools.tbx")
arcpy.ddd.InterpolateShape(
    in_surface="n01_e034_1arc__ProjectRaster",
    in_feature_class="kabwangsi_line_Project",
    out_feature_class=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_campus",
    sample_distance=None,
    z_factor=1,
    method="BILINEAR",
    vertices_only="DENSIFY",
    pyramid_level_resolution=0,
    preserve_features="EXCLUDE"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.GeneratePointsAlongLines(
    Input_Features="kabwangsi_campus",
    Output_Feature_Class=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_campus_GeneratePointsAlongLines",
    Point_Placement="DISTANCE",
    Distance="20 Meters",
    Percentage=None,
    Include_End_Points="NO_END_POINTS",
    Add_Chainage_Fields="NO_CHAINAGE",
    Distance_Field=None,
    Distance_Method="PLANAR"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportCAD(
    in_features="kabwangsi_campus_GeneratePointsAlongLines;kabwangsi_campus;kabwangsi_line_Project",
    Output_Type="DWG_R2018",
    Output_File=r"D:\PORTAFOLIO\PROYECTO 02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_G_ExportCAD.dwg",
    Ignore_FileNames="Ignore_Filenames_in_Tables",
    Append_To_Existing="Overwrite_Existing_Files",
    Seed_File=None
)
arcpy.ImportToolbox(r"@\3D Analyst Tools.tbx")
arcpy.ddd.Contour(
    in_raster="n01_e034_1arc__ProjectRaster",
    out_polyline_features=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Contour",
    contour_interval=2,
    base_contour=0,
    z_factor=1,
    contour_type="CONTOUR",
    max_vertices_per_feature=None
)
arcpy.ImportToolbox(r"@\3D Analyst Tools.tbx")
arcpy.ddd.Contour(
    in_raster="n01_e034_1arc__ProjectRaster",
    out_polyline_features=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Contour",
    contour_interval=1,
    base_contour=0,
    z_factor=1,
    contour_type="CONTOUR",
    max_vertices_per_feature=None
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="n01_e034_1arc__ProjectRaster",
        reclass_field="Value",
        remap="1021 1577,301961 1;1577,301961 2586,407843 2;2586,407843 4320 3",
        missing_values="DATA"
    )
    out_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Reclass_terrain")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="n01_e034_1arc__ProjectRaster",
        reclass_field="Value",
        remap="1021 1169 1;1169 1200 2;1200 1201 3",
        missing_values="DATA"
    )
    out_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Reclass_n01_1")
arcpy.ImportToolbox(r"@\3D Analyst Tools.tbx")
arcpy.ddd.Slope(
    in_raster="n01_e034_1arc__ProjectRaster",
    out_raster=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Slope_n01_e01",
    output_measurement="PERCENT_RISE",
    z_factor=1,
    method="PLANAR",
    z_unit="METER",
    analysis_target_device="GPU_THEN_CPU"
)
arcpy.ImportToolbox(r"@\Analysis Tools.tbx")
arcpy.analysis.Buffer(
    in_features="kabwangsi_campus",
    out_feature_class=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_campus_Buffer",
    buffer_distance_or_field="100 Meters",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="ALL",
    dissolve_field=None,
    method="PLANAR"
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    out_raster = arcpy.sa.ExtractByMask(
        in_raster="n01_e034_1arc__ProjectRaster",
        in_mask_data="kabwangsi_campus_Buffer",
        extraction_area="INSIDE",
        analysis_extent='624657.157300003 125886.296093348 625317.767300001 126366.987106657 PROJCS["Adindan_UTM_Zone_36N".GEOGCS["GCS_Adindan".DATUM["D_Adindan".SPHEROID["Clarke_1880_RGS".6378249.145.293.465]].PRIMEM["Greenwich".0.0].UNIT["Degree".0.0174532925199433]].PROJECTION["Transverse_Mercator"].PARAMETER["False_Easting".500000.0].PARAMETER["False_Northing".0.0].PARAMETER["Central_Meridian".33.0].PARAMETER["Scale_Factor".0.9996].PARAMETER["Latitude_Of_Origin".0.0].UNIT["Meter".1.0]]'
    )
    out_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Extract_n01_1")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="Extract_n01_1",
        reclass_field="Value",
        remap="1162 1166,666667 1;1166,666667 1171,333333 2;1171,333333 1176 3",
        missing_values="DATA"
    )
    out_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_dem_reclass")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    out_raster = arcpy.sa.ExtractByMask(
        in_raster="Slope_n01_e01",
        in_mask_data="kabwangsi_campus",
        extraction_area="INSIDE",
        analysis_extent='624757.157300001 125986.195400003 625217.7673 126267.087800002 PROJCS["Adindan_UTM_Zone_36N".GEOGCS["GCS_Adindan".DATUM["D_Adindan".SPHEROID["Clarke_1880_RGS".6378249.145.293.465]].PRIMEM["Greenwich".0.0].UNIT["Degree".0.0174532925199433]].PROJECTION["Transverse_Mercator"].PARAMETER["False_Easting".500000.0].PARAMETER["False_Northing".0.0].PARAMETER["Central_Meridian".33.0].PARAMETER["Scale_Factor".0.9996].PARAMETER["Latitude_Of_Origin".0.0].UNIT["Meter".1.0]]'
    )
    out_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_pendiente_linea")
arcpy.ImportToolbox(r"@\Analysis Tools.tbx")
arcpy.analysis.Buffer(
    in_features="kabwangsi_campus",
    out_feature_class=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_campus_Buffer1",
    buffer_distance_or_field="1 Millimeters",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)
arcpy.ImportToolbox(r"@\3D Analyst Tools.tbx")
arcpy.ddd.Int(
    in_raster_or_constant="Slope_n01_e01",
    out_raster=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Int_Slope_n01"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.BuildRasterAttributeTable(
    in_raster="Int_Slope_n01",
    overwrite="NONE",
    convert_colormap="NONE"
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression=' "Int_Slope_n01" /1000'
    )
    output_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\pendiente_porcentaje")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression=' "Int_Slope_n01" / 100'
    )
    output_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\pendiente_porcentaje")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression=' "Int_Slope_n01" /100'
    )
    output_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\pendiente_porcentaje")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="pendiente_porcentaje",
        reclass_field="VALUE",
        remap="0 3 1;3 6 2;6 7,940000 3",
        missing_values="DATA"
    )
    out_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Reclass_pendientes")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression=' Con("Reclass_pendientes" ==1 ,"Reclass_pendientes")'
    )
    output_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\low_pendients")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    output_raster = arcpy.sa.RasterCalculator(
        expression=' Con("Slope_n01_e01" <=3 ,"Slope_n01_e01")'
    )
    output_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\pendientes_bajas")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    out_raster = arcpy.sa.ExtractByMask(
        in_raster="pendientes_bajas",
        in_mask_data="kabwangsi_campus",
        extraction_area="INSIDE",
        analysis_extent='624757.157300001 125986.195400003 625217.7673 126267.087800002 PROJCS["Adindan_UTM_Zone_36N".GEOGCS["GCS_Adindan".DATUM["D_Adindan".SPHEROID["Clarke_1880_RGS".6378249.145.293.465]].PRIMEM["Greenwich".0.0].UNIT["Degree".0.0174532925199433]].PROJECTION["Transverse_Mercator"].PARAMETER["False_Easting".500000.0].PARAMETER["False_Northing".0.0].PARAMETER["Central_Meridian".33.0].PARAMETER["Scale_Factor".0.9996].PARAMETER["Latitude_Of_Origin".0.0].UNIT["Meter".1.0]]'
    )
    out_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\pendientes_bajas_clip")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(scratchWorkspace=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb"):
    out_raster = arcpy.sa.ExtractByMask(
        in_raster="pendientes_bajas",
        in_mask_data="kabwangsi_campus",
        extraction_area="INSIDE",
        analysis_extent='624757.157300001 125986.195400003 625217.7673 126267.087800002 PROJCS["Adindan_UTM_Zone_36N".GEOGCS["GCS_Adindan".DATUM["D_Adindan".SPHEROID["Clarke_1880_RGS".6378249.145.293.465]].PRIMEM["Greenwich".0.0].UNIT["Degree".0.0174532925199433]].PROJECTION["Transverse_Mercator"].PARAMETER["False_Easting".500000.0].PARAMETER["False_Northing".0.0].PARAMETER["Central_Meridian".33.0].PARAMETER["Scale_Factor".0.9996].PARAMETER["Latitude_Of_Origin".0.0].UNIT["Meter".1.0]]'
    )
    out_raster.save(r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\Extract_pend1")
arcpy.ImportToolbox(r"@\3D Analyst Tools.tbx")
arcpy.ddd.Int(
    in_raster_or_constant="Extract_pend1",
    out_raster=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\pendientes_bajas_entero"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPolygon(
        in_raster="pendientes_bajas_entero",
        out_polygon_features=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\low_pend_poly",
        simplify="SIMPLIFY",
        raster_field="Value",
        create_multipart_features="SINGLE_OUTER_PART",
        max_vertices_per_feature=None
    )
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPolygon(
        in_raster="pendientes_bajas_entero",
        out_polygon_features=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\RasterT_pendien1",
        simplify="NO_SIMPLIFY",
        raster_field="Value",
        create_multipart_features="SINGLE_OUTER_PART",
        max_vertices_per_feature=None
    )
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateGeometryAttributes(
    in_features="low_pend_poly",
    geometry_property="Area_m2 AREA",
    length_unit="",
    area_unit="SQUARE_METERS",
    coordinate_system='PROJCS["Adindan_UTM_Zone_36N",GEOGCS["GCS_Adindan",DATUM["D_Adindan",SPHEROID["Clarke_1880_RGS",6378249.145,293.465]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",33.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    coordinate_format="SAME_AS_INPUT"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportTable(
    in_table="low_pend_poly",
    out_table=r"D:\PORTAFOLIO\PROYECTO02. UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\low_pend_poly_Table",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Id "Id" true true false 4 Long 0 0,First,#,low_pend_poly,Id,-1,-1;Area_m2 "Area_m2" true true false 8 Double 0 0,First,#,low_pend_poly,Area_m2,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportTable(
    in_table="low_pend_poly",
    out_table=r"D:\PORTAFOLIO\PROYECTO02.UGANDA\KABWANGASI\low_pendt_poly_table.dbf",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Id "Id" true true false 4 Long 0 0,First,#,low_pend_poly,Id,-1,-1;gridcode "gridcode" true true false 4 Long 0 0,First,#,low_pend_poly,gridcode,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,low_pend_poly,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,low_pend_poly,Shape_Area,-1,-1;Area_m2 "Area_m2" true true false 8 Double 0 0,First,#,low_pend_poly,Area_m2,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.TableToExcel(
    Input_Table="low_pend_poly_Table",
    Output_Excel_File=r"D:\PORTAFOLIO\PROYECTO02.UGANDA\KABWANGASI\low_pendt_poly_table.xls",
    Use_field_alias_as_column_header="NAME",
    Use_domain_and_subtype_description="CODE"
)
arcpy.ImportToolbox(r"@\Analysis Tools.tbx")
arcpy.analysis.Buffer(
    in_features="kabwangsi_campus",
    out_feature_class=r"D:\PORTAFOLIO\PROYECTO02.UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\kabwangsi_campus_Buffer",
    buffer_distance_or_field="10 Meters",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="ALL",
    dissolve_field=None,
    method="PLANAR"
)
arcpy.ImportToolbox(r"@\Analysis Tools.tbx")
arcpy.analysis.Clip(
    in_features="low_pend_poly",
    clip_features="kabwangsi_campus_Buffer",
    out_feature_class=r"D:\PORTAFOLIO\PROYECTO02.UGANDA\KABWANGASI\kabwangsi_campus_MAP\kabwangsi_campus_MAP.gdb\low_pend_poly_Clip",
    cluster_tolerance=None
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.FeatureClassToShapefile(
    Input_Features="kabwangsi_campus_GeneratePointsAlongLines;kabwangsi_campus",
    Output_Folder=r"D:\PORTAFOLIO\PROYECTO02.UGANDA2025\PATHS\PATHS_AUTOCAD"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportCAD(
    in_features="kabwangsi_campus_GeneratePointsAlongLines;kabwangsi_campus",
    Output_Type="DWG_R2018",
    Output_File=r"D:\PORTAFOLIO\PROYECTO02.UGANDA2025\PATHS\PATHS_AUTOCAD\kabwangsi_campus_path.dwg",
    Ignore_FileNames="Ignore_Filenames_in_Tables",
    Append_To_Existing="Overwrite_Existing_Files",
    Seed_File=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateGeometryAttributes(
    in_features="kabwangsi_campus",
    geometry_property="Long LENGTH",
    length_unit="KILOMETERS",
    area_unit="",
    coordinate_system='PROJCS["Adindan_UTM_Zone_36N",GEOGCS["GCS_Adindan",DATUM["D_Adindan",SPHEROID["Clarke_1880_RGS",6378249.145,293.465]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",33.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    coordinate_format="SAME_AS_INPUT"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.TableToExcel(
    Input_Table="low_pend_poly_Clip",
    Output_Excel_File=r"D:\PORTAFOLIO\PROYECTO02.UGANDA2025\LOWER_TERRAIN_POLYGONS\kabwangsi_campus_table_poly.xls",
    Use_field_alias_as_column_header="NAME",
    Use_domain_and_subtype_description="CODE"
)
