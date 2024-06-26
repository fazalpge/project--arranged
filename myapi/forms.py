from django import forms

class attritionForm(forms.Form):
    Age= forms.IntegerField()
    BusinessTravel= forms.ChoiceField(choices=[("Travel_Rarely", "Travel_Rarely"),("Travel_Frequently", "Travel_Frequently"),("Non-Travel", "Non-Travel")])
    DailyRate= forms.IntegerField()
    Department= forms.ChoiceField(choices=[("Sales", "Sales"),("Research_&_Development", "Research_&_Development"),("Human_Resources","Human_Resources")])
    DistanceFromHome= forms.IntegerField()
    #Education= forms.ChoiceField(choices=[("Below_College", "Below_College"),("College", "College"),("Bachelor", "Bachelor"),("Master","Master"),("Docter","Docter")])
    Education= forms.IntegerField()
    EducationField= forms.ChoiceField(choices=[("Life_Sciences", "Life_Sciences"),("Medical", "Medical"),("other", "other"),("Marketing", "Marketing"),("Technical_Degree", "Technical_Degree"),("Human_Resources", "Human_Resources")])
    EmployeeNumber=forms.IntegerField()
    #EnvironmentSatisfaction=forms.ChoiceField(choices=[("Low", "Low"),("Medium", "Medium"),("High", "High"),("Very_High","Very_High")])
    EnvironmentSatisfaction=forms.IntegerField()
    Gender= forms.ChoiceField(choices=[("Male", "Male"),("Female", "Female")])
    HourlyRate= forms.IntegerField()
    #JobInvolvement= forms.ChoiceField(choices=[("Low", "Low"),("Medium", "Medium"),("High", "High"),("Very_High","Very_High")])
    JobInvolvement= forms.IntegerField()
    JobLevel=forms.IntegerField()
    #IntegerField()
    JobRole= forms.ChoiceField(choices=[("Sales_Executive", "Sales_Executive"),("Research_Scientist","Research_Scientist"),("Laboratory_Technician", "Laboratory_Technician"),("Manufacturing_Director","Manufacturing_Director"),("Research_Director","Research_Director"),("Healthcare_Representative","Healthcare_Representative"),("manager", "Manager"),("Sales_Representative", "Sales_Representative")])
    #JobSatisfaction=forms.ChoiceField(choices=[("Low", "Low"),("Medium", "Medium"),("High", "High"),("Very_High","Very_High")])
    JobSatisfaction=forms.IntegerField()
    MaritalStatus= forms.ChoiceField(choices=[("Married", "Married"),("single", "Single"),("Divorced", "Divorced")])
    MonthlyIncome= forms.IntegerField()
    MonthlyRate= forms.IntegerField()
    NumCompaniesWorked= forms.IntegerField()
    OverTime= forms.ChoiceField(choices=[("YES", "YES"),("NO", "NO")])
    PercentSalaryHike= forms.IntegerField()
    #PerformanceRating= forms.ChoiceField(choices=[ ("Low", "Low"),("Good", "Good"),("Excellent", "Excellent"),("Outstanding","Outstanding")])
    PerformanceRating= forms.IntegerField()
    #RelationshipSatisfaction=forms.ChoiceField(choices=[("Low", "Low"),("Medium", "Medium"),("High", "High"),("Very_High","Very_High")])
    RelationshipSatisfaction= forms.IntegerField()
    StockOptionLevel= forms.IntegerField()
    TotalWorkingYears= forms.IntegerField()
    TrainingTimesLastYear= forms.IntegerField()
    #WorkLifeBalance= forms.ChoiceField(choices=[("Excellent", "Excellent"),("Good", "Good"),("Average", "Average"),("Poor", "Poor")])
    WorkLifeBalance= forms.IntegerField()
    YearsAtCompany= forms.IntegerField()
    YearsInCurrentRole= forms.IntegerField()
    YearsSinceLastPromotion= forms.IntegerField()
    YearsWithCurrManager= forms.IntegerField()
    
    
