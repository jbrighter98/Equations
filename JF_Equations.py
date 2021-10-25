class Data():
    
    # Formatting rules:   https://matplotlib.org/stable/tutorials/text/mathtext.html
    #
    # Write equations like this inside braces of self.equations
    #
    #    1 : r'$___INSERT FORMATTED EQUATION HERE___$',
    #    2 : r'$___INSERT FORMATTED EQUATION HERE___$',
    #    ...
    #
    #
    # Write the name of the equation coresponding to the same number
    #
    #    1 : "Name of Equation 1", 
    #    2 : "Name of Equation 2",
    #    ...
    #
    # DON'T FORGET COMMAS!!!
    # THE LAST ONE IN THE LISTS DON'T GET COMMAS
    

    def __init__(self):
        self.equations = {
            
            1 : "r'$\tau=\mu\frac{dV}{dy}$'",
            2 : "r'$L= N\mathrm{cos}\alpha-A\mathrm{sin}\alpha$'",
            3 : "r'$D= N\mathrm{sin}\alpha+A\mathrm{cos}\alpha$'",
            4 : "r'$q=\frac{1}{2}\rhoV^{2}$'",
            5 : "r'$dp=-g\rhody$'",
            6 : "r'$\frac{\partial \rho}{\partial t}+\frac{\partial \rho U}{\partial x}+\frac{\partial \rho V}{\partial y}+\frac{\partial \rho W}{\partial z}=0$
            7 : "r'$\nabla \times \bar{U}=0$'",
            8 : "r'$\nabla \cdot \bar{U}=0$'",
            9 : "r'$\frac{\partial \rho U}{\partial t}+\frac{\partial\left(\rho U U+P-\tau_{x x}\right)}{\partial x}+\frac{\partial\left(\rho U V-\tau_{x y}\right)}{\partial y}+\frac{\partial\left(\rho U W-\tau_{x z}\right)}{\partial z}=0$'",
            10 : "r'$\frac{\partial \rho W}{\partial t}+\frac{\partial\left(\rho W U-\tau_{x z}\right)}{\partial x}+\frac{\partial\left(\rho W V-\tau_{y z}\right)}{\partial y}+\frac{\partial\left(\rho W W+P-\tau_{z z}\right)}{\partial z}=0$'",
            11 : "r'$\frac{\partial \rho V}{\partial t}+\frac{\partial\left(\rho V U-\tau_{x y}\right)}{\partial x}+\frac{\partial\left(\rho V V+P-\tau_{y y}\right)}{\partial y}+\frac{\partial\left(\rho V W-\tau_{y z}\right)}{\partial z}=0$'",
            12 : "r'$\delta Q=d E+\delta W$'",
            13 : "r'$T d s=d e+P d v$'",
            14 : "r'$h=e+P v$'",
            15 : "r'$P=\rho R T$'",
            16 : "r'$\gamma=\frac{C_{p}}{C_{v}}$'",
            17 : "r'$S=k \ln (W)$'",
            18 : "r'$\int_{A}(\bar{n} \times \nabla F) d A=\oint_{C} F \bar{c} d C$'",
            19 : "r'$\int_{V}(\nabla \times \bar{F}) d V=\int_{A} \bar{n} \times \bar{F} d A$'",
            20 : "r''",
            21 : "r''",
            22 : "r''",
            23 : "r''",
            24 : "r''",
            25 : "r''",
            26 : "r''",
            27 : "r''",
            28 : "r''",
            29 : "r''",
            30 : "r''",
            23 : "r''",
            24 : "r''",
            
            
        }

        self.names = {
            
            1: "Shear Stress",
            2 : "Lift",
            3 : "Drag",
            4 : "Dynamic Pressure",
            5 : "Hydrostatic Equation",
            6 : "Continuity Equation",
            7 : "Irrotational Flow",
            8 : "Incompressible Flow",
            9 : "Conservation of Momentum (x-direction)",
            10 : "Conservation of Momentum (y-direction)",
            11 : "Conservation of Momentum (z-direction)",
            12 : "First Law of Thermodynamics",
            13 : "Gibb's Equation (Second Law of Thermodynamics",
            14 : "Enthalpy",
            15 : "Ideal Gas Law",
            16 : "Ratio of Specific Heats",
            17 : "Entropy in terms of Boltzmann's Constant",
            18 : "Stokes' Theroem",
            19 : "Gauss's Theorem",
            20 : "",
            21 : "",
            22 : "",
            23 : "",
            24 : "",
            25 : "",
            26 : "",
            27 : "",
            28 : "",
            29 : "",
            30 : "",
       
        }
