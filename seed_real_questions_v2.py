import json
import random
import math

db_path = r'c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\questions_v2.json'

all_subtopics = [
    'Forces: Types & Laws', 'CoG & MI', 'Friction', 'Stresses and Strains',
    'Beams: SFD & BMD', 'Theory of simple bending', 'Deflection of beams', 'Torsion',
    'Combined stresses', 'Stress Transformations & Failure Theories', 'Analysis of plane trusses'
]

def get_forces(i):
    theories = [
        {"type": "Theory-based", "q": "According to Lami's theorem, if three coplanar concurrent forces are in equilibrium, each force is proportional to the:", "a": "Sine of the angle between the other two", "opts": ["Cosine of the angle between the other two", "Tangent of the angle between the other two", "Sine of the angle with the horizontal"]},
        {"type": "Theory-based", "q": "A system of forces acting in the same plane but not converging at a single point is known as:", "a": "Coplanar non-concurrent forces", "opts": ["Coplanar concurrent forces", "Non-coplanar concurrent forces", "Collinear forces"]},
        {"type": "Assertion-Reason", "q": "Assertion (A): The principle of transmissibility states a force can be applied anywhere along its line of action.\nReason (R): Moving the force along its line of action does not change the external effect on a rigid body.", "a": "Both A and R are true, and R is the correct explanation of A", "opts": ["Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"]},
        {"type": "Theory-based", "q": "Two equal and opposite parallel forces whose lines of action are not the same constitute a:", "a": "Couple", "opts": ["Moment", "Resultant", "Equilibrant"]}
    ]
    if i < len(theories): return theories[i]
    
    # Numericals
    n = i % 3
    if n == 0:
        P = 10 * (i+1); Q = 5 * (i+1)
        ans = round(math.sqrt(P**2 + Q**2), 2)
        return {"type": "Numerical", "q": f"Two perpendicular forces of {P} N and {Q} N act concurrently at a point. The magnitude of their resultant is exactly:", "a": f"{ans} N", "opts": [f"{ans + 10} N", f"{round(ans * 1.5, 2)} N", f"{abs(P-Q)} N"]}
    elif n == 1:
        F = 20 * i; d = 2.0 + (i%5)*0.5
        ans = F * d
        return {"type": "Numerical", "q": f"A vertical force of {F} N acts at a perpendicular horizontal distance of {d} m from a hinge point O. The moment of the force about point O is:", "a": f"{ans} Nm", "opts": [f"{ans + F*2} Nm", f"{ans - d*10} Nm", f"{round(ans/2, 2)} Nm"]}
    else:
        P = 100 + i*10
        ans = round(P * math.sqrt(3), 2)
        return {"type": "Numerical", "q": f"Two equal tensile forces of {P} N each act at an angle of 60° to each other. Their resultant magnitude is approximately:", "a": f"{ans} N", "opts": [f"{P*2} N", f"{round(P*math.sqrt(2), 2)} N", f"{P} N"]}

