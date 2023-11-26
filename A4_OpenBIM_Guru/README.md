<style>
</style>

# **Introduction**

The chosen OpenBIM role is "level 1 models," which serves as an introductory
exercise for using OpenBIM. The tutorial video explains how to correctly
download BlenderBIM. It then demonstrates how to insert the transmission
coefficient for an exterior wall using scripting, utilizing an original IFC
model. At the end it demostrates how to save the new changes in a new IFC-file.
The purpose of this OpenBIM role is to explain how BlenderBIM works and how one
can use scripting to add missing data. This way, everyone will be able to
utilize our script, both beginners and those with more experience.

The focus area encompasses the indoor climate of a building. A comfortable indoor climate creates a pleasant environment, promoting good health and well-being for
occupants. By having an efficient indoor climate, energy consumption is reduced
since the building experiences less heat loss. For a building, the transmission
coefficient is crucial as it indicates the extent of heat loss. A low transmission coefficient means less heat is lost through the building's structure, reducing the need for heating or cooling. This can lead to lower energy consumption and energy costs. A low transmission coefficient influences maintaining a more consistent and comfortable indoor temperature. By reducing energy consumption, it contributes to reducing the overall environmental impact of the building by decreasing CO2 emissions from heating and cooling.

Our focus area is relevant for building owners as they often aim to reduce operational costs and may therefore be interested in having an energy-efficient building with a good transmission coefficient to decrease energy consumption. The focus area is also relevant for architects and engineers as they concentrate on creating energy-efficient and sustainable buildings.

# **Guide**

This is a guide on how to install Blender and Blender Add-ons. Additionally, we'll demonstrate how to use a script on an IFC file in Blender BIM.

**Download and install Blender:**

1. First you have to download Blender, which is a free and open-source program for 3D authoring.

2. Blender works on Linux, Mac, and Windows. You need to choose your preference.

3. Once you have downloaded Blender, click on the completed download and open the Blender setup.

4. Click "Next."

5. Now you will proceed to the "End-User License Agreement," where you accept the terms

6. Click "Next."

7. In the new window "Custom Setup," click "Next" again.

8. Now you are ready to instal Blender, so click "Install."

9. Once the installation is complete, click "Finish."

10. Now Blender is installed as a program on your computer.

11. Open Blender, where you will need toperform a quick setup. Click "Next."

12. The program is now ready for use.



**Download
BlenderBIM Add-on:**

1. Now you need to download the
   BlenderBIM add-on here: [Download - install the BlenderBIM Add-on for Windows, Mac, and Linux](https://blenderbim.org/download.html)

2. BlenderBIM Add-on works on Linux, Mac, and Windows. You have to choose your preference.

3. The BlenderBIM Add-on is now in downloads.

4. Create a folder on your computer called BlenderBIM, and move the file there.

5. Now open Blender.

6. In the top left, you will find the shortcut "Edit."

7. Select "Preferences."

8. The "Blender Preferences" window will open; click on "Add-ons."

9. In the top right corner, click "Install."

10. Now select your BlenderBIM folder.

11. Choose your Add-on and press "Install Add-on."

12. In the search field, type "BlenderBIM," and the Add-on will appear under the name "Import-Export: BlenderBIM."

13. Enable the add-on by pressing the checkbox.

14. Now the add-on is installed.



**Import an IFC-file in Blender:**

1. Now you have to import an IFC-file in Blender.

2. In the upper left corner, you'll find the shortcut 'File.'

3. Select 'Open IFC Project' and choose your preferred model.

4. Your building will now appear.
   
   

**Create folder structure:**

Now, you need to create a folder structure that consists of the script and a folder where the IFC model is located. 



**Open Github:**

1. Now you have to open GitHub. You can click on the link given in the report. link: [F23_41934_Advanced_BIM_Group_4/A3_OpenBIM_Change at
   main · s215270/F23_41934_Advanced_BIM_Group_4 (github.com)](https://github.com/s215270/F23_41934_Advanced_BIM_Group_4/tree/main/A3_OpenBIM_Change)

2. Download the Python script "Main.py".
   
   

**How toscript in Blender:**

1. Now you open a new window by placing the mouse in the corner until a plus icon appears. You can then drag it up, creating a new window. Here, in the toolbar, you can select 'Text Editor'.

2. Now choose "Open" and select the Python script "Main.py.



**Explainationof the script:**

1. First we are going to Import thenecessary libraries:
   
   1. `pathlib.Path` is imported to work
      with path names
   
   2. `ifcopenshell` is imported to handle
      IFC (Industry Foundation Classes) files.

2. Now we are going to Define variables and attempt to open an IFC model:
   
   1. `modelname` is the name of the model to be opened (in this case, "LLYN_ARK").
   
   2. The code first tries to open the file path where this code is executed (if possible) to find the IFC model.
   
   3. If that fails, it tries to use
      Blender's `bpy` library to find the model. If the model can't be found at the
      specified locations, it prints an error message.

3. Now we are going to Import more libraries and define the script:
   
   1. Additional libraries are imported for use in the rest of the code.
   
   2. Now the actual script begins

4. Collect the wall elements:
   
   1. `walls = (model.by_type('IfcWall'))`collects all wall elements from the opened IFC model that are the type 'IfcWall' and places them in the variable `walls`. The assumption is that these elements represent the walls in the model.

5. Iterate through wall elements:
   
   1. `for wall in walls:` starts a for loop that iterates through each wall element (`wall`) in the collection of walls.

6. Now we are going to Handle each wall element:
   
   1. For each wall, the code performs the following steps:
      
      1. `pset = ifcopenshell.util.element.get_pset(wall, 'Pset_WallCommon`  retrieves the properties (Property Sets) for the current wall based on a common name called 'Pset_WallCommon'
   
   2. Now we need to examine the wall’s
      properties (`pset`) for specific references:
      
      1. If the wall's reference matches a specific condition (e.g., "Concrete 200"), the code makes changes to the wall's properties; in this case, it changes the thermal transmittance value (ThermalTransmittance).
      
      2. After the changes, the wall's updated properties are printed, such as whether it's external (IsExternal), its name (Reference), and its thermal transmittance value (ThermalTransmittance).

7. This is repeated for each wall:
   
   1. The code repeats this pattern for each wall in the collected list, allowing for changing conditions and actions based on the wall's specific properties

8. saving changes and write it to a new IFC file:
   
   1. Finally, the changes made to the
      model are saved in a new IFC file at the specified path.
      
      

**Open a newIFC file:**

1. Now, use the chosen path to find the new IFC file.

2. Open the new IFC file

3. Check if the changes have been made.



The overarching purpose of the code is to find specific types of walls in an IFC model, alter their thermal transmittance values based on their reference description, and then save these changes in a new IFC file.
