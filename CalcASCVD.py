import math


def calc_lifetime_ascvd(gender, total_chol, blood_presure, hypertension, diabetes, smoking):
    try:
        gender = gender.upper()
        if (gender not in ('M', 'F')) and (blood_presure not in (90, 200)) and (hypertension not in (0, 1)) \
                and (diabetes not in (0, 1)) and (smoking not in (0, 1)):
            print("Please Check the inputs")
    except Exception as exp:
        print("Inputs are not in correct format!!!")
        print(exp.message)
        return

    sum_of_major = (1 if total_chol >= 240 else 0) + (1 if blood_presure >= 160 else 0) + \
                   (hypertension + smoking + diabetes)

    all_optimal = (1 if blood_presure < 120 else 0) * (1 if hypertension == 0 else 0) * \
                  (1 if total_chol < 180 else 0) * (1 if sum_of_major == 0 else 0)

    elevated = (((1 if total_chol >= 200 else 0) * (1 if total_chol < 240 else 0)) * \
                (1 if hypertension == 0 else 0)) * (1 if sum_of_major == 0 else 0)

    not_optimal = (1 if blood_presure >= 120 else 0) * (1 if blood_presure < 140 else 0) * \
                 (1 if hypertension == 0 else 0) + (1 if total_chol >= 180 else 0) * \
                                                   (1 if total_chol < 200 else 0) * \
                                                   (1 if blood_presure >= 140 else 0) * \
                                                   (1 if blood_presure < 160 else 0) * \
                                                   (1 if hypertension == 0 else 0) + \
                 (1 if total_chol >= 200 else 0) * (1 if total_chol < 240 else 0) * (1 if sum_of_major == 0 else 0)

    if gender == 'M':
        lifetime_ascvd = (1 if sum_of_major == 2 else 0) * 69 + (1 if sum_of_major == 1 else 0) * 50 + elevated * 46 + \
            not_optimal * 36 + all_optimal * 5
    else:
        lifetime_ascvd = (1 if sum_of_major == 2 else 0) * 50 + (1 if sum_of_major == 1 else 0) * 39 + elevated * 39 + \
                         not_optimal * 27 + all_optimal * 8

    print "Your Lifetime ASCVD is : ", lifetime_ascvd


"""
this ln function is made by Adrian Statescu ('https://gist.github.com/thinkphp/1529713')
    special thanks to his kindness and help to spread useful health related applications
"""
def loge(n, li, ls):
    if math.fabs(li - ls) <= 0.000001:
        return (li + ls) / 2.0
    if (math.exp(li) - n) * (math.exp((li + ls) / 2.0) - n) < 0:
        return loge(n, li, (li + ls) / 2.0)
    else:
        return loge(n, (li + ls) / 2.0, ls)


def ln(n):
    if n == 0 or n < 0:
        return "Math Domain Error"
    if n == 1:
        return 0
    if n > 0 and n < 1:
        return loge(n, 0, -n - 80)
    else:
        return loge(n, 0, n)

"""
END OF Adrian Statescu CODE
"""


def calc_10_years_ascvd(gender, age, total_chol, hdl, blood_presure, hypertension, diabetes, smoking):
    try:
        gender = gender.upper()
        if (gender not in ('M', 'F')) and (age not in (40, 79)) and (hdl not in (20, 100)) \
                and (blood_presure not in (90, 200)) and (hypertension not in (0, 1)) and (diabetes not in (0, 1)) and (
            smoking not in (0, 1)):
            print("Please Check the inputs")
    except Exception:
        print("Inputs are not in correct format!!!")
        return

    if gender == 'M':
        risk = 12.344 * ln(age) + 11.853 * ln(total_chol) + (-2.664 * ln(age) * ln(total_chol)) + (-7.99 * ln(hdl)) + \
            1.769 * ln(age) * ln(hdl) + 1.797 * ln(blood_presure) * (0 if hypertension == 0 else 1) + 1.764 * \
            ln(blood_presure) * (1 if hypertension == 0 else 0) + 7.837 * smoking + (-1.795 * ln(age) * smoking) + \
               0.658 * diabetes
        risk = (1 - (pow(0.91436,math.exp(risk-61.1816)))) * 100
    else:

        risk = (-29.799 * ln(age)) + 4.884 * ln(age) * ln(age) + 13.54 * ln(total_chol) + (-3.114 * ln(age) \
            * ln(total_chol)) + (-13.578 * ln(hdl)) + 3.149 * ln(age) * ln(hdl) + 2.019 * ln(blood_presure) * \
            hypertension + 1.957 * ln(blood_presure) * (1 if hypertension == 0 else 0) + 7.574 * smoking + \
               (-1.665 * ln(age) * smoking) + 0.661 * diabetes
        risk = (1 - (pow(0.96652, math.exp(risk+29.1817)))) * 100
    if risk:
        print "Your 10 years ahead ASCVD is : ", risk

if __name__ == "__main__":
    print("""
        Calculation of Atherosclerotic Cardiovascular disease
        you can check the results with reference sites like
        these listed below:
            -   http://tools.acc.org/ASCVD-Risk-Estimator/
            -   http://www.cvriskcalculator.com/
        main article: http://circ.ahajournals.org/content/early/2013/11/11/01.cir.0000437741.48606.98

        PLEASE PAY ATTENTION:
        THIS VERSION IS MADE FOR MIDDLE EAST PEOPLE AND IS NOT CORRECT FOR OTHER RACES

    """)
    calc_lifetime_ascvd('F', 130, 120, 0, 0, 0)
    calc_10_years_ascvd('F', 45, 170, 55, 130, 1, 0, 0)
