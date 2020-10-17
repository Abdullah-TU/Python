"""
Ohjelmointi 1 / Programming 1
Paracetamol
"""
def calculate_dose(weight, time,  total_doze_24):

    max_time=24
    time_left=max_time-time

    dose=15
    given_dose=dose*weight

    max_dose=4000
    haveto_give=max_dose-total_doze_24

    if time==6:
        dose_maxi=750
        print("The amount of Parasetamol to give to the patient: {}".format(dose_maxi))
    elif time>6 and time<=24:
        print("The amount of Parasetamol to give to the patient: {}".format(haveto_give))



def main():
    weight=int(input("Patient's weight (kg): "))
    time=int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24=int(input("The total dose for the last 24 hours (mg): "))

    calculate_dose(weight, time, total_doze_24)

if __name__ == "__main__":
    main()
