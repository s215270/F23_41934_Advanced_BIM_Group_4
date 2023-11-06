# A3 Use Case: Indoor Climate Group

## A3 Reflect

In the previous tasks, we encountered some challenges related to data quality and completeness. We lacked data regarding which walls, doors, and windows were interior or exterior elements in the Skylab model. The data in the Skylab model contained errors, with some interior windows marked as exterior in the data, and vice versa, the same issue occurred with walls and doors. This made it very difficult to perform a heat loss calculation for the building. Additionally, there were no U-values provided for the building constructions in the Skylab model, which further complicated the heat loss calculation. Attempting to calculate U-values for elements like walls was not feasible due to the lack of layer information in the model. 

Consequently, we identified multiple data deficiencies in this model. Therefore, the objective of this task was to address these data gaps. We aimed to input the layer information for the walls and U-values for various building constructions. Furthermore, we wanted to correctly classify the building constructions as interior or exterior elements within the building. 

In a broader perspective, this optimization would not only enhance the accuracy of heat loss calculations but also facilitate various other analyses and optimizations related to the building. If this data were incorporated into the BIM model, it would simplify building optimization and enable additional analyses, such as thermal comfort, indoor climate, conceptual design, and more. 

## 3A Analyse use case

#### Goal

Our goal is to enable the most accurate calculation of heat loss for the Skylab model. Therefore, we wish to find data on U-values for the different materials in the BIM model, material layers, whether the constructions are interior or exterior. The purpose is to optimize the building's energy efficiency and minimize heat loss for the building by optimizing its constructions, thereby achieving better long-term results. This contributes to creating an optimal indoor climate. This approach involves a detailed analysis of the materials in the ceiling, walls, floors, windows, etc. 

This will also be beneficial from a company perspective as they can obtain the most optimal BIM model to present to their clients. They can demonstrate how energy-efficient the building is based on useful results that will be incorporated into the model. This initiative is crucial as it has a direct impact on people's health and well-being. By prioritizing a good indoor climate, we aim to improve residents' well-being. It's not just about energy savings but also about creating a comfortable and healthy environment where people can thrive. Therefore, it is of the utmost importance to focus on this area. 

#### Model uses

There are several different BIM uses applied in this case. You can see soome of them down below.  

###### Facility Management

Operation and Maintenance Planning: 

The BIM model can be used to develop a plan for the operation and maintenance of the building, including maintenance of HVAC systems, insulation, and windows to maintain thermal comfort and efficiency. 



Energy Management and Optimization: 

BIM can be used to monitor and optimize the building's energy consumption over time by collecting data on indoor climate, heating and cooling systems, and thermal properties. 



Renovation and Upgrades: 

The BIM model can be used to plan renovations and upgrades with a focus on thermal performance and indoor climate improvements. 



Identification of Thermal Bridges:

BIM can help identify potential thermal bridges in the building's construction that can lead to thermal inefficiency. 



###### Design and Planning

Concept and Design Phase: 

BIM can be used to integrate thermal performance analysis into the design process to optimize building construction and material selection. 



Climate Analysis: 

BIM can be used to conduct climate analyses to assess how the building will respond to different weather conditions and seasons. 



Material Selection and Specification: 

BIM can assist in selecting insulation materials and constructions suitable for thermal performance and indoor climate.

 

Zoning and Layout Optimization: 

BIM can be used to optimize the building's interior layout and thermal zoning to maximize thermal comfort and energy efficiency. 



Construction Phase: 

BIM can help monitor and ensure that the building's construction and materials are implemented in compliance with thermal and indoor climate standards. 



Energy Simulation and Analysis: 

The BIM model can be used to perform energy simulations to assess the building's energy efficiency and thermal performance, including the calculation of U-values for building constructions and materials. 



Thermal Comfort Analysis: 

BIM can be used to conduct thermal comfort analysis to assess whether indoor climate meets comfort standards, including the evaluation of heating and cooling zones within the building. 



Simulation of Heat Loss and Heat Gain: 

Using BIM, you can simulate heat loss and heat gain through the building's constructions and identify areas with potential thermal inefficiency. 



Assessment of Insulation Materials: 

The BIM model can be used to assess the impact of different insulation materials and construction layers on the building's insulation properties. 



Visualization of Thermal Zones: 

BIM can be used to create visual representations of thermal zones within the building to help identify areas with thermal challenges. 



3B: Propose a (design for a) tool / workflow 

The process of our use case has been modelled in a BPMN diagram 1. 

![BPMN-diagram 1](https://github.com/s215270/F23_41934_Advanced_BIM_Group_4/blob/main/A3_OpenBIM_Change/img/BPMN_diagram_1.svg)



The tool/workflow is designed to determine the heat loss of the building model. The IFC-file is imported from the building model "Skylabmodel." The model is analyzed with a focus on the external construction elements, where a lack of data is observed. Data on material layers for the constructions and their U-values is missing. The model cannot distinguish between which elements are external and internal. By scripting in Python, the missing data will be inserted, resulting in a new IFC-model that contains the necessary data to determine the heat loss of the building model. 



Below is BPMN diagram 2, which shows the process we have created in our Python script. Here, our sole focus is to add the U-value for specific external wall types to the BIM model's dataset.

![BPMN diagram 2](https://github.com/s215270/F23_41934_Advanced_BIM_Group_4/blob/main/A3_OpenBIM_Change/img/BPMN_diagram_2.svg)



## 3D: Value What is the potential improvement offered by this tool?

#### Business value

Energy and resource efficiency: 

By having data regarding the building's heat loss, businesses can optimize resource allocation. This enables the selection of the most suitable insulation materials and construction techniques to minimize heat loss and reduce energy costs. 



Budget planning:

With the provided value for heat loss, budgets for energy consumption and maintenance can be created. This allows for better financial planning and the reduction of unnecessary expenses. 



Competitive advantages:  

A company that possesses expertise in heat loss assessment can gain a competitive advantage by offering innovative and cost-effective solutions. This can attract more customers and strengthen their market position. 



#### Social value

Environmental benefits: 

Reducing heat loss in the building leads to lower energy consumption, which can minimize greenhouse gas emissions. This can contribute to sustainability efforts in meeting environmental regulatory requirements. 



Economic Sustainability: 

Lower energy costs lead to economic sustainability for both individual households and society as a whole. It frees up funds that can be invested elsewhere and supports economic development.
