##############################################################################
# Identifier map. Used to lookup valid identifier names.

identifier_map = {
    # The key is the identifier name used internally by the translator and the
    # NJOY documentation. The value associated with each key is a list of
    # valid identifier names for the key.
    # If a {better,descriptive,long,...} identifier name is wanted, just add
    # it to the appropriate list. Some example names have been provided.
    'akxy' : ['akxy'], # errorr.
    'alpha2' : ['alpha2'], # groupr.
    'alpha3' : ['alpha3'], # groupr.
    'aw' : ['aw'],
    'beta' : ['beta'], # groupr.
    'cards' : ['cards'],
    'dap' : ['dap'], # errorr.
    'eb' : ['eb', 'thermal_break'], # errorr, groupr.
    'ec' : ['ec', 'fission_break'], # errorr, groupr.
    'ed' : ['ed'],
    'efmean' : ['efmean'], # errorr.
    'egg' : ['egg', 'gamma_group_breaks'], # groupr.
    'egn' : ['egn', 'neutron_group_breaks'], # errorr, groupr.
    'ehi' : ['ehi'], # groupr.
    'ek' : ['ek'], # errorr
    'emax' : ['emax'], # thermr, ...
    'enode' : ['enode'],
    'epmin' : ['epmin'], # covr, ...
    'err' : ['err'],
    'errint' : ['errint'], # broadr, XXX.
    'errmax' : ['errmax'], # broadr, XXX.
    'errthn' : ['errthn'], # broadr.
    'gamma' : ['gamma'], # groupr.
    'hdescr' : ['hdescr'], # covr.
    'hk' : ['hk', 'description'],
    'hlibid' : ['hlibid'], # covr.
    'icoh' : ['icoh'], # thermr.
    'icolor' : ['icolor'], # covr.
    'ielas' : ['ielas'],
    'ifissp' : ['ifissp'], # errorr.
    'ign' : ['ign', 'neutron_group_structure'], # errorr, groupr.
    'igg' : ['igg', 'gamma_group_structure'], # groupr.
    'iinc' : ['iinc'], # thermr.
    'infile' : ['infile', 'input'], # viewr.
    'iopt' : ['iopt', 'acer_run_option'],
    'iopp' : ['iopp'],
    'iprint' : ['iprint', 'print_control'], # errorr, groupr, thermr, ...
    'iread' : ['iread'], # errorr
    'irelco' : ['irelco'], # covr, errorr, ...
    'irespr' : ['irespr'], # errorr
    'istart' : ['istart', 'restart'], # broadr.
    'istrap' : ['istrap', 'bootstrap'], # broadr.
    'iwt' : ['iwt'], # errorr, groupr.
    'iz' : ['iz'],
    # XXX: Treat iza as an array?
    'iza01' : ['iza01'],
    'iza02' : ['iza02'],
    'iza03' : ['iza03'],
    'jsigz' : ['jsigz'], # groupr.
    'legord' : ['legord'], # errorr.
    'local' : ['local'],
    'lord' : ['lord', 'legendre_order'], # groupr.
    'mat' : ['mat'], # covr, ...
    'mat1' : ['mat1'], # broadr, covr, ...
    'matb' : ['matb'], # errorr, groupr.
    'matc' : ['matc'], # errorr
    'matd' : ['matd', 'material'], # errorr, groupr, ...
    'matde' : ['matde'], # thermr.
    'matdp' : ['matdp'], # thermr.
    'matype' : ['matype'], # covr, ...
    'mfcov' : ['mfcov'], # errorr.
    'mfd' : ['mfd'], # groupr.
    'mprint' : ['mprint'], # errorr
    'mt' : ['mt'], # covr,
    'mt1' : ['mt1'], # covr,
    'mta' : ['mta'],
    'mtb' : ['mtb'], # errorr
    'mtc' : ['mtc'], # errorr
    'mtd' : ['mtd'], # groupr.
    'mte' : ['mte'],
    'mti' : ['mti'],
    'mtk' : ['mtk'],
    'mtname' : ['mtname'], # groupr.
    'mtref' : ['mtref'], # thermr.
    'mts' : ['mts'], # errorr
    'nace' : ['nace', 'ace_output'],
    'natom' : ['natom'], # thermr.
    'nbin' : ['nbin'], # thermr.
    'nbint' : ['nbint'],
    'ncards' : ['ncards'],
    'ncase' : ['ncase'], # covr, ...
    'ndir' : ['ndir', 'mcnp_directory_output'],
    'ndiv' : ['ndiv'], # covr, ...
    'nek' : ['nek'], # errorr, ...
    'nendf' : ['nendf', 'endf_input'],
    'newfor' : ['newfor'],
    'nflmax' : ['nflmax', 'max_flux_points'], # groupr.
    'ngend' : ['ngend', 'multigroup_photon_input'],
    'ngg' : ['ngg', 'number_of_gamma_groups'], # groupr.
    'ngn' : ['ngn', 'number_of_neutron_groups'], # errorr, groupr.
    'ngrid' : ['ngrid'],
    'ngout' : ['ngout', 'group_xsec_input'], # errorr.
    'ngout1' : ['ngout1', 'gout_input'], # groupr.
    'ngout2' : ['ngout2', 'gout_output'], # groupr.
    'nin' : ['nin', 'pendf_input'], # covr, ...
    'ninwt' : ['ninwt'], # groupr.
    'nmix' : ['nmix'],
    'nmt' : ['nmt'], # errorr
    'ntemp' : ['ntemp', 'number_of_temperatures'], # groupr, thermr, ...
    'ntemp2' : ['ntemp2', 'number_of_final_temperatures'], # broadr.
    'ntype' : ['ntype', 'ace_output_type'],
    'noleg' : ['noleg'], # covr, ...
    'nout' : ['nout', 'pendf_output'], # covr, errorr, ...
    'npend' : ['npend', 'pendf_input'],
    'npk' : ['npk', 'number_of_partial_kermas'],
    'nplot' : ['nplot'], # covr, ...
    'nps' : ['nps', 'output'], # viewr.
    'nqa' : ['nqa', 'number_of_q_values'],
    'nsigz' : ['nsigz', 'number_of_sigma_zeroes'], # groupr.
    'nstan' : ['nstan'], # errorr
    'nstart' : ['nstart'], # covr, ...
    'nxtra' : ['nxtra'],
    'qa' : ['qa'],
    'qbar' : ['qbar'],
    'sam' : ['sam'],
    'sigpot' : ['sigpot'], # groupr.
    'sigz' : ['sigz', 'sigma_zero_values'], # groupr.
    'suff' : ['suff'],
    'tb' : ['tb', 'thermal_temperature'], # errorr, groupr.
    'tc' : ['tc', 'fission_temperature'], # errorr, groupr.
    'temp' : ['temp', 'temperature'], # groupr.
    'temp1' : ['temp1', 'start_temp'], # broadr. 
    'temp2' : ['temp2', 'final_temp'], # broadr.
    'tempd' : ['tempd', 'temperature'],
    'tempin' : ['tempin'], # errorr.
    'tempr' : ['tempr', 'temperature'], # thermr, ...
    # XXX: Treat thin as an array?
    'thin01' : ['thin01'],
    'thin02' : ['thin02'],
    'thin03' : ['thin03'],
    'thnmax' : ['thnmax'], # broadr.
    'title' : ['title'], # groupr.
    'tlabel' : ['tlabel'],
    'tname' : ['tname'],
    'tol' : ['tol', 'tolerance'], # thermr.
    'wght' : ['wght'], # errorr, groupr.
}
