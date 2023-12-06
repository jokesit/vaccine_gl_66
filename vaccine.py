
#check condition
age = 45
gender_is_male = False #true is men / false is female


pregnancy =False
health_care_personel = False
heart_or_diabetes_or_lung_disease = False
chronic_kidney_disease = False
chronic_liver_disease = False
asplenia =False
hiv_with_high_cd4_200 = False
hiv_with_low_cd4_200 = False
immunocompromising_condition = False
solid_organ_transplantation = False
hematopoietic_stem_cell_transplantation = False
traveller = False


# vaccine name
td_vaccine='วัคซีนบาดทะยักคอตีบ'
influ_vaccine='วัคซีนป้องกันไข้หวัดใหญ่'
mmr_vaccine = 'วัคซีนป้องกันหัด หัดเยอรมัน คางทูม'
varicella_vaccine = 'วัคซีนป้องกันอีสุกอีใส'
hpv_vaccine = 'วัคซีนป้องกัน เอชพีวี'
hep_b_vaccine = 'วัคซีนป้องกันไวรัสตับอักเสบบี'
hep_a_vaccine = 'วัคซีนป้องกันไวรัสตับอักเสบเอ'
pneumo_vaccine = 'วัคซีนป้องกันนิวโมคอคคัส'
zoster_recombinant_vaccine = 'วัคซีนป้องกันงูสวัด ชนิด recombinant'
zoster_live_vaccine = 'วัคซีนป้องกันงูสวัด ชนิดเชื้อเป็น'
je_vaccine = 'วัคซีนป้องกันไข้สมองอักเสบ เจอี'
tdap_vaccine = 'วัคซีนบาดทะยัก คอตีบ ไอกรน'
dengue_chimeric_vaccine = 'วัคซีนป้องกันโรคไข้เลือดออก ชนิด chimeric'
dengue_2_vaccine = 'วัคซีนป้องกันโรคไข้เลือดออก ชนิด dengue2'
meningo_vaccine = 'วัคซีนป้องกันโรคไข้กาฬหลังแอ่น'
yellow_vaccine = 'วัคซีนป้องกันไข้เหลือง'
rabie_vaccine = 'วัคซีนพิษสุนัขบ้า'
typhoid_vaccine='วัคซีนไทฟอยด์'
cholera_vaccine ='วัคซีนป้องกันอหิวาตกโรค'


# age 1 18-26
age_1_main_vaccine = [td_vaccine,influ_vaccine,mmr_vaccine,
                      varicella_vaccine,hpv_vaccine,hep_b_vaccine] # gender is female
age_1_with_risk_vaccine =[hep_a_vaccine,pneumo_vaccine,
                          zoster_recombinant_vaccine,je_vaccine]
age_1_option_vaccine = [tdap_vaccine,hpv_vaccine,
                        dengue_chimeric_vaccine,dengue_2_vaccine] # tdap 1 time sub / hpv if male

# age 2 27-64
age_2_main_vaccine=[td_vaccine,influ_vaccine,mmr_vaccine,
                    varicella_vaccine,hep_b_vaccine] #all same
age_2_with_risk_vaccine=[hep_a_vaccine,pneumo_vaccine,
                         zoster_recombinant_vaccine,je_vaccine] #zrv to 49
age_2_option_vaccine=[tdap_vaccine,dengue_chimeric_vaccine,
                      dengue_2_vaccine,zoster_recombinant_vaccine,zoster_live_vaccine]  
age_2_with_share_clinical =[hpv_vaccine] #all same

age_26_to_45_option_vaccine =[tdap_vaccine,dengue_chimeric_vaccine,
                            dengue_2_vaccine,]
age_26_to_45_with_risk_vaccine =[hep_a_vaccine,pneumo_vaccine,
                         zoster_recombinant_vaccine,je_vaccine,]

age_45_to_49_option_vaccine =[tdap_vaccine,dengue_2_vaccine,]
age_45_to_49_with_risk_vaccine =[hep_a_vaccine,pneumo_vaccine,
                         zoster_recombinant_vaccine,je_vaccine,]

age_50_to_59_option_vaccine =[tdap_vaccine,dengue_2_vaccine,
                              zoster_recombinant_vaccine]
