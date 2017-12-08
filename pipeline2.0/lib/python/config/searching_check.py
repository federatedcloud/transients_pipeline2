#!/usr/bin/env python
import config_types

searching = config_types.ConfigList('searching')
searching.add_config('use_subbands', config_types.BoolConfig())
searching.add_config('fold_rawdata', config_types.BoolConfig())
searching.add_config('datatype_flag', config_types.StrConfig())
searching.add_config('rfifind_chunk_time', config_types.FloatConfig())
searching.add_config('singlepulse_threshold', config_types.FloatConfig())
searching.add_config('singlepulse_plot_SNR', config_types.FloatConfig())
searching.add_config('singlepulse_maxwidth', config_types.FloatConfig())
searching.add_config('to_prepfold_sigma', config_types.FloatConfig())
searching.add_config('max_cands_to_fold', config_types.IntConfig())
searching.add_config('numhits_to_fold', config_types.IntConfig())
searching.add_config('low_DM_cutoff', config_types.FloatConfig())
searching.add_config('lo_accel_numharm', config_types.IntConfig())
searching.add_config('lo_accel_sigma', config_types.FloatConfig())
searching.add_config('lo_accel_zmax', config_types.IntConfig())
searching.add_config('lo_accel_flo', config_types.FloatConfig())
searching.add_config('hi_accel_numharm', config_types.IntConfig())
searching.add_config('hi_accel_sigma', config_types.FloatConfig())
searching.add_config('hi_accel_zmax', config_types.IntConfig())
searching.add_config('hi_accel_flo', config_types.FloatConfig())
searching.add_config('low_T_to_search', config_types.FloatConfig())

searching.add_config('sifting_sigma_threshold', config_types.FloatConfig())
searching.add_config('sifting_r_err', config_types.FloatConfig())
searching.add_config('sifting_short_period', config_types.FloatConfig())
searching.add_config('sifting_long_period', config_types.FloatConfig())
searching.add_config('sifting_harm_pow_cutoff', config_types.FloatConfig())

if __name__=='__main__':
    import searching as configs
    searching.populate_configs(configs.__dict__)
    searching.check_sanity()