# Certificate-Automation
Certificate Automation Project 🚀 Project Overview The Certificate Automation Project automates the creation of personalized certificates for events by processing data from Excel files. It generates certificates with participant details, saving time, eliminating manual effort, and ensuring high-quality output for easy distribution.

## 🛠 Features
+ __Excel Data Processing :__  Reads participant names from an Excel file (Names.xlsx).<br/>
+ __Certificate Template :__  Utilizes a pre-designed certificate template (certificate_template.png) to insert names.<br/>
+ __Customizable Font :__  Uses a customizable font for participant names.<br/>
+ __PDF Output :__  Saves generated certificates as PDF files.<br/>
+ __Efficient Automation :__  Eliminates manual effort, saving time and ensuring consistency.<br/>


## 📝 How It Works
+ __Excel Input :__ The script reads an Excel file (Names.xlsx) containing a list of participant names. The names are extracted to generate certificates.<br/>
+ __Template Customization :__ The certificate template (certificate_template.png) is loaded, and the name is dynamically inserted at a calculated position.<br/>
+ __Font Customization :__ The Arial font is used to print the names, with adjustable font size.<br/>
+ __Certificate Generation :__ Each name is placed on the template and saved as a PDF file in the specified output directory (certificates).<br/>


## 🛠 Requirements
+ Python 3.x<br/>
+ __Pandas:__ For handling Excel file input.<br/>
+ __Pillow:__ For image processing and text drawing on the certificate.<br/>
+ Font file (e.g., ARIAL.TTF): Ensure the correct path to your font.<br/>
<br/>
You can install the required dependencies using:<br/>
[ pip install pandas pillow ]
<br/>

## 📁 File Structure
+ certificate_template.png: The template image for the certificate.<br/>
+ Names.xlsx: The Excel file containing participant names.<br/>
+ generate_certificates.py: Python script that automates certificate generation.<br/>
+ /certificates: Directory where generated PDF certificates are saved.<br/>
<br/>

I Hope You Like It