age_50_to_59_with_risk_vaccine =[hep_a_vaccine,pneumo_vaccine,je_vaccine,]

age_60_option_vaccine=[tdap_vaccine,dengue_2_vaccine,
                              zoster_recombinant_vaccine,zoster_live_vaccine]
age_60_with_risk_vaccine = [hep_a_vaccine,pneumo_vaccine,je_vaccine,]

age_61_to_64_option_vaccine =[tdap_vaccine,zoster_recombinant_vaccine,
                              zoster_live_vaccine]
age_61_to_64_with_risk_vaccine =[hep_a_vaccine,pneumo_vaccine,je_vaccine,]





# age 3 65 up
age_3_main_vaccine=[td_vaccine,influ_vaccine,mmr_vaccine,
                    varicella_vaccine,hep_b_vaccine,pneumo_vaccine]
age_3_with_risk_vaccine=[hep_a_vaccine,je_vaccine]
age_3_option_vaccine=[tdap_vaccine,zoster_live_vaccine,
                      zoster_recombinant_vaccine]
age_3_with_share_clinical =[hpv_vaccine] #same with age 2








# check avoid vaccine by risk factorfunction
def contraindicated_by_factor_vaccine(pregnancy ,
                                    hiv_with_low_cd4_200,
                                    immunocompromising_condition ,
                                    solid_organ_transplantation,
                                    hematopoietic_stem_cell_transplantation,
                                    ) :
    contraindicated_vaccine =[]
    # if age >= 18 and age <= 26 :
    if pregnancy :
        contraindicated_vaccine_for_pregnancy = [mmr_vaccine,varicella_vaccine,
                                                hpv_vaccine,dengue_2_vaccine,dengue_chimeric_vaccine,
                                                zoster_live_vaccine,zoster_recombinant_vaccine,je_vaccine,
                                                yellow_vaccine]
        contraindicated_vaccine.extend(contraindicated_vaccine_for_pregnancy)
        
        # print(f'avoid for pregnancy : {contraindicated_vaccine}')
    else :
        pass
    if hiv_with_low_cd4_200 :
        contraindicated_vaccine_for_low_cd4_200 = [dengue_2_vaccine,dengue_chimeric_vaccine,
                                                zoster_live_vaccine,je_vaccine,yellow_vaccine,]
                                                
        for item in contraindicated_vaccine_for_low_cd4_200 :
            if item not in contraindicated_vaccine :
                contraindicated_vaccine.append(item)
            else :
                pass

        # print(f'avoid for low cd4 : {contraindicated_vaccine}')
        
    if immunocompromising_condition :
        contraindicated_vaccine_immunocompromising_condition = [mmr_vaccine,varicella_vaccine,
                                                                dengue_2_vaccine,dengue_chimeric_vaccine,
                                                                zoster_live_vaccine,je_vaccine,yellow_vaccine]
        for item in contraindicated_vaccine_immunocompromising_condition :
            if item not in contraindicated_vaccine :
                contraindicated_vaccine.append(item)
            else :
                pass

        # print(f'avoid for imunocompromised : {contraindicated_vaccine}')
        
    if solid_organ_transplantation : 
        contraindicated_vaccine_solid_organ_transplantation =[mmr_vaccine,varicella_vaccine,dengue_2_vaccine,
                                                            dengue_chimeric_vaccine,zoster_live_vaccine,
                                                            je_vaccine,yellow_vaccine]
        for item in contraindicated_vaccine_solid_organ_transplantation :
            if item not in contraindicated_vaccine :
                contraindicated_vaccine.append(item)
            else :
                pass
        # print(f'avoid for SOT :{contraindicated_vaccine}')
        
    if hematopoietic_stem_cell_transplantation : 
        contraindicated_vaccine_hematopoietic_stem_cell_transplantation =[dengue_2_vaccine,
                                                            dengue_chimeric_vaccine,zoster_live_vaccine,
                                                            je_vaccine,yellow_vaccine]
        for item in contraindicated_vaccine_hematopoietic_stem_cell_transplantation :
            if item not in contraindicated_vaccine :
                contraindicated_vaccine.append(item)
            else :
                pass
        # print(f'avoid for HSCT : {contraindicated_vaccine}')
    return contraindicated_vaccine
   

