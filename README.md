# ProjectDemoExplain
train_covid19.py is done by Adrian Rosebrock.

X-ray images dataset from Dr. Joseph Cohen GitHub : https://github.com/ieee8023/covid-chestxray-dataset

Read me:

1-	Put all the code files in the same directory.

2-	First, you need to train the model by executing the train_covid19.py script with “python train_covid19.py --dataset dataset”
(after you already downloaded tensorflow and keras on your computer)
    
3-	After you execute it successfully (it will take some time) a new covid19.model file should appear in the directory file

4-	Flash the ParticleCode file to your particle device

5-	Open the GUI-code.py file and Replace your-device-ID-goes-here with your actual device ID and replace your-access-token-goes-here with your actual access token, in line 52 and 57.

6-	Transfer the GUI_code.py and the covid19.model file to your Raspberry Pi device

7-	Connect to your Raspberry Pi remotely and then execute the GUI_code.py

P.S: If you are having problems downloading tensorflow and keras on your Raspberry Pi device, try follow my guide here: https://www.hackster.io/moe-hdaib/detecting-covid-19-from-x-ray-images-d4fd38


