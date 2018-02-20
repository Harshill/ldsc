directory = '/home/harshill/GithubProjects/ldsc/data/scz/'


def get_ldsc(dir=directory, file='22', wind_measure='--ld-wind-cm', use_wind=1):
    out = '--bfile {}{}'.format(dir, file)
    out += ' --l2 {} {}'.format(wind_measure, use_wind)
    out += ' --out {}{}'.format(dir, file)
    return out


def get_h2(dir=directory, sumstats_file='22', ld_path='eur_w_ld_chr', outfile='scz_h2'):
    out = '--h2 {}{}'.format(dir, sumstats_file)
    out += ' --ref-ld-chr {}{}'.format(dir, ld_path)
    out += ' --w-ld-chr {}{}'.format(dir, ld_path)
    out += ' --out {}{}'.format(dir, outfile)
    return out


def get_munge(dir=directory, sumstats_file='pgc.cross.SCZ17.2013-05.txt', N=17115, outfile='scz', merge=True):
    out = '--sumstats {}{}'.format(dir, sumstats_file)
    out += ' --N {}'.format(N)
    out += ' --out {}{}'.format(dir, outfile)

    if merge:
        out += '--merge - alleles / home / harshill / GithubProjects / ldsc / data / scz / w_hm3.snplist'

    return out


for func in [get_ldsc, get_h2, get_munge]:
    print func()