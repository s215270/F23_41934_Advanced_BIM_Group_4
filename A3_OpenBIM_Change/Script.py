from pathlib import Path
import ifcopenshell

modelname = "LLYN_ARK"

try:
    dir_path = Path(__file__).parent
    model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
    model = ifcopenshell.open(model_url)
except OSError:
    try:
        import bpy
        model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        print(f"ERROR: please check your model folder : {model_url} does not exist")


import ifcopenshell.api
import bpy
from blenderbim.bim.ifc import IfcStore


### Our script ###


import bpy
            
walls = (model.by_type('IfcWall'))

for wall in walls:

    pset = ifcopenshell.util.element.get_pset(wall, 'Pset_WallCommon')
    #psets_WallCommon = psets['Pset_WallCommon']
    if "Beton 200" in pset['Reference']:
        ifcopenshell.api.run("pset.edit_pset", model, pset=model.by_id(pset["id"]), properties={"ThermalTransmittance": 0.35})
        pset = ifcopenshell.util.element.get_pset(wall, 'Pset_WallCommon')
        External=(pset['IsExternal'])
        Reference=(pset['Reference'])
        ThermalTransmittance=(pset['ThermalTransmittance'])
        print("External:",External,",","Name:",Reference,",","U-value:",ThermalTransmittance)
        
    if "Beton 350" in pset['Reference']:
        ifcopenshell.api.run("pset.edit_pset", model, pset=model.by_id(pset["id"]), properties={"ThermalTransmittance": 0.25})
        pset = ifcopenshell.util.element.get_pset(wall, 'Pset_WallCommon')
        External=(pset['IsExternal'])
        Reference=(pset['Reference'])
        ThermalTransmittance=(pset['ThermalTransmittance'])
        print("External:",External,",","Name:",Reference,",","U-value:",ThermalTransmittance)
        
    if "Sandwichelementer 305" in pset['Reference']:
        ifcopenshell.api.run("pset.edit_pset", model, pset=model.by_id(pset["id"]), properties={"ThermalTransmittance": 0.30})
        pset = ifcopenshell.util.element.get_pset(wall, 'Pset_WallCommon')
        External=(pset['IsExternal'])
        Reference=(pset['Reference'])
        ThermalTransmittance=(pset['ThermalTransmittance'])
        print("External:",External,",","Name:",Reference,",","U-value:",ThermalTransmittance)
    
model.write(r'C:\Users\cecil\OneDrive\Skrivebord\Assignment 3\New.ifc')
