import tkinter as tk
from tkinter import ttk

# Periodic Table data for a few elements
elements = {
     "H": {"name": "Hydrogen", "atomic_number": 1, "symbol": "H", "atomic_mass": 1.008, "category": "Non-metal", "description": "Hydrogen is the lightest and most abundant chemical element in the universe."},
    "He": {"name": "Helium", "atomic_number": 2, "symbol": "He", "atomic_mass": 4.0026, "category": "Noble Gas", "description": "Helium is a colorless, odorless, tasteless, inert, monatomic gas that heads the noble gases group."},
    "Li": {"name": "Lithium", "atomic_number": 3, "symbol": "Li", "atomic_mass": 6.94, "category": "Alkali Metal", "description": "Lithium is a soft, silvery-white alkali metal that is highly reactive and flammable."},
    "Be": {"name": "Beryllium", "atomic_number": 4, "symbol": "Be", "atomic_mass": 9.0122, "category": "Alkaline Earth Metal", "description": "Beryllium is a strong, lightweight, and brittle metal that is highly toxic."},
    "B": {"name": "Boron", "atomic_number": 5, "symbol": "B", "atomic_mass": 10.81, "category": "Metalloid", "description": "Boron is a metalloid element that is used in glass and ceramics."},
    "C": {"name": "Carbon", "atomic_number": 6, "symbol": "C", "atomic_mass": 12.011, "category": "Non-metal", "description": "Carbon is a non-metal element that forms the basis of all life on Earth."},
    "N": {"name": "Nitrogen", "atomic_number": 7, "symbol": "N", "atomic_mass": 14.007, "category": "Non-metal", "description": "Nitrogen is a colorless, odorless gas that makes up 78% of Earth's atmosphere."},
    "O": {"name": "Oxygen", "atomic_number": 8, "symbol": "O", "atomic_mass": 15.999, "category": "Non-metal", "description": "Oxygen is essential for respiration in many organisms and combustion processes."},
    "F": {"name": "Fluorine", "atomic_number": 9, "symbol": "F", "atomic_mass": 18.998, "category": "Halogen", "description": "Fluorine is a highly reactive, pale yellow gas that is toxic."},
    "Ne": {"name": "Neon", "atomic_number": 10, "symbol": "Ne", "atomic_mass": 20.180, "category": "Noble Gas", "description": "Neon is a colorless, odorless gas that emits a distinct reddish-orange glow when electrified."},
    "Na": {"name": "Sodium", "atomic_number": 11, "symbol": "Na", "atomic_mass": 22.990, "category": "Alkali Metal", "description": "Sodium is a soft, silvery-white metal that is highly reactive with water."},
    "Mg": {"name": "Magnesium", "atomic_number": 12, "symbol": "Mg", "atomic_mass": 24.305, "category": "Alkaline Earth Metal", "description": "Magnesium is a light, silvery-white metal that is essential for life."},
    "Al": {"name": "Aluminum", "atomic_number": 13, "symbol": "Al", "atomic_mass": 26.982, "category": "Post-transition Metal", "description": "Aluminum is a lightweight, silvery-white metal used in a variety of industries."},
    "Si": {"name": "Silicon", "atomic_number": 14, "symbol": "Si", "atomic_mass": 28.085, "category": "Metalloid", "description": "Silicon is a metalloid element that is essential for electronic devices and solar panels."},
    "P": {"name": "Phosphorus", "atomic_number": 15, "symbol": "P", "atomic_mass": 30.974, "category": "Non-metal", "description": "Phosphorus is a highly reactive non-metal used in fertilizers."},
    "S": {"name": "Sulfur", "atomic_number": 16, "symbol": "S", "atomic_mass": 32.06, "category": "Non-metal", "description": "Sulfur is a yellow, non-metal element that is essential for life and is used in industrial processes."},
    "Cl": {"name": "Chlorine", "atomic_number": 17, "symbol": "Cl", "atomic_mass": 35.45, "category": "Halogen", "description": "Chlorine is a greenish-yellow gas used in disinfectants and bleaching agents."},
    "Ar": {"name": "Argon", "atomic_number": 18, "symbol": "Ar", "atomic_mass": 39.948, "category": "Noble Gas", "description": "Argon is a colorless, odorless, inert gas used in welding and in incandescent light bulbs."},
    "K": {"name": "Potassium", "atomic_number": 19, "symbol": "K", "atomic_mass": 39.098, "category": "Alkali Metal", "description": "Potassium is a soft, silvery-white alkali metal that is essential for living organisms."},
    "Ca": {"name": "Calcium", "atomic_number": 20, "symbol": "Ca", "atomic_mass": 40.078, "category": "Alkaline Earth Metal", "description": "Calcium is a soft gray alkaline earth metal that is vital for bones and teeth."},
    "Sc": {"name": "Scandium", "atomic_number": 21, "symbol": "Sc", "atomic_mass": 44.956, "category": "Transition Metal", "description": "Scandium is a soft, silvery-white metal used in lightweight alloys."},
    "Ti": {"name": "Titanium", "atomic_number": 22, "symbol": "Ti", "atomic_mass": 47.867, "category": "Transition Metal", "description": "Titanium is a strong, lightweight, and corrosion-resistant metal used in aerospace applications."},
    "V": {"name": "Vanadium", "atomic_number": 23, "symbol": "V", "atomic_mass": 50.942, "category": "Transition Metal", "description": "Vanadium is used to make strong steel alloys and is essential in some biological systems."},
    "Cr": {"name": "Chromium", "atomic_number": 24, "symbol": "Cr", "atomic_mass": 52.00, "category": "Transition Metal", "description": "Chromium is a hard, silvery metal used in stainless steel and chrome plating."},
    "Mn": {"name": "Manganese", "atomic_number": 25, "symbol": "Mn", "atomic_mass": 54.938, "category": "Transition Metal", "description": "Manganese is used in steel production and plays a role in various biological processes."},
    "Fe": {"name": "Iron", "atomic_number": 26, "symbol": "Fe", "atomic_mass": 55.845, "category": "Transition Metal", "description": "Iron is one of the most common metals on Earth and is vital for the transport of oxygen in blood."},
    "Co": {"name": "Cobalt", "atomic_number": 27, "symbol": "Co", "atomic_mass": 58.933, "category": "Transition Metal", "description": "Cobalt is used in batteries and alloys, and is essential in vitamin B12."},
    "Ni": {"name": "Nickel", "atomic_number": 28, "symbol": "Ni", "atomic_mass": 58.693, "category": "Transition Metal", "description": "Nickel is used in stainless steel and is a key component in rechargeable batteries."},
    "Cu": {"name": "Copper", "atomic_number": 29, "symbol": "Cu", "atomic_mass": 63.546, "category": "Transition Metal", "description": "Copper is widely used in electrical wiring and is an essential trace element in living organisms."},
    "Zn": {"name": "Zinc", "atomic_number": 30, "symbol": "Zn", "atomic_mass": 65.38, "category": "Transition Metal", "description": "Zinc is used in galvanization and is important for immune function."},
    "Ga": {"name": "Gallium", "atomic_number": 31, "symbol": "Ga", "atomic_mass": 69.723, "category": "Post-transition Metal", "description": "Gallium is used in semiconductors and light-emitting diodes (LEDs)."},
    "Ge": {"name": "Germanium", "atomic_number": 32, "symbol": "Ge", "atomic_mass": 72.63, "category": "Metalloid", "description": "Germanium is used in transistors and is a key material for infrared optics."},
    "As": {"name": "Arsenic", "atomic_number": 33, "symbol": "As", "atomic_mass": 74.922, "category": "Metalloid", "description": "Arsenic is a toxic element used in pesticides and can be found in contaminated water."},
    "Se": {"name": "Selenium", "atomic_number": 34, "symbol": "Se", "atomic_mass": 78.971, "category": "Non-metal", "description": "Selenium is an essential trace element and is used in solar cells and electronics."},
    "Br": {"name": "Bromine", "atomic_number": 35, "symbol": "Br", "atomic_mass": 79.904, "category": "Halogen", "description": "Bromine is a reddish-brown liquid that is used in flame retardants and disinfectants."},
    "Kr": {"name": "Krypton", "atomic_number": 36, "symbol": "Kr", "atomic_mass": 83.798, "category": "Noble Gas", "description": "Krypton is used in lighting and in the production of certain kinds of photographic flashes."},
    "Rb": {"name": "Rubidium", "atomic_number": 37, "symbol": "Rb", "atomic_mass": 85.468, "category": "Alkali Metal", "description": "Rubidium is a soft, silvery metal used in research and in special types of glass."},
    "Sr": {"name": "Strontium", "atomic_number": 38, "symbol": "Sr", "atomic_mass": 87.62, "category": "Alkaline Earth Metal", "description": "Strontium is used in fireworks and magnets."},
    "Y": {"name": "Yttrium", "atomic_number": 39, "symbol": "Y", "atomic_mass": 88.906, "category": "Transition Metal", "description": "Yttrium is used in phosphors and superconductors."},
    "Zr": {"name": "Zirconium", "atomic_number": 40, "symbol": "Zr", "atomic_mass": 91.224, "category": "Transition Metal", "description": "Zirconium is used in nuclear reactors and in dental implants."},
    "Nb": {"name": "Niobium", "atomic_number": 41, "symbol": "Nb", "atomic_mass": 92.906, "category": "Transition Metal", "description": "Niobium is used in superconducting materials and steel alloys."},
    "Mo": {"name": "Molybdenum", "atomic_number": 42, "symbol": "Mo", "atomic_mass": 95.95, "category": "Transition Metal", "description": "Molybdenum is used in steel production and is essential for many enzymes."},
    "Tc": {"name": "Technetium", "atomic_number": 43, "symbol": "Tc", "atomic_mass": 98, "category": "Transition Metal", "description": "Technetium is the first element to be artificially produced and has no stable isotopes."},
    "Ru": {"name": "Ruthenium", "atomic_number": 44, "symbol": "Ru", "atomic_mass": 101.07, "category": "Transition Metal", "description": "Ruthenium is used in electronics, catalysts, and as a corrosion-resistant material."},
    "Rh": {"name": "Rhodium", "atomic_number": 45, "symbol": "Rh", "atomic_mass": 102.91, "category": "Transition Metal", "description": "Rhodium is used in catalytic converters and jewelry."},
    "Pd": {"name": "Palladium", "atomic_number": 46, "symbol": "Pd", "atomic_mass": 106.42, "category": "Transition Metal", "description": "Palladium is used in catalytic converters and hydrogen storage."},
    "Ag": {"name": "Silver", "atomic_number": 47, "symbol": "Ag", "atomic_mass": 107.87, "category": "Transition Metal", "description": "Silver is widely used in jewelry, electronics, and as currency."},
    "Cd": {"name": "Cadmium", "atomic_number": 48, "symbol": "Cd", "atomic_mass": 112.41, "category": "Transition Metal", "description": "Cadmium is used in batteries and coatings but is highly toxic."},
    "In": {"name": "Indium", "atomic_number": 49, "symbol": "In", "atomic_mass": 114.82, "category": "Post-transition Metal", "description": "Indium is used in electronics and solders."},
    "Sn": {"name": "Tin", "atomic_number": 50, "symbol": "Sn", "atomic_mass": 118.71, "category": "Post-transition Metal", "description": "Tin is used in alloys and coatings."},
    "Sb": {"name": "Antimony", "atomic_number": 51, "symbol": "Sb", "atomic_mass": 121.76, "category": "Metalloid", "description": "Antimony is used in flame retardants and semiconductors."},
    "I": {"name": "Iodine", "atomic_number": 53, "symbol": "I", "atomic_mass": 126.90, "category": "Halogen", "description": "Iodine is essential for thyroid function and is used in disinfectants."},
    "Xe": {"name": "Xenon", "atomic_number": 54, "symbol": "Xe", "atomic_mass": 131.29, "category": "Noble Gas", "description": "Xenon is used in light sources and anesthesia."},
    "Cs": {"name": "Cesium", "atomic_number": 55, "symbol": "Cs", "atomic_mass": 132.91, "category": "Alkali Metal", "description": "Cesium is used in atomic clocks and radiation detection."},
    "Ba": {"name": "Barium", "atomic_number": 56, "symbol": "Ba", "atomic_mass": 137.33, "category": "Alkaline Earth Metal", "description": "Barium is used in x-ray imaging and as a weight in oil and gas drilling."},
    "La": {"name": "Lanthanum", "atomic_number": 57, "symbol": "La", "atomic_mass": 138.91, "category": "Lanthanide", "description": "Lanthanum is used in lighting and in catalysts."},
    "Ce": {"name": "Cerium", "atomic_number": 58, "symbol": "Ce", "atomic_mass": 140.12, "category": "Lanthanide", "description": "Cerium is used in catalysts and in the glass industry."},
    "Pr": {"name": "Praseodymium", "atomic_number": 59, "symbol": "Pr", "atomic_mass": 140.91, "category": "Lanthanide", "description": "Praseodymium is used in magnets and in alloying."},
    "Nd": {"name": "Neodymium", "atomic_number": 60, "symbol": "Nd", "atomic_mass": 144.24, "category": "Lanthanide", "description": "Neodymium is used in high-strength magnets and lasers."},
    "Pm": {"name": "Promethium", "atomic_number": 61, "symbol": "Pm", "atomic_mass": 145, "category": "Lanthanide", "description": "Promethium is a radioactive element used in nuclear batteries."},
    "Sm": {"name": "Samarium", "atomic_number": 62, "symbol": "Sm", "atomic_mass": 150.36, "category": "Lanthanide", "description": "Samarium is used in magnets and in neutron capture applications."},
    "Eu": {"name": "Europium", "atomic_number": 63, "symbol": "Eu", "atomic_mass": 151.98, "category": "Lanthanide", "description": "Europium is used in phosphorescent and fluorescent applications."},
    "Gd": {"name": "Gadolinium", "atomic_number": 64, "symbol": "Gd", "atomic_mass": 157.25, "category": "Lanthanide", "description": "Gadolinium is used in magnetic resonance imaging (MRI) and in neutron capture."},
    "Tb": {"name": "Terbium", "atomic_number": 65, "symbol": "Tb", "atomic_mass": 158.93, "category": "Lanthanide", "description": "Terbium is used in phosphors and in fiber optic systems."},
    "Dy": {"name": "Dysprosium", "atomic_number": 66, "symbol": "Dy", "atomic_mass": 162.50, "category": "Lanthanide", "description": "Dysprosium is used in magnets and in lasers."},
    "Ho": {"name": "Holmium", "atomic_number": 67, "symbol": "Ho", "atomic_mass": 164.93, "category": "Lanthanide", "description": "Holmium is used in lasers and in magnetic materials."},
    "Er": {"name": "Erbium", "atomic_number": 68, "symbol": "Er", "atomic_mass": 167.26, "category": "Lanthanide", "description": "Erbium is used in fiber optics and in nuclear reactors."},
    "Tm": {"name": "Thulium", "atomic_number": 69, "symbol": "Tm", "atomic_mass": 168.93, "category": "Lanthanide", "description": "Thulium is used in X-ray machines and lasers."},
    "Yb": {"name": "Ytterbium", "atomic_number": 70, "symbol": "Yb", "atomic_mass": 173.04, "category": "Lanthanide", "description": "Ytterbium is used in laser technology and in metallurgy."},
    "Lu": {"name": "Lutetium", "atomic_number": 71, "symbol": "Lu", "atomic_mass": 175.00, "category": "Lanthanide", "description": "Lutetium is used in high-performance scintillators and as a catalyst."},
    "Hf": {"name": "Hafnium", "atomic_number": 72, "symbol": "Hf", "atomic_mass": 178.49, "category": "Transition Metal", "description": "Hafnium is used in nuclear reactors and in semiconductor fabrication."},
    "Ta": {"name": "Tantalum", "atomic_number": 73, "symbol": "Ta", "atomic_mass": 180.95, "category": "Transition Metal", "description": "Tantalum is used in electronics and in surgical implants."},
    "W": {"name": "Tungsten", "atomic_number": 74, "symbol": "W", "atomic_mass": 183.84, "category": "Transition Metal", "description": "Tungsten is a heavy metal with the highest melting point and is used in light bulbs and welding."},
    "Re": {"name": "Rhenium", "atomic_number": 75, "symbol": "Re", "atomic_mass": 186.21, "category": "Transition Metal", "description": "Rhenium is used in jet engines and in catalysts."},
    "Os": {"name": "Osmium", "atomic_number": 76, "symbol": "Os", "atomic_mass": 190.23, "category": "Transition Metal", "description": "Osmium is a dense, blue-gray metal used in electrical contacts and in pen tips."},
    "Ir": {"name": "Iridium", "atomic_number": 77, "symbol": "Ir", "atomic_mass": 192.22, "category": "Transition Metal", "description": "Iridium is used in high-temperature applications and in electronics."},
    "Pt": {"name": "Platinum", "atomic_number": 78, "symbol": "Pt", "atomic_mass": 195.08, "category": "Transition Metal", "description": "Platinum is used in catalytic converters and in jewelry."},
    "Au": {"name": "Gold", "atomic_number": 79, "symbol": "Au", "atomic_mass": 196.97, "category": "Transition Metal", "description": "Gold is a soft, yellow metal used in jewelry and as a currency."},
    "Hg": {"name": "Mercury", "atomic_number": 80, "symbol": "Hg", "atomic_mass": 200.59, "category": "Transition Metal", "description": "Mercury is the only metal that is liquid at room temperature and is used in thermometers."},
    "Tl": {"name": "Thallium", "atomic_number": 81, "symbol": "Tl", "atomic_mass": 204.38, "category": "Post-transition Metal", "description": "Thallium is used in electronics and in the production of semiconductors."},
    "Pb": {"name": "Lead", "atomic_number": 82, "symbol": "Pb", "atomic_mass": 207.2, "category": "Post-transition Metal", "description": "Lead is a toxic metal once used in paints, pipes, and batteries."},
    "Bi": {"name": "Bismuth", "atomic_number": 83, "symbol": "Bi", "atomic_mass": 208.98, "category": "Post-transition Metal", "description": "Bismuth is used in cosmetics, medical imaging, and as a replacement for lead."},
    "Po": {"name": "Polonium", "atomic_number": 84, "symbol": "Po", "atomic_mass": 209, "category": "Metalloid", "description": "Polonium is a highly radioactive element discovered by Marie Curie."},
    "At": {"name": "Astatine", "atomic_number": 85, "symbol": "At", "atomic_mass": 210, "category": "Halogen", "description": "Astatine is a rare and highly radioactive element."},
    "Rn": {"name": "Radon", "atomic_number": 86, "symbol": "Rn", "atomic_mass": 222, "category": "Noble Gas", "description": "Radon is a colorless, odorless gas that is radioactive and harmful to health."},
    "Fr": {"name": "Francium", "atomic_number": 87, "symbol": "Fr", "atomic_mass": 223, "category": "Alkali Metal", "description": "Francium is a highly unstable, radioactive element."},
    "Ra": {"name": "Radium", "atomic_number": 88, "symbol": "Ra", "atomic_mass": 226, "category": "Alkaline Earth Metal", "description": "Radium is a radioactive element discovered by Marie Curie."},
    "Ac": {"name": "Actinium", "atomic_number": 89, "symbol": "Ac", "atomic_mass": 227, "category": "Actinide", "description": "Actinium is a radioactive element used in neutron sources."},
    "Th": {"name": "Thorium", "atomic_number": 90, "symbol": "Th", "atomic_mass": 232.04, "category": "Actinide", "description": "Thorium is a radioactive metal used in nuclear reactors."},
    "Pa": {"name": "Protactinium", "atomic_number": 91, "symbol": "Pa", "atomic_mass": 231.04, "category": "Actinide", "description": "Protactinium is a radioactive element used in nuclear research."},
    "U": {"name": "Uranium", "atomic_number": 92, "symbol": "U", "atomic_mass": 238.03, "category": "Actinide", "description": "Uranium is a heavy metal used as nuclear fuel."},
    "Np": {"name": "Neptunium", "atomic_number": 93, "symbol": "Np", "atomic_mass": 237, "category": "Actinide", "description": "Neptunium is a radioactive element used in nuclear reactors."},
    "Pu": {"name": "Plutonium", "atomic_number": 94, "symbol": "Pu", "atomic_mass": 244, "category": "Actinide", "description": "Plutonium is a highly radioactive metal used in nuclear weapons and reactors."},
    "Am": {"name": "Americium", "atomic_number": 95, "symbol": "Am", "atomic_mass": 243, "category": "Actinide", "description": "Americium is used in smoke detectors."},
    "Cm": {"name": "Curium", "atomic_number": 96, "symbol": "Cm", "atomic_mass": 247, "category": "Actinide", "description": "Curium is used in nuclear reactors and in cancer treatment."},
    "Bk": {"name": "Berkelium", "atomic_number": 97, "symbol": "Bk", "atomic_mass": 247, "category": "Actinide", "description": "Berkelium is a radioactive element used in scientific research."},
    "Cf": {"name": "Californium", "atomic_number": 98, "symbol": "Cf", "atomic_mass": 251, "category": "Actinide", "description": "Californium is used in neutron sources and in nuclear reactors."},
    "Es": {"name": "Einsteinium", "atomic_number": 99, "symbol": "Es", "atomic_mass": 252, "category": "Actinide", "description": "Einsteinium is a radioactive element used in nuclear research."},
    "Fm": {"name": "Fermium", "atomic_number": 100, "symbol": "Fm", "atomic_mass": 257, "category": "Actinide", "description": "Fermium is used in scientific research."},
    "Md": {"name": "Mendelevium", "atomic_number": 101, "symbol": "Md", "atomic_mass": 258, "category": "Actinide", "description": "Mendelevium is a synthetic element used in scientific studies."},
    "No": {"name": "Nobelium", "atomic_number": 102, "symbol": "No", "atomic_mass": 259, "category": "Actinide", "description": "Nobelium is used in scientific experiments."},
    "Lr": {"name": "Lawrencium", "atomic_number": 103, "symbol": "Lr", "atomic_mass": 262, "category": "Actinide", "description": "Lawrencium is a synthetic element used in research."},
    "Rf": {"name": "Rutherfordium", "atomic_number": 104, "symbol": "Rf", "atomic_mass": 267, "category": "Transition Metal", "description": "Rutherfordium is a synthetic element used in scientific studies."},
    "Db": {"name": "Dubnium", "atomic_number": 105, "symbol": "Db", "atomic_mass": 270, "category": "Transition Metal", "description": "Dubnium is a synthetic element used in scientific research."},
    "Sg": {"name": "Seaborgium", "atomic_number": 106, "symbol": "Sg", "atomic_mass": 271, "category": "Transition Metal", "description": "Seaborgium is a synthetic element used in nuclear research."},
    "Bh": {"name": "Bohrium", "atomic_number": 107, "symbol": "Bh", "atomic_mass": 270, "category": "Transition Metal", "description": "Bohrium is a synthetic element used in scientific studies."},
    "Hs": {"name": "Hassium", "atomic_number": 108, "symbol": "Hs", "atomic_mass": 277, "category": "Transition Metal", "description": "Hassium is a synthetic element used in scientific research."},
    "Mt": {"name": "Meitnerium", "atomic_number": 109, "symbol": "Mt", "atomic_mass": 278, "category": "Transition Metal", "description": "Meitnerium is a synthetic element used in research."},
    "Ds": {"name": "Darmstadtium", "atomic_number": 110, "symbol": "Ds", "atomic_mass": 281, "category": "Transition Metal", "description": "Darmstadtium is a synthetic element used in scientific experiments."},
    "Rg": {"name": "Roentgenium", "atomic_number": 111, "symbol": "Rg", "atomic_mass": 280, "category": "Transition Metal", "description": "Roentgenium is a synthetic element used in scientific research."},
    "Cn": {"name": "Copernicium", "atomic_number": 112, "symbol": "Cn", "atomic_mass": 285, "category": "Transition Metal", "description": "Copernicium is a synthetic element used in scientific research."},
    "Nh": {"name": "Nihonium", "atomic_number": 113, "symbol": "Nh", "atomic_mass": 284, "category": "Post-transition Metal", "description": "Nihonium is a synthetic element with no significant uses outside research."},
    "Fl": {"name": "Flerovium", "atomic_number": 114, "symbol": "Fl", "atomic_mass": 289, "category": "Post-transition Metal", "description": "Flerovium is a synthetic element used in scientific experiments."},
    "Mc": {"name": "Moscovium", "atomic_number": 115, "symbol": "Mc", "atomic_mass": 288, "category": "Post-transition Metal", "description": "Moscovium is a synthetic element with no significant uses outside research."},
    "Lv": {"name": "Livermorium", "atomic_number": 116, "symbol": "Lv", "atomic_mass": 293, "category": "Post-transition Metal", "description": "Livermorium is a synthetic element with no significant uses outside research."},
    "Ts": {"name": "Tennessine", "atomic_number": 117, "symbol": "Ts", "atomic_mass": 294, "category": "Halogen", "description": "Tennessine is a synthetic element with no significant uses outside research."},
    "Og": {"name": "Oganesson", "atomic_number": 118, "symbol": "Og", "atomic_mass": 294, "category": "Noble Gas", "description": "Oganesson is a synthetic element with no significant uses outside research."},
}

