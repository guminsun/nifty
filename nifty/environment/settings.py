##############################################################################
# Identifier map. Used to lookup valid identifier names.

identifier_map = {
    # The key is the identifier name used internally by the translator and the
    # NJOY documentation. The value associated with each key is a list of
    # valid identifier names for the key.
    # If a {better,descriptive,long,...} identifier name is wanted, just add
    # it to the appropriate list. Some example names have been provided.
    'akxy' : ['akxy'], # errorr.
    'aleg' : ['aleg'], # plotr, viewr
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
    'egg' : ['egg', 'gamma_group_breaks'], # gaminr, groupr.
    'egn' : ['egn', 'neutron_group_breaks'], # errorr, groupr.
    'eh' : ['eh'], # plotr
    'ehi' : ['ehi'], # groupr.
    'ek' : ['ek'], # errorr
    'el' : ['el'], # plotr
    'emax' : ['emax'], # thermr, ...
    'enode' : ['enode'],
    'epmin' : ['epmin'], # covr, ...
    'err' : ['err'],
    'errint' : ['errint'], # broadr, XXX.
    'errmax' : ['errmax'], # broadr, XXX.
    'errthn' : ['errthn'], # broadr.
    'factx' : ['factx'], # plotr
    'facty' : ['facty'], # plotr
    'gamma' : ['gamma'], # groupr.
    'hdescr' : ['hdescr'], # covr.
    'hk' : ['hk', 'description'],
    'hlibid' : ['hlibid'], # covr.
    'iccol' : ['iccol'], # plotr, viewr
    'icoh' : ['icoh'], # thermr.
    'icolor' : ['icolor'], # covr.
    'icon' : ['icon'], # plotr, viewr
    'idash' : ['idash'], # plotr, viewr
    'ielas' : ['ielas'],
    'ifissp' : ['ifissp'], # errorr.
    'ign' : ['ign', 'neutron_group_structure'], # errorr, groupr.
    'igg' : ['igg', 'gamma_group_structure'], # gaminr, groupr.
    'igrid' : ['igrid'], # plotr, viewr
    'iinc' : ['iinc'], # thermr.
    'ileg' : ['ileg'], # plotr, viewr
    'infile' : ['infile', 'input'], # viewr.
    'iopt' : ['iopt', 'acer_run_option'],
    'iopp' : ['iopp'],
    'iplot' : ['iplot'], # plotr, viewr
    'ipcol' : ['ipcol'], # plotr
    'iprint' : ['iprint', 'print_control'], # errorr, groupr, thermr, ...
    'iread' : ['iread'], # errorr
    'irelco' : ['irelco'], # covr, errorr, ...
    'irespr' : ['irespr'], # errorr
    'ishade' : ['ishade'], # plotr, viewr
    'istart' : ['istart', 'restart'], # broadr.
    'istyle' : ['istyle'], # plotr
    'istrap' : ['istrap', 'bootstrap'], # broadr.
    'isym' : ['isym'], # plotr, viewr
    'ithick' : ['ithick'], # plotr, viewr
    'itype' : ['itype'], # plotr, viewr
    'iverf' : ['iverf'], # plotr
    'iwcol' : ['iwcol'], # plotr, viewr
    'iwt' : ['iwt'], # errorr, gaminr, groupr.
    'iz' : ['iz'],
    # XXX: Treat iza as an array?
    'iza01' : ['iza01'],
    'iza02' : ['iza02'],
    'iza03' : ['iza03'],
    'jsigz' : ['jsigz'], # groupr.
    'jtype' : ['jtype'], # plotr, viewr
    'legord' : ['legord'], # errorr.
    'local' : ['local'],
    'lord' : ['lord', 'legendre_order'], # gaminr, groupr.
    'lori' : ['lori'], # plotr
    'mat' : ['mat'], # covr, ...
    'mat1' : ['mat1'], # broadr, covr, ...
    'matb' : ['matb'], # errorr, gaminr, groupr.
    'matc' : ['matc'], # errorr
    'matd' : ['matd', 'material'], # errorr, groupr, ...
    'matde' : ['matde'], # thermr.
    'matdp' : ['matdp'], # thermr.
    'matype' : ['matype'], # covr, ...
    'mfcov' : ['mfcov'], # errorr.
    'mfd' : ['mfd'], # gaminr, groupr, plotr
    'mprint' : ['mprint'], # errorr
    'mt' : ['mt'], # covr,
    'mt1' : ['mt1'], # covr,
    'mta' : ['mta'],
    'mtb' : ['mtb'], # errorr
    'mtc' : ['mtc'], # errorr
    'mtd' : ['mtd'], # gaminr, groupr, plotr
    'mte' : ['mte'],
    'mti' : ['mti'],
    'mtk' : ['mtk'],
    'mtname' : ['mtname'], # gaminr, groupr.
    'mtref' : ['mtref'], # thermr.
    'mts' : ['mts'], # errorr
    'nace' : ['nace', 'ace_output'],
    'natom' : ['natom'], # thermr.
    'nbin' : ['nbin'], # thermr, purr.
    'nbint' : ['nbint'],
    'ncards' : ['ncards'],
    'ncase' : ['ncase'], # covr, ...
    'ndir' : ['ndir', 'mcnp_directory_output'],
    'ndiv' : ['ndiv'], # covr, ...
    'nek' : ['nek'], # errorr, ...
    'nendf' : ['nendf', 'endf_input'],
    'newfor' : ['newfor'],
    'nflmax' : ['nflmax', 'max_flux_points'], # groupr.
    'nform' : ['nform'], # plotr, viewr
    'ngam1' : ['ngam1'], # gaminr.
    'ngam2' : ['ngam2'], # gaminr.
    'ngend' : ['ngend', 'multigroup_photon_input'],
    'ngg' : ['ngg', 'number_of_gamma_groups'], # gaminr, groupr.
    'ngn' : ['ngn', 'number_of_neutron_groups'], # errorr, groupr.
    'ngrid' : ['ngrid'],
    'ngout' : ['ngout', 'group_xsec_input'], # errorr.
    'ngout1' : ['ngout1', 'gout_input'], # groupr.
    'ngout2' : ['ngout2', 'gout_output'], # groupr.
    'nin' : ['nin', 'pendf_input'], # covr, ...
    'ninwt' : ['ninwt'], # groupr.
    'nkh' : ['nkh'], # plotr.
    'nladr' : ['nladr'], # purr.
    'nmix' : ['nmix'],
    'nmt' : ['nmt'], # errorr
    'noleg' : ['noleg'], # covr, ...
    'nout' : ['nout', 'pendf_output'], # covr, errorr, ...
    'npend' : ['npend', 'pendf_input'],
    'npk' : ['npk', 'number_of_partial_kermas'],
    'nplot' : ['nplot'], # covr, ...
    'nplt' : ['nplt'], # plotr
    'nplt0' : ['nplt0'], # plotr
    'nps' : ['nps', 'output'], # viewr.
    'nqa' : ['nqa', 'number_of_q_values'],
    'nsigz' : ['nsigz', 'number_of_sigma_zeroes'], # groupr.
    'nstan' : ['nstan'], # errorr
    'nstart' : ['nstart'], # covr, ...
    'ntemp' : ['ntemp', 'number_of_temperatures'], # groupr, thermr, ...
    'ntemp2' : ['ntemp2', 'number_of_final_temperatures'], # broadr.
    'ntype' : ['ntype', 'ace_output_type'],
    'nth' : ['nth'], # plotr
    'ntk' : ['ntk'], # plotr
    'ntp' : ['ntp'], # plotr
    'nunx' : ['nunx'], # purr.
    'nxtra' : ['nxtra'],
    'qa' : ['qa'],
    'qbar' : ['qbar'],
    'rbot' : ['rbot'], # plotr
    'rl' : ['rl'], # plotr, viewr
    'rmax' : ['rmax'], # viewr
    'rmin' : ['rmin'], # viewr
    'rtop' : ['rtop'], # plotr
    'rstep' : ['rstep'], # plotr, viewr
    'sam' : ['sam'],
    'sigpot' : ['sigpot'], # groupr.
    'sigz' : ['sigz', 'sigma_zero_values'], # groupr.
    'size' : ['size'], # plotr
    'suff' : ['suff'],
    't1' : ['t1'], # plotr, viewr
    't2' : ['t2'], # plotr, viewr
    'tb' : ['tb', 'thermal_temperature'], # errorr, groupr.
    'tc' : ['tc', 'fission_temperature'], # errorr, groupr.
    'temp' : ['temp', 'temperature'], # groupr.
    'temp1' : ['temp1', 'start_temp'], # broadr.
    'temp2' : ['temp2', 'final_temp'], # broadr.
    'tempd' : ['tempd', 'temperature'],
    'tempin' : ['tempin'], # errorr.
    'temper' : ['temper'], # plotr
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
    'tpid' : ['tpid'], # moder
    'wght' : ['wght'], # errorr, gaminr, groupr.
    'wh' : ['wh'], # plotr, viewr
    'wr' : ['wr'], # plotr, viewr
    'ww' : ['ww'], # plotr, viewr
    'x' : ['x'], # viewr
    'x3' : ['x3'], # plotr, viewr
    'xdata' : ['xdata'], # plotr, viewr
    'xerr1' : ['xerr1'], # plotr, viewr
    'xerr2' : ['xerr2'], # plotr, viewr
    'xlabl' : ['xlabl'], # plotr, viewr
    'xll' : ['xll'], # plotr, viewr
    'xmax' : ['xmax'], # viewr
    'xmin' : ['xmin'], # viewr
    'xpoint' : ['xpoint'], # plotr, viewr
    'xstep' : ['xstep'], # plotr
    'xtag' : ['xtag'], # plotr, viewr
    'xv' : ['xv'], # plotr, viewr
    'y' : ['y'], # viewr
    'y3' : ['y3'], # plotr, viewr
    'ydata' : ['ydata'], # plotr, viewr
    'yerr1' : ['yerr1'], # plotr, viewr
    'yerr2' : ['yerr2'], # plotr, viewr
    'yh' : ['yh'], # plotr
    'yl' : ['yl'], # plotr
    'ylabl' : ['ylabl'], # plotr, viewr
    'yll' : ['yll'], # plotr, viewr
    'ymax' : ['ymax'], # viewr
    'ymin' : ['ymin'], # viewr
    'ytag' : ['ytag'], # plotr, viewr
    'ystep' : ['ystep'], # plotr, viewr
    'yv' : ['yv'], # plotr, viewr
    'z' : ['z'], # viewr
    'z3' : ['z3'], # plotr, viewr
    'zv' : ['zv'], # plotr, viewr
}
