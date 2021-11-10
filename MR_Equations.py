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
            1 : r'$\overline{v} = \frac{\Delta s}{\Delta t}$',
            2 : r'$\overline{a} = \frac{\Delta v}{\Delta t}$',
            3 : r'$\Sigma F = ma$',
            4 : r'$W = mg$',
            5 : r'$f_s \leq \mu_s N$',
            6 : r'$f_k = \mu_k N$',
            7 : r'$a_c = \frac{v^2}{r}$',
            8 : r'$a_c = - \omega^2 r$',
            9 : r'$p = mv$',
            10 : r'$J = \Delta p$',
            11 : r'$F dt = \int F dt$',
            12 : r'$W = \int F \cdot ds$',
            13 : r'$\int F \cdot ds = \Delta E$',
            14 : r'$K = \frac{1}{2} m v^2$',
            15 : r'$K = \frac{p^2}{2m}$',
            16 : r'$F = - \nabla U$',
        }

        self.names = {
            1: "Velocity",
            2 : "Acceleration",
            3 : "Newton's Second Law",
            4 : "Weight",
            5 : "Static Friction",
            6 : "Kinetic Friction",
            7 : "Centripetal Acceleration",
            8 : "Centripetal Acceleration",
            9 : "Momentum",
            10 : "Impulse",
            11 : "Impulse-Momentum",
            12 : "Work",
            13 : "Work-Energy",
            14 : "Kinetic Energy", 
            15 : "Kinetic Energy", 
            16 : "General Potential Energy", 
        }

        self.des = {
            
        }
