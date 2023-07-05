#!/usr/bin/env python
# coding: utf-8

# In[10]:


# def savings(gross_pay, tax_rate, expenses):
    
#     take_home = (gross_pay * (1 - tax_rate)) - expenses
#     return take_home

    
# take_home = savings(1000000, 0.10, 55930)
# print(take_home)


# In[14]:


# def material_waste(total_material, material_units, num_jobs, job_consumption):
#     mat_consumed = num_jobs * job_consumption
#     waste = mat_consumed - total_material 
#     return waste

# sample = material_waste(10000, "kg", 3, 3929)
# print(sample)


# In[20]:


# def interest(principal, rate, periods):
#     output = (principal * (rate * periods)) + principal
#     round(output)
#     return output


# sample = interest(100000, 0.03, 12)
# print(sample)


# In[21]:


# def body_mass_index(weight, height):
#     w_feet = height[0]
#     w_inch = height[1]
#     conv_w = weight * 0.453592
#     conv_h = (w_feet * 0.3048) + (w_inch * 0.0254)
    
#     bmi_final = conv_w / ((conv_h)**2)
#     return bmi_final

# sample_bmi = body_mass_index(139.5, [5, 10])
# print(sample_bmi)
    


# In[2]:


# def savings(gross_pay, tax_rate, expenses):
#     '''Savings.
#     5 points.

#     This function calculates the money remaining
#         for an employee after taxes and expenses.

#     To get the take-home pay of an employee, we will
#         follow the following process:
#         1. Apply the tax rate to the gross pay of the employee; round down
#         2. Subtract the expenses from the after-tax pay of the employee

#     Parameters
#     ----------
#     gross_pay: int
#         the gross pay of an employee for a certain time period, expressed in centavos
#     tax_rate: float
#         the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
#     expenses: int
#         the expenses of an employee for a certain time period, expressed in centavos

#     Returns
#     -------
#     int
#         the number of centavos remaining from an employee's pay after taxes and expenses
#     '''
#     # Replace `pass` with your code.
#     # Stay within the function. Only use the parameters as input. The function should return your answer.

def savings(gross_pay, tax_rate, expenses):
    
    take_home = (gross_pay * (1 - tax_rate)) - expenses
    return round(take_home)

    
take_home = savings(1000000, 0.10, 55930)
print(take_home)

# def material_waste(total_material, material_units, num_jobs, job_consumption):
#     '''Material Waste.
#     5 points.

#     This function calculates how much material input will be wasted
#         after running a certain number of jobs that consume
#         a set amount of material.

#     To get the waste of a set of jobs:
#         1. Multiply the number of jobs by the material consumption per job.
#         2. Subtract the total material consumed from the total material available.

#     The users of this function also want you to format the output as a string, annotated with the
#         units in which the material is expressed. Do not add a space between the number and the unit.

#     Parameters
#     ----------
#     total_material: int
#         the total material available
#     material_units: str
#         the units used to express a quantity of the material (e.g., "kg", "L", etc.)
#     num_jobs: int
#         the number of jobs to run
#     job_consumption: int
#         the amount of material consumed per job

#     Returns
#     -------
#     str
#         the amount of remaining material expressed with its unit (e.g., "10kg").
#     '''
#     # Replace `pass` with your code.
#     # Stay within the function. Only use the parameters as input. The function should return your answer.

def material_waste(total_material, material_units, num_jobs, job_consumption):
    mat_consumed = num_jobs * job_consumption
    waste = mat_consumed - total_material 
    return waste

sample = material_waste(10000, "kg", 3, 3929)
print(sample)

# def interest(principal, rate, periods):
#     '''Interest.
#     5 points.

#     This function calculates the final value of an investment after
#         gaining simple interest over a number of periods.

#     To calculate simple interest, simply multiply the principal to the quantity (rate * time).
#         Add this amount to the principal to get the final value.

#     Round down the final amount.

#     Parameters
#     ----------
#     principal: int
#         the principal (i.e., starting) amount invested, expressed in centavos
#     rate: float
#         the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
#     periods: int
#         the number of periods invested

#     Returns
#     -------
#     int
#         the final value of the investment
#     '''
#     # Replace `pass` with your code.
#     # Stay within the function. Only use the parameters as input. The function should return your answer.
def interest(principal, rate, periods):
    output = (principal * (rate * periods)) + principal
    return round(output)


sample = interest(100000, 0.03, 12)
print(sample)

# def body_mass_index(weight, height):
#     '''Body Mass Index.
#     5 points.

#     This function calculates the body mass index (BMI) of a person
#         given their weight and height.

#     The formula for BMI is: kg / (m ^ 2)
#         (i.e., kilograms over meters squared)

#     Unfortunately, the users of this function use the imperial system.
#         You will need to first convert their arguments to the metric system.

#     Parameters
#     ----------
#     weight: float
#         the weight of the person, in pounds
#     height: list
#         the height of the person, expressed as a list of two integers.
#         the first integer is the foot component of their height.
#         the second integer is the inches component of their height.
#         for example, 5'10" would be passed as [5, 10].

#     We have not yet discussed lists, but use the skills you developed
#         in the command line exercise. How would you learn how to work with
#         lists?

#     Returns
#     -------
#     float
#         the BMI of the person.
#     '''
#     # Replace `pass` with your code.
#     # Stay within the function. Only use the parameters as input. The function should return your answer.
def body_mass_index(weight, height):
    w_feet = height[0]
    w_inch = height[1]
    conv_w = weight * 0.453592
    conv_h = (w_feet * 0.3048) + (w_inch * 0.0254)
    
    bmi_final = conv_w / ((conv_h)**2)
    return bmi_final

sample_bmi = body_mass_index(139.5, [5, 10])
print(sample_bmi)

