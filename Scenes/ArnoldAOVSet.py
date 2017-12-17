import mtoa.aovs as aovs

# Create AOV
aovs.AOVInterface().addAOV('N', aovType='float')
aovs.AOVInterface().addAOV('P', aovType='float' outputs='defaultArnoldFilter')
aovs.AOVInterface().addAOV('Z', aovType='float')

aovs.AOVInterface().addAOV('diffuse_color', aovType='float')
aovs.AOVInterface().addAOV('direct_backlight', aovType='float')
aovs.AOVInterface().addAOV('direct_diffuse', aovType='float')
aovs.AOVInterface().addAOV('direct_diffuse_raw', aovType='float')
aovs.AOVInterface().addAOV('direct_specular', aovType='float')
aovs.AOVInterface().addAOV('direct_specular_2', aovType='float')
aovs.AOVInterface().addAOV('indirect_backlight', aovType='float')
aovs.AOVInterface().addAOV('indirect_diffuse', aovType='float')
aovs.AOVInterface().addAOV('indirect_diffuse_raw', aovType='float')
aovs.AOVInterface().addAOV('indirect_specular', aovType='float')
aovs.AOVInterface().addAOV('indirect_specular_2', aovType='float')
aovs.AOVInterface().addAOV('refraction', aovType='float')
aovs.AOVInterface().addAOV('single_scatter', aovType='float')
aovs.AOVInterface().addAOV('sss', aovType='float')
aovs.AOVInterface().addAOV('uv', aovType='float')
aovs.AOVInterface().addAOV('emission', aovType='float')

aovs.AOVInterface().addAOV('id_1', aovType='float')
aovs.AOVInterface().addAOV('id_2', aovType='float')
aovs.AOVInterface().addAOV('id_3', aovType='float')
aovs.AOVInterface().addAOV('id_4', aovType='float')
aovs.AOVInterface().addAOV('id_5', aovType='float')

# List all AOVs with their names
print(aovs.AOVInterface().getAOVNodes(names=True))