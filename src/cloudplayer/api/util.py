"""
    cloudplayer.api.util
    ~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Nicolas Drebenstedt
    :license: GPL-3.0, see LICENSE for details
"""
import random
import string


def gen_token(n, alphabet=string.ascii_lowercase + string.digits):
    """Cryptographically sufficient token generator for length `n`."""
    urand = random.SystemRandom()
    return ''.join(urand.choice(alphabet) for i in range(n))
