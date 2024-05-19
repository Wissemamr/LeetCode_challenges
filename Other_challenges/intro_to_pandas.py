from typing import List
import pandas as pd


# Q1 : Create a dataframe from a list of lists
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    ids = [student[0] for student in student_data]
    ages = [student[1] for student in student_data]
    student_dict = {"student_id": ids, "age": ages}
    return pd.DataFrame(student_dict)


# Q2 : get the size of a df
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]


# Q3 : select first 3 rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]


# Q4 : select data from a df
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]


# Q5 : create a new column
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees


# Q6 : drop duplicates
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=["email"])
    return customers


# Q7 : drop missing data
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset=["name"])
    return students


# Q8 : modify columns
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees


# Q9 : rename columns
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        },
        inplace=True,
    )
    return students


#  Q10 : change data type
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students.grade.astype(int)
    return students


# Q11 : fill missing data
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.fillna({"quantity": 0}, inplace=True)
    return products


# Q12 : seshape data : concat
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)


# Q13 : reshape data : pivot
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month", columns="city", values="temperature")


#  Q14 : reshape data : melt
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=["product"], var_name="quarter", value_name="sales")


# Q15 : method chaining
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[
        ["name"]
    ]
