import os
repo_path='~/(^.*schumacher--ppartl)/'
cur_path='getcwd'
outpath=repo_path
yaml_default=repo_path+'/sv_packs/tb/common/yamls/uvmf'
yaml_path=yaml_default
scripts=os.environ.get('UVMF_HOME')+"scripts/yaml2uvmf.py"
module_name=''
m_path=''
merge_option=''
tmpl_option=''
tmpl_path=''
uvmf_cmd=''
no_copy=True
no_code_gen=True
gen_only=True
#check moudle nmae ext
#check outpath
yaml_list=[module_name+"_in_interface.yaml",
           module_name+"_out_interface.yaml",
           module_name+"_util_comp_alu_predictor.yaml",
           module_name+"_environment.yaml",
           module_name+"_bench.yaml",
          ]
##check if all require yaml fiels exits
def get_yaml_list(yaml_path):
    pass
#check if uvmf codes in repo,
#if so mergr with exitsing codes
dst_path='out_path/sv_packs/tb'
dst_lib='st_path/uvc_lib'
dst_env='dst_path/uvm'+module_name
dst_tc='dst_path/uvm'+module_name+"tests/testcases"
dst_seq='dst_path/uvm'+module_name+"tests/sequences"
dst_tb='repo_path/units/'+module_name+'/src/tb'
uvmf_intf='/verification_ip/interface_packages'
uvmf_env='verification_ip/environment_packages'
uvmf_test='project_benches'+module_name+"tb/sequnces"
#mergesource