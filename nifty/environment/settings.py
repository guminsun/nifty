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
    'emax' : ['emax'],
    'enode' : ['enode'],
    'err' : ['err'],
    'errint' : ['errint'],
    'errmax' : ['errmax'],
    'gamma' : ['gamma'], # Used by groupr.
    'hk' : ['hk'],
    'ielas' : ['ielas'],
    'ign' : ['ign', 'neutron_group_structure'], # Used by groupr.
    'igg' : ['igg', 'gamma_group_structure'], # Used by groupr.
    'iopt' : ['iopt'],
    'iopp' : ['iopp'],
    'iprint' : ['iprint'], # Used by groupr.
    'iwt' : ['iwt'], # Used by groupr.
    'iz' : ['iz'],
    # XXX: Treat iza as an array?
    'iza01' : ['iza01'],
    'iza02' : ['iza02'],
    'iza03' : ['iza03'],
    'jsigz' : ['jsigz'], # Used by groupr.
    'local' : ['local'],
    'lord' : ['lord', 'legendre_order'], # Used by groupr. 
    # XXX: Use a single name to indicate material?
    'mat' : ['mat', 'matd'],
    'matb' : ['matb'], # Used by groupr.
    'matd' : ['matd', 'mat', 'material'], # Used by groupr.
    'mfd' : ['mfd'], # Used by groupr.
    'mta' : ['mta'],
    'mtd' : ['mtd'], # Used by groupr.
    'mte' : ['mte'],
    'mti' : ['mti'],
    'mtk' : ['mtk'],
    'mtname' : ['mtname'], # Used by groupr.
    'nace' : ['nace'],
    'nin' : ['nin', 'pendf_input'],
    'nbint' : ['nbint'],
    'ncards' : ['ncards'],
    'ndir' : ['ndir'],
    'nendf' : ['nendf', 'endf_input'],
    'newfor' : ['newfor'],
    'nflmax' : ['nflmax', 'max_flux_points'], # Used by groupr.
    'ngend' : ['ngend'],
    'ngg' : ['ngg', 'number_of_gamma_groups'], # Used by groupr.
    'ngn' : ['ngn', 'number_of_neutron_groups'], # Used by groupr.
    'ngrid' : ['ngrid'],
    'ngout1' : ['ngout1', 'gout_input'], # Used by groupr.
    'ngout2' : ['ngout2', 'gout_output'], # Used by groupr.
    'ninwt' : ['ninwt'], # Used by groupr.
    'nmix' : ['nmix'],
    'ntemp' : ['ntemp', 'number_of_temperatures'], # Used by groupr.
    'ntype' : ['ntype'],
    'nout' : ['nout', 'pendf_output'],
    'npend' : ['npend', 'pendf_input'],
    'npk' : ['npk', 'number_of_partial_kermas'],
    'nplot' : ['nplot'],
    'nqa' : ['nqa', 'number_of_q_values'],
    'nsigz' : ['nsigz', 'number_of_sigma_zeroes'], # Used by groupr.
    'nxtra' : ['nxtra'],
    'qa' : ['qa'],
    'qbar' : ['qbar'],
    'sam' : ['sam'],
    'sigpot' : ['sigpot'], # Used by groupr.
    'sigz' : ['sigz', 'sigma_zero_values'], # Used by groupr.
    'suff' : ['suff'],
    # XXX: Use a single name to denote temperatures in kelvin?
    'tb' : ['tb', 'thermal_temperature'], # Used by groupr.
    'tc' : ['tc', 'fission_temperature'], # Used by groupr.
    'temp' : ['temp'], # Used by groupr.
    'tempd' : ['tempd'],
    'tempr' : ['tempr'],
    # XXX: Treat thin as an array?
    'thin01' : ['thin01'],
    'thin02' : ['thin02'],
    'thin03' : ['thin03'],
    # XXX: Use a single name to denote labels and titles?
    'title' : ['title'], # Used by groupr.
    'tlabel' : ['tlabel'],
    'tname' : ['tname'],
    'wght' : ['wght'], # Used by groupr.
}