a = contraindicated_by_factor_vaccine(pregnancy=True,
                                      hiv_with_low_cd4_200=False,
                                      immunocompromising_condition=False,
                                      solid_organ_transplantation=False,
                                      hematopoietic_stem_cell_transplantation=False)
    
print(a)
# create function check main vaccine
def main_vaccine_all_age(age,gender_is_male) :
    all_main_vaccine = []
    if age >= 18 and age <= 26 and  gender_is_male==True:
        
        age_1_main_vaccine.remove(hpv_vaccine)
        all_main_vaccine.extend(age_1_main_vaccine)
        return all_main_vaccine
            # print(f'option{age_1_option_vaccine}')
    elif age >= 18 and age <= 26 and  gender_is_male==False :
        age_1_main_vaccine
        all_main_vaccine.extend(age_1_main_vaccine)
        return all_main_vaccine
    elif age > 26 and age <= 64 :
        age_2_main_vaccine
        all_main_vaccine.extend(age_2_main_vaccine)
        return all_main_vaccine
        
    elif age > 64 :
        age_3_main_vaccine
        all_main_vaccine.extend(age_3_main_vaccine)
        return all_main_vaccine
    

# create function check optional vaccine
def option_vaccine_all_age(age,gender_is_male) :
    all_option_vaccine =[]
    if age >= 18 and age <= 26 and gender_is_male==True :
        all_option_vaccine.extend(age_1_option_vaccine)
        return all_option_vaccine
    elif age >= 18 and age <= 26 and gender_is_male==False :  
        age_1_option_vaccine.remove(hpv_vaccine)
        all_option_vaccine.extend(age_1_option_vaccine)
        return all_option_vaccine
    elif age > 26 and age <= 45 :
        all_option_vaccine.extend(age_26_to_45_option_vaccine)
        return all_option_vaccine
    elif age > 45 and age <= 49 :
        all_option_vaccine.extend(age_45_to_49_option_vaccine)
        return all_option_vaccine
    elif age >49 and age < 60 :
        all_option_vaccine.extend(age_50_to_59_option_vaccine)
        return all_option_vaccine
    elif age >= 50 and age < 59 :
        all_option_vaccine.extend(age_50_to_59_option_vaccine)
        return all_option_vaccine
    elif age == 60 :
        all_option_vaccine.extend(age_60_option_vaccine)
        return all_option_vaccine
    elif age > 60 and age <=  64 :
        all_option_vaccine.extend(age_61_to_64_option_vaccine)
        return all_option_vaccine
    elif age > 64 :
        all_option_vaccine.extend(age_3_option_vaccine)
        return all_option_vaccine




# create function check additional risk factor vaccine
def additional_risk_factor_vaccine(age) :
    all_with_risk_vaccine = []
    if age >= 18 and age <= 26 :
        all_with_risk_vaccine.extend(age_1_with_risk_vaccine)
        return all_with_risk_vaccine
    elif age > 26 and age <= 64 :
        if age < 50 :
            all_with_risk_vaccine.extend(age_2_with_risk_vaccine)
            return all_with_risk_vaccine
        if age >= 50 and age <= 64 :
            age_2_with_risk_vaccine.remove(zoster_recombinant_vaccine)
            all_with_risk_vaccine.extend(age_2_with_risk_vaccine)
            return all_with_risk_vaccine
    elif age > 64 :
        all_with_risk_vaccine.extend(age_3_with_risk_vaccine)
        return all_with_risk_vaccine 



# create function check share clinical vaccine
def share_clinical_vaccine(age):
    all_share_clinical_vaccine = []
    if age >26 :
        all_share_clinical_vaccine.extend(age_2_with_share_clinical)

    



# check for remove contraindicated vaccine
'''
main_vaccine = ['a', 'b', 'c', 'd', 'e']
contraindicated_vaccine = ['b', 'c']

result = [item for item in main_vaccine if item not in contraindicated_vaccine]

print(result)

or

a = ['a', 'b', 'c', 'd', 'e']
b = ['b', 'c']

result = list(filter(lambda x: x not in b, a))

print(result)


'''