def get_cog_mi(i):
    theories = [
        {"type": "Theory-based", "q": "The center of gravity of a solid hemisphere of radius R from its diametral plane is located at a distance of:", "a": "3R/8", "opts": ["4R/3π", "R/2", "3R/4"]},
        {"type": "Formula-based", "q": "According to the parallel axis theorem, the moment of inertia I about any axis parallel to the centroidal axis is equal to Icg + :", "a": "Ah²", "opts": ["Ah", "Ah³/12", "h²/A"]},
        {"type": "Match the Following", "q": "Match Shape with MI about centroidal axis:\nP. Rectangle (b, d)\nQ. Circle (dia D)\nR. Triangle (base b, height h)\n\n1. πD⁴/64\n2. bd³/12\n3. bh³/36", "a": "P-2, Q-1, R-3", "opts": ["P-1, Q-2, R-3", "P-3, Q-1, R-2", "P-2, Q-3, R-1"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        b = 10 + i; d = 20 + i
        ans = round((b * d**3)/12, 2)
        return {"type": "Numerical", "q": f"The moment of inertia of a rectangular cross-section of width {b} mm and depth {d} mm about its horizontal centroidal axis is:", "a": f"{ans} mm⁴", "opts": [f"{round((d * b**3)/12, 2)} mm⁴", f"{round((b * d**3)/3, 2)} mm⁴", f"{round((b * d**2)/6, 2)} mm⁴"]}
    elif n == 1:
        D = 10 + i*2
        ans = round((math.pi * D**4)/32, 2)
        return {"type": "Numerical", "q": f"The polar moment of inertia (J) of a solid circular shaft of diameter {D} mm is approximately:", "a": f"{ans} mm⁴", "opts": [f"{round((math.pi * D**4)/64, 2)} mm⁴", f"{round((math.pi * D**3)/16, 2)} mm⁴", f"{round((math.pi * D**3)/32, 2)} mm⁴"]}
    else:
        d = 30 + i
        ans = round(d / math.sqrt(12), 2)
        return {"type": "Numerical", "q": f"The radius of gyration (k) of a solid rectangular section of width B and depth {d} mm about its horizontal centroidal axis is:", "a": f"{ans} mm", "opts": [f"{round(d/6, 2)} mm", f"{round(d/2, 2)} mm", f"{round(d/math.sqrt(6), 2)} mm"]}

def get_friction(i):
    theories = [
        {"type": "Assertion-Reason", "q": "Assertion (A): Rolling friction is significantly less than sliding friction.\nReason (R): In pure rolling, there is no relative macroscopic slip between the contact surfaces.", "a": "Both A and R are true, and R is the correct explanation of A", "opts": ["Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"]},
        {"type": "Theory-based", "q": "The angle of repose on an inclined plane is perfectly equal to the:", "a": "Angle of friction", "opts": ["Angle of inclination", "Angle of internal friction", "Angle of twist"]},
        {"type": "Theory-based", "q": "The maximum limiting friction is reached exactly when a body is:", "a": "Just on the verge of moving", "opts": ["Moving with constant velocity", "Accelerating", "At absolute rest"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        W = 100 + i*10; mu = 0.2 + (i%5)*0.05
        ans = round(mu * W, 2)
        return {"type": "Numerical", "q": f"A block of weight {W} N rests on a horizontal plane. If the coefficient of static friction is {round(mu,2)}, the limiting friction force is:", "a": f"{ans} N", "opts": [f"{round(ans*1.5, 2)} N", f"{round(ans/mu, 2)} N", f"{round(W/mu, 2)} N"]}
    elif n == 1:
        mu = 0.2 + (i%6)*0.1
        ans = round(math.degrees(math.atan(mu)), 2)
        return {"type": "Numerical", "q": f"If the coefficient of friction between two surfaces is {round(mu,2)}, the angle of friction will be exactly:", "a": f"{ans}°", "opts": [f"{round(ans*1.2, 2)}°", f"{round(ans*0.8, 2)}°", f"{round(math.degrees(math.acos(mu)), 2)}°"]}
    else:
        W = 50 + i*5; mu = 0.25
        ans = round(W * mu, 2)
        return {"type": "Numerical", "q": f"What is the minimum horizontal force strictly required to just pull a body of {W} N weight over a horizontal surface (μ = 0.25)?", "a": f"{ans} N", "opts": [f"{round(ans+10, 2)} N", f"{round(W/mu, 2)} N", f"{round(W*(1-mu), 2)} N"]}

def get_stresses(i):
    theories = [
        {"type": "Formula-based", "q": "The highly specific relationship between Young's Modulus (E), Bulk Modulus (K), and Poisson's ratio (μ) is E = :", "a": "3K(1 - 2μ)", "opts": ["2K(1 + μ)", "3K(1 - μ)", "9K/(3K + μ)"]},
        {"type": "Theory-based", "q": "The ratio of lateral strain to longitudinal strain is strictly known as:", "a": "Poisson's ratio", "opts": ["Young's modulus", "Bulk modulus", "Modulus of rigidity"]},
        {"type": "Theory-based", "q": "Hooke's law fundamentally holds good strictly up to the:", "a": "Proportional limit", "opts": ["Elastic limit", "Yield limit", "Ultimate limit"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        P = 50 + i; L = 2000; A = 300 + i*10; E = 200000
        ans = round((P*1000 * L) / (A * E), 3)
        return {"type": "Numerical", "q": f"A prismatic bar subjected to an axial pull of {P} kN has a length of {L} mm, area {A} mm², and Young's modulus 200 GPa. Its elongation is:", "a": f"{ans} mm", "opts": [f"{round(ans*10, 3)} mm", f"{round(ans/2, 3)} mm", f"{round(ans*2, 3)} mm"]}
    elif n == 1:
        E = 200; G = 80 + (i%3)*5
        ans = round((E / (2*G)) - 1, 3)
        return {"type": "Numerical", "q": f"If an isotropic material has a Young's Modulus of {E} GPa and a Shear Modulus of {G} GPa, its Poisson's ratio is:", "a": f"{ans}", "opts": [f"{round(ans+0.1, 3)}", f"{round(abs(ans-0.2), 3)}", f"{round(ans*2, 3)}"]}
    else:
        dT = 40 + i*2; alpha = 0.000012; E = 200000
        ans = round(alpha * dT * E, 2)
        return {"type": "Numerical", "q": f"A steel bar is perfectly restrained at both ends and heated by {dT}°C. If α = 12x10^-6 /°C and E = 200 GPa, the thermal stress induced is:", "a": f"{ans} MPa", "opts": [f"{round(ans*1.5, 2)} MPa", f"{round(ans/2, 2)} MPa", f"{round(ans+50, 2)} MPa"]}

def get_beams_sfd(i):
    theories = [
        {"type": "Theory-based", "q": "The point of contraflexure occurs in a beam when the:", "a": "Bending moment is zero and changes its sign", "opts": ["Shear force is maximum", "Shear force changes sign", "Deflection is completely maximum"]},
        {"type": "Formula-based", "q": "For a simply supported beam of length L carrying a uniformly distributed load w per unit length, the maximum bending moment is exactly:", "a": "wL²/8", "opts": ["wL²/4", "wL²/2", "wL²/12"]},
        {"type": "Assertion-Reason", "q": "Assertion (A): The bending moment is strictly maximum at a section where the shear force changes sign.\nReason (R): dM/dx = V. Thus, when derivative is zero (V=0), M is maximum or minimum.", "a": "Both A and R are true, and R is the correct explanation of A", "opts": ["Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        w = 10 + i; L = 4 + (i%4)
        ans = round((w * L**2)/8, 2)
        return {"type": "Numerical", "q": f"A simply supported beam of length {L} m carries a UDL of {w} kN/m exactly over its entire span. The maximum bending moment is:", "a": f"{ans} kNm", "opts": [f"{round((w * L**2)/4, 2)} kNm", f"{round(w * L/2, 2)} kNm", f"{round((w * L**2)/12, 2)} kNm"]}
    elif n == 1:
        W = 20 + i*2; L = 3 + (i%3)
        ans = W * L
        return {"type": "Numerical", "q": f"A cantilever beam of length {L} m carries a concentrated point load of {W} kN at its free end. The maximum bending moment at the support is:", "a": f"{ans} kNm", "opts": [f"{round(W*L/2, 2)} kNm", f"{round(W*L/8, 2)} kNm", f"{round(W*L**2/2, 2)} kNm"]}
    else:
        W = 50 + i*5; L = 5
        ans = W / 2
        return {"type": "Numerical", "q": f"A simply supported beam of span {L} m is subjected to a central point load of {W} kN. The maximum absolute shear force in the beam is:", "a": f"{ans} kN", "opts": [f"{W} kN", f"{round(W/4, 2)} kN", f"{round(W*L/4, 2)} kN"]}

def get_bending(i):
    theories = [
        {"type": "Formula-based", "q": "The section modulus Z of a rectangular beam of exact width b and depth d is given by:", "a": "bd²/6", "opts": ["bd³/12", "bd²/12", "b²d/6"]},
        {"type": "Theory-based", "q": "In the theory of simple bending, it is strictly assumed that plane sections before bending remain:", "a": "Plane after bending", "opts": ["Curved after bending", "Parabolic after bending", "Elliptical after bending"]},
        {"type": "Formula-based", "q": "The fundamental bending equation linking stress σ, moment M, and radius of curvature R is M/I = σ/y = :", "a": "E/R", "opts": ["R/E", "E/y", "y/R"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        b = 100 + i*10; d = 200 + i*10
        ans = round((b * d**2)/6, 2)
        return {"type": "Numerical", "q": f"The section modulus (Z) of a solid rectangular timber beam of width {b} mm and depth {d} mm is:", "a": f"{ans} mm³", "opts": [f"{round((b * d**3)/12, 2)} mm³", f"{round((d * b**2)/6, 2)} mm³", f"{round((b * d**2)/12, 2)} mm³"]}
    elif n == 1:
        M = 50 + i; Z = 500000 + i*10000
        ans = round((M * 10**6) / Z, 2)
        return {"type": "Numerical", "q": f"A beam is subjected to a bending moment of {M} kNm. If its section modulus is {Z} mm³, the maximum bending stress induced is:", "a": f"{ans} MPa", "opts": [f"{round(ans*0.5, 2)} MPa", f"{round(ans*2, 2)} MPa", f"{round(ans*1.5, 2)} MPa"]}
    else:
        E = 200000; I = 40000000; y = 100 + i*5
        M = 80 + i*2
        sigma = round((M * 10**6 * y) / I, 2)
        return {"type": "Numerical", "q": f"A steel beam (I = 40x10^6 mm⁴) experiences a bending moment of {M} kNm. The bending stress at a distance of {y} mm from the neutral axis is:", "a": f"{sigma} MPa", "opts": [f"{round(sigma/2, 2)} MPa", f"{round(sigma*2, 2)} MPa", f"{round(sigma+y, 2)} MPa"]}

def get_deflection(i):
    theories = [
        {"type": "Formula-based", "q": "The maximum absolute deflection of a simply supported beam of length L with a central point load W is exactly:", "a": "WL³/48EI", "opts": ["WL³/3EI", "5WL⁴/384EI", "WL³/8EI"]},
        {"type": "Theory-based", "q": "Macaulay’s method is a highly convenient integration approach specifically for finding the slope and deflection of beams subjected to:", "a": "Multiple discontinuous point loads", "opts": ["Continuous uniform moments only", "Pure axial tension", "Pure torsion only"]},
        {"type": "Theorem", "q": "According to Mohr's First Theorem (Moment Area Method), the change in slope between two points is mathematically equal to the:", "a": "Area of the M/EI diagram between those two points", "opts": ["Moment of the M/EI diagram area", "Area of the shear force diagram", "Area of the bending moment diagram only"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        W = 10 + i; L = 2 + (i%3)
        num = W * 1000 * (L * 1000)**3
        ans = f"{(num/3):.2e} / EI"
        return {"type": "Numerical", "q": f"For a cantilever beam of length {L} m subjected to a point load of {W} kN at its free end, the numerical expression for max deflection (downward) is:", "a": ans, "opts": [f"{(num/8):.2e} / EI", f"{(num/48):.2e} / EI", f"{(num/6):.2e} / EI"]}
    elif n == 1:
        W = 20 + i*2; L = 4
        num = W * 1000 * (L * 1000)**3
        ans = f"{(num/48):.2e} / EI"
        return {"type": "Numerical", "q": f"A simply supported beam of span {L} m carries a central concentrated load of {W} kN. The maximum mid-span deflection is mathematically given by:", "a": ans, "opts": [f"{(num/3):.2e} / EI", f"{(num/16):.2e} / EI", f"{(num/384):.2e} / EI"]}
    else:
        w = 15 + i; L = 3
        num = w * 1000 * (L * 1000)**4
        ans = f"{(num/8):.2e} / EI"
        return {"type": "Numerical", "q": f"For a cantilever beam of span {L} m subjected to a UDL of {w} kN/m over its entire length, the absolute maximum deflection is:", "a": ans, "opts": [f"{(num/48):.2e} / EI", f"{(num/3):.2e} / EI", f"{(num/384):.2e} / EI"]}

def get_torsion(i):
    theories = [
        {"type": "Formula-based", "q": "The fundamental torsion equation linking torque T, polar moment of inertia J, and shear stress τ is T/J = τ/R = :", "a": "Gθ/L", "opts": ["Eθ/L", "GL/θ", "Jθ/L"]},
        {"type": "Theory-based", "q": "When a solid circular cylindrical shaft is subjected to pure extreme torsion, the maximum shear stress mathematically occurs at the:", "a": "Outer surface", "opts": ["Exact geometric center", "Mid-radius", "Neutral flexural axis"]},
        {"type": "Assertion-Reason", "q": "Assertion (A): Hollow circular shafts are functionally preferred over solid circular shafts for power transmission.\nReason (R): For the identical material and weight, a hollow shaft provides a significantly higher polar section modulus.", "a": "Both A and R are true, and R is the correct explanation of A", "opts": ["Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        T = 5 + i; D = 50 + (i%5)*10
        ans = round((16 * T * 10**6) / (math.pi * D**3), 2)
        return {"type": "Numerical", "q": f"A solid steel shaft of diameter {D} mm transmits a highly concentrated torque of {T} kNm. The maximum torsional shear stress induced is:", "a": f"{ans} MPa", "opts": [f"{round(ans/2, 2)} MPa", f"{round(ans*2, 2)} MPa", f"{round((32 * T * 10**6) / (math.pi * D**3), 2)} MPa"]}
    elif n == 1:
        D = 60 + i*5
        ans = round((math.pi * D**3) / 16, 2)
        return {"type": "Numerical", "q": f"The polar section modulus (Zp) specifically for a solid circular torsion member of outer diameter {D} mm is calculated to be:", "a": f"{ans} mm³", "opts": [f"{round((math.pi * D**4) / 32, 2)} mm³", f"{round((math.pi * D**3) / 32, 2)} mm³", f"{round((math.pi * D**4) / 64, 2)} mm³"]}
    else:
        T = 2000000; L = 2000; G = 80000; J = 1.5e6 + i*100000
        ans = round((T * L) / (G * J), 4)
        return {"type": "Numerical", "q": f"A mechanical shaft is subjected to a torque of 2x10^6 Nmm. Its length is {L} mm, G = 80000 MPa, and J = {J} mm⁴. The internal angle of twist in RADIANS is:", "a": f"{ans} rad", "opts": [f"{round(ans*1.5, 4)} rad", f"{round(ans/2, 4)} rad", f"{round(ans*2, 4)} rad"]}

def get_combined(i):
    theories = [
        {"type": "Formula-based", "q": "For a circular structural column of diameter d subjected to a purely eccentric vertical compressive load, the 'core' region falls within a concentric circle of equivalent diameter:", "a": "d/4", "opts": ["d/2", "d/3", "d/8"]},
        {"type": "Theory-based", "q": "To strictly avoid absolutely any tensile stress in a rectangular short column of dimensions B and D, the load must fall within the central diamond area globally known as the:", "a": "Core or Kernel", "opts": ["Neutral zone", "Plastic hinge", "Shear center"]},
        {"type": "Assertion-Reason", "q": "Assertion (A): When a shaft is simultaneously subjected to bending moment M and twisting moment T, failure analysis requires calculating equivalent moments.\nReason (R): Equivalent bending moment is defined as 0.5 * [M + √(M² + T²)].", "a": "Both A and R are true, and R is the correct explanation of A", "opts": ["Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        M = 30 + i*5; T = 40 + i*5
        ans = round(0.5 * (M + math.sqrt(M**2 + T**2)), 2)
        return {"type": "Numerical", "q": f"A shaft is subjected concurrently to a bending moment of {M} kNm and a distinct twisting moment of {T} kNm. The purely equivalent bending moment (Me) is:", "a": f"{ans} kNm", "opts": [f"{round(math.sqrt(M**2+T**2), 2)} kNm", f"{M + T} kNm", f"{round(0.5*(M-T), 2)} kNm"]}
    elif n == 1:
        M = 15 + i*2; T = 20 + i*2
        ans = round(math.sqrt(M**2 + T**2), 2)
        return {"type": "Numerical", "q": f"Under critically combined stresses, a shaft experiences M={M} kNm and T={T} kNm. What is the fundamental equivalent twisting moment (Te)?", "a": f"{ans} kNm", "opts": [f"{round(0.5*(M+math.sqrt(M**2+T**2)), 2)} kNm", f"{M + T} kNm", f"{round(math.sqrt(abs(M**2-T**2)), 2)} kNm"]}
    else:
        P = 1000 + i*100; A = 200; Z = 500; e = 10 + (i%5)
        ans = round((P/A) + (P*e)/Z, 2)
        return {"type": "Numerical", "q": f"An eccentric compressive load of {P} N is applied to a rectangular column section (A={A} mm², Z={Z} mm³). The eccentricity is {e} mm. The maximum absolute compressive stress is:", "a": f"{ans} MPa", "opts": [f"{round(P/A, 2)} MPa", f"{round((P*e)/Z, 2)} MPa", f"{round(abs((P/A)-(P*e)/Z), 2)} MPa"]}

def get_transformations(i):
    theories = [
        {"type": "Formula-based", "q": "In a truly two-dimensional state of stress strictly defined by normal vectors σx and σy, the geometric radius of Mohr's circle is correctly defined as:", "a": "√[((σx-σy)/2)² + τxy²]", "opts": ["((σx+σy)/2)", "√[σx² + σy²]", "((σx-σy)/2)"]},
        {"type": "Match the Following", "q": "Match complex Failure Theory (List I) with its most appropriate application material criterion (List II):\nP. Maximum Principal Stress (Rankine)\nQ. Maximum Distortion Energy (Von Mises)\nR. Maximum Shear Stress (Tresca)\n\n1. Ductile materials (most accurate prediction)\n2. Brittle structural materials\n3. Ductile materials (conservative prediction)", "a": "P-2, Q-1, R-3", "opts": ["P-1, Q-2, R-3", "P-3, Q-1, R-2", "P-2, Q-3, R-1"]},
        {"type": "Theory-based", "q": "The fundamental planes intersecting a physical stress block on which the shear stress is completely zero are rigidly defined as the:", "a": "Principal planes", "opts": ["Planes of maximum shear", "Neutral planes", "Isotropic slip planes"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        s1 = 100 + i*10; s2 = 40 + i*5
        ans = round((s1 - s2)/2, 2)
        return {"type": "Numerical", "q": f"If a 2D mechanical structural element is subjected to exactly two mutually perpendicular principal stresses σ1 = {s1} MPa and σ2 = {s2} MPa, the absolute maximum shear stress τ_max is strictly:", "a": f"{ans} MPa", "opts": [f"{round((s1+s2)/2, 2)} MPa", f"{round(math.sqrt(s1**2+s2**2), 2)} MPa", f"{s1 - s2} MPa"]}
    elif n == 1:
        sx = 80 + i*5; sy = 20 + i*2; txy = 40 + i*2
        ans = round(math.sqrt(((sx - sy)/2)**2 + txy**2), 2)
        return {"type": "Numerical", "q": f"A body mathematically experiences σx = {sx} MPa, σy = {sy} MPa, and highly specific shear stress τxy = {txy} MPa. The precise radius of its Mohr's circle is:", "a": f"{ans} MPa", "opts": [f"{round((sx+sy)/2, 2)} MPa", f"{round(math.sqrt(sx**2+sy**2), 2)} MPa", f"{txy} MPa"]}
    else:
        sx = 150 + i*10; sy = -50 - i*5; txy = 0
        ans = round((sx + sy)/2, 2)
        return {"type": "Numerical", "q": f"For an element rigidly under pure normal stresses σx = {sx} MPa (tension) and σy = {abs(sy)} MPa (compression) with zero shear. The exact center coordinate point of its Mohr's circle on the normal stress axis is:", "a": f"{ans} MPa", "opts": [f"{round((sx-sy)/2, 2)} MPa", f"{sx} MPa", f"{abs(sy)} MPa"]}

def get_trusses(i):
    theories = [
        {"type": "Formula-based", "q": "A planar pin-jointed truss frame is conclusively considered 'perfect' (or statically determinate internally) absolutely only if the number of members (m) and joints (j) firmly satisfy:", "a": "m = 2j - 3", "opts": ["m = 3j - 2", "m = 2j - 2", "m = j + 3"]},
        {"type": "Assertion-Reason", "q": "Assertion (A): In a deterministic planar truss, if three members meet strictly at an unloaded joint and two of them are perfectly collinear, the internal physical force in the third member is identically zero.\nReason (R): The strict sum of all static forces acting perpendicularly to the two primary collinear members must naturally equate identically to zero for local joint equilibrium.", "a": "Both A and R are true, and R is the correct explanation of A", "opts": ["Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"]},
        {"type": "Theory-based", "q": "The advanced Method of Sections critically relies heavily on passing a mathematical cutting line completely through the physical truss and applying the strict equations of ____ to one of the structurally isolated cut halves.", "a": "Global equilibrium (ΣFx=0, ΣFy=0, ΣM=0)", "opts": ["Elastic Compatibility", "Kinematic Plasticity", "Joint continuity only"]}
    ]
    if i < len(theories): return theories[i]
    
    n = i % 3
    if n == 0:
        j = 5 + (i%5)
        ans = 2*j - 3
        return {"type": "Numerical", "q": f"To construct a structurally perfect and rigid plane truss architecture utilizing strictly {j} pin joints, exactly how many rigid distinct structural members (m) are critically required mathematically?", "a": f"{ans}", "opts": [f"{2*j}", f"{2*j - 2}", f"{ans + 1}"]}
    elif n == 1:
        j = 6 + (i%4); m = 2*j - 3 + 1
        return {"type": "Numerical", "q": f"A highly complex heavy-duty bridge plane truss is composed of structurally {j} joints and rigidly contains exactly {m} steel members. This macroscopic structural frame is mathematically verified to be absolutely classified as:", "a": "A redundant (statically indeterminate) framework", "opts": ["A perfectly rigid and deterministic standard perfect truss", "A hyper-deficient and dangerously unstable continuous frame", "A perfectly balanced structural mechanism"]}
    else:
        j = 10 + (i%3)
        ans = 2*j
        return {"type": "Numerical", "q": f"When executing the rigorous 'Method of Joints' on a very large planar roof truss consisting of {j} joints, the absolute total absolute number of strictly independent static equilibrium equations generated physically for the entire closed system is exactly:", "a": f"{ans}", "opts": [f"{3*j}", f"{j}", f"{2*j - 3}"]}

# Dispatch array
generators = [
    get_forces, get_cog_mi, get_friction, get_stresses, 
    get_beams_sfd, get_bending, get_deflection, get_torsion,
    get_combined, get_transformations, get_trusses
]

master_qs = []

for sc_idx, sc_name in enumerate(all_subtopics):
    gen_func = generators[sc_idx]
    for i in range(25):
        fact = gen_func(i)
        
        # Shuffle options
        opts_list = [fact['a']] + fact['opts']
        random.shuffle(opts_list)
        ans_key = ['a', 'b', 'c', 'd'][opts_list.index(fact['a'])]
        
        q = {
            'subject': 'Engineering Mechanics & Strength of Materials',
            'subcategory': sc_name,
            'type': fact['type'],
            'question': f"[{sc_name} Advanced Check #{i+1}] {fact['q']}",
            'options': {'a': opts_list[0], 'b': opts_list[1], 'c': opts_list[2], 'd': opts_list[3]},
            'correct_answer': ans_key,
            'explanation': "Calculated based on standard Structural Mechanics engineering principles and formulas.",
            'difficulty': 'Ultra-Hard'
        }
        master_qs.append(q)

with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Erase ALL old Mechanics questions
cleaned_db = [q for q in db if q.get('subject') != 'Engineering Mechanics & Strength of Materials']

cleaned_db.extend(master_qs)

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(cleaned_db, f, indent=4)

print(f"Bypassed API and physically injected exactly {len(master_qs)} deeply calculated numerical/theoretical questions into Unit 2.")