# Function to update the display of element info
def display_element_info():
    element_symbol = combo.get()
    element_info = elements.get(element_symbol, None)

    if element_info:
        info_label.config(state=tk.NORMAL)  # Enable editing for the Text widget

        # Clear previous content
        info_label.delete(1.0, tk.END)

        # Insert content with appropriate tags for color and style
        info_label.insert(tk.END, "Name: ", "bold_underline")
        info_label.insert(tk.END, element_info['name'] + "\n", "name")

        info_label.insert(tk.END, "Atomic Number: ", "bold_underline")
        info_label.insert(tk.END, str(element_info['atomic_number']) + "\n", "atomic_number")

        info_label.insert(tk.END, "Symbol: ", "bold_underline")
        info_label.insert(tk.END, element_info['symbol'] + "\n", "symbol")

        info_label.insert(tk.END, "Atomic Mass: ", "bold_underline")
        info_label.insert(tk.END, str(element_info['atomic_mass']) + "\n", "atomic_mass")

        info_label.insert(tk.END, "Category: ", "bold_underline")
        info_label.insert(tk.END, element_info['category'] + "\n", "category")

        info_label.insert(tk.END, "Description: ", "bold_underline")
        info_label.insert(tk.END, element_info['description'], "description")

        info_label.config(state=tk.DISABLED)  # Disable editing

    else:
        info_label.config(state=tk.NORMAL)
        info_label.delete(1.0, tk.END)
        info_label.insert(tk.END, "Element not found", "error")
        info_label.config(state=tk.DISABLED)

