import datetime


def read_file(path):
    with open(path) as f:
        data = f.readlines()
        return [x.strip() for x in data]


def split_time_string(time_string):
    time_string = time_string.split("-")
    return (datetime.datetime.strptime(time_string[0], '%H:%M').time(),
            datetime.datetime.strptime(time_string[1], '%H:%M').time())


def calculate_hour_worked_price(time_string, schedule_arr, payment_dict):
    time_string = split_time_string(time_string)

    schedule_range_arr = [split_time_string(x) for x in schedule_arr]
    init_time = time_string[0]
    end_time = time_string[1]
    hours_worked = end_time.hour - init_time.hour
    hour_price = 0

    for i in range(len(schedule_range_arr)):
        if init_time >= schedule_range_arr[i][0] and end_time <= schedule_range_arr[i][1]:
            hour_price = float(payment_dict[schedule_arr[i]])
            break

    return (hour_price, hours_worked)


def calculate_salary(employee_data_path, schedule_arr, payment_dict, weekend_bonus):
    data = read_file(employee_data_path)
    for employee in data:
        separated_data = employee.split("=")
        employee_name = separated_data[0]
        employe_payment_arr = separated_data[1].split(",")
        employee_salary = 0
        for payment in employe_payment_arr:
            payment_schedule = payment[2::]
            hours_worked_price = calculate_hour_worked_price(payment_schedule,
                                                             schedule_arr, payment_dict)
            if payment[0:2] in ["MO", "TU", "WE", "TH", "FR"]:
                employee_salary += hours_worked_price[0]*hours_worked_price[1]
            else:
                employee_salary += (hours_worked_price[0] +
                                    weekend_bonus)*hours_worked_price[1]

        print("The amount to pay {0} is: {1} USD".format(
            employee_name, employee_salary))


def create_payment_dict(schedule_arr, payment_arr):
    return dict(zip(schedule_arr, payment_arr))


if __name__ == '__main__':

    schedule_arr = [
        "00:01-09:00",
        "09:01-18:00",
        "18:01-23:59"
    ]
    payment_arr = [
        25,
        15,
        20
    ]
    weekend_bonus = 5
    file_path = 'employee_data.txt'
    payment_dict = create_payment_dict(
        schedule_arr, payment_arr)
    calculate_salary(file_path, schedule_arr, payment_dict, weekend_bonus)
