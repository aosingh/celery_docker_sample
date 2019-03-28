#!/usr/bin/python

from tasks import parse_url

URLS = [
            "https://www.ncnr.nist.gov/programs/crystallography/software/cif/ciftools.html",
            "http://tess2.uspto.gov/tmdb/dscm/dsc_ai.htm",
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aib.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aic.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aid.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aie.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aif.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aig.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aih.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aii.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aij.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aik.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_ail.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aim.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_ain.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aio.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aip.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aiq.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_air.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_ais.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_ait.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aiu.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aiv.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aiw.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aix.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aiy.htm',
            'http://tess2.uspto.gov/tmdb/dscm/dsc_aiz.htm'
]

if __name__ == '__main__':
    for url in URLS:
        args = (url,)
        parse_url.apply_async(args)

