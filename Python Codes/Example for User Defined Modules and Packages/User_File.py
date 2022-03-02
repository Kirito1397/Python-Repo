from Sample_Module import * # Imports the Sample module and it's functions.

from Package import main_package_module # Imports "main_package_module" module/file from Package directory

from Package.Sub_Package import Sub_Package_Module # Imports "Sub_Package_Module" module/file from Package>Sub_Package directory

from Package.Sub_Package_2.Sub_Package_Module_2 import sub_package_module_2 # Imports function "sub_package_module_2" from "Sub_Package_Module_2" module in Package>Sub_Package_2 directory

sample_module()
sample_module_2()

main_package_module.main_package_module()

Sub_Package_Module.sub_package_module()

sub_package_module_2()