# Creating the main window
root = tk.Tk()
root.title("Periodic Table Explorer")
root.geometry("900x900")  # Larger window size for bigger fonts
root.config(bg="#FF00FF")  # Bright purple background color

# Header frame with a title
header_frame = tk.Frame(root, bg="#FF6347", pady=20)
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="Periodic Table Explorer", font=("Arial Black", 30, "bold"), fg="white", bg="#FF6347")
header_label.pack()

# Dropdown for selecting element symbol
combo_label = tk.Label(root, text="Select Element Symbol:", font=("Papyrus", 30, "bold"), fg="#FF1493", bg="#FFD700")
combo_label.pack(pady=10)

combo = ttk.Combobox(root, values=list(elements.keys()), width=10, font=("Algerian", 30, "bold"))
combo.pack(pady=16)

# Button to display info of selected element
info_button = tk.Button(root, text="Show Element Info", command=display_element_info, font=("Algerian", 30, "bold"), bg="#FF4500", fg="white", relief="flat", width=20)
info_button.pack(pady=20)

# Label to display the information (Text widget for rich text display)
info_label = tk.Text(root, height=10, width=60, wrap=tk.WORD, font=("Lucida Handwriting", 20, "bold"), fg="black", bg="#FFFAF0", bd=4, relief="solid")
info_label.pack(pady=10)
info_label.config(state=tk.DISABLED)  # Initially disable the Text widget

# Configuring tags for styling with more colors, larger fonts, and bold/darker text
info_label.tag_configure("bold_underline", font=("Algerian",30, "bold", "underline"), foreground="black")
info_label.tag_configure("name", foreground="#FF00FF", font=("Comic Sans MS", 30, "bold"))  # Bright Magenta
info_label.tag_configure("atomic_number", foreground="#1E90FF", font=("Algerian", 30, "bold"))  # Dodger Blue
info_label.tag_configure("symbol", foreground="#32CD32", font=("Comic Sans MS", 30, "bold"))  # Lime Green
info_label.tag_configure("atomic_mass", foreground="#FFD700", font=("Algerian", 30, "bold"))  # Gold
info_label.tag_configure("category", foreground="#FF4500", font=("Comic Sans MS", 30, "bold"))  # Orange Red
info_label.tag_configure("description", foreground="#FF6347", font=("Algerian", 30, "bold"))  # Tomato Red
info_label.tag_configure("error", foreground="red", font=("Comic Sans MS", 30, "bold"))

# Start the Tkinter main loop
root.mainloop()

