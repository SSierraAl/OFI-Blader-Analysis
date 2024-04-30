# OFI-Weight-Analysis
This repository contains the code needed to run the Load cell sensor both in python and in arduino in the OFI color project. Read all about the OFI Color project here: https://github.com/SSierraAl/OFI_Color_Project/blob/main/README.md

## Project objectives
1. To measure the weight in real time thus removing the need for the weighing scale.
2. To measure the rate of change in weight in real time.
3. To display the values in a real time plot in the UI.

## How the folder is divided
1. **Global Gui**
   Main folder, contains all the codes required to run the program
   
   1.1 **Gui**
      Folder that supports the main interface, to run the ui.
   
   1.2 **PLot.py**
      Main file running the weight analysis, the rate of change of the weight and the graph plot and display.
   
   1.3 **Thread Weight.py**
      Python file for aquisition of data from the arduino board.
   
   1.4 **load cell.ino**
      Arduino Code for calibration of the Load cell sensor and HX711 load cell amplifier.
   
   1.5 **requirements.txt**
      All libraries needed to run the program. Install using pip install
   
3. **.gitignore**: file with files to ignore for the github
  
4. **Commands.txt** : important commands to build the new interface changes (Only qt design changes)

5. **STL**: files used in the design of the hanging holding structure of the load cell.

## Components used 
1. **Load Cell CZL635 - 5KG**
   
    ![load cell](https://github.com/EsthWa/OFI-Weight-Analysis/assets/157009718/f4239e49-81e3-45c1-aeab-9920d008796b)
   
2. **LOAD CELL AMPLIFIER**
   
    ![image](https://github.com/EsthWa/OFI-Weight-Analysis/assets/157009718/52b404cd-f277-45fd-b11c-0322ca83c188)

3. **ARDUINO UNO BOARD**

   ![image](https://github.com/EsthWa/OFI-Weight-Analysis/assets/157009718/ffd5e2e0-1eb3-4799-a44d-50a0506169bd)

4. **Python and Github**

   Have python and Github installed in your computer.
   
## Working procedure
1. **From the load cell sensor to the HX711 amplifier**
   
   The connection is as folows:
   
   Red to VCC pin
   
   Black to Ground pin
   
   White to Amplifier-(A-)
   
   Green to Amplifier+(A+)
   
2. **From the HX711 amplifier to the Arduino UnoR3**
   
   The connection is as follows:
   
   VCC to 5V VCC pin
   
   GND to GND
   
   DAT pin to D3
   
   CLK pin to D2
   
   Include the HX711 arduino library by Bogdan Necula.

   When a force is applied to the load cell the strain gauges deform slightly which changes their electrical resistance.

   That tiny electrical signal from the load cell isn't strong enough that is why we use the load cell amplifier. It amplifies the weak signal from the load cell making it easier to use    and read by data acquisition.

   Data is acquired by the python file which is then analysed and plotted. 

   Threading is important to prevent the GUI from crashing during its operation. Threads allow multiple programs to run simultaneously hence the use of thread weight to capture the         arduino data while plotting and saving is running in the GUI. 

3. **The App**
   
   Launch the app and you will see the home page
   
   Click on the search icon.
   
   ![load cell 1](https://github.com/EsthWa/OFI-Weight-Analysis/assets/157009718/a78222d9-7ba7-45df-88dc-2f296e3ce7b4)

   Next select the channel 'COM' port connected to the arduino uno R3 and click confirm.
   
   ![load cell 2](https://github.com/EsthWa/OFI-Weight-Analysis/assets/157009718/cef61120-0935-4afb-a3f3-b343cc9b1915)

   Then select the file format .csv or .mat, enter file diretory followed by a forward slash\ and file name.
   
   Press Start.

   ![load cell 4](https://github.com/EsthWa/OFI-Weight-Analysis/assets/157009718/b29d9fef-6ade-43ab-9c88-6676f6f786d2)

   Press reset to zero to tare the scale.
   
   Press stop to stop the program and save the acquired data.
   
4. **Data saved**
   
   According to the format chosen, the format can either be in .mat or .csv , the first column represents the weight  and the second column represents rate of change.
   
