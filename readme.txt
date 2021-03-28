Assuming you have a windows system:

1) Donwload anaconda with python 3.8 from https://www.anaconda.com/products/individual.
Anaconda will install the latest version of spyder and jupyter notebook.
2) Next open spyder separately to see its working. Use a simple print('Hello World') command to see if its working.
3) Open anaconda prompt (search using search bar) in windows
4) Install all the required packages using the pip installer (anaconda comes with pip installer so no issues)
5) use pip install $package_name$ to install all the required modules:
pip install pandas
pip install numpy
pip install opencv-python
pip install os-sys
pip install Pillow==2.2.2
pip install jsonlib
pip install apyio
pip install matplotlib
pip install seaborn
pip install requests
pip install python-docx

* Some of these modules might already be preinstalled - None the less run all these commands to make sure you have everything you need.

6) Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki. Install for all users 
Note the default tesseract installation path:
Default installation path will most likely be : 'C:\Program Files\Tesseract-OCR\tesseract.exe' or 'C:\Users\USER\AppData\Local\Tesseract-OCR' 
It may change so please check the installation path.
7) pip install pytesseract in anaconda prompt
8) Close and reopen spyder
9) In ocr.py - in 7th line: if the path of your tesseract.exe is different then change it. 
I have set the path as 'C:\Program Files\Tesseract-OCR\tesseract.exe' since that's the installation path for my
It should
10) In spyder, set your working directory as the 'Optical Recognition' folder
11) Run the code, if it says that a particular module is not installed, then go to anaconda prompt and install that module and restart spyder
12) Note that everytime you start spyder, you need to set your working directory.
13) The result will be written to a file called "result.txt" 
14) Kindly check the result for "image4" and "trialimg".
15) You can do so by replacing the file name in the code.

