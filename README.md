
# Iris Flower Species Predictor (Naive Bayes + Flask)

This is a simple Flask web application that uses a **Naive Bayes classifier** to predict the species of an Iris flower based on **only two inputs**: Petal Length and Petal Width.

---

## 🧠 Overview

The app is built using:
- **Python**
- **Flask** (for the backend)
- **HTML/CSS** (for a simple UI)
- **scikit-learn** (for machine learning)

The model was trained on the classic **Iris dataset** using only the most informative features: `PetalLength` and `PetalWidth`.

---

## 📁 Project Structure

```
iris-naivebayes-app/
│
├── model.py              
├── iris.data             
├── model.pkl              
├── label_encoder.pkl      
├── app.py                 
├── templates/
│   └── index.html        
├── static/
│   └── style.css          
└── README.md              
```

---

## 🚀 How It Works

1. User inputs:
   - Petal Length (cm)
   - Petal Width (cm)

2. The Flask backend sends these to the pre-trained model (`model.pkl`)
3. The model predicts one of:
   - `Iris-setosa`
   - `Iris-versicolor`
   - `Iris-virginica`

4. Result is shown on the webpage.

---

## 🔧 Installation

### 1. Install Dependencies
```bash
pip install flask scikit-learn pandas numpy
```

### 2. Train the Model (if not already)
```bash
python model.py
```

### 3. Run the Flask App
```bash
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## Sample UI

**Input**:

- Petal Length: 5
- Petal Width: 6
 <img width="720" height="536" alt="image" src="https://github.com/user-attachments/assets/9123e493-895f-48f5-9bfc-aa4cc8f876f0" />

**Output**:

<img width="720" height="536" alt="image" src="https://github.com/user-attachments/assets/495e27cb-b1e9-4edd-ae94-508d08937814" />

```
Predicted Species: Iris-virginica
```
---

## 🙋‍♂️ Author

**Hari Prasath S**  
[GitHub Profile](https://github.com/hariprasath2105)

---

## 📘 License

This project is open source and free to use.
