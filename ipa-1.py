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
    


# In[17]:


def savings(gross_pay, tax_rate, expenses):
    
    take_home = (gross_pay * (1 - tax_rate)) - expenses
    return round(take_home)

    
take_home = savings(1000000, 0.10, 55930)
print(take_home)



def material_waste(total_material, material_units, num_jobs, job_consumption):
    mat_consumed = num_jobs * job_consumption
    waste = mat_consumed - total_material

    return waste, material_units

sample, unit = material_waste(10000, "kg", 3, 3929)
print(sample, unit)

def interest(principal, rate, periods):
    output = (principal * (rate * periods)) + principal
    return int(output)


sample = interest(100000, 0.03, 12)
print(sample)

def body_mass_index(weight, height):
    w_feet = height[0]
    w_inch = height[1]
    conv_w = weight * 0.453592
    conv_h = (w_feet * 0.3048) + (w_inch * 0.0254)
    
    bmi_final = conv_w / ((conv_h)**2)
    return bmi_final

sample_bmi = body_mass_index(139.5, [5, 10])
print(sample_bmi)


# In[ ]:




