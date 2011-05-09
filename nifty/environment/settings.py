##############################################################################
# Identifier map. Used to lookup valid identifier names.

identifier_map = {
    # The key is the identifier name used internally by the translator and the
    # NJOY documentation. The value associated with each key is a list of
    # valid identifier names for the key.
    # If a {better,descriptive,long,...} identifier name is wanted, just add
    # it to the appropriate list. Some example names have been provided.
    'alpha2' : ['alpha2'], # Used by groupr.
    'alpha3' : ['alpha3'], # Used by groupr.
    'aw' : ['aw'],
    'beta' : ['beta'], # Used by groupr.
    'cards' : ['cards'],
    'eb' : ['eb', 'thermal_break'], # Used by groupr.
    'ec' : ['ec', 'fission_break'], # Used by groupr.
    'ed' : ['ed'],
    'egg' : ['egg', 'gamma_group_breaks'], # Used by groupr.
    'egn' : ['egn', 'neutron_group_breaks'], # Used by groupr.
    'ehi' : ['ehi'], # Used by groupr.
    'emax' : ['emax'], # Used by thermr, ...
    'enode' : ['enode'],
    'epmin' : ['epmin'], # Used by covr, ...
    'err' : ['err'],
    'errint' : ['errint'], # Used by broadr, XXX.
    'errmax' : ['errmax'], # Used by broadr, XXX.
    'errthn' : ['errthn'], # Used by broadr.
    'gamma' : ['gamma'], # Used by groupr.
    'hdescr' : ['hdescr'], # Used by covr.
    'hk' : ['hk', 'description'],
    'hlibid' : ['hlibid'], # Used by covr.
    'icoh' : ['icoh'], # Used by thermr.
    'icolor' : ['icolor'], # Used by covr.
    'ielas' : ['ielas'],
    'ign' : ['ign', 'neutron_group_structure'], # Used by groupr.
    'igg' : ['igg', 'gamma_group_structure'], # Used by groupr.
    'iinc' : ['iinc'], # Used by thermr.
    'infile' : ['infile', 'input'], # Used by viewr.
    'iopt' : ['iopt', 'acer_run_option'],
    'iopp' : ['iopp'],
    'iprint' : ['iprint', 'print_control'], # Used by groupr, thermr, ...
    'irelco' : ['irelco'], # Used by covr, ...
    'istart' : ['istart', 'restart'], # Used by broadr.
    'istrap' : ['istrap', 'bootstrap'], # Used by broadr.
    'iwt' : ['iwt'], # Used by groupr.
    'iz' : ['iz'],
    # XXX: Treat iza as an array?
    'iza01' : ['iza01'],
    'iza02' : ['iza02'],
    'iza03' : ['iza03'],
    'jsigz' : ['jsigz'], # Used by groupr.
    'local' : ['local'],
    'lord' : ['lord', 'legendre_order'], # Used by groupr.
    'mat' : ['mat'], # Used by covr, ...
    'mat1' : ['mat1'], # Used by broadr, covr, ...
    'matb' : ['matb'], # Used by groupr.
    'matd' : ['matd', 'material'], # Used by groupr.
    'matde' : ['matde'], # Used by thermr.
    'matdp' : ['matdp'], # Used by thermr.
    'matype' : ['matype'], # Used by covr, ...
    'mfd' : ['mfd'], # Used by groupr.
    'mt' : ['mt'], # Used by covr,
    'mt1' : ['mt1'], # Used by covr,
    'mta' : ['mta'],
    'mtd' : ['mtd'], # Used by groupr.
    'mte' : ['mte'],
    'mti' : ['mti'],
    'mtk' : ['mtk'],
    'mtname' : ['mtname'], # Used by groupr.
    'mtref' : ['mtref'], # Used by thermr.
    'nace' : ['nace', 'ace_output'],
    'natom' : ['natom'], # Used by thermr.
    'nin' : ['nin', 'pendf_input'], # Used by covr, ...
    'nbin' : ['nbin'], # Used by thermr.
    'nbint' : ['nbint'],
    'ncards' : ['ncards'],
    'ncase' : ['ncase'], # Used by covr, ...
    'ndir' : ['ndir', 'mcnp_directory_output'],
    'ndiv' : ['ndiv'], # Used by covr, ...
    'nendf' : ['nendf', 'endf_input'],
    'newfor' : ['newfor'],
    'nflmax' : ['nflmax', 'max_flux_points'], # Used by groupr.
    'ngend' : ['ngend', 'multigroup_photon_input'],
    'ngg' : ['ngg', 'number_of_gamma_groups'], # Used by groupr.
    'ngn' : ['ngn', 'number_of_neutron_groups'], # Used by groupr.
    'ngrid' : ['ngrid'],
    'ngout1' : ['ngout1', 'gout_input'], # Used by groupr.
    'ngout2' : ['ngout2', 'gout_output'], # Used by groupr.
    'ninwt' : ['ninwt'], # Used by groupr.
    'nmix' : ['nmix'],
    'ntemp' : ['ntemp', 'number_of_temperatures'], # Used by groupr, thermr, ...
    'ntemp2' : ['ntemp2', 'number_of_final_temperatures'], # Used by broadr.
    'ntype' : ['ntype', 'ace_output_type'],
    'noleg' : ['noleg'], # Used by covr, ...
    'nout' : ['nout', 'pendf_output'], # Used by covr, ...
    'npend' : ['npend', 'pendf_input'],
    'npk' : ['npk', 'number_of_partial_kermas'],
    'nplot' : ['nplot'], # Used by covr, ...
    'nps' : ['nps', 'output'], # Used by viewr.
    'nqa' : ['nqa', 'number_of_q_values'],
    'nsigz' : ['nsigz', 'number_of_sigma_zeroes'], # Used by groupr.
    'nstart' : ['nstart'], # Used by covr, ...
    'nxtra' : ['nxtra'],
    'qa' : ['qa'],
    'qbar' : ['qbar'],
    'sam' : ['sam'],
    'sigpot' : ['sigpot'], # Used by groupr.
    'sigz' : ['sigz', 'sigma_zero_values'], # Used by groupr.
    'suff' : ['suff'],
    'tb' : ['tb', 'thermal_temperature'], # Used by groupr.
    'tc' : ['tc', 'fission_temperature'], # Used by groupr.
    'temp' : ['temp', 'temperature'], # Used by groupr.
    'temp1' : ['temp1', 'start_temp'], # Used by broadr. 
    'temp2' : ['temp2', 'final_temp'], # Used by broadr.
    'tempd' : ['tempd', 'temperature'],
    'tempr' : ['tempr', 'temperature'], # Used by thermr, ...
    # XXX: Treat thin as an array?
    'thin01' : ['thin01'],
    'thin02' : ['thin02'],
    'thin03' : ['thin03'],
    'thnmax' : ['thnmax'], # Used by broadr.
    'title' : ['title'], # Used by groupr.
    'tlabel' : ['tlabel'],
    'tname' : ['tname'],
    'tol' : ['tol', 'tolerance'], # Used by thermr.
    'wght' : ['wght'], # Used by groupr.
}
