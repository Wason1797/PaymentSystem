import datetime

schedule1 = "00:01-09:00"
schedule2 = "09:01-18:00"
schedule3 = "18:01-23:59"
weekend_bonus = 5

payment_dict = {
    schedule1: 25,
    schedule2: 15,
    schedule3: 20
}

with open('employee_data.txt') as f:
    data = f.readlines()
data = [x.strip() for x in data]


def split_time_string(time_string):
    time_string = time_string.split("-")
    return (datetime.datetime.strptime(time_string[0], '%H:%M').time(),
            datetime.datetime.strptime(time_string[1], '%H:%M').time())


def calculate_hour_worked_price(time_string):

    time_string = split_time_string(time_string)
    schedule_range1 = split_time_string(schedule1)
    schedule_range2 = split_time_string(schedule2)
    schedule_range3 = split_time_string(schedule3)
    init_time = time_string[0]
    end_time = time_string[1]
    hours_worked = end_time.hour - init_time.hour
    hour_price = 0

    if init_time >= schedule_range1[0] and end_time <= schedule_range1[1]:
        hour_price = float(payment_dict[schedule1])
    elif init_time >= schedule_range2[0] and end_time <= schedule_range2[1]:
        hour_price = float(payment_dict[schedule2])
    elif init_time >= schedule_range3[0] and end_time <= schedule_range3[1]:
        hour_price = float(payment_dict[schedule3])
    return (hour_price, hours_worked)


def calculate_salary():
    for employee in data:
        separated_data = employee.split("=")
        employee_name = separated_data[0]
        employe_payment_arr = separated_data[1].split(",")
        employee_salary = 0
        for payment in employe_payment_arr:
            payment_schedule = payment[2::]
            hours_worked_price = calculate_hour_worked_price(payment_schedule)
            if payment_schedule in ["MO", "TU", "WE", "TH", "FR"]:
                employee_salary += hours_worked_price[0]*hours_worked_price[1]
            else:
                employee_salary += (hours_worked_price[0] +
                                    weekend_bonus)*hours_worked_price[1]

        print("The amount to pay {0} is: {1} USD".format(
            employee_name, employee_salary))


if __name__ == '__main__':
    calculate_salary()
