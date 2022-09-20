import pandas as pd

def calculate_demographic_data(print_data=False):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    print(race_count)

    # What is the average age of men?
    age = df[['age']][df.sex == 'Male']
    average_age_men = round(age.mean(), 1)[0]

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[['education']][df.education == 'Bachelors'].count() / df['education'].count()) * 100, 1)[0]

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate')]
    lower_education = df[(df.education != 'Bachelors') & (df.education != 'Masters') & (df.education != 'Doctorate')]
    
    # percentage with salary >50K
    higher_education_rich = round((higher_education[['education']][higher_education.salary == '>50K'].count() / higher_education['education'].count()) * 100, 1)[0]    
    lower_education_rich = round((lower_education[['education']][lower_education.salary == '>50K'].count() / lower_education['education'].count()) * 100, 1)[0]
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[['hours-per-week', 'salary']][df['hours-per-week'] == 1]
    rich_percentage = round(num_min_workers[['hours-per-week']][num_min_workers.salary == '>50K'].count() / num_min_workers.count()[0] * 100, 1)[0]

    # What country has the highest percentage of people that earn >50K?
    highest_earning_by_country = df['native-country'][df.salary == '>50K'].value_counts()
    highest_earning_by_country.name = 'high_earning'

    all_countries = df['native-country'].value_counts()
    all_countries.name = 'all'
    
    earnings_by_country = pd.concat([all_countries, highest_earning_by_country], axis=1, join='inner')
    earnings_by_country['percentage_high_earners'] = round((earnings_by_country['high_earning'] / earnings_by_country['all'] * 100), 1)
    earnings_by_country_sorted = earnings_by_country.nlargest(1, 'percentage_high_earners')

    highest_earning_country = earnings_by_country_sorted.index[0]

    highest_earning_country_percentage = earnings_by_country.percentage_high_earners.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_earners = df['occupation'][(df['native-country'] == 'India') & (df['salary'] == '>50K')].value_counts().nlargest(1)

    top_IN_occupation = india_high_earners.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()