
---

### 🎨 Designer Tools – A Language for Graphic Designers  
**Automate image editing with a simple, non programmer-friendly language!**  

![Designer Tools](https://github.com/OmarNeira/ComputersScienceIIIOmarNeira/tree/main/FinalProyect/DesignerTools)  

---

## 📌 Overview  
**Designer Tools** is a domain-specific language built for graphic designers who need to process multiple images efficiently. This language allows non-programmers to automate image enhancements, apply filters, and perform transformations with ease.  

✅ **Easy to Use** – No programming knowledge required 
✅ **Built with Python** – Powered by Pillow & other libraries.  
✅ **Batch Processing** – Apply operations to multiple images at once.  

---

## 🔥 Why Designer Tools?  
Manually editing multiple images is time-consuming and tedious. Designer Tools simplifies the process:  

💡 **Enhance images effortlessly** – Adjust brightness, contrast, and colors.  
🎭 **Apply artistic filters** – Convert images to sepia, grayscale, negative, and more.  
🔄 **Transform images** – Flip, rotate, or blur with simple commands.  

---

## 🚀 How It Works  
Designer Tools uses a simple English-based syntax to define image operations.  

```txt
START
  START_OP
    TO_IMAGE (image.jpg)
    APPLY_FILTER sepia
  END_OP

  START_OP
    TO_FOLDER (example)
    APPLY_ENHANCE contrast 8
  END_OP

  START_OP
    TO_IMAGE (example/design.png)
    APPLY_TRANSFORM rotate 180
  END_OP
END
```
👆 This script:  
✔ Applies a **sepia filter** to `image.jpg`  
✔ Increases **contrast** of all images in `example/` folder  
✔ Rotates `design.png` **180 degrees**  

---

## 📜 Supported Features  
### 🎨 Filters  
- **Sepia**, **Negative**, **Grayscale**, **Blur**, **Contour**, **Detail**, **Emboss**, etc.  

### ✨ Enhancements  
- **Brightness**, **Contrast**, **Color Boost**, **Sharpness**  

### 🔄 Transformations  
- **Flip Horizontally**, **Flip Vertically**, **Rotate**  

Check out the documentation for more!  

---

## 🛠 Installation & Usage  
1️⃣ **Clone the repository**  
```sh
git clone https://github.com/OmarNeira/ComputersScienceIIIOmarNeira.git
cd FinalProyect/DesignerTools
```  
2️⃣ **Create a virtual environment**  
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```  
3️⃣ **Install dependencies**  
```sh
pip install -r requirements.txt
```  
4️⃣ **Run an example**  
```sh
python main.py
```  

---

## 📂 Project Structure  
📁 **DesignerTools/** – Main project folder  
┣ 📜 `main.py` – Connects the compiler to user input  
┣ 📜 `comp.py` – Compiler that translates commands into image operations  
┣ 📁 `input_analyzer/` – Handles syntax, lexical, and semantic analysis  
┣ 📁 `features/` – Implements image processing functions  
┣ 📜 `paths.py` – Manages file paths  

---

## 🎯 Conclusion  
✅ Designer Tools **simplifies image editing** by allowing designers to **write simple scripts** instead of performing repetitive manual edits.  
✅ **Extendable & Customizable** – Developers can easily add new features!  

---

💻 **Developed by:** Omar Armando Neira Ordoñez  
📩 **Contact:** oaneirao@udistrital.edu.co  

---