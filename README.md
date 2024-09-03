# knights_algorithm

This python script finds all 10-key sequences that can be keyed into the keypad
in the following manner: <br>

●	The initial keypress can be any of the keys. <br>
●	Each subsequent keypress must be a knight move from the previous keypress. <br>
●	There can be at most 2 vowels in the sequence. <br>

A knight move is made in one of the following ways:
1.	Move two steps horizontally and one step vertically
2.	Move two steps vertically and one step horizontally

The keypad provided is: <br>
<img width="385" alt="image" src="https://github.com/user-attachments/assets/47da3383-d09e-48be-894c-765dc0e15e7d">

Examples of a valid knight move: <br>
<img width="310" alt="image" src="https://github.com/user-attachments/assets/608aabd0-a4e0-4f09-b55c-c14cdf965c3d">

# Pre-requisites

1. Have Windows 10 installed on your PC
2. Have python installed on you system

# How to trigger the code and get output

1. Extract the package knights_algorithm.zip
2. Navigate into the folder knights_algorithm. Confirm presence of these 4 folders with the exact names: data, environments, model, result.
3. Holding down the Shift key and right-clicking inside the folder will open a drop down menu with several options. Choose "Open PowerShell window here" and if not available then choose "Open Command window here". On the left of the ">" synbol, you can see the location of the folder knights_algorithm on your PC.
4. Type "pip install conda". This step will download and install packages which might take a few minutes. For issues consult https://pypi.org/project/conda/ or check the troubleshooting section underneath.
5. Once it is finished, type "cd environments" which will take you into the environments folder where you can see the contents within the folder by typing "ls -ll". Check if the output displayed mentions the file knights_algorithm.yaml as shown here: ![image](https://github.com/user-attachments/assets/29f2e128-6c31-4266-8463-33d195723b3c)
6. Type the code "conda env create -f knights_algorithm.yml" to install all the necessary packages into your python environment. This will take several minutes and is finished when you see the folder path to your current directory.
7. Once it is finished, type "conda activate knights_algorithm".
8. Then type "cd ../model" to navigate from the environments folder back into the models folder as mentioned in step 2 and 3 on your terminal.
9. Type the code "python knight_algo_final.py" and you should see the output like shown here: ![image](https://github.com/user-attachments/assets/461aeea7-497f-48c2-8f3e-b7403c60b067)

## Troubleshooting

1. In case of file missing error, check and confirm that the necessary file exists in the data, environments, models or results folder. This can also be compared  with a fresh download of the zipped folder
2. In case of other errors, please contact dineshswamybvp@gmail.com
