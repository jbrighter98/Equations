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
    # Lastly for desctription, do the same as the names but if you want to start a new line, start the new line with \n like
    #
    #   1 : "This is the first line
    #       \nThis is the second line
    #       \nThis is the third line",
    #   2 : "....",
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
            20 : "r'$L=\frac{1}{2} \rho_{\infty} V_{\infty}^{2} S C_{L}$'",
            21 : "r'$D=\frac{1}{2} \rho_{\infty} V_{\infty}^{2} S C_{D}$'",
            22 : "r'$\nabla \cdot \mathbf{V}=\frac{\partial V_{x}}{\partial x}+\frac{\partial V_{y}}{\partial y}+\frac{\partial V_{z}}{\partial z}$'",
            23 : "r'$\nabla \mathbf{x} \mathbf{V}=\left|\begin{array}{ccc}\mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ V_{x} & V_{y} & V_{z}\end{array}\right|$'",
            24 : "r'$\oint_{a}^{b} \mathbf{A} \cdot \mathbf{d s}$'",
            25 : "r'$\oint_{C} \mathbf{A} \cdot \mathbf{d} \mathbf{s}=\iint_{S}(\nabla \times \mathbf{A}) \cdot \mathbf{d} \mathbf{S}$'",
            26 : "r'$\oiint_{S} \mathbf{A} \cdot \mathbf{d} \mathbf{S}=\oiiint_{\mathcal{V}}(\nabla \cdot \mathbf{A}) d \mathcal{V}$'",
            27 : "r'$\oiint_{S} p \mathbf{d} \mathbf{S}=\oiiint_{\mathcal{V}} \nabla p d \mathcal{V}$'",
            28 : "r'$\dot{m}=\rho V_{n} A$'",
            29 : "r'Mass flux $=\frac{\dot{m}}{A}=\rho V_{n}$'",
            30 : "r'$\frac{\partial}{\partial t} \oiiint_{\mathcal{V}} \rho \rho d \mathcal{V}+\oiiint_{S} \rho \mathbf{V} \cdot \mathbf{d} \mathbf{S}=0$'",
            23 : "r'$\frac{\partial \rho}{\partial t}+\nabla \cdot(\rho \mathbf{V})=0$'",
            24 : "r'$\frac{\partial}{\partial t} \oiiint_{\mathcal{V}} \rho_{\mathbf{V}} d \mathcal{V}+\oiint_{S}(\rho \mathbf{V} \cdot \mathbf{d} \mathbf{S}) \mathbf{V}=-\oiint_{S} p \mathbf{d} \mathbf{S}+\oiiint_{\mathcal{V}} \rho \mathbf{f} d \mathcal{V}+\mathbf{F}_{\text {viscous }}$'",
            30 : "r'$\oiiint_{\mathcal{V}} \dot{q} \rho d \mathcal{V}+\dot{Q}_{\text {viscous }}-\oiint_{S} p \mathbf{V} \cdot \mathbf{d} \mathbf{S}+\oiiint_{\mathcal{V}} \rho(\mathbf{f} \cdot \mathbf{V}) d \mathcal{V}+\dot{W}_{\text {viscous }}$'",
            30 : "r'$=\frac{\partial}{\partial t} \oiiint_{\mathcal{V}} \rho\left(e+\frac{V^{2}}{2}\right) d \mathcal{V}+\oiint_{S} \rho\left(e+\frac{V^{2}}{2}\right) \mathbf{V} \cdot \mathbf{d} \mathbf{S}$'",
            23 : "r''",
            24 : "r''",
            30 : "r''",
            23 : "r''",
            24 : "r''",
            30 : "r''",
            23 : "r''",
            24 : "r''",
            30 : "r''",
            23 : "r''",
            24 : "r''",
            30 : "r''",
            23 : "r''",
            24 : "r''",
            30 : "r''",
            23 : "r''",
            24 : "r''",
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
            20 : "Lift",
            21 : "Drag",
            22 : "Divergence",
            23 : "Curl",
            24 : "Line Integral",
            25 : "Stokes' Theorem",
            26 : "Divergence Theorem",
            27 : "Gradient Theorem",
            28 : "Mass Flow",
            29 : "Mass Flux",
            30 : "Continuity Equation",
            30 : "Continuity Equation",
            30 : "Momentum Equation",
            30 : "Energy Equation",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
            30 : "",
       
        }
        
        self.des = {
                
        }
