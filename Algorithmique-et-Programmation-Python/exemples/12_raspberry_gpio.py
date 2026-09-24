"""MATÉRIEL REQUIS : Raspberry Pi ; contact entre BCM17 et GND, entrée seulement."""

from gpiozero import Button

with Button(17, pull_up=True) as contact:
    print("Contact fermé :", contact.is_pressed)
