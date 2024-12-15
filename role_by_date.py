import datetime


class Role:
    def __init__(self, title, date):
        self.title = title
        self.date = date


def get_role_by_date(history, dates):
    role_by_date = dict()

    history.sort(key=lambda emp_role: emp_role.date)

    for target_date in dates:
        for i, start_role in enumerate(history):
            if i == 0 and target_date < start_role.date:
                role_by_date[target_date] = "No role"
                break
            elif i < len(history) - 1:
                next_role = history[i + 1]
                if start_role.date <= target_date < next_role.date:
                    role_by_date[target_date] = start_role.title
                    break
            else:
                role_by_date[target_date] = start_role.title

    return role_by_date


if __name__ == "__main__":
    emp_roles_history = [
        Role("Team Leader", datetime.date(2020, 8, 1)),
        Role("Fullstack developer", datetime.date(2016, 5, 15)),
        Role("Frontend developer", datetime.date(2015, 11, 17))
    ]

    roles_dates = [
        datetime.date(2021, 1, 1),
        datetime.date(2014, 1, 1),
        datetime.date(2015, 12, 1),
        datetime.date(2016, 6, 1)
    ]

    print(get_role_by_date(emp_roles_history, roles_dates))
