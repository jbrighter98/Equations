# Equations

Write your equations using MathTex Markup language in your designated python files.
https://matplotlib.org/stable/tutorials/text/mathtext.html

write them in this format:

### variable = r'$z=\frac{x}{y^2}$'


which would look like

![image](https://user-images.githubusercontent.com/44352550/137235995-f5352c10-75e5-4d07-a806-d2aecc7a1dc6.png)

Write equations like this inside braces of self.equations

   1 : r'$___INSERT FORMATTED EQUATION HERE___$',
   2 : r'$___INSERT FORMATTED EQUATION HERE___$',
   ...
 
Write the name of the equation coresponding to the same number

   1 : "Name of Equation 1", 
   2 : "Name of Equation 2",
   ...

DON'T FORGET COMMAS!!!
THE LAST ONE IN THE LISTS DON'T GET COMMAS
