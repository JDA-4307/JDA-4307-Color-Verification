# Color Verification & Validation Project

This project, "Color Verification & Validation," is designed to assist QA operators and field engineers in identifying wood veneer colors with high accuracy. It currently identifies **Medium Cherry** and **Graphite Walnut**, with plans to expand functionality for color validation in future releases.

---

## Instructions

### Prerequisites:
- **Python Version:** Python 3.8 or higher
- **Required Libraries:** Install the dependencies using the following command:
	pip install -r requirements.txt


### Steps:
1. **[Download the model](https://drive.google.com/file/d/1L-xwOJkQyGt5-RdzT-VCRaANdbaJTYc1/view?usp=sharing)**
2. Move the `color_detection_model.zip` file into the `color_verification_demo` folder.
3. Open a terminal:
 - **Mac:** Use the built-in **Terminal** app.
 - **Windows:** Use **Command Prompt** or **PowerShell**.
4. Run the `app.py` script by typing:
	python app.py


5. Open `index.html` in your web browser to view the demo interface.

---

## Artifact Demonstration

[![Watch the video](https://img.youtube.com/vi/FBtAFtMBl1I/hqdefault.jpg)](https://youtu.be/FBtAFtMBl1I?feature=shared&t=85)

Click the image above to watch the demonstration starting at the specified time.

---

## Rationale for Feature Selection

The color identification feature was chosen as the first implemented functionality due to its critical role in the overall project. Identifying a veneer’s color is the foundation upon which the color validation feature will be built. This feature allows us to test our chosen tech stack, including Python for machine learning and Flask for web app integration, and evaluate its strengths and weaknesses.

---

## Release Notes

### Version 0.0.0

#### **Features**
- Identifies wood veneer colors as either **Medium Cherry** or **Graphite Walnut**.
- Enables users to upload images via a simple web interface for color identification.

#### **Bug Fixes**
- No fixes in this release, as this is the first iteration.

#### **Known Issues**
- **Desert Oak images** are incorrectly formatted due to inconsistencies in the dataset preprocessing pipeline. A future update will address this by implementing preprocessing steps.
- The current model supports only two color classes; additional classes will be implemented in future iterations.

---

## Technical Assessment

### Strengths:
- **Python**: Its libraries, such as TensorFlow, provided robust tools for developing and training the model efficiently.
- **Flask**: Enabled rapid development of a lightweight web interface for the demo.
- **GitHub**: Streamlined code collaboration and dataset management among team members.

### Weaknesses:
- Flask’s scalability is limited; transitioning to a more robust framework may be necessary for production deployment.
- Dataset preprocessing requires enhancements to handle inconsistencies in image formats and metadata.

---

## Future Work

1. **Expand Color Classes:** Add support for additional wood veneer colors, as requested by Steelcase.
2. **Develop Color Validation Feature:** Build a model to determine if the identified color falls within acceptable thresholds.
3. **Enhance App UI/UX:** Create a user-friendly and intuitive interface optimized for operators and field engineers.
4. **Improve Dataset Processing:** Address current issues with formatting and standardize dataset preparation workflows.
5. **Integration and Testing:** Deploy the app on a scalable cloud platform and conduct thorough testing to ensure reliability.

---

## Contributors

- **Rishi**: Research, backend organization  
- **Zuhair**: AI model development  
- **Chen**: UI design and front-end tasks  
- **Ethan**: UI design and mobile app development  
- **Benson**: Research and meeting documentation 

