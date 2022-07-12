from typing_extensions import assert_type
from typing import Tuple


# Empty tuples, see #8275
class TupleSub(Tuple[int, ...]):
    pass


assert_type(TupleSub(), TupleSub)
assert_type(TupleSub([1, 2, 3]), TupleSub)