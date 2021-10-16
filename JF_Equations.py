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
            
            r'$\tau = \mu \frac{dV}{dy}$'
            r'$L = N\mathrm{cos}\alpha - A\mathrm{sin}\alpha$'
            r'$D = N\mathrm{sin}\alpha + A\mathrm{cos}\alpha$'
            r'$q = \frac{1}{2}\rhoV^{2}$'
            r'$dp = -g \rho dy$'
            
        }

        self.names = {
            
            "Shear Stress",
            "Lift",
            "Drag",
            "Dynamic Pressure",
            "Hydrostatic Equation"
            
        }
