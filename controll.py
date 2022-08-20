#!/usr/bin/python
import numpy as np

def output(fl,fr,bl,br):
    print("Wheel num:")
    print(f"1: {fl:.1f}, 2: {fr:.1f}, 3: {bl:.1f}, 4: {br:.1f}")


def radio_emulator():
    """
    Skal emulere en fjernkontroll/RC reciver der:
    ch2: fremover/bakover       [-1000-1000]
    ch1: venstre/høyre          [-1000-1000]
    ch4: rotasjon venstre/høyre [-1000-1000]
    """
    ch2 = 0
    ch1 = 0
    ch4 = 0
    return ch2, ch1, ch4


def calculate_speed_dir(FR, LR, tol):
    """
    Regner ut farten og retningen til stikka basert på FR(channel 2) og LR(channel 1)
    tol er tolleransen om FR/LR skal bli tatt i betrakning om de er for små
    """
    # Om utslagene er mindre enn tol skal de gjøres til 0
    if abs(FR) < tol:
        FR = 0
    if abs(LR) < tol:
        LR = 0

    Radio_Speed = np.sqrt(LR*LR+FR*FR) # Regner farten/lengden fra senter
    Radio_Angle = np.arctan2(LR,FR) #Regner vinkelen stikka har i radianer

    return Radio_Speed, Radio_Angle


def calculate_output(desired_speed, desired_angle, turning_speed):
    """
    Regner ut motorhastighetene til de 4 motorene basert på desired_speed, desired_angle og turning_speed
    """
    ThetaD45 = desired_angle+np.pi/4
    V1 = desired_speed*np.sin(ThetaD45)+turning_speed
    V2 = desired_speed*np.cos(ThetaD45)-turning_speed
    V3 = desired_speed*np.cos(ThetaD45)+turning_speed
    V4 = desired_speed*np.sin(ThetaD45)-turning_speed
    return V1, V2, V3, V4


def main(tol):
    FR = 0 #Forwards/Backwards
    LR = 0 #Stear Left/Right
    CCW= 0 #Rotation
    FR, LR, CCW = radio_emulator()
    desired_speed, desired_angle = calculate_speed_dir(FR, LR, tol)
    turning_speed = CCW

    V1, V2, V3, V4 = calculate_output(desired_speed, desired_angle, turning_speed)
    output(V1,V2,V3,V4)


if __name__ == '__main__':
    main(10